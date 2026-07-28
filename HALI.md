# HALI YA KAZI
### Sasisha faili hili mwisho wa kila kikao (mwongozo 12.5). Soma mwanzoni mwa kila kikao.

## Tulipoishia
**Inayofuata:** Kitabu cha Elimu, sehemu ya 2: hadithi ya Abu Musa (uk. 14–15 za Kiarabu), kuendelea hadi mwisho wa kitabu (uk. 26).
**LAKINI:** sampuli ya sasa (dibaji + elimu sehemu ya 1) inasubiri idhini ya mtumiaji. Usianze sehemu mpya kabla ya idhini (mwongozo 12.2).

## Rejista ya ufunikaji (kurasa za PDF ya Kiarabu, `chanzo/mukhtasar-minhaj-alqasidin-arnaut.pdf`)

| Kurasa | Sehemu | Hali |
|---|---|---|
| 1–2 | Jalada la Kiarabu na ukurasa wa mwaka | Taarifa zake zimo kwenye ukurasa wa jina; hazitafsiriwi |
| 3–4 | Dibaji ya mchapishaji (Bashir ʿUyūn) | ✅ Muhtasari kwa maneno yetu: `sura/00-utangulizi/03-toleo-na-wahariri.html` |
| 5–8 | Dibaji ya Sheikh Dahmān | ✅ Muhtasari kwa maneno yetu: faili ileile |
| 9–12 | Dibaji ya mwandishi | ✅ Imetafsiriwa kamili: `04-dibaji-ya-mwandishi.html`. Inasubiri idhini |
| 13 – 14 (hadi swali la samaki) | Elimu, sehemu ya 1 | ✅ Imetafsiriwa: `sura/robo-1-ibada/01-elimu.html`. Inasubiri idhini |
| 14 (hadithi ya Abu Musa) – 26 | Elimu, sehemu ya 2+ | ⬜ Inayofuata |
| 27–408 | Vitabu vilivyobaki (30) | ⬜ Ramani kamili yenye kurasa: `toc.md` (alama ⚠️ = mipaka bado kuthibitishwa kwa picha) |
| 409–415 | Fihris ya asili | Haitafsiriwi; Yaliyomo yetu inazalishwa na zana |

**Kazi za Hatua 0 zilizosalia:** kuthibitisha alama ⚠️ za `toc.md` kwa picha za kurasa; ukaguzi wa kurasa tupu za mchapishaji (mwongozo 8.8d).

## Nanga ya mtindo
Hakuna sehemu iliyoidhinishwa bado. Sampuli inayosubiri idhini: `04-dibaji-ya-mwandishi.html` + `01-elimu.html`. Ikishaidhinishwa, hizo ndizo nanga.

## Zana (kiufundi)
- Jenga PDF: `python3 zana/jenga-pdf.py` → `matokeo/minhaj-kiswahili-rasimu.pdf`. Injini: Chromium + Paged.js; fonti zimewekwa ndani (Amiri kwa Kiarabu, P052 kwa Kiswahili, Caladea kwa vichwa).
- **WeasyPrint imekatazwa:** iliharibu unakili wa Kiarabu (tahadhari ya mwongozo 11.3 ilithibitika kwayo).
- Jaribio la Kiarabu (11.3), kila ujenzi: `pdftotext matokeo/minhaj-kiswahili-rasimu.pdf - | grep العلماء` (au neno jingine) — herufi zitoke sahihi. Dosari inayojulikana na kukubalika: baadhi ya program huingiza nafasi ndani ya neno wakati wa kunakili; herufi zenyewe ni sahihi.
- Maelezo ya chini: namba zake zinawekwa na zana wakati wa ujenzi (haziandikwi kwa mkono).

## Kumbukumbu za vikao
- **28 Julai 2026 (1):** muundo wa folda umesafishwa; TOC halisi imetolewa kutoka PDF; git imeanzishwa.
- **28 Julai 2026 (2):** dibaji ya mwandishi + Elimu uk. 13–14 zimetafsiriwa; zana ya PDF imejengwa.
- **28 Julai 2026 (3):** mtindo v1.2 (bila em dash; masimulizi Kiswahili tu); injini imehamia Chromium + Paged.js baada ya kugundua Kiarabu kilichoharibika; Amiri imewekwa.
- **28 Julai 2026 (4):** MWONGOZO v3.0 umeingizwa kama CLAUDE.md; HALI.md na MASWALI.md zimeanzishwa (zinachukua nafasi ya MAENDELEO.md na ANZA_HAPA.md); khutba ya dibaji imerudishiwa mtiririko (4.4); alama za hadithi » «; ukurasa wa ufunguo umeundwa; chapa kwa 11.1; maelezo ya hadithi yamefuatishwa na 8.3 na 12.3.
