#!/usr/bin/env python3
"""Usawazishaji wa kimitambo wa mtindo wa msomaji (uamuzi wa mtumiaji, 27 Septemba 2026).

    python3 zana/sawazisha.py [FAILI...]   # bila faili: sura/ zote

Hufanya:
  1. Huondoa matamshi ya herufi za Kilatini (<p class="tr">) ya aya na hadithi.
  2. Huondoa "Maana yake: " mwanzoni mwa aya za maana.
  3. Heshima: (r.a.) kwa Maswahaba, (a.s.) kwa Manabii, ﷺ kwa Mtume.
  4. Majina na istilahi kwa tahajia rahisi: ā->a, ḥ->h, ʿ/ʾ -> ' (au hufutwa mwanzoni/mwishoni mwa neno).
Hati ya Kiarabu ya aya haiguswi. Kinachoweza kurudiwa bila madhara (idempotent).
"""
import re
import sys
from pathlib import Path

MZIZI = Path(__file__).resolve().parent.parent

HESHIMA = [
    ("(Mwenyezi Mungu awaridhie wote wawili)", "(r.a.)"),
    ("(Mwenyezi Mungu awaridhie wote)", "(r.a.)"),
    ("(Mwenyezi Mungu awaridhie)", "(r.a.)"),
    ("(Mwenyezi Mungu Mtukufu amridhie)", "(r.a.)"),
    ("(Mwenyezi Mungu amridhie)", "(r.a.)"),
    ("(Mwenyezi Mungu amuwie radhi)", "(r.a.)"),
    ("(Amani iwashukie wote wawili)", "(a.s.)"),
    ("(Amani iwashukie)", "(a.s.)"),
    ("(Amani imshukie)", "(a.s.)"),
    ("(Rehema na Amani zimshukie)", "ﷺ"),
]

HERUFI = str.maketrans({
    "ā": "a", "ī": "i", "ū": "u", "Ā": "A", "Ī": "I", "Ū": "U",
    "ḥ": "h", "Ḥ": "H", "ṣ": "s", "Ṣ": "S", "ṭ": "t", "Ṭ": "T",
    "ḍ": "d", "Ḍ": "D", "ẓ": "z", "Ẓ": "Z", "ḏ": "dh", "ṯ": "th",
    "ġ": "gh", "ḫ": "kh",
})

KIARABU = re.compile(r"[؀-ۿﭐ-﷿ﹰ-﻿]")


def herufi_rahisi(maandishi):
    """Hurahisisha herufi za matamshi nje ya tagi za HTML na nje ya Kiarabu."""
    def kipande(m):
        s = m.group(0)
        if s.startswith("<"):
            return s
        if KIARABU.search(s):
            # Kiarabu kinabaki; herufi za matamshi zilizo kando yake zinarahisishwa
            return re.sub(r"[^\u0600-\u06FF\uFB50-\uFDFF\uFE70-\uFEFF]+",
                          lambda x: herufi_rahisi(x.group(0)), s)
        s = s.translate(HERUFI)
        # ʿ na ʾ: hufutwa mwanzoni/mwishoni mwa neno, ndani ya neno huwa '
        s = re.sub(r"(?<![A-Za-z])[ʿʾ]|[ʿʾ](?![A-Za-z])", "", s)
        s = s.replace("ʿ", "'").replace("ʾ", "'")
        return s
    return re.sub(r"<[^>]+>|[^<]+", kipande, maandishi)


def sawazisha(njia):
    s = njia.read_text(encoding="utf-8")
    asili = s
    s = re.sub(r'^[ \t]*<p class="tr">.*?</p>[ \t]*\n', "", s, flags=re.M)
    s = re.sub(r'(<p class="sw maana">)\s*Maana yake:\s*', r"\1", s)
    for a, b in HESHIMA:
        s = s.replace(a, b)
    s = herufi_rahisi(s)
    if s != asili:
        njia.write_text(s, encoding="utf-8")
        return True
    return False


def main():
    faili = [Path(f) for f in sys.argv[1:]] or sorted((MZIZI / "sura").rglob("*.html"))
    kwa = [f for f in faili if sawazisha(f)]
    print(f"Faili zilizobadilika: {len(kwa)}")


if __name__ == "__main__":
    main()
