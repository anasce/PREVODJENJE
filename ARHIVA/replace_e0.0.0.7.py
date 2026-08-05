import sys, os, re 
EXACT = [
      ('unapređenjima', 'unaprjeđenjima'),
      ('unapređenje', 'unaprjeđenje'),
      ('unapređenja', 'unaprjeđenja'),
      ('unapređenju', 'unaprjeđenju'),
      ('pravoverci', 'pravovjerni'),
      ('vjerbalne', 'verbalne'),
      ('zahtevao', 'zahtijevao'),
      ('celinama', 'cjelinama'),
      ('verbalne', 'verbalne'),
      ('razboleo', 'razbolio'),
      ('doprineo', 'doprinio'),
      ('sledeći', 'sljedeći'),
      ('zamenik', 'zamjenik'),
      ('verzija', 'verzija'),
      ('celina', 'cjelina'),
      ('celine', 'cjeline'),
      ('celini', 'cjelini'),
      ('celinu', 'cjelinu'),
      ('svideo', 'svidio'),
      ('uvideo', 'uvidio'),
      ('napred', 'naprijed'),
      ('veruju', 'vjeruju'),
      ('celima', 'cijelima'),
      ('drugde', 'drugdje'),
      ('reka', 'rijeka'),
      ('reke', 'rijeke'),
      ('reku', 'rijeku'),
      ('reko', 'rijeko'),
      ('dele', 'dijele'),
      ('dete', 'dijete'),
      ('nigde', 'nigdje'),
      ('plen', 'plijen'),
      ('cela', 'cijela'),
      ('cele', 'cijele'),
      ('celi', 'cijeli'),
      ('celo', 'cijelo'),
      ('celu', 'cijelu'),
      ('dedovi', 'djedovi'),
      ('dedama', 'djedovima'),
      ('vreme', 'vrijeme'),
      ('svest', 'svijest'),
      ('doneo', 'donijeo'),
      ('želeo', 'želio'),
      ('žudeo', 'žudio'),
      ('sreda', 'srijeda'),
      ('uspeo', 'uspio'),
      ('pevac', 'kokot'),
      ('uspeo', 'uspio'),
      ('video', 'vidio'),
      ('rekao', 'rekao'),
      ('rekla', 'rekla'),
      ('vera', 'vjera'),
      ('vere', 'vjere'),
      ('veri', 'vjeri'),
      ('veru', 'vjeru'),
      ('leta', 'ljeta'),
      ('dedu', 'djedu'),
      ('dedi', 'djedi'),
      ('dece', 'djece'),
      ('hteo', 'htio'),
      ('smeo', 'smio'),
      ('dede', 'djedovi'),
      ('žele', 'žele'),
      ('uvid', 'uvid'),
      ('dev', 'djev'),
      ('ded', 'djed'),
      ('sme', 'smije'),
      ('lek', 'lijek'),
      ('obe', 'obje'),
      ('ceo', 'cio'),
      ('deo', 'dio'),
      ('dve', 'dvije'),
      ('pre', 'prije'),
      ('bes', 'bijes'),

]


