#!/usr/bin/env python3
"""Jenga PDF ya tafsiri: hukusanya vipande vya HTML kutoka sura/ kwa mpangilio,
huunda Yaliyomo yenye namba za kurasa zinazobofyeka, na kutoa PDF kwa WeasyPrint.

Matumizi:  python3 zana/jenga-pdf.py
Matokeo:   matokeo/minhaj-kiswahili-rasimu.pdf
"""
import re
import sys
from pathlib import Path

MZIZI = Path(__file__).resolve().parent.parent
MPANGILIO = [
    "sura/00-utangulizi",
    "sura/robo-1-ibada",
    "sura/robo-2-ada",
    "sura/robo-3-muhlikat",
    "sura/robo-4-munjiyat",
]


def weka_namba_za_maelezo(kipande):
    """Huweka namba za maelezo ya chini wakati wa ujenzi (1..n kwa kila faili).

    Namba zinaandikwa moja kwa moja ndani ya HTML: <sup>n</sup> kwenye alama,
    na "n. " mwanzoni mwa maelezo. Kwa njia hii namba ya alama na ya maelezo
    haziwezi kutofautiana, injini yoyote ikitumika.
    """
    hesabu = {"fnref": 0, "fn": 0}

    def alama(m):
        hesabu["fnref"] += 1
        return m.group(0)[:-len("</a>")] + f"<sup>{hesabu['fnref']}</sup></a>"

    def maelezo(m):
        hesabu["fn"] += 1
        return m.group(0) + f'<span class="fn-num">{hesabu["fn"]}.&nbsp;</span>'

    kipande = re.sub(r'<a class="fnref"[^>]*></a>', alama, kipande)
    kipande = re.sub(r'<span class="fn" [^>]*>', maelezo, kipande)
    if hesabu["fnref"] != hesabu["fn"]:
        sys.exit(f"Jozi za maelezo hazilingani: {hesabu}")
    return kipande


def kusanya():
    vipande = []
    for folda in MPANGILIO:
        for faili in sorted((MZIZI / folda).glob("*.html")):
            vipande.append(weka_namba_za_maelezo(faili.read_text(encoding="utf-8")))
    return vipande


def tengeneza_yaliyomo(vipande):
    orodha = []
    for kipande in vipande:
        for m in re.finditer(
            r'<article[^>]*id="([^"]+)"[^>]*>.*?<h1>(.*?)</h1>', kipande, re.S
        ):
            kichwa = re.sub(r"<[^>]+>", "", m.group(2)).strip()
            orodha.append(f'<li><a href="#{m.group(1)}">{kichwa}</a></li>')
    if not orodha:
        return ""
    return (
        '<section class="yaliyomo"><h1>Yaliyomo</h1><ol>'
        + "\n".join(orodha)
        + "</ol></section>"
    )


def jenga():
    """Hujenga PDF kwa Chromium headless + Paged.js.

    Kwa nini si WeasyPrint: WeasyPrint (hadi v69) huharibu tabaka la maandishi
    la Kiarabu kwenye PDF (nakili-ubandike hutoa herufi zilizopotoka, mf. قال
    hutoka تال). Chromium hutoa Unicode halisi inayonakilika; Paged.js
    inaleta sifa za kitabu (maelezo chini ya ukurasa, namba za kurasa,
    vichwa vya juu, TOC yenye namba).
    """
    import shutil
    import subprocess

    vipande = kusanya()
    if not vipande:
        sys.exit("Hakuna vipande vya HTML vilivyopatikana katika sura/")

    # Jalada kwanza, kisha Yaliyomo, kisha vipande vingine
    jalada = [v for v in vipande if 'class="jalada"' in v]
    vingine = [v for v in vipande if 'class="jalada"' not in v]
    mwili = "".join(jalada) + tengeneza_yaliyomo(vingine) + "".join(vingine)

    # CSS inaingizwa ndani ya HTML moja kwa moja: Paged.js huvuta <link> kwa
    # fetch(), na fetch ya file:// imezuiwa na Chromium (CORS) — hushindwa kimya.
    css = (MZIZI / "zana" / "mtindo.css").read_text(encoding="utf-8")

    # Paged.js huipa jina jipya id ya maelezo inapoyahamishia chini ya ukurasa
    # (fn-XX inakuwa note-<uuid>). Baada ya upangaji, tunaelekeza upya href za
    # alama kwenye id mpya, ili viungo vibaki vinabofyeka kwenye PDF.
    rekebisha_viungo = (
        "<script>window.PagedConfig={after:()=>{"
        'document.querySelectorAll("a.fnref").forEach(a=>{'
        'const id=a.getAttribute("href").slice(1);'
        "const note=document.querySelector('[id^=\"note-\"][data-id=\"'+id+'\"]');"
        'if(note)a.setAttribute("href","#"+note.id);'
        "});}};</script>"
    )

    html = (
        '<!DOCTYPE html><html lang="sw"><head><meta charset="utf-8">'
        "<title>Mukhtasar Minhaj al-Qasidin — Tafsiri ya Kiswahili</title>"
        f"<style>{css}</style>"
        f"{rekebisha_viungo}"
        '<script src="paged.polyfill.js"></script>'
        "</head><body>" + mwili + "</body></html>"
    )

    matokeo = MZIZI / "matokeo"
    matokeo.mkdir(exist_ok=True)
    pdf = matokeo / "minhaj-kiswahili-rasimu.pdf"

    chromium = shutil.which("chromium-browser") or shutil.which("chromium")
    if not chromium:
        sys.exit("Chromium haipatikani; inahitajika kujenga PDF")

    # Faili la ujenzi linakaa ndani ya zana/ ili "fonti/..." na
    # "paged.polyfill.js" zipatikane kwa njia ileile (relative).
    faili_html = MZIZI / "zana" / ".kitabu-build.html"
    faili_html.write_text(html, encoding="utf-8")
    try:
        amri = [
            chromium,
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--export-tagged-pdf",
            "--virtual-time-budget=120000",
            f"--print-to-pdf={pdf}",
            f"file://{faili_html}",
        ]
        r = subprocess.run(amri, capture_output=True, text=True, timeout=300)
        if not pdf.exists():
            sys.exit(f"Chromium imeshindwa:\n{r.stderr[-2000:]}")
    finally:
        faili_html.unlink(missing_ok=True)
    print(f"Imekamilika: {pdf}")


if __name__ == "__main__":
    jenga()
