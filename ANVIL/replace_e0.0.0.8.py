import sys, os, re 



EXACT = [
    ('unapređenjima', 'unaprjeđenjima'),
    ('pravovercima', 'pravovjernima'),
    ('unapređenja', 'unaprjeđenja'),
    ('unapređenje', 'unaprjeđenje'),
    ('unapređenju', 'unaprjeđenju'),
    ('pravoverca', 'pravovjernog'),
    ('pravoverce', 'pravovjerne'),
    ('pravoverci', 'pravovjerni'),
    ('pravovercu', 'pravovjernom'),
    ('celinama', 'cjelinama'),
    ('doprineo', 'doprinio'),
    ('pretrpeo', 'pretrpio'),
    ('razboleo', 'razbolio'),
    ('verbalne', 'verbalne'),
    ('verbalne', 'verbalne'),
    ('verzija', 'verzija'),
    ('verzija', 'verzija'),
    ('zamenik', 'zamjenik'),
    ('celima', 'cijelima'),
    ('celina', 'cjelina'),
    ('celine', 'cjeline'),
    ('celini', 'cjelini'),
    ('celinu', 'cjelinu'),
    ('dedama', 'djedovima'),
    ('dedovi', 'djedovi'),
    ('drugde', 'drugdje'),
    ('najpre', 'najprije'),
    ('napred', 'naprijed'),
    ('nemima', 'nijemima'),
    ('rečima', 'riječima'),
    ('svideo', 'svidio'),
    ('uvideo', 'uvidio'),
    ('doneo', 'donio'),
    ('nigde', 'nigdje'),
    ('pevac', 'kokot'),
    ('rekao', 'rekao'),
    ('rekla', 'rekla'),
    ('rečju', 'riječji'),
    ('sreda', 'srijeda'),
    ('svest', 'svijest'),
    ('uspeo', 'uspio'),
    ('uspeo', 'uspio'),
    ('video', 'vidio'),
    ('vreme', 'vrijeme'),
    ('želeo', 'želio'),
    ('žudeo', 'žudio'),
    ('cela', 'cijela'),
    ('cele', 'cijele'),
    ('celi', 'cijeli'),
    ('celo', 'cijelo'),
    ('celu', 'cijelu'),
    ('dece', 'djece'),
    ('dede', 'djedovi'),
    ('dedi', 'djedi'),
    ('dedu', 'djedu'),
    ('dele', 'dijele'),
    ('dete', 'dijete'),
    ('hteo', 'htio'),
    ('leta', 'ljeta'),
    ('nem.', 'njem.'),
    ('nema', 'nijema'),
    ('neme', 'nijeme'),
    ('nemi', 'nijemi'),
    ('nemo', 'nijemo'),
    ('plen', 'plijen'),
    ('reka', 'rijeka'),
    ('reke', 'rijeke'),
    ('reko', 'rijeko'),
    ('reku', 'rijeku'),
    ('reči', 'riječ'),
    ('smeo', 'smio'),
    ('uvek', 'uvijek'),
    ('uvid', 'uvid'),
    ('vera', 'vjera'),
    ('vere', 'vjere'),
    ('veri', 'vjeri'),
    ('veru', 'vjeru'),
    ('vide', 'vide'),
    ('žele', 'žele'),
    ('bes', 'bijes'),
    ('ceo', 'cio'),
    ('ded', 'djed'),
    ('deo', 'dio'),
    ('dev', 'djev'),
    ('dve', 'dvije'),
    ('lek', 'lijek'),
    ('nem', 'nijem'),
    ('obe', 'obje'),
    ('pre', 'prije'),
    ('reč', 'riječ'),
    ('sme', 'smije'),
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
    ('potpreds', 'potpredsj'),
    ('predvide', 'predvidje'),
    ('pregreja', 'pregrija'),
    ('pretrpel', 'pretrpjel'),
    ('ravnomer', 'ravnomjern'),
    ('tromeseč', 'tromjeseč'),
    ('verovatn', 'vjerovatn'),
    ('zakasnel', 'zakašnjel'),
    ('zaveštan', 'zavještan'),
    ('delegat', 'delegat'),
    ('delimič', 'djelimič'),
    ('izbegav', 'izbjegav'),
    ('letelic', 'letjelic'),
    ('nadžive', 'nadživje'),
    ('napredn', 'napredn'),
    ('napredo', 'napredo'),
    ('neizbež', 'neizbjež'),
    ('neizmer', 'neizmjer'),
    ('obavest', 'obavijest'),
    ('obavešt', 'obavješt'),
    ('obezbed', 'obezbijed'),
    ('obezbeđ', 'obezbjeđ'),
    ('ocenjiv', 'ocjenjiv'),
    ('odeljak', 'odjeljak'),
    ('osvedoč', 'osvjedoč'),
    ('osvetli', 'osvijetli'),
    ('osvetlj', 'osvjetlj'),
    ('podsmeh', 'podsmjeh'),
    ('pogreši', 'pogriješi'),
    ('poverlj', 'povjerlj'),
    ('povredi', 'povrijedi'),
    ('prebole', 'prebolje'),
    ('predlog', 'prijedlog'),
    ('premest', 'premjest'),
    ('premešt', 'premješt'),
    ('prethod', 'prethod'),
    ('primedb', 'primjedb'),
    ('primeni', 'primijeni'),
    ('primenj', 'primijenj'),
    ('procena', 'procjena'),
    ('procene', 'procjene'),
    ('proceni', 'procijeni'),
    ('procenj', 'procjenj'),
    ('procenu', 'procjenu'),
    ('prosleđ', 'prosljeđ'),
    ('rasejan', 'rasijan'),
    ('razbole', 'razbolje'),
    ('razmenj', 'razmjenj'),
    ('razume', 'razumije'),
    ('telefon', 'telefon'),
    ('umetnik', 'umjetnik'),
    ('unapređ', 'unapređ'),
    ('zabelež', 'zabiljež'),
    ('zahteva', 'zahtijeva'),
    ('zaplena', 'zapljena'),
    ('zaplene', 'zapljene'),
    ('zapleni', 'zaplijeni'),
    ('zaplenu', 'zapljenu'),
    ('bekstv', 'bjekstv'),
    ('decemb', 'decemb'),
    ('dedukt', 'dedukt'),
    ('delima', 'djelima'),
    ('delimi', 'djelimi'),
    ('detalj', 'detalj'),
    ('detinj', 'djetinj'),
    ('dodeli', 'dodijeli'),
    ('dodelj', 'dodjelj'),
    ('dospel', 'dospjel'),
    ('dožive', 'doživje'),
    ('gnezdo', 'gnijezdo'),
    ('izgore', 'izgorje'),
    ('izvesn', 'izvjesn'),
    ('izvest', 'izvijest'),
    ('menjač', 'mjenjač'),
    ('nalepn', 'naljepn'),
    ('namešt', 'namješt'),
    ('nasled', 'naslijed'),
    ('nasmeš', 'nasmiješ'),
    ('nedelj', 'nedjelj'),
    ('nemošć', 'nijemošć'),
    ('neretk', 'nerijetk'),
    ('neuspe', 'neuspje'),
    ('obelež', 'obiljež'),
    ('odeven', 'odjeven'),
    ('pešačk', 'pješačk'),
    ('pobedi', 'pobijedi'),
    ('pobegl', 'pobjegl'),
    ('podela', 'podjela'),
    ('podseć', 'podsjeć'),
    ('porekl', 'porijekl'),
    ('posled', 'posljed'),
    ('posred', 'posred'),
    ('povest', 'povijest'),
    ('povređ', 'povrijeđ'),
    ('predse', 'predsje'),
    ('predst', 'predst'),
    ('predst', 'predst'),
    ('preduz', 'preduz'),
    ('preseć', 'presjeć'),
    ('prevar', 'prevar'),
    ('preživ', 'preživ'),
    ('preživ', 'preživj'),
    ('primen', 'primjen'),
    ('primer', 'primjer'),
    ('proleć', 'proljeć'),
    ('promen', 'promjen'),
    ('prosek', 'prosijek'),
    ('proseč', 'prosječ'),
    ('prosle', 'proslije'),
    ('proter', 'protjer'),
    ('prover', 'provjer'),
    ('razmer', 'razmjer'),
    ('razreš', 'razriješ'),
    ('razume', 'razumje'),
    ('razume', 'razumije'),
    ('reklam', 'reklam'),
    ('rešenj', 'rješenj'),
    ('savest', 'savjest'),
    ('smatra', 'smatra'),
    ('stalež', 'stalež'),
    ('strelj', 'strijelj'),
    ('svetlo', 'svjetlo'),
    ('svetsk', 'svjetsk'),
    ('svugde', 'svugdje'),
    ('unapre', 'unaprije'),
    ('vaspit', 'vaspit'),
    ('verova', 'vjerova'),
    ('vremen', 'vremen'),
    ('zahtev', 'zahtjev'),
    ('zahtev', 'zahtijev'),
    ('zamenj', 'zamjenj'),
    ('zamenj', 'zamjenj'),
    ('zaplen', 'zaplijen'),
    ('zapose', 'zaposje'),
    ('zaposl', 'zapošlj'),
    ('beleg', 'biljeg'),
    ('belež', 'biljež'),
    ('celin', 'cjelin'),
    ('celog', 'cijelog'),
    ('cenit', 'cijeniti'),
    ('cveta', 'cvjeta'),
    ('decem', 'decem'),
    ('delat', 'djelat'),
    ('deleć', 'dijeleć'),
    ('delim', 'dijelim'),
    ('delić', 'djelić'),
    ('delić', 'delić'),
    ('detet', 'djetet'),
    ('devet', 'devet'),
    ('devoj', 'djevoj'),
    ('dodel', 'dodjel'),
    ('donel', 'donijel'),
    ('greja', 'grija'),
    ('greši', 'griješi'),
    ('izbeg', 'izbjeg'),
    ('izbeg', 'izbjeg'),
    ('izmen', 'izmijen'),
    ('izmer', 'izmjer'),
    ('izned', 'izned'),
    ('iznet', 'iznijet'),
    ('izveš', 'izvješ'),
    ('kolen', 'koljen'),
    ('kolev', 'kolijev'),
    ('koren', 'korijen'),
    ('lekar', 'ljekar'),
    ('lepot', 'ljepot'),
    ('lepot', 'ljepot'),
    ('letak', 'letak'),
    ('letnj', 'ljetnj'),
    ('levic', 'ljevic'),
    ('levič', 'ljevič'),
    ('mesec', 'mjesec'),
    ('namer', 'namjer'),
    ('napad', 'napad'),
    ('napad', 'napad'),
    ('nared', 'nared'),
    ('nared', 'nared'),
    ('nedel', 'nedjel'),
    ('negde', 'negdje'),
    ('nemac', 'njemac'),
    ('nemač', 'njemač'),
    ('nemoć', 'nemoć'),
    ('never', 'nevjer'),
    ('obole', 'obolje'),
    ('oceni', 'ocijeni'),
    ('ocenj', 'ocjenj'),
    ('odole', 'odolje'),
    ('opsed', 'opsjed'),
    ('oseća', 'osjeća'),
    ('osvet', 'osvjet'),
    ('pobeg', 'pobjeg'),
    ('podel', 'podijel'),
    ('podne', 'podne'),
    ('pomer', 'pomjer'),
    ('pomer', 'pomjer'),
    ('posed', 'posjed'),
    ('poset', 'posjet'),
    ('poseć', 'posjeć'),
    ('posle', 'poslije'),
    ('pover', 'povjer'),
    ('prene', 'prenije'),
    ('preti', 'prijeti'),
    ('rasej', 'rasijan'),
    ('savet', 'savjet'),
    ('sever', 'sjever'),
    ('smeja', 'smija'),
    ('smenj', 'smjenj'),
    ('smest', 'smjest'),
    ('smešt', 'smješt'),
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
    ('veruj', 'vjeruj'),
    ('vetar', 'vjetar'),
    ('videl', 'vidjel'),
    ('volet', 'voljet'),
    ('zamen', 'zamijen'),
    ('zamer', 'zamjer'),
    ('zamer', 'zamjer'),
    ('zased', 'zasijed'),
    ('zaver', 'zavjer'),
    ('zvezd', 'zvijezd'),
    ('zvezd', 'zvjezd'),
    ('zvezd', 'zvijezd'),
    ('čovek', 'čovjek'),
    ('čoveč', 'čovječ'),
    ('želel', 'željel'),
    ('želet', 'željet'),
    ('živel', 'živjel'),
    ('živeo', 'živio'),
    ('živet', 'živjet'),
    ('žudel', 'žudel'),
    ('besn', 'bijesn'),
    ('besv', 'besvj'),
    ('beža', 'bježa'),
    ('bled', 'blijed'),
    ('breg', 'brijeg'),
    ('cena', 'cijena'),
    ('ceni', 'cijeni'),
    ('cent', 'cent'),
    ('cenu', 'cijenu'),
    ('cvet', 'cvijet'),
    ('deca', 'djeca'),
    ('deci', 'djeci'),
    ('deco', 'djeco'),
    ('decu', 'djecu'),
    ('deli', 'dijeli'),
    ('deča', 'dječa'),
    ('done', 'donije'),
    ('dvem', 'dvjem'),
    ('gnev', 'gnjev'),
    ('greh', 'grijeh'),
    ('hleb', 'hljeb'),
    ('leka', 'lijeka'),
    ('leko', 'ljeko'),
    ('leku', 'lijeku'),
    ('lenj', 'lijen'),
    ('leti', 'ljeti'),
    ('leto', 'ljeto'),
    ('letu', 'ljetu'),
    ('mese', 'mjese'),
    ('mesn', 'mjesn'),
    ('mest', 'mjest'),
    ('mlek', 'mlijek'),
    ('nemc', 'njemc'),
    ('nežn', 'nježn'),
    ('ocen', 'ocjen'),
    ('odel', 'odijel'),
    ('odel', 'odjel'),
    ('odeć', 'odjeć'),
    ('odne', 'odnije'),
    ('onde', 'ondje'),
    ('oset', 'osjet'),
    ('oseć', 'osjeć'),
    ('ovde', 'ovdje'),
    ('pesm', 'pjesm'),
    ('peva', 'pjeva'),
    ('peša', 'pješa'),
    ('peša', 'pješa'),
    ('retk', 'rijetk'),
    ('rečn', 'rječn'),
    ('reša', 'rješa'),
    ('reši', 'riješi'),
    ('seti', 'sjeti'),
    ('slep', 'slijep'),
    ('smeh', 'smijeh'),
    ('smel', 'smjel'),
    ('smer', 'smjer'),
    ('sneg', 'snijeg'),
    ('sten', 'stijen'),
    ('teme', 'tjeme'),
    ('tera', 'tjera'),
    ('tesn', 'tijesn'),
    ('ubed', 'ubijed'),
    ('ubeđ', 'ubjeđ'),
    ('unet', 'unijet'),
    ('unel', 'unijel'),
    ('uneš', 'uneš'),
    ('uspe', 'uspje'),
    ('uteh', 'utjeh'),
    ('uver', 'uvjer'),
    ('venc', 'vijenc'),
    ('venč', 'vjenč'),
    ('vero', 'vjero'),
    ('vers', 'vjers'),
    ('vest', 'vijest'),
    ('vetr', 'vjetr'),
    ('veća', 'veća'),
    ('veće', 'veće'),
    ('veći', 'veći'),
    ('vešt', 'vješt'),
    ('volj', 'volj'),
    ('vred', 'vrijed'),
    ('vređ', 'vrijeđ'),
    ('zver', 'zvijer'),
    ('žele', 'žele'),
    ('bed', 'bijed'),
    ('bel', 'bijel'),
    ('cep', 'cijep'),
    ('cev', 'cijev'),
    ('gde', 'gdje'),
    ('hte', 'htje'),
    ('lep', 'lijep'),
    ('les', 'ljes'),
    ('lev', 'lijev'),
    ('leč', 'liječ'),
    ('leš', 'lješ'),
    ('mer', 'mjer'),
    ('meš', 'mješ'),
    ('mle', 'mlje'),
    ('pes', 'pijes'),
    ('pev', 'pjev'),
    ('ređ', 'rjeđ'),
    ('reš', 'rješ'),
    ('sen', 'sjen'),
    ('seć', 'sjeć'),
    ('seć', 'sjeć'),
    ('tel', 'tijel'),
    ('vek', 'vijek'),
    ('več', 'vječ'),

 
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
        'kljucevi2': ['bog', 'crkv', 'otac', 'duh', 'krst', 'ikona', 'svešten', 'vjera','knji','vidi'],
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
    'ekavski': ['dela', 'delu', 'delo', 'delima'],
    'kljucevi1': ['značajn', 'sabran', 'knjig', 'pisac', 'umetnik', 'umjetnik', 'stvor', 'autor', 'opus', 'bibliotek'],

    'kljucevi2': ['kuć', 'poslovn', 'prostor', 'imovin', 'zemljišt', 'plac', 'soba', 'sprat', 'zgrad', 'dvorišt', 'ispit'],
    'mape_grupa1': {'dela': 'djela', 'delu': 'djelu', 'delo': 'djelo', 'delima': 'djelima'}, 

    'mape_grupa2': {'dela': 'dijela', 'delu': 'dijelu'} 
},
 {
        'ekavski': ['veće'],
        'kljucevi1': ['glomazn', 'gabarit', 'velik', 'poras', 'poveć', 'broj', 'dimenzij', 'tež', 'vis', 'šir', 'manj', 'dupl'],
        'kljucevi2': ['zasijed', 'zasjed', 'odbor', 'sudsk', 'ministarsk', 'gradsk', 'odluk', 'član', 'glasan', 'sastan', 'skupštin', 'savet', 'savjet'],
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
    'kljucevi2': ['preć', 'stić', 'doć', 'zakorač', 'most', 'prug', 'šin', 'put', 'ulic', 'rijek', 'potok', 'strana','obala','granic','objav','potrebn'],
    'mape_grupa1': {'preko': 'prijeko', 'preka': 'prijeka'},
    'mape_grupa2': {'preko': 'preko'}
}