STEMS = [
      ('četvoromeseč', 'četvoromjeseč'),
      ('desetomeseč', 'desetomjeseč'),
      ('devetomeseč', 'devetomjeseč'),
      ('predstavnik', 'predstavnik'),
      ('jednomeseč', 'jednomjeseč'),
      ('pretpostav', 'pretpostav'),
      ('sedmomeseč', 'sedmmjeseč'),
      ('šestomeseč', 'šestomjeseč'),
      ('osmomeseč', 'osmoomjeseč'),
      ('petomeseč', 'petomjeseč'),
      ('podrazume', 'podrazumije'),
      ('presecanj', 'presijecanj'),
      ('presecanj', 'presijecanj'),
      ('bezuspeš', 'bezuspješ'),
      ('celobroj', 'cjelobroj'),
      ('doprinel', 'doprinijel'),
      ('doprinos', 'doprinios'),
      ('dragocen', 'dragocjen'),
      ('dvomeseč', 'dvomjeseč'),
      ('opredeli', 'opredijeli'),
      ('opredelj', 'opredjelj'),
      ('ponedelj', 'ponedjelj'),
      ('potpreds', 'potpredsj'),
      ('predvide', 'predvidje'),
      ('pregreja', 'pregrija'),
      ('ravnomer', 'ravnomjern'),
      ('tromeseč', 'tromjeseč'),
      ('zakasnel', 'zakašnjel'),
      ('zaveštan', 'zavještan'),
      ('potpreds', 'potpredsj'),
      ('delimič', 'djelimič'),
      ('izbegav', 'izbjegav'),
      ('letelic', 'letjelic'),
      ('nadžive', 'nadživje'),
      ('neizbež', 'neizbjež'),
      ('neizmer', 'neizmjer'),
      ('obavest', 'obavijest'),
      ('obavešt', 'obavješt'),
      ('ocenjiv', 'ocjenjiv'),
      ('odeljak', 'odjeljak'),
      ('osvedoč', 'osvjedoč'),
      ('osvetli', 'osvijetli'),
      ('osvetlj', 'osvjetlj'),
      ('pogreši', 'pogriješi'),
      ('poverlj', 'povjerlj'),
      ('povredi', 'povrijedi'),
      ('prebole', 'prebolje'),
      ('premest', 'premjest'),
      ('premešt', 'premješt'),
      ('procenj', 'procjenj'),
      ('primenj', 'primijenj'),
      ('prosleđ', 'prosljeđ'),
      ('razbole', 'razbolje'),
      ('razmenj', 'razmjenj'),
      ('telefon', 'telefon'),
      ('umetnik', 'umjetnik'),
      ('unapređ', 'unapređ'),
      ('zahteva', 'zahtijeva'),
      ('zaplene', 'zapljene'),
      ('zapleni', 'zaplijeni'),
      ('zaplenu', 'zapljenu'),
      ('zaplena', 'zapljena'),
      ('delegat', 'delegat'),
      ('napredn', 'napredn'),
      ('napredo', 'napredo'),
      ('podsmeh', 'podsmjeh'),
      ('predlog', 'prijedlog'),
      ('primeni', 'primijeni'),
      ('procena', 'procjena'),
      ('procene', 'procjene'),
      ('proceni', 'procijeni'),
      ('procenu', 'procjenu'),
      ('zabelež', 'zabiljež'),
      ('obezbed', 'obezbijed'),
      ('obezbeđ', 'obezbjeđ'),
      ('prethod', 'prethod'),
      ('primedb', 'primjedb'),
      ('verovatn', 'vjerovatn'),
      ('nalepn', 'naljepn'),
      ('proter', 'protjer'),
      ('zaposl', 'zapošlj'),
      ('bekstv', 'bjekstv'),
      ('decemb', 'decemb'),
      ('dedukt', 'dedukt'),
      ('delima', 'djelima'),
      ('delimi', 'djelimi'),
      ('detalj', 'detalj'),
      ('detinj', 'djetinj'),
      ('dodeli', 'dodijeli'),
      ('dodelj', 'dodijelj'),
      ('dospel', 'dospjel'),
      ('dožive', 'doživje'),
      ('gnezdo', 'gnijezdo'),
      ('izgore', 'izgorje'),
      ('izvesn', 'izvjesn'),
      ('izvest', 'izvijest'),
      ('menjač', 'mjenjač'),
      ('namešt', 'namješt'),
      ('nasled', 'naslijed'),
      ('nemošć', 'nijemošć'),
      ('neretk', 'nerijetk'),
      ('neuspe', 'neuspje'),
      ('obelež', 'obiljež'),
      ('odeven', 'odjeven'),
      ('pešačk', 'pješačk'),
      ('pobedi', 'pobijedi'),
      ('pobegl', 'pobjegl'),
      ('podela', 'podjela'),
      ('porekl', 'porijekl'),
      ('posled', 'posljed'),
      ('posred', 'posred'),
      ('povređ', 'povrijeđ'),
      ('povest', 'povijest'),
      ('predse', 'predsje'),
      ('predst', 'predst'),
      ('preduz', 'preduz'),
      ('preseć', 'presjeć'),
      ('prevar', 'prevar'),
      ('preživ', 'preživ'),
      ('preživ', 'preživj'),
      ('primer', 'primjer'),
      ('proleć', 'proljeć'),
      ('promen', 'promjen'),
      ('proseč', 'prosječ'),
      ('prosek', 'prosijek'),
      ('prosle', 'proslije'),
      ('razmer', 'razmjer'),
      ('razreš', 'razriješ'),
      ('razume', 'razumje'),
      ('razume', 'razumije'),
      ('reklam', 'reklam'),
      ('savest', 'savjest'),
      ('smatra', 'smatra'),
      ('stalež', 'stalež'),
      ('svetlo', 'svjetlo'),
      ('svetsk', 'svjetsk'),
      ('svugde', 'svugdje'),
      ('unapre', 'unaprije'),
      ('vaspit', 'vaspit'),
      ('vremen', 'vremen'),
      ('zahtev', 'zahtjev'),
      ('zahtev', 'zahtijev'),
      ('zamenj', 'zamjenj'),
      ('zaplen', 'zaplijen'),
      ('zapose', 'zaposje'),
      ('nasmeš', 'nasmiješ'),
      ('nedelj', 'nedjelj'),
      ('podseć', 'podsjeć'),
      ('predst', 'predst'),
      ('primen', 'primjen'),
      ('prover', 'provjer'),
      ('sledeć', 'slijedeć'),
      ('strelj', 'strijelj'),
      ('zamenj', 'zamjenj'),
      ('belež', 'biljež'),
      ('celin', 'cjelin'),
      ('cenit', 'cijeniti'),
      ('cveta', 'cvjeta'),
      ('delat', 'djelat'),
      ('delim', 'dijelim'),
      ('detet', 'djetet'),
      ('devet', 'devet'),
      ('devoj', 'djevoj'),
      ('izbeg', 'izbjeg'),
      ('izmen', 'izmijen'),
      ('izmer', 'izmjer'),
      ('izveš', 'izvješ'),
      ('kolev', 'kolijev'),
      ('koren', 'korijen'),
      ('lekar', 'ljekar'),
      ('lepot', 'ljepot'),
      ('letnj', 'ljetnj'),
      ('levic', 'ljevic'),
      ('levič', 'ljevič'),
      ('mesec', 'mjesec'),
      ('namer', 'namjer'),
      ('napad', 'napad'),
      ('nared', 'nared'),
      ('negde', 'negdje'),
      ('nemac', 'njemac'),
      ('nemač', 'njemač'),
      ('never', 'nevjer'),
      ('obole', 'obolje'),
      ('oceni', 'ocijeni'),
      ('odole', 'odolje'),
      ('opsed', 'opsjed'),
      ('osvet', 'osvjet'),
      ('pobeg', 'pobjeg'),
      ('podel', 'podijel'),
      ('podne', 'podne'),
      ('pomer', 'pomjer'),
      ('poseć', 'posjeć'),
      ('posed', 'posjed'),
      ('poset', 'posjet'),
      ('posle', 'poslije'),
      ('pover', 'povjer'),
      ('prene', 'prenije'),
      ('preti', 'prijeti'),
      ('rasej', 'rasijan'),
      ('savet', 'savjet'),
      ('smeja', 'smija'),
      ('smest', 'smjest'),
      ('smešt', 'smješt'),
      ('smenj', 'smjenj'),
      ('svedo', 'svjedo'),
      ('svide', 'svidje'),
      ('ubeđe', 'ubijeđe'),
      ('ucena', 'ucjena'),
      ('ucene', 'ucjene'),
      ('uceni', 'ucijeni'),
      ('ucenu', 'ucjenu'),
      ('umest', 'umjest'),
      ('usled', 'usljed'),
      ('uspeh', 'uspjeh'),
      ('uvežb', 'uvježb'),
      ('uvide', 'uvidje'),
      ('venac', 'vijenac'),
      ('vetar', 'vjetar'),
      ('zamen', 'zamijen'),
      ('zamer', 'zamjer'),
      ('zased', 'zasijed'),
      ('zaver', 'zavjer'),
      ('zvezd', 'zvijezd'),
      ('zvezd', 'zvjezd'),
      ('želel', 'željel'),
      ('živel', 'živjel'),
      ('živeo', 'živio'),
      ('živet', 'živjet'),
      ('žudel', 'žudel'),
      ('beleg', 'biljeg'),
      ('čovek', 'čovjek'),
      ('čoveč', 'čovječ'),
      ('decem', 'decem'),
      ('deleć', 'dijeleć'),
      ('delić', 'djelić'),
      ('delić', 'delić'),
      ('dodel', 'dodjel'),
      ('donel', 'donijel'),
      ('greja', 'grija'),
      ('greši', 'griješi'),
      ('izbeg', 'izbjeg'),
      ('izned', 'izned'),
      ('iznet', 'iznijet'),
      ('lepot', 'ljepot'),
      ('letak', 'letak'),
      ('napad', 'napad'),
      ('nared', 'nared'),
      ('nedel', 'nedjel'),
      ('nemoć', 'nemoć'),
      ('ocenj', 'ocjenj'),
      ('oseća', 'osjeća'),
      ('pomer', 'pomjer'),
      ('sever', 'sjever'),
      ('zamer', 'zamjer'),
      ('zvezd', 'zvijezd'),
      ('želet', 'željet'),
      ('oset', 'osjet'),
      ('ovde', 'ovdje'),
      ('peša', 'pješa'),
      ('besn', 'bijesn'),
      ('besv', 'besvj'),
      ('beža', 'bježa'),
      ('bled', 'blijed'),
      ('breg', 'brijeg'),
      ('cena', 'cijena'),
      ('ceni', 'cijeni'),
      ('cenu', 'cijenu'),
      ('cent', 'cent'),
      ('cvet', 'cvijet'),
      ('deca', 'djeca'),
      ('deča', 'dječa'),
      ('deci', 'djeci'),
      ('deco', 'djeco'),
      ('decu', 'djecu'),
      ('deli', 'dijeli'),
      ('delo', 'djelo'),
      ('dela', 'djela'),
      ('delu', 'djelu'),
      ('done', 'donije'),
      ('dvem', 'dvjem'),
      ('gnev', 'gnjev'),
      ('greh', 'grijeh'),
      ('leka', 'lijeka'),
      ('leko', 'ljeko'),
      ('leku', 'lijeku'),
      ('lenj', 'lijen'),
      ('lete', 'letje'),
      ('leti', 'ljeti'),
      ('leto', 'ljeto'),
      ('letu', 'ljetu'),
      ('mesn', 'mjesn'),
      ('mese', 'mjese'),
      ('mest', 'mjest'),
      ('mlek', 'mlijek'),
      ('nemc', 'njemc'),
      ('nežn', 'nježn'),
      ('ocen', 'ocjen'),
      ('odeć', 'odjeć'),
      ('odel', 'odijel'),
      ('odel', 'odjel'),
      ('odne', 'odnije'),
      ('onde', 'ondje'),
      ('oseć', 'osjeć'),
      ('pesm', 'pjesm'),
      ('peva', 'pjeva'),
      ('peša', 'pješa'),
      ('rečn', 'riječn'),
      ('reši', 'riješi'),
      ('retk', 'rijetk'),
      ('sled', 'sljed'),
      ('smeh', 'smijeh'),
      ('smer', 'smjer'),
      ('smel', 'smjel'),
      ('sneg', 'snijeg'),
      ('sten', 'stijen'),
      ('svet', 'svijet'),
      ('seti', 'sjeti'),
      ('tesn', 'tijesn'),
      ('tera', 'tjera'),
      ('ubeđ', 'ubjeđ'),
      ('ubed', 'ubijed'),
      ('uspe', 'uspje'),
      ('uteh', 'utjeh'),
      ('uver', 'uvjer'),
      ('veća', 'veća'),
      ('veće', 'veće'),
      ('veći', 'veći'),
      ('vešt', 'vješt'),
      ('venc', 'vijenc'),
      ('venč', 'vjenč'),
      ('vest', 'vijest'),
      ('vide', 'vidje'),
      ('vred', 'vrijed'),
      ('vređ', 'vrijeđ'),
      ('žele', 'žele'),
      ('zver', 'zvijer'),
      ('hleb', 'hljeb'),
      ('leč', 'liječ'),
      ('les', 'ljes'),
      ('leš', 'lješ'),
      ('meš', 'mješ'),
      ('mer', 'mjer'),
      ('seć', 'sjeć'),
      ('bed', 'bijed'),
      ('bel', 'bijel'),
      ('cep', 'cijep'),
      ('cev', 'cijev'),
      ('gde', 'gdje'),
      ('hte', 'htje'),
      ('lep', 'lijep'),
      ('lev', 'lijev'),
      ('mle', 'mlje'),
      ('pev', 'pjev'),
      ('pes', 'pijes'),
      ('reč', 'riječ'),
      ('ređ', 'rjeđ'),
      ('reš', 'rješ'),
      ('sen', 'sjen'),
      ('seć', 'sjeć'),
      ('tel', 'tijel'),
      ('une', 'unije'),
      ('več', 'vječ'),
      ('vek', 'vijek'),
      ('vol', 'volj')
]



