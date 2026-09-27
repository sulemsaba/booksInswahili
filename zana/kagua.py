#!/usr/bin/env python3
"""Ukaguzi wa kimitambo wa sura zote (hakitumii AI).

    python3 zana/kagua.py            # faili zote za sura/
    python3 zana/kagua.py FAILI...   # faili maalum

Hukagua:
  1. Dashi za Unicode (U+2012..U+2015, U+2212): marufuku kabisa.
  2. Kiarabu nje ya aya za Qur'an (<p class="ar aya">) na maeneo yanayoruhusiwa.
  3. Tanbihi: kila fnref ina fn yake na kinyume chake; id hazirudiwi.
  4. Dalili za muhtasari ("Mwandishi anaeleza", "anataja", "n.k.", "...").
  5. Ukamilifu: uwiano wa herufi za Kiswahili dhidi ya herufi za Kiarabu za
     kurasa za kitengo (pdftotext). Uwiano mdogo = huenda kimefupishwa.
"""
import html
import re
import subprocess
import sys
from pathlib import Path

MZIZI = Path(__file__).resolve().parent.parent
PDF = MZIZI / "chanzo" / "mukhtasar-minhaj-alqasidin-arnaut.pdf"

# faili -> (ukurasa wa mwanzo, ukurasa wa mwisho) wa PDF ya Kiarabu
KURASA = {
    "sura/robo-1-ibada/01-elimu.html": (13, 26),
    "sura/robo-1-ibada/02-twahara-swala.html": (27, 36),
    "sura/robo-1-ibada/03-zaka.html": (37, 42),
    "sura/robo-1-ibada/04-swaumu.html": (43, 45),
    "sura/robo-1-ibada/05-hija.html": (46, 49),
    "sura/robo-1-ibada/06-adabu-quran.html": (50, 54),
    "sura/robo-1-ibada/07-adhkari-dua.html": (55, 70),
    "sura/robo-2-ada/01-adabu-kula.html": (71, 75),
    "sura/robo-2-ada/02-ndoa.html": (76, 81),
    "sura/robo-2-ada/03-kuchuma.html": (82, 96),
    "sura/robo-2-ada/04-usuhuba-udugu.html": (97, 122),
    "sura/robo-2-ada/05-amri-na-makatazo.html": (123, 147),
    "sura/robo-3-muhlikat/01-ajabu-za-moyo.html": (148, 151),
    "sura/robo-3-muhlikat/02-kuiadibu-nafsi.html": (151, 162),
    "sura/robo-3-muhlikat/03-matamanio-mawili.html": (163, 164),
    "sura/robo-3-muhlikat/04-maafa-ya-ulimi.html": (165, 177),
    "sura/robo-3-muhlikat/05-hasira-kinyongo-husuda.html": (178, 208),
    "sura/robo-3-muhlikat/06-cheo-na-riyaa.html": (209, 226),
    "sura/robo-3-muhlikat/07-kibri-na-kujiona.html": (227, 236),
    "sura/robo-3-muhlikat/08-ghururi.html": (237, 250),
    "sura/robo-4-munjiyat/01-tawba.html": (251, 267),
    "sura/robo-4-munjiyat/02-subira-na-shukrani.html": (268, 296),
    "sura/robo-4-munjiyat/03-rajaa-na-khofu.html": (297, 315),
    "sura/robo-4-munjiyat/04-zuhudi-na-ufakiri.html": (316, 320),
    "sura/robo-4-munjiyat/05-halali-na-haramu.html": (321, 330),
    "sura/robo-4-munjiyat/06-tawhidi-na-tawakkali.html": (331, 337),
    "sura/robo-4-munjiyat/07-mahabba-shauku-unsi-radhi.html": (338, 358),
    "sura/robo-4-munjiyat/08-nia-ikhlasi-ukweli.html": (359, 369),
    "sura/robo-4-munjiyat/09-muhasaba-muraqaba.html": (370, 377),
    "sura/robo-4-munjiyat/10-tafakuri.html": (378, 381),
    "sura/robo-4-munjiyat/11-kumbukumbu-la-mauti.html": (382, 408),
}

