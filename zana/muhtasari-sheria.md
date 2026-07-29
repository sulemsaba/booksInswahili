# MUHTASARI WA SHERIA KWA WAKALA (toleo 1 — 29 Julai 2026)
### Hii ndiyo briefing pekee unayosoma kikamilifu. Ikitokea shaka mahususi TU, fungua sehemu husika ya CLAUDE.md. Kamusi (`kamusi/kamusi.md`) LAZIMA isomwe — ni katiba ya maneno.

## KANUNI KUU
Msomaji wa Kiswahili apate elimu YOTE na uzoefu WOTE wa msomaji wa Kiarabu — sawa au bora. Hakuna kuongeza, hakuna kupunguza, hakuna kufupisha kimyakimya (kosa zito kuliko yote). Kila sentensi ya Kiarabu ina mwenzake kamili.

## CHANZO
- Tafsiri kutoka PICHA za kurasa (Read, pages: "X-Y") za `chanzo/mukhtasar-minhaj-alqasidin-arnaut.pdf`. OCR ghafi ni ya kutafutia tu.
- Sentensi ikiendelea ukurasa unaofuata, isome uimalizie kwa mshono wa asili; taja kwenye vidokezo ulipoishia.

## REJISTA (kamili kwenye kamusi)
Mwenyezi Mungu (si Allah; matamshi pekee: *Allāh*) · viwakilishi Vyake kwa herufi kubwa (Yake, Wake, Kwake) · تعالى = Mtukufu · Mtume = **ﷺ** · Swahaba: (Mwenyezi Mungu amridhie); wawili: (…awaridhie wote wawili) · mwanachuoni aliyetangulia: (Mwenyezi Mungu amrehemu) · Nabii mwingine: (Amani imshukie) · wanachuoni (si wanazuoni) · fiqh (si fikihi) · uongofu (Al-Farsy pekee huandika "uwongofu" ndani ya nukuu zake — usiguse nukuu) · majina kwa alama kamili: Abū Hurayra, Ibn Qudāmah, Muʿādh bin Jabal.

## MTINDO
- Rule 0: elewa Kiarabu kwanza → rasimu aminifu → ng'arisha kwa MPANGILIO MZURI WA KISWAHILI ukisoma kwa sauti.
- **Usikate sentensi** — iandike kwa mpangilio wa Kiswahili; maneno 30–40+ ni kengele ya kusoma kwa sauti, kukata ni suluhisho la mwisho.
- Viunganishi (Na, Basi, Kisha) pale tu Kiswahili kinavyohitaji; marudio ya Kiarabu (inamwajibikia…) yabadilishwe: anawajibika / inampasa / analazimika.
- Fomula za mwandishi ni takatifu: swali la balagha libaki swali; wito ubaki wito («Ewe…!»); swali-na-jibu (Ikiulizwa: … Jibu ni kwamba…) libaki hivyo.
- Kiswahili rasmi cha imamu msomi wa Dar; usirembeshe, usihubiri, usimboreshe mwandishi.
- Usahihi wa hukumu za kisheria ni mtakatifu: wajibu / sunna / mubāḥ / makruhu / haramu havichanganywi.
- HAKUNA em dash (—) popote: nukta, koma, koloni au nusukoloni.
- Vichwa vya ndani: vilivyomo kwenye Kiarabu tu (فصل = «Fasili: …»; vya mabano [] ni vya wahariri — taja kwenye tanbihi mara ya kwanza kwenye faili). USIBUNI vichwa.

## MUUNDO WA FAILI (HTML — templeti kamili)
```html
<article class="kitabu" id="ID">
<p class="robo-kichwa">ROBO YA ____ YA KITABU: ROBO YA ____</p>
<h1>Kichwa halisi cha kitabu kutoka ukurasa wa Kiarabu</h1>

<section class="kifungu">
  <p class="sw">Masimulizi ya mwandishi kwa Kiswahili tu (bila Kiarabu sambamba).</p>
</section>

<!-- AYA (Kiarabu kwa Qur'an PEKE YAKE kitabuni): -->
<section class="kifungu">
  <p class="sw">Amesema Mwenyezi Mungu Mtukufu:</p>
  <p class="ar aya">﴿…matini ya aya kwa tashkeel…﴾</p>
  <p class="tr">Matamshi ya aya.</p>
  <p class="sw maana">Maana yake: «NUKUU YA AL-FARSY NENO KWA NENO, pamoja na mabano yake» (Sura: n).</p>
</section>
<!-- Nukuu ya Al-Farsy: grep kwenye chanzo/alfarsy/*.txt (kwa neno moja la nukuu unayotarajia,
     nafasi za OCR zisafishwe tu, maneno yabaki YAKE). Usipoipata: tafsiri maana mwenyewe + [?] kwenye maswali. -->

<!-- HADITHI (bila hati ya Kiarabu): -->
<section class="kifungu">
  <p class="sw">Kutoka kwa Abū Hurayra (Mwenyezi Mungu amridhie), amesema: Amesema Mtume wa Mwenyezi Mungu ﷺ:</p>
  <p class="tr">Matamshi kamili ya matn.</p>
  <p class="sw maana">Maana yake: «…»<a class="fnref" id="fnr-XXnn" href="#fn-XXnn"></a><span class="fn" id="fn-XXnn">Chanzo na hukumu.</span></p>
</section>
</article>
```

## TANBIHI (footnotes)
- Jozi: `<a class="fnref" id="fnr-XXnn" href="#fn-XXnn"></a>` + `<span class="fn" id="fn-XXnn">…</span>` PAPO HAPO (XX = kiambishi ulichopewa; nn mfululizo). Namba za kuonyesha huwekwa na zana — si wewe.
- Chanzo cha hadithi kama mwandishi alivyotaja. Maelezo ya wahariri (chini ya ukurasa wa Kiarabu): kwa maneno yako, ukiwataja («Wahariri…»). Wahariri wakinyamaza kwa hadithi isiyo na hukumu: sema wamenyamaza. Chanzo kisichotajwa: WebSearch (sunnah.com, dorar.net) ukitaje «uthibitisho wa mfasiri»; usipoweza: [?] kwenye maswali. KAMWE usikisie; ukiwa na shaka: [?], si ubunifu.
- Istilahi mpya ya dini: fafanua mara ya kwanza (mabano au tanbihi) + orodhesha kwenye kamusi_mapya.

## KABLA YA KUMALIZA (lazima)
1. Mstari kwa mstari dhidi ya picha: hakuna sentensi iliyorukwa wala kuongezwa.
2. `grep "—" faili` itoe tupu; jozi za fnref/fn zilingane.
3. Soma kwa sauti aya moja ya maandishi kila ukurasa; isiyosomeka, iandike upya.

## MARUFUKU
jenga-pdf.py · git · kuhariri kamusi/HALI/MASWALI/CLAUDE au faili za wengine · kubuni chanzo/hukumu/kichwa · em dash · Kiarabu nje ya aya za Qur'an.