KONTEKST_MAPE = [
    {
        'ekavski': ['sedela', 'sedeli', 'sedeo', 'sedio', 'sede', 'sedu', 'sedi', 'sedog', 'sedoh'],
        'kljucevi1': ['kos', 'brad', 'zalisc', 'star', 'godin', 'glav', 'vlas', 'obrv', 'mrsi'],
        'kljucevi2': ['stolic', 'fotelj', 'klup', 'mest', 'sto', 'sof', 'park', 'sati', 'mirn', 'prozor', 'pod', 'kuć', 'ispred'],
        'mape_grupa1': {
            'sedela': 'sijedila', 'sedeli': 'sijedili', 'sedeo': 'sijedio', 'sedio': 'sijedio',
            'sede': 'sijede', 'sedu': 'sijedu', 'sedi': 'sijedi', 'sedog': 'sijedog', 'sedoh': 'sijedoh'
        },
        'mape_grupa2': {
            'sedela': 'sjedjela', 'sedeli': 'sjedjeli', 'sedeo': 'sjedio', 'sedio': 'sjedio',
            'sede': 'sjede', 'sedu': 'sjedu', 'sedi': 'sjedi', 'sedog': 'sjedog', 'sedoh': 'sjedoh'
        }
    },
   
    {
        'ekavski': ['svet'],
        'kljucevi1': ['zemlj', 'planet', 'ljud', 'narod', 'putov', 'obid', 'držav'],
        'kljucevi2': ['bog', 'crkv', 'otac', 'duh', 'krst', 'ikona', 'svešten', 'vjera'],
        'mape_grupa1': {'svet': 'svijet'},
        'mape_grupa2': {'svet': 'svet'}
    },
    {
        'ekavski': ['leci'],
        'kljucevi1': ['papir', 'prospekt', 'reklam', 'dijel', 'štamp', 'sto', 'kutij'],
        'kljucevi2': ['boles', 'doktor', 'bolnic', 'zdrav', 'lijek', 'pacijent', 'ran'],
        'mape_grupa1': {'leci': 'letci'},
        'mape_grupa2': {'leci': 'liječi'}
    },
    {
        'ekavski': ['bela', 'bele'],
        'kljucevi1': ['boj', 'papir', 'košulj', 'snijeg', 'haljin', 'zid', 'platn'],
        'kljucevi2': ['pladn', 'dan', 'zabel', 'platn', 'košulj', 'zid', 'boj'],
        'mape_grupa1': {'bela': 'bijela', 'bele': 'bijele'},
        'mape_grupa2': {'bela': 'bjelila', 'bele': 'bjelile'}
    },
    {
        'ekavski': ['selo'],
        'kljucevi1': ['mjest', 'mesto', 'livad', 'životinj', 'krav', 'ovc', 'babi', 'ded', 'djed', 'imanj', 'prirod', 'oranic'],
        'kljucevi2': ['stolic', 'fotelj', 'klup', 'mest', 'sto', 'sof', 'park', 'sati', 'mirn', 'prozor', 'pod', 'kuć', 'ispred', 'ptica', 'dete', 'dijete'],
        'mape_grupa1': {'selo': 'selo'}, # selo (mjesto)
        'mape_grupa2': {'selo': 'sjelo'} # sjelo (glagol)
    },
    {
        'ekavski': ['dela'],
        'kljucevi1': ['značajn', 'sabran', 'knjig', 'pisac', 'umetnik', 'umjetnik', 'stvor', 'autor', 'opus', 'bibliotek'],
        'kljucevi2': ['kuć', 'poslovn', 'prostor', 'imovin', 'zemljišt', 'plac', 'soba', 'sprat', 'zgrad', 'dvorišt'],
        'mape_grupa1': {'dela': 'djela'}, # djela (umjetnička)
        'mape_grupa2': {'dela': 'dijela'} # dijela (dijelovi)
    },
 {
        'ekavski': ['veće'],
        'kljucevi1': ['glomazn', 'gabarit', 'velik', 'poras', 'poveć', 'broj', 'dimenzij', 'tež', 'vis', 'šir', 'manj'],
        'kljucevi2': ['zasijed', 'zasjed', 'odbor', 'sudsk', 'ministarsk', 'gradsk', 'odluk', 'član', 'glasan', 'sastan', 'skupštin'],
        'mape_grupa1': {'veće': 'veće'},
        'mape_grupa2': {'veće': 'vijeće'}
    },
{
    'ekavski': ['primene'],
    'kljucevi1': ['znanj', 'teorij', 'praks', 'metod', 'zakon', 'pravil', 'sistem', 'funkcij', 'rezultat'],
    'kljucevi2': ['alat', 'oruđ', 'kupil', 'sprem', 'priprem', 'planir', 'kazn', 'mjer', 'mjere', 'sankcij'],
    'mape_grupa1': {'primene': 'primjene'},
    'mape_grupa2': {'primene': 'primijene'}
},
{
    'ekavski': ['reci'],
    'kljucevi1': ['nekom', 'tati', 'bratu', 'prijatelj', 'kaž', 'rekn', 'istinu', 'poruk', 'pism', 'glasn', 'tiho'],
    'kljucevi2': ['približ', 'obali', 'vod', 'tok', 'most', 'pliv', 'brod', 'čam', 'rib', 'jezer', 'mor', 'morsk'],
    'mape_grupa1': {'reci': 'reci'},
    'mape_grupa2': {'reci': 'rijeci'}
},
{
    'ekavski': ['preko', 'preka'],
    'kljucevi1': ['ljut', 'pogled', 'mrštit', 'osion', 'gled', 'izraz', 'oko', 'reč', 'riječ', 'narav', 'gnev', 'gnijev', 'prekor', 'hladn'],
    'kljucevi2': ['preć', 'stić', 'doć', 'zakorač', 'most', 'prug', 'šin', 'put', 'ulic', 'rijek', 'potok', 'strana','obala','granic'],
    'mape_grupa1': {'preko': 'prijeko', 'preka': 'prijeka'},
    'mape_grupa2': {'preko': 'preko'}
}


]