,
{
    'ekavski': ['slede','sledi','slediti','sledile','sledila','sledilo'],
    'kljucevi1': ['primjer', 'uputstv', 'pravil', 'savjet', 'savet', 'korak', 'trag', 'put', 'vođ', 'mentor'],
    'kljucevi2': ['krv', 'strah', 'užas', 'šok', 'hladnoć', 'mraz', 'led', 'pogled'],
    'mape_grupa1': {'slede': 'slijede','sledi': 'slijedi','slediti': 'slijediti','sledile': 'slijedile','sledila': 'slijedila','sledilo': 'slijedilo'},
    'mape_grupa2': {'slede': 'slede','sledi': 'sledi','slediti': 'slediti','sledila': 'sledila','sledilo': 'sledilo','sledili': 'sledili'}
}
,
{
    'ekavski': ['sledeća','sledeći','sledeće','sledeću','sledećih'],
    'kljucevi1': ['primjer', 'uputstv', 'pravil', 'savjet', 'savet', 'korak', 'trag', 'put', 'vođ', 'mentor'],
    'kljucevi2':['pacijent', 'bolesnik', 'kandidat', 'učenik', 'kupac', 'gost', 'putnik', 'čovjek','čovek','voz','autobus','čovjek','let','polazak','tokom'] ,
    'mape_grupa1': {'sledeća': 'slijedeća','sledeći': 'slijedeći','sledećih': 'slijedećih'},
    'mape_grupa2': {'sledeća': 'sljedeća','sledeći': 'sljedeći','sledeće': 'sljedeće','sledeću': 'sljedeću','sledećih': 'sljedećih'},

}
]


