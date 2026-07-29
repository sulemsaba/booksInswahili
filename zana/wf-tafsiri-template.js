export const meta = {
  name: 'tafsiri-batch',
  description: 'Tafsiri ya kundi dogo la vitabu: mtafsiri (briefing fupi) + sheikh anayehakiki na kurekebisha',
  phases: [
    { title: 'Tafsiri', detail: 'briefing fupi (muhtasari-sheria.md), si rulebook nzima' },
    { title: 'Uhakiki', detail: 'sheikh anahakiki NA kurekebisha mwenyewe (wakala 1)' },
  ],
}

// args = { robo: "ROBO YA PILI YA KITABU: ROBO YA ADA",
//          units: [{ id, jina, faili, pref, parts: [[a,b],...] }] }

const ROOT = '/home/msaba/Desktop/me/Priority/minhaj-tafsiri-workspace'
const PDF = ROOT + '/chanzo/mukhtasar-minhaj-alqasidin-arnaut.pdf'

const TRANS = {
  type: 'object', additionalProperties: false,
  properties: {
    imekamilika: { type: 'boolean' },
    maswali: { type: 'array', items: { type: 'string' } },
    kamusi_mapya: { type: 'array', items: { type: 'string' } },
    vidokezo: { type: 'string' },
  },
  required: ['imekamilika', 'maswali', 'kamusi_mapya', 'vidokezo'],
}

const REVIEW = {
  type: 'object', additionalProperties: false,
  properties: {
    hali: { type: 'string', enum: ['IMEKUBALIWA', 'IMEREKEBISHWA'] },
    marekebisho: { type: 'array', items: { type: 'string' } },
    maswali: { type: 'array', items: { type: 'string' } },
  },
  required: ['hali', 'marekebisho', 'maswali'],
}

function transPrompt(u, a, b, sehemu, jumla, robo) {
  const mode = sehemu > 1
    ? `Faili ${ROOT}/${u.faili} LIPO: lisome, endeleza kutoka mwisho wake bila mtiririko kukatika, ingiza kabla ya </article> kwa Edit.`
    : `Unda ${ROOT}/${u.faili} kwa Write kwa templeti ya briefing: robo-kichwa ni "${robo}"; h1 ni kichwa halisi kutoka ukurasa wa Kiarabu.`
  return `Wewe ni mfasiri wa "Mukhtasar Minhaj al-Qasidin" kwa Kiswahili.

SOMA KWANZA (briefing fupi, ndiyo sheria zinazokufunga): ${ROOT}/zana/muhtasari-sheria.md kisha ${ROOT}/kamusi/kamusi.md. Usisome CLAUDE.md nzima; fungua sehemu mahususi TU ukiwa na shaka.

KAZI: tafsiri kurasa ${a}-${b} za ${PDF} (Read pages:"${a}-${b}", kama picha) — sehemu ${sehemu}/${jumla} ya "${u.jina}". Sentensi ikiendelea ukurasa ${b + 1}, isome uimalizie kwa mshono wa asili; taja kwenye vidokezo.

${mode}

Kiambishi cha tanbihi: "${u.pref}" (endelea na namba baada ya zilizopo kama faili lipo).

Rudisha: imekamilika, maswali, kamusi_mapya, vidokezo (mshono ulipoishia).`
}

function revPrompt(u, robo) {
  const kurasa = u.parts[0][0] + '-' + u.parts[u.parts.length - 1][1]
  return `Wewe ni SHEIKH-MHAKIKI: sheikh mzoefu wa Dar es Salaam, hafidhi, mjuzi wa fiqh, hadithi na Kiswahili cha dini. Unahakiki NA kurekebisha mwenyewe; kilicho sahihi hakiguswi.

SOMA KWANZA: ${ROOT}/zana/muhtasari-sheria.md kisha ${ROOT}/kamusi/kamusi.md (tu).

KAZI: hakiki ${ROOT}/${u.faili} ("${u.jina}", ${robo}) dhidi ya kurasa ${kurasa} za ${PDF} (picha, mstari kwa mstari): ukamilifu (hakuna kilichorukwa/kilichoongezwa); uaminifu na hukumu za kisheria; aya = Al-Farsy neno kwa neno (grep ${ROOT}/chanzo/alfarsy/); hadithi kwa kanuni; rejista na kamusi; muundo/tanbihi/hakuna em dash/hakuna Kiarabu nje ya aya; soma kwa sauti.

KOSA ULILOLITHIBITISHA: lirekebishe MWENYEWE kwa Edit, kwa mabadiliko madogo yanayowezekana. Jambo la uamuzi wa mtumiaji: kwenye maswali tu.

Rudisha: hali, marekebisho, maswali.`
}

if (!args || !Array.isArray(args.units) || !args.units.length || !args.robo) {
  throw new Error('args inahitajika: { robo, units: [{id, jina, faili, pref, parts}] }')
}

const results = await pipeline(
  args.units,
  async (u) => {
    let mwisho = null
    for (let i = 0; i < u.parts.length; i++) {
      const [a, b] = u.parts[i]
      mwisho = await agent(transPrompt(u, a, b, i + 1, u.parts.length, args.robo), {
        label: `tafsiri:${u.id}:${a}-${b}`, phase: 'Tafsiri', schema: TRANS,
      })
    }
    return { u, trans: mwisho }
  },
  async (r) => {
    const rev = await agent(revPrompt(r.u, args.robo), { label: `sheikh:${r.u.id}`, phase: 'Uhakiki', schema: REVIEW })
    return {
      kitabu: r.u.jina, faili: r.u.faili,
      hali: rev ? rev.hali : 'HAIJULIKANI',
      marekebisho: rev ? rev.marekebisho : [],
      maswali: [...((r.trans && r.trans.maswali) || []), ...((rev && rev.maswali) || [])],
      kamusi_mapya: (r.trans && r.trans.kamusi_mapya) || [],
      vidokezo: (r.trans && r.trans.vidokezo) || '',
    }
  }
)

return results.filter(Boolean)