IMENA_IZUZECI_KORIJENI = ['vera','veri','veru','sedić', 'seden', 'sedlar', 'razbolović', 'slepčević']

def _wb(rijec): return re.compile(r'(?<![^\W\d_])' + re.escape(rijec) + r'(?![^\W\d_])', re.UNICODE | re.IGNORECASE)
def _stem(korijen): return re.compile(r'(?<![^\W\d_])(' + re.escape(korijen) + r')(\w*)', re.UNICODE | re.IGNORECASE)

_EXACT = [(_wb(e), e, i) for e, i in EXACT]
_STEMS = [(_stem(e), e, i) for e, i in STEMS]

def da_li_je_pocetak_recenice(tekst, pozicija):
    p = tekst[:pozicija].strip()
    return True if not p or p[-1] in ['.', '!', '?', '\n', '"', '„', '(', '['] else False

def _sacuvaj_velika_slova(izvorna, zamjena, sufiks=""):
    if izvorna.isupper(): return zamjena.upper() + sufiks.upper()
    if izvorna.istitle(): return zamjena.capitalize() + sufiks
    return zamjena + sufiks

def _primijeni_exact(tekst):
    for pat, e, i in _EXACT:
        def _r(m):
            s = m.group(0)
            if da_li_je_pocetak_recenice(tekst, m.start()):
                if any(s.lower().startswith(korijen) for korijen in IMENA_IZUZECI_KORIJENI):
                    return s
            # POPRAVLJENO: s[0].isupper() provjerava samo veliko početno slovo
            return s if (s[0].isupper() and not da_li_je_pocetak_recenice(tekst, m.start())) else _sacuvaj_velika_slova(s, i)
        tekst = pat.sub(_r, tekst)
    return tekst