IMENA_IZUZECI_KORIJENI = ['vera','veri','veru','sedić', 'seden', 'sedlar', 'razbolović', 'slepčević','unesk']

IZUZECI_VELIKO_SLOVO = ['Nemci', 'Nemcima', 'Nemaca','Svetsko', 'Svetskom']

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
                
            if s.isupper() and not da_li_je_pocetak_recenice(tekst, m.start()):
                # Ako je cela reč u listi izuzetaka, ostaje nepromenjena
                if (s + suf) in IZUZECI_VELIKO_SLOVO:
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

def cirilica_u_latinicu(tekst):
    mapa_cir_lat = {
        'Љ': 'Lj', 'Њ': 'Nj', 'Џ': 'Dž', 'љ': 'lj', 'њ': 'nj', 'џ': 'dž',
        'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
        'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Ђ': 'Đ', 'ђ': 'đ',
        'Е': 'E', 'е': 'e', 'Ж': 'Ž', 'ж': 'ž', 'З': 'Z', 'з': 'z',
        'И': 'I', 'и': 'i', 'Ј': 'J', 'ј': 'j', 'К': 'K', 'к': 'k',
        'Л': 'L', 'л': 'l', 'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n',
        'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r',
        'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'Ћ': 'Ć', 'ћ': 'ć',
        'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'H', 'х': 'h',
        'Ц': 'C', 'ц': 'c', 'Č': 'Č', 'č': 'č', 'Ш': 'Š', 'š': 'š'
    }
    return "".join(mapa_cir_lat.get(c, c) for c in tekst)

