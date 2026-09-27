# AGENTS.md - handoff for any AI assistant (ChatGPT, Codex, Claude, Gemini...)

This repository is the Swahili translation of *Mukhtasar Minhaj al-Qasidin* by Ibn Qudamah al-Maqdisi.
Whatever tool you are, you follow exactly the same rules and procedure the work was done with so far.
Nothing here replaces `CLAUDE.md`; this file tells you how to apply it.

## 1. Read before any work (in this order)

1. `CLAUDE.md` - the full rulebook (in Swahili). **Every rule in it is binding**, including the
   user additions at the end (NYONGEZA, KANUNI KUU, KANUNI ZA DHAHABU 20, points 5-7).
   If two rules conflict, stop and ask the user. Do not choose yourself.
2. `zana/muhtasari-sheria.md` - the short working brief + the exact HTML template.
3. `kamusi/kamusi.md` - the glossary. Locked terms never change without the user's approval.
4. `HALI.md` - where the work stands. `MASWALI.md` - open questions (only the user deletes one).
5. Style anchor: `sura/robo-2-ada/03-kuchuma.html` (read its opening to match voice and markup).

## 2. The non-negotiable rules (summary; `CLAUDE.md` is the authority)

- **Full translation, never a summary.** Every sentence, hadith, athar, poem, list and example of the
  author is translated. Forbidden: shortening, merging paragraphs, "Mwandishi anaeleza...",
  "Kisha anataja...", "n.k.", skipping because it is long. If you run out of room, stop at an exact
  sentence and say where. Skipping silently is the worst error in this project.
- **Translate meaning, not Arabic grammar.** Do not chop sentences into short pieces; rebuild them in
  natural, fluent Swahili (user rule: «Usikate sentensi, bali iandike kwa mpangilio mzuri wa Kiswahili»).
  Keep the five style modes: sermon flow, direct address, rhetorical questions stay questions, etc.
- Reader: an ordinary Muslim in Dar es Salaam. Simple everyday vocabulary, full scholarly voice.
- **Arabic script only for Qur'an verses.** Hadith and everything else: transliteration (italic) +
  Swahili meaning + footnote.
- **Qur'an meanings: Sheikh Ali Muhsin Al-Barwani only** (Al-Farsy is no longer used).
  Get the text with `python3 zana/aya.py SURA AYA [AYA_END]`. Keep Barwani's words and order; only
  modernise spelling (Mwenyeezi -> Mwenyezi, mnayo yatenda -> mnayoyatenda, uchamngu -> uchamungu).
  If the author quotes part of a verse, quote only the matching part. Always cite (Sura: n).
  Never quote a verse from memory.
- **Hadith footnotes:** source + ruling **by name** ("Wahariri (al-Arna'ut) wameihukumu kuwa dhaifu").
  If the editors are silent: "Wahariri hawakutoa hukumu hapa." Never "this hadith is sahih" without a
  name. Editors' notes are facts restated in our own words, never copied word for word.
- Honorifics and names exactly as in `zana/muhtasari-sheria.md` (Mwenyezi Mungu, ﷺ, Mtukufu, ...).
- Keep voices apart (Ibn Qudamah vs Ibn al-Jawzi vs al-Ghazali vs quoted scholars).
- **Never write an em dash, en dash or any Unicode dash** (U+2012-U+2015, U+2212). ASCII "-" only.
- Doubts go to `MASWALI.md` with `[?]` in the text. Never guess.
- The English Dar as-Sunnah translation must never be used, not even for comparison.

## 3. Sources and tools

| What | Where / command |
|---|---|
| Arabic source (authority) | `chanzo/mukhtasar-minhaj-alqasidin-arnaut.pdf` - read the page **images** |
| Arabic text layer (helper, imperfect OCR) | `pdftotext -f N -l N chanzo/mukhtasar-minhaj-alqasidin-arnaut.pdf -` |
| Qur'an (Al-Barwani) | `python3 zana/aya.py SURA AYA` (DB: `chanzo/quran-ali-muhsin-al-barwani.sqlite`) |
| Mechanical checks (run after every change) | `python3 zana/kagua.py [files]` |
| Build the PDF | `python3 zana/jenga-pdf.py` -> `matokeo/minhaj-kiswahili-rasimu.pdf` (needs Chromium + Python Playwright; takes ~4 min; check the last page ends with the final dua) |
| Arabic copy test (rule 11.3) | `pdftotext matokeo/minhaj-kiswahili-rasimu.pdf - \| grep -P '\p{Arabic}' \| head` |

