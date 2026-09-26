export const meta = {
  name: 'uhakiki-robo-1',
  description: 'Sheikh-mhakiki: uhakiki na marekebisho ya vitabu vya Robo 1 (wakala 1 kwa kitabu)',
  phases: [{ title: 'Uhakiki na Marekebisho', detail: 'sheikh anahakiki NA kurekebisha mwenyewe' }],
}

const ROOT = '/home/msaba/Desktop/me/Priority/minhaj-tafsiri-workspace'
const PDF = ROOT + '/chanzo/mukhtasar-minhaj-alqasidin-arnaut.pdf'

const UNITS = [
  { id: 'elimu', jina: 'Kitabu cha Elimu', faili: 'sura/robo-1-ibada/01-elimu.html', kurasa: '13-26' },
  { id: 'twahara', jina: 'Kitabu cha Twahara na Swala', faili: 'sura/robo-1-ibada/02-twahara-swala.html', kurasa: '27-36' },
  { id: 'zaka', jina: 'Kitabu cha Zaka', faili: 'sura/robo-1-ibada/03-zaka.html', kurasa: '37-42' },
  { id: 'swaumu', jina: 'Kitabu cha Swaumu', faili: 'sura/robo-1-ibada/04-swaumu.html', kurasa: '43-46' },
  { id: 'hija', jina: 'Kitabu cha Hija', faili: 'sura/robo-1-ibada/05-hija.html', kurasa: '46-49' },
  { id: 'adabu-quran', jina: 'Kitabu cha Adabu za Kusoma Qur\'an', faili: 'sura/robo-1-ibada/06-adabu-quran.html', kurasa: '50-54' },
  { id: 'adhkari', jina: 'Kitabu cha Adhkari na Dua', faili: 'sura/robo-1-ibada/07-adhkari-dua.html', kurasa: '55-70' },
]

const SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    hali: { type: 'string', enum: ['IMEKUBALIWA', 'IMEREKEBISHWA'] },
    marekebisho: { type: 'array', items: { type: 'string' } },
    maswali: { type: 'array', items: { type: 'string' } },
  },
  required: ['hali', 'marekebisho', 'maswali'],
}

function prompt(u) {
  return `Wewe ni SHEIKH-MHAKIKI: sheikh mzoefu wa Dar es Salaam, hafidhi, mjuzi wa fiqh, hadithi na Kiswahili cha dini. Unahakiki NA kurekebisha mwenyewe, kwa uadilifu: kilicho sahihi hakiguswi.

SOMA KWANZA (briefing fupi, ndiyo sheria zinazokufunga): ${ROOT}/zana/muhtasari-sheria.md kisha ${ROOT}/kamusi/kamusi.md. Usisome CLAUDE.md nzima; fungua sehemu yake mahususi TU ukiwa na shaka.

KAZI: hakiki ${ROOT}/${u.faili} ("${u.jina}") dhidi ya kurasa ${u.kurasa} za ${PDF} (zisome kama picha, Read pages:"${u.kurasa}"). Linganisha MSTARI KWA MSTARI:
1. Ukamilifu: hakuna sentensi ya Kiarabu iliyorukwa; hakuna kilichoongezwa.
2. Uaminifu: maana halisi (hakuna maana ya hewa); hukumu za kisheria kamili; fomula za mwandishi zimehifadhiwa.
3. Aya: nukuu ya maana ni ya Al-Barwani (thibitisha kwa python3 ${ROOT}/zana/aya.py SURA AYA); (Sura: n) sahihi.
4. Hadithi: matamshi sahihi; chanzo/hukumu kwa kanuni za briefing; hakuna ubunifu.
5. Rejista, kamusi, muundo wa HTML, tanbihi (jozi kamili), hakuna em dash, hakuna Kiarabu nje ya aya.
6. Soma kwa sauti: Kiswahili la imamu msomi, sentensi hazikatwa-katwa.

KOSA ULILOLITHIBITISHA: lirekebishe MWENYEWE kwa Edit, papo hapo, kwa usahihi mdogo unaowezekana (usibadilishe mtindo usio na kosa). Jambo linalohitaji uamuzi wa mtumiaji: liweke kwenye maswali, usilibadilishe.

Rudisha: hali (IMEKUBALIWA kama hukugusa chochote; IMEREKEBISHWA kama ulirekebisha), marekebisho (orodha fupi ya ulichokibadilisha na kwa nini), maswali.`
}

const chagua = Array.isArray(args) && args.length ? UNITS.filter(u => args.includes(u.id)) : UNITS
log(`Uhakiki wa vitabu ${chagua.length}: ${chagua.map(u => u.id).join(', ')}`)

phase('Uhakiki na Marekebisho')
const results = await parallel(chagua.map(u => () =>
  agent(prompt(u), { label: `sheikh:${u.id}`, phase: 'Uhakiki na Marekebisho', schema: SCHEMA })
    .then(r => ({ kitabu: u.jina, ...r }))
))

return results.filter(Boolean)
