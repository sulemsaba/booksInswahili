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


def kusanya():
    vipande = []
    for folda in MPANGILIO:
        for faili in sorted((MZIZI / folda).glob("*.html")):
            vipande.append(faili.read_text(encoding="utf-8"))
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
    from weasyprint import HTML, CSS

    vipande = kusanya()
    if not vipande:
        sys.exit("Hakuna vipande vya HTML vilivyopatikana katika sura/")

    # Jalada kwanza, kisha Yaliyomo, kisha vipande vingine
    jalada = [v for v in vipande if 'class="jalada"' in v]
    vingine = [v for v in vipande if 'class="jalada"' not in v]
    mwili = "".join(jalada) + tengeneza_yaliyomo(vingine) + "".join(vingine)

    html = (
        '<html lang="sw"><head><meta charset="utf-8">'
        "<title>Mukhtasar Minhaj al-Qasidin — Tafsiri ya Kiswahili</title>"
        "</head><body>" + mwili + "</body></html>"
    )

    matokeo = MZIZI / "matokeo"
    matokeo.mkdir(exist_ok=True)
    pdf = matokeo / "minhaj-kiswahili-rasimu.pdf"
    HTML(string=html, base_url=str(MZIZI)).write_pdf(
        pdf, stylesheets=[CSS(str(MZIZI / "zana" / "mtindo.css"))]
    )
    print(f"Imekamilika: {pdf}")


if __name__ == "__main__":
    jenga()
