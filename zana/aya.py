#!/usr/bin/env python3
"""Chapisha tafsiri ya Barawani ya aya: python3 zana/aya.py SURA AYA [AYA_MWISHO] [--tanbihi]"""
import sqlite3, sys, pathlib
db = pathlib.Path(__file__).resolve().parent.parent / "chanzo" / "quran-ali-muhsin-al-barwani.sqlite"
a = [x for x in sys.argv[1:] if not x.startswith("--")]
sura, mwanzo = int(a[0]), int(a[1])
mwisho = int(a[2]) if len(a) > 2 else mwanzo
con = sqlite3.connect(db)
for aya, t, fn in con.execute("select aya, translation, footnotes from translations where sura=? and aya between ? and ? order by aya", (sura, mwanzo, mwisho)):
    print(f"({sura}:{aya}) {t}")
    if "--tanbihi" in sys.argv and fn:
        print(f"    [tanbihi] {fn}")