`zana/kagua.py` checks: Unicode dashes, Arabic outside verses, footnote pairs, summary phrases, and a
completeness ratio (Swahili letters / Arabic letters of the unit's pages). Complete chapters score about
1.4-2.8; below 1.1 means something is probably missing. A good ratio does NOT prove completeness;
only the line-by-line review does.

## 4. Procedure (the same one used so far)

Work one unit (Kitabu or Bab) at a time, in parts of about 6-8 PDF pages.

**Step A - translator, per part.** Read the pages as images. Three passes (Rule 0): understand,
faithful draft, polish into fluent Swahili and read it aloud. The first part creates the file from the
template (`<article class="kitabu" id="...">`, `<p class="robo-kichwa">`, `<h1>` = translated real
Arabic heading). Later parts continue exactly where the file ends: no gap, no repetition. Start exactly
at the unit's opening heading and stop exactly before the next unit's heading, even mid-page.
Footnote ids: `fn-PREFNN` / `fnr-PREFNN`, continuing the file's numbering; the build script prints the
numbers, never type them yourself.

**Step B - sheikh-reviewer, per unit.** Act as an experienced Dar es Salaam sheikh who knows fiqh,
hadith and religious Swahili. Compare the whole file with the PDF paragraph by paragraph.
Priority 1: completeness (translate in full anything skipped or summarised; check the joins between
parts). Then: meaning and legal rulings (wajibu/sunna/mubah/makruhu/haramu never mixed), Barwani
verses and citations, hadith footnotes, glossary, voices, no Unicode dashes, no Arabic outside verses,
clean HTML. Fix errors directly with minimal edits; put decisions that belong to the user in
`MASWALI.md`.

**Step C - after each unit:** run `python3 zana/kagua.py FILE`, update `HALI.md` (pages covered, where
it ends), add new terms to `kamusi/kamusi.md` with the date, then commit and push.

## 5. Units, files and exact boundaries (checked against the PDF headings)

| File | PDF pages | Starts at |
|---|---|---|
| sura/robo-2-ada/04-usuhuba-udugu.html | 97-122 | كتاب آداب الصحبة والأخوة |
| sura/robo-2-ada/05-amri-na-makatazo.html | 123-147 | كتاب الأمر بالمعروف (includes bab 131, bab 145) |
| sura/robo-3-muhlikat/01-ajabu-za-moyo.html | 148-151 | Robo 3 heading + كتاب شرح عجائب القلوب |
| sura/robo-3-muhlikat/02-kuiadibu-nafsi.html | 151-162 | كتاب رياضة النفس (starts mid-page 151) |
| sura/robo-3-muhlikat/03-matamanio-mawili.html | 163-164 | كتاب كسر الشهوتين |
| sura/robo-3-muhlikat/04-maafa-ya-ulimi.html | 165-177 | كتاب آفات اللسان |
| sura/robo-3-muhlikat/05-hasira-kinyongo-husuda.html | 178-208 | كتاب ذم الغضب والحقد والحسد (bab 185, 190, 195 inside) |
| sura/robo-3-muhlikat/06-cheo-na-riyaa.html | 209-226 | كتاب ذم الجاه والرياء |
| sura/robo-3-muhlikat/07-kibri-na-kujiona.html | 227-236 | كتاب ذم الكبر والعجب |
| sura/robo-3-muhlikat/08-ghururi.html | 237-250 | كتاب الغرور |
| sura/robo-4-munjiyat/01-tawba.html | 251-267 | Robo 4 heading + كتاب التوبة |
| sura/robo-4-munjiyat/02-subira-na-shukrani.html | 268-296 | كتاب الصبر والشكر |
| sura/robo-4-munjiyat/03-rajaa-na-khofu.html | 297-315 | كتاب الرجاء والخوف |
| sura/robo-4-munjiyat/04-zuhudi-na-ufakiri.html | 316-330 | كتاب الزهد والفقر (pp. 321-330 are its second half; there is no Kitabu of Halali na Haramu) |
| sura/robo-4-munjiyat/06-tawhidi-na-tawakkali.html | 331-337 | كتاب التوحيد والتوكل |
| sura/robo-4-munjiyat/07-mahabba-shauku-unsi-radhi.html | 338-358 | كتاب المحبة والشوق والأنس والرضى |
| sura/robo-4-munjiyat/08-nia-ikhlasi-ukweli.html | 359-369 | باب في النية والإخلاص والصدق |
| sura/robo-4-munjiyat/09-muhasaba-muraqaba.html | 370-377 | باب في المحاسبة والمراقبة |
| sura/robo-4-munjiyat/10-tafakuri.html | 378-381 | باب التفكر |
| sura/robo-4-munjiyat/11-kumbukumbu-la-mauti.html | 382-408 | باب في ذكر الموت (bab 383, 389, 406 inside) |

Pages 409-416 are the original index: not translated.

## 6. Status and remaining work (27 September 2026)

**Translation: complete as a draft (27 Sep 2026).** Every page 1-408 is translated; the six last gaps were filled and the checker reports 0 issues. Translator questions are in `MASWALI.md` section F.

- **Sheikh review done:** Robo 1, Adabu za kula, Ndoa, Kuchuma, Ajabu za moyo, Kuiadibu nafsi,
  Matamanio, Maafa ya ulimi, Zuhudi (316-320), Tawhidi na tawakkali, Muhasaba, Tafakuri.
- **Sheikh review NOT done yet (step B above), this is the next job:** Usuhuba, Amri na makatazo,
  Hasira/kinyongo/husuda, Cheo na riyaa, Kibri, Ghururi, Tawba, Subira na shukrani, Rajaa na khofu,
  Zuhudi pp. 321-330, Mahabba, Nia/ikhlasi/ukweli, Kumbukumbu la mauti.
- **Resolved (user decision, 27 Sep 2026):** pp. 321-330 were merged into the Zuhudi file; there is no separate Kitabu cha Halali na Haramu (the name on p. 321 is only an in-text reference).
- Hadith numbers marked as the translator's own verification came from memory: verify each against a real source (rule 12.3).
- End tasks still to do: back-of-book glossary, whole-book consistency check (terms, style, numbers),
  intentional blank pages and final layout (rule 8.8), then the user's and a real sheikh's review.
- After every change: `python3 zana/kagua.py`, rebuild the PDF, update `HALI.md`, commit, push.

## 7. Git rules

- The user (Suleiman Msaba) is the only author. **Never** add `Co-Authored-By` lines, "Generated
  with ..." lines or any AI attribution to commits or pull requests. Never bypass hooks (`--no-verify`).
- Commit after each finished unit or checkpoint, then `git push` (remote: `origin`, branch `main`).
- Never delete agent drafts; incomplete ones move to `rasimu-wakala/`.
