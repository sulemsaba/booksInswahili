> **MAAGIZO YA KUDUMU KWA CLAUDE CODE:** Soma faili hili kikamilifu kabla ya kazi yoyote ya kikao. Kisha soma `MAENDELEO.md` (dira ya kazi — inaonyesha tulipoishia; isasishwe mwisho wa kila kikao) na `kamusi/kamusi.md` (katiba ya mradi; tahajia iliyofungwa HAIBADILIKI bila idhini ya mtumiaji). TOC yenye kurasa za PDF iko `toc.md`. Chanzo kiko `chanzo/`. Neno la OCR lenye shaka HALIBUNIWI — liwekwe alama na kuulizwa. Usinakili maelezo ya mhariri (Arna'ut) neno kwa neno; hukumu zake zitajwe kwa maneno yetu.

# MPANGO WA KAZI (v2.0) — Tafsiri ya *Mukhtasar Minhaj al-Qasidin* kwa Kiswahili
### Work Plan & Best Practices | Ibn Qudamah al-Maqdisi (Allah amrehemu)
*Toleo la 2.0 — muundo wa folda umesafishwa; TOC halisi imetolewa kutoka PDF; MAENDELEO.md imeongezwa*

---

## 0. MUUNDO WA FOLDA (Folder structure)

```
minhaj-tafsiri-workspace/
├── CLAUDE.md          ← faili hili (mpango + sera)
├── MAENDELEO.md       ← dira ya kila kikao: hali ya kila kitabu (SASISHA kila kikao)
├── toc.md             ← TOC halisi yenye kurasa za PDF (⚠️ = haijathibitishwa)
├── ANZA_HAPA.md       ← maelekezo ya vikao
├── kamusi/kamusi.md   ← katiba ya istilahi
├── chanzo/
│   ├── mukhtasar-minhaj-alqasidin-arnaut.pdf   ← chanzo kikuu (kurasa 416)
│   └── ocr-ghafi-usiitumainie.txt              ← OCR ghafi ya PDF nzima — ya kutafutia
│                                                  TU, kamwe si chanzo cha tafsiri
├── sura/              ← tafsiri, faili moja kwa kitabu, muundo wa HTML (majina: MAENDELEO.md)
│   ├── 00-utangulizi/     (jalada, kanuni za mfasiri, kuhusu toleo, dibaji ya mwandishi)
│   ├── robo-1-ibada/
│   ├── robo-2-ada/
│   ├── robo-3-muhlikat/
│   └── robo-4-munjiyat/
├── zana/
│   ├── jenga-pdf.py   ← hujenga PDF: python3 zana/jenga-pdf.py (WeasyPrint)
│   └── mtindo.css     ← muundo wa kitabu (fonti, kurasa, maelezo ya chini)
└── matokeo/
    └── minhaj-kiswahili-rasimu.pdf   ← PDF ya kusomwa na mtumiaji (jengwa upya kila kikao)
```

**Muundo wa faili za sura (HTML):** kila kifungu ni `<section class="kifungu">` yenye `<p class="ar">` (Kiarabu kilichothibitishwa kwa PICHA ya ukurasa, si OCR), kisha `<p class="sw">` (Kiswahili; ndani yake transliteration ya aya/hadithi kwa `<em>«…»</em>`). Maelezo ya chini: `<a class="fnref" id="fnr-XX" href="#fn-XX"></a><span class="fn" id="fn-XX">…</span>` — namba zinajipanga zenyewe, alama inabofyeka, maelezo hukaa chini ya ukurasa wake. Kiarabu ndani ya matini ya Kilatini kifungwe `<span class="ar-inline">`.

**Muundo wa kitabu chenyewe:** robo nne (Ibada · Ada · Muhlikat · Munjiyat), vitabu/milango 31 + dibaji — tazama `toc.md`.

---

## 1. KANUNI ZILIZOKWISHA KUBALIWA (Rules agreed)

| Jambo | Uamuzi |
|---|---|
| Chanzo (source) | Kiarabu — maneno ya Ibn Qudamah mwenyewe. Toleo la Arna'ut ni rejea (tazama 1a) |
| Aya na Hadithi | Arabic script → transliteration (italics) → maana kwa Kiswahili |
| Maneno ya dini | swala, zaka, tawhidi, ikhlasi, khofu, subira, shukrani, zuhudi, tawakkali, nia, twahara |
| Maneno mapya yaliyofungwa | **rajaa** (matumaini — kwa mabano mara ya kwanza tu), **taqwa** (haitafsiriwi), **nafsi**, *'ubudiyyah* → itaamuliwa kwenye kamusi kabla ya sura ya kwanza |
| Mtume | – Rehema na Amani zimshukie – (ﷺ) |
| Allah | Subhanahu wa Ta'ala |
| Wanazuoni | Allah amrehemu |
| Maswahaba | Allah amuwie radhi |
| Lugha | Kiswahili Sanifu + msamiati wa Kiislamu unaojulikana Dar es Salaam. Tafsiri ni maana-kwa-maana, KAMWE si neno-kwa-neno |
| Faili la mwisho | **PDF** (uamuzi wa mtumiaji, Julai 2026) — hujengwa kwa `python3 zana/jenga-pdf.py` → `matokeo/minhaj-kiswahili-rasimu.pdf` |
| Maelezo ya chini | Ni ya kweli kitaaluma: yanakaa CHINI YA UKURASA WAO wenyewe, alama ya juu inabofyeka (link) kuruka hadi kwenye maelezo (uamuzi wa mtumiaji, Julai 2026) |
| Mtiririko wa kazi | Tafsiri inakwenda kwa mfuatano kuanzia mwanzo wa kitabu; hatua ya "sura ya mfano ikubaliwe kwanza" imeondolewa kwa agizo la mtumiaji. Mapitio ya sheikh yanabaki kupendekezwa mwishoni |

**1a. Haki za toleo (muhimu):** Maneno ya Ibn Qudamah ni mali ya umma (public domain). Lakini toleo la kisasa lina vitu vya mhariri — dibaji yake, maelezo yake ya footnotes, mpangilio. **Hatunakili maelezo ya Arna'ut neno kwa neno.** Tunatumia *hukumu* zake za hadithi kama taarifa, kwa maneno yetu: *"Arna'ut ameihukumu kuwa sahihi."*

**1b. Uamuzi uliobaki:** tafsiri ya Qur'an ya nyumbani. Pendekezo: **Al-Farsy (Qurani Takatifu)** — tunanukuu aya moja moja tu, kwa kutaja chanzo wazi kila mara. Mbadala huru kabisa: tafsiri ya King Fahd Complex.

---

## 2. HATUA ZA KAZI (Workflow)

**HATUA 0 — Ukaguzi wa ubora wa PDF** — *imeanza*
- ✅ TOC rasimu yenye kurasa (`toc.md`) imetolewa kutoka tabaka la maandishi la PDF.
- ⬜ Kulinganisha OCR na picha za kurasa (mwanzo, katikati, mwisho); ripoti kwenye `ripoti-ocr.md`.
- ⬜ Kuthibitisha alama zote ⚠️ za `toc.md` (vichwa vilivyopotoshwa, mipaka ya vitabu, mahali pa *Halali na Haramu*).
- Ubora wa OCR unaojulikana: maneno huungana (`علىمنتحت`), herufi hupotoshwa, takataka za Kilatini huingia. Kwa hiyo `chanzo/ocr-ghafi-usiitumainie.txt` ni ya KUTAFUTIA tu — kila kipande kinachotafsiriwa kisomwe kutoka picha ya ukurasa wa PDF.

**HATUA 0b — Uthibitisho wa Kiarabu, kila sehemu (verification checklist):**
Kabla ya kutafsiri kila sehemu:
1. Maandishi ya OCR yanalinganishwa na picha ya ukurasa halisi.
2. Neno gumu au lenye shaka linakaguliwa dhidi ya toleo jingine la Kiarabu (Shamela / Dar al-Hijaz).
3. Maneno ya OCR yenye shaka yanawekwa alama na kuonyeshwa kwako — hayabuniwi.
4. Vichwa vya sura vinathibitishwa.
*Sababu: herufi moja hubadilisha maana — العلم (elimu) dhidi ya الحلم (upole).*

**HATUA 1 — Kamusi ya istilahi (Master glossary v1.0)**
- Neno la Kiarabu → tahajia ya Kiswahili iliyofungwa. Inaamuliwa mara moja, haibadiliki.
- **Sera ya uthibitisho wa maneno:** neno lolote tusilokuwa na uhakika nalo linatafutwa kwanza — tunaangalia jinsi linavyotumika kwenye machapisho ya Kiislamu ya Tanzania — kabla ya kulifunga. Lisilopatikana au lenye utata: linaamuliwa na wewe (na sheikh ikiwezekana).

**HATUA 2 — Sura ya mfano** — *IMEONDOLEWA kwa agizo la mtumiaji (Julai 2026):* tafsiri inakwenda kwa mfuatano kuanzia mwanzo, bila kusubiri idhini ya mtindo. Mapitio (ya mtumiaji, na ya sheikh hasa kwa aya na hadithi) yanabaki kwenye Hatua 5.

**HATUA 3 — Tafsiri kitabu kwa kitabu**, kwa mfuatano wa `MAENDELEO.md`; kikao kimoja = kipande kimoja kamili (kanuni iko MAENDELEO.md). Kabla ya kipande: Hatua 0b. Baada ya kipande: sasisha hali kwenye MAENDELEO.md + git commit.

**HATUA 4 — Kuunganisha:** PDF inajengwa tangu sasa kila kikao (`python3 zana/jenga-pdf.py`); jalada, kanuni za mfasiri na TOC tayari vimo. Kilichobaki cha mwisho: kamusi ya istilahi nyuma ya kitabu + ukaguzi wa uthabiti wa matini yote.

**HATUA 5 — Mapitio:** wewe, kisha (ushauri wa dhati) sheikh mmoja au wawili wa Dar — hasa aya na hadithi.

---

## 3. MPANGILIO WA TABAKA TATU (Three-layer structure)

Kila kifungu kikuu kinafuata mpangilio huu:

**Tabaka 1 — Kiarabu asilia** (matini ya Ibn Qudamah)
**Tabaka 2 — Tafsiri ya Kiswahili**
**Tabaka 3 — Maelezo (footnotes):** chanzo cha hadithi, daraja (kwa kumtaja mwenye hukumu), ufafanuzi wa neno mara ya kwanza.

---

## 4. SERA YA HADITHI (Hadith policy)

Kwa kila hadithi:
- **Matini:** Kiarabu → transliteration → Kiswahili.
- **Footnote:** (a) chanzo — Bukhari, Muslim, Tirmidhi, Abu Daud, Nasai, Ibn Majah, Ahmad; (b) daraja **kwa kumtaja mwenye hukumu**: *"Sahihi — kwa hukumu ya Arna'ut"* — kamwe si "hadithi hii ni dhaifu" bila jina, kwa sababu wanazuoni hutofautiana; (c) tofauti za hukumu zikijulikana, zinatajwa kwa ufupi bila upande.

---

## 5. SERA YA KUEPUKA FITNA (Avoiding fitna)

1. **Maneno ya Ibn Qudamah tu.** Hatuongezi maoni, hatupunguzi, hatufafanui kwa msimamo wa kambi yoyote.
2. **Hukumu za hadithi zinatajwa kwa jina la mwenye hukumu** — uwazi badala ya hukumu ya kificho.
3. **Tahajia na heshima zisizo za kambi:** mfumo tuliokubali unasomeka kwa Mwislamu wa kawaida wa Tanzania bila kubeba bendera ya kundi.
4. **Vyanzo vya mtandao vinakaguliwa kwanza — nani kachapisha?** Tovuti za Kiswahili cha Kiislamu ni za makundi mbalimbali (Ahmadiyya, Shia, Sufi, Salafi, Hanafi wa nje). Chanzo kinakuwa kigezo cha mtindo TU baada ya kujulikana. Vyanzo vya msingi vya matumizi ya maneno: tafsiri ya Al-Farsy, machapisho ya register ya BAKWATA, uislamu.org. Vinginevyo: ushahidi wa tahajia tu, si wa itikadi.
5. **Ukurasa wa kanuni za mfasiri** (§6) unaweka kila kitu wazi — uwazi ndio ngao ya fitna.
6. Panapotokea ibara yenye hisasi za kiitikadi ndani ya matini yenyewe, tunatafsiri kwa uaminifu bila kuongeza — na tunaweka alama kwa mapitio ya sheikh.

---

## 6. UKURASA WA KANUNI ZA MFASIRI (Translator's principles page)

Mwanzoni mwa kitabu cha mwisho, ukurasa mfupi unaeleza:
- Toleo la Kiarabu lililotumika (na mahali lilipopatikana).
- Njia ya tafsiri: maana-kwa-maana, si neno-kwa-neno.
- Jinsi maneno ya Kiarabu yalivyoshughulikiwa (rejea kamusi nyuma).
- Chanzo cha tafsiri za aya (jina kamili la tafsiri ya nyumbani).
- Utaratibu wa hadithi na hukumu zake.

---

## 7. MTINDO NA CHAPA (Writing style & typography)

**Mtindo wa maandishi:**
- Sentensi za Kiswahili halisi — maana ya Kiarabu, muziki wa Kiswahili. Si tafsiri ya neno kwa neno.
- Istilahi za ibada hazibadilishwi kwa maneno ya kawaida (swala si "maombi").
- Rejista ya heshima, tulivu, ya mawaidha — kama vitabu vya dini vya Dar, si ya kitaaluma baridi wala ya mtaani.

**Chapa (PDF — inasimamiwa na `zana/mtindo.css`, WeasyPrint):**
| Sehemu | Fonti | Ukubwa |
|---|---|---|
| Matini ya Kiswahili | Noto Serif | 10.5 pt |
| Kiarabu (matini na aya) | Noto Naskh Arabic | 13–13.5 pt |
| Transliteration | italiki ya Noto Serif | 9.8 pt |
| Maelezo ya chini | Noto Serif | 8.2 pt |

- Ukubwa wa ukurasa 150×222 mm (kama toleo la Kiarabu); namba za kurasa; kichwa cha kitabu juu ya kila ukurasa; TOC ya moja kwa moja yenye namba za kurasa zinazobofyeka.
- Kiarabu: right-to-left, aya ndani ya alama ﴿ ﴾.
- Maelezo ya chini: chini ya ukurasa wao, mstari wa kuyatenga, alama inayobofyeka; namba zinaanza upya kila kitabu.

---

## 8. KUMBUKUMBU KATI YA VIKAO — MUHIMU SANA

Vikao havina kumbukumbu ya kudumu; kumbukumbu ni FAILI za mradi. **Itifaki ya kila kikao:**

**Mwanzo wa kikao:** soma `CLAUDE.md` → `MAENDELEO.md` (tulipoishia) → `kamusi/kamusi.md`.
**Mwisho wa kikao (kamwe usiruke):**
1. Sasisha hali kwenye `MAENDELEO.md`.
2. Neno jipya lililofungwa? — liingize `kamusi/kamusi.md` na tarehe.
3. `git commit` (ujumbe kwa Kiswahili, mf. `tafsiri: elimu sehemu ya 1/2`).
4. Swali lolote lililobaki kwa mtumiaji liandikwe kwenye MAENDELEO.md chini ya kitabu husika — lisipotee.

---

## 9. MAKADIRIO (halisi, kutoka PDF)

PDF kurasa 416; matini ya kitabu kurasa ~13–408 (≈ kurasa 395 za Kiarabu). Robo 4, vitabu/milango 31 + dibaji. Makadirio: vikao ~55–65. Kazi ya miezi — ubora kwanza, kasi ya pili.

---

*Bismillah — hatua inayofuata: kumalizia Hatua 0 (uthibitisho wa OCR kwa picha + alama ⚠️ za toc.md), kisha Hatua 1 (kamusi v1.0 — maamuzi ya sehemu C ni ya mtumiaji).*