def latinica_u_cirilicu(tekst):
    za_zamjenu = [
        ('lj', 'љ'), ('nj', 'њ'), ('dž', 'џ'), 
        ('Lj', 'Љ'), ('Nj', 'Њ'), ('Dž', 'Џ'),
        ('LJ', 'Љ'), ('NJ', 'Њ'), ('DŽ', 'Џ')
    ]
    for lat, cir in za_zamjenu:
        tekst = tekst.replace(lat, cir)
        
    mapa_lat_cir = {
        'A': 'А', 'a': 'а', 'B': 'Б', 'b': 'б', 'V': 'В', 'v': 'в',
        'G': 'Г', 'g': 'г', 'D': 'Д', 'd': 'д', 'Đ': 'Ђ', 'đ': 'ђ',
        'E': 'Е', 'e': 'е', 'Ž': 'Ж', 'ž': 'ж', 'Z': 'З', 'z': 'з',
        'I': 'И', 'i': 'и', 'J': 'Ј', 'j': 'ј', 'K': 'К', 'k': 'к',
        'L': 'Л', 'l': 'л', 'M': 'М', 'm': 'м', 'N': 'Н', 'n': 'н',
        'O': 'О', 'o': 'о', 'P': 'П', 'p': 'п', 'R': 'Р', 'r': 'р',
        'S': 'С', 's': 'с', 'T': 'Т', 't': 'т', 'Ć': 'Ћ', 'ć': 'ћ',
        'U': 'У', 'u': 'у', 'F': 'Ф', 'f': 'f', 'H': 'Х', 'h': 'х',
        'C': 'Ц', 'c': 'ц', 'Č': 'Č', 'č': 'č', 'Š': 'Ш', 'š': 'ш'
    }
    return "".join(mapa_lat_cir.get(c, c) for c in tekst)


def zamijeni_rijeci(tekst):
    if not tekst:
        return tekst
        
    cirilica_skup = set('АБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЋУФХЦЧЏШабвгдђежзијклљмнњопрстћуфхцчџш')
    
    tekst_provjera = tekst.lstrip()
    prvo_slovo = tekst_provjera[0] if tekst_provjera else ""
    
    je_cirilica = prvo_slovo in cirilica_skup
    
    if je_cirilica:
        tekst = cirilica_u_latinicu(tekst)
        
    tekst_ijekavski = _primijeni_kontekst_prozor(_primijeni_stems(_primijeni_exact(tekst)))
    
    if je_cirilica:
        return latinica_u_cirilicu(tekst_ijekavski)
        
    return tekst_ijekavski

def obradi_datoteku(ulaz, izlaz):
    if not os.path.isfile(ulaz): print(f"Greška: '{ulaz}'..."); sys.exit(1)
    with open(ulaz, encoding="utf-8") as f: t = f.read()
    with open(izlaz, "w", encoding="utf-8") as f: f.write(zamijeni_rijeci(t))
    print(f"Završeno: '{ulaz}' -> '{izlaz}'")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        obradi_datoteku(sys.argv[1], sys.argv[2])