def _primijeni_stems(tekst):
    TACNA_IMENA = ['vera', 'veri', 'veru']
    KORIJENI_PREZIMENA = ['sedić', 'seden', 'sedlar', 'razbolović', 'slepčević']
    TEHNICKI_IZUZECI = ['telefon', 'televiz', 'telegram', 'telefons', 'televizij', 'teleskop']
    
    for pat, e, i in _STEMS:
        def _r(m):
            s, suf = m.group(1), m.group(2)
            puna_rec = (s + suf).lower()
            
            if da_li_je_pocetak_recenice(tekst, m.start()):
                if puna_rec in TACNA_IMENA or any(puna_rec.startswith(k) for k in KORIJENI_PREZIMENA):
                    return m.group(0)
                    
            if any(puna_rec.startswith(izuzetak) for izuzetak in TEHNICKI_IZUZECI):
                return m.group(0)
                
            if s[0].isupper() and not da_li_je_pocetak_recenice(tekst, m.start()):
                return m.group(0)
                
            return _sacuvaj_velika_slova(s, i, suf)
            
        tekst = pat.sub(_r, tekst)
    return tekst


def _primijeni_kontekst_prozor(tekst):
    recenice = re.split(r'([.!?\n]+)', tekst)
    novi_delovi = []
    
    for recenica in recenice:
        if not recenica.strip() or re.match(r'^[...!?\n]+$', recenica):
            novi_delovi.append(recenica)
            continue
            
        tokeni = re.split(r'([^\W\d_]+)', recenica, flags=re.UNICODE)
        idx_p = [idx for idx, t in enumerate(tokeni) if re.match(r'^[^\W\d_]+$', t)]
        okolina = recenica.lower()
        
        for i, t_idx in enumerate(idx_p):
            trenutna_rijec = tokeni[t_idx]
            rijec_lower = trenutna_rijec.lower()
            
            if i == 0 and any(rijec_lower.startswith(korijen) for korijen in IMENA_IZUZECI_KORIJENI):
                continue
                
            for mapa in KONTEKST_MAPE:
                if rijec_lower in mapa['ekavski']:
                    skor1 = sum(1 for k in mapa['kljucevi1'] if k in okolina)
                    skor2 = sum(1 for k in mapa['kljucevi2'] if k in okolina)
                    
                    if skor1 > skor2:
                        baza_zamjene = mapa['mape_grupa1']
                    else:
                        baza_zamjene = mapa['mape_grupa2']
                    
                    if rijec_lower in baza_zamjene:
                        tokeni[t_idx] = _sacuvaj_velika_slova(trenutna_rijec, baza_zamjene[rijec_lower])
                        
        novi_delovi.append("".join(tokeni))
        
    return "".join(novi_delovi)

def zamijeni_rijeci(tekst):
    return _primijeni_kontekst_prozor(_primijeni_stems(_primijeni_exact(tekst)))

def obradi_datoteku(ulaz, izlaz):
    if not os.path.isfile(ulaz): print(f"Greška: '{ulaz}'..."); sys.exit(1)
    with open(ulaz, encoding="utf-8") as f: t = f.read()
    with open(izlaz, "w", encoding="utf-8") as f: f.write(zamijeni_rijeci(t))
    print(f"Završeno: '{ulaz}' -> '{izlaz}'")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        obradi_datoteku(sys.argv[1], sys.argv[2])