DASHI = re.compile("[‒-―−]")
KIARABU = re.compile("[؀-ۿﭐ-﷿ﹰ-﻿]{2,}")
RUHUSA_KIARABU = re.compile(
    r'<(p|span|div|h\d)[^>]*class="[^"]*\b(ar|ar-inline|ar-kichwa)\b[^"]*"[^>]*>.*?</\1>', re.S)
MUHTASARI = re.compile(
    r"Mwandishi (anaeleza|anataja|anaelekeza|anasema kwamba)|Kisha anataja|\bn\.k\.")
# Uwiano wa chini unaokubalika (herufi za Kiswahili / herufi za Kiarabu).
# Sura zilizohakikiwa kuwa kamili zina uwiano wa ~1.4 au zaidi.
UWIANO_WA_CHINI = 1.1


def maandishi(s):
    s = re.sub(r"<[^>]+>", " ", s)
    return html.unescape(s)


def herufi_za_kiarabu(a, b):
    try:
        t = subprocess.run(["pdftotext", "-f", str(a), "-l", str(b), str(PDF), "-"],
                           capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return None
    # ondoa tanbihi za wahariri (chini ya ukurasa) kwa makadirio: hesabu herufi zote
    return len(re.findall("[ء-ي]", t))


def kagua(faili):
    njia = MZIZI / faili
    s = njia.read_text(encoding="utf-8")
    kasoro = []

    for n, mstari in enumerate(s.splitlines(), 1):
        if DASHI.search(mstari):
            kasoro.append(f"dashi ya Unicode, mstari {n}")

    bila_maoni = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    bila_ruhusa = RUHUSA_KIARABU.sub(" ", bila_maoni)
    for m in KIARABU.finditer(bila_ruhusa):
        kasoro.append(f"Kiarabu nje ya aya: {m.group(0)[:30]}")
        break

    refs = re.findall(r'class="fnref"[^>]*id="fnr-([^"]+)"', s) + \
        re.findall(r'id="fnr-([^"]+)"[^>]*class="fnref"', s)
    fns = re.findall(r'class="fn"[^>]*id="fn-([^"]+)"', s) + \
        re.findall(r'id="fn-([^"]+)"[^>]*class="fn"', s)
    if len(set(refs)) != len(refs):
        kasoro.append("id za fnref zimerudiwa")
    if len(set(fns)) != len(fns):
        kasoro.append("id za fn zimerudiwa")
    for x in sorted(set(refs) ^ set(fns)):
        kasoro.append(f"tanbihi haina jozi: {x}")

    matini = maandishi(bila_maoni)
    for m in MUHTASARI.finditer(matini):
        kasoro.append(f"dalili ya muhtasari: «{matini[max(0, m.start()-40):m.end()+20].strip()}»")

    uwiano = None
    if faili in KURASA:
        ar = herufi_za_kiarabu(*KURASA[faili])
        sw = len(re.findall(r"[A-Za-z]", matini))
        if ar:
            uwiano = sw / ar
            if uwiano < UWIANO_WA_CHINI:
                kasoro.append(f"uwiano {uwiano:.2f} < {UWIANO_WA_CHINI}: huenda kimefupishwa au hakijakamilika")
    return uwiano, kasoro


def main():
    faili = sys.argv[1:] or sorted(str(p.relative_to(MZIZI)) for p in (MZIZI / "sura").rglob("*.html"))
    jumla = 0
    for f in faili:
        uwiano, kasoro = kagua(f)
        u = f"{uwiano:.2f}" if uwiano is not None else "  - "
        print(f"{'OK ' if not kasoro else 'XX '} {u}  {f}")
        for k in kasoro:
            print(f"      - {k}")
        jumla += len(kasoro)
    print(f"\nKasoro: {jumla}")
    sys.exit(1 if jumla else 0)


if __name__ == "__main__":
    main()
