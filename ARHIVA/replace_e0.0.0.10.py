#E2I PREVODILAC
#Konvertor ekavice u ijekavicu
import sys, os, re 

EXACT = [
   ('unapređenjima', 'unaprjeđenjima'),
   ('pravovercima', 'pravovjernima'),
   ('deduktivnog', 'deduktivnog'),
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
   ('doživeo', 'doživio'),
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
   ('prosek', 'prosijek'),
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
   ('međuzvezdan', 'međuzvjezdan'),
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
   ('dodeljen', 'dodijeljen'),
   ('doprinel', 'doprinijel'),
   ('doprinos', 'doprinios'),
   ('dragocen', 'dragocjen'),
   ('dvomeseč', 'dvomjeseč'),
   ('opredeli', 'opredijeli'),
   ('opredelj', 'opredjelj'),
   ('pomeranj', 'pomjeranj'),
   ('ponedelj', 'ponedjelj'),
   ('potkolen', 'potkoljen'),
   ('potpreds', 'potpredsj'),
   ('potpreds', 'potpredsj'),
   ('predvide', 'predvidje'),
   ('pregreja', 'pregrija'),
   ('pretrpel', 'pretrpjel'),
   ('ravnomer', 'ravnomjern'),
   ('ravnomer', 'ravnomjer'),
   ('tromeseč', 'tromjeseč'),
   ('verovatn', 'vjerovatn'),
   ('zakasnel', 'zakašnjel'),
   ('zasenjen', 'zasjenjen'),
   ('zaveštan', 'zavještan'),
   ('delegat', 'delegat'),
   ('delimič', 'djelimič'),
   ('doprine', 'doprinije'),
   ('doživet', 'doživjet'),
   ('doživel', 'doživjel'),
   ('izbegav', 'izbjegav'),
   ('letelic', 'letjelic'),
   ('nadžive', 'nadživje'),
   ('naleplj', 'naljeplj'),
   ('napredn', 'napredn'),
   ('napredo', 'napredo'),
   ('nasledn', 'nasljedn'),
   ('neizbež', 'neizbjež'),
   ('neizmer', 'neizmjer'),
   ('obavest', 'obavijest'),
   ('obavešt', 'obavješt'),
   ('obezbed', 'obezbijed'),
   ('obezbeđ', 'obezbjeđ'),
   ('ocenjen', 'ocijenjen'),
   ('ocenjiv', 'ocjenjiv'),
   ('odeljak', 'odjeljak'),
   ('osvedoč', 'osvjedoč'),
   ('osvetli', 'osvijetli'),
   ('osvetlj', 'osvjetlj'),
   ('podsmeh', 'podsmjeh'),
   ('pogreši', 'pogriješi'),
   ('pogrešk', 'pogrešk'),
   ('pomešan', 'pomiješan'),
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
   ('promeni', 'promijeni'),
   ('prosleđ', 'prosljeđ'),
   ('rascepi', 'rascijepi'),
   ('rasejan', 'rasijan'),
   ('razbole', 'razbolje'),
   ('razmenj', 'razmjenj'),
   ('smešten', 'smješten'),
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
   ('gnezdo', 'gnijezdo'),
   ('grejat', 'grijat'),
   ('izgore', 'izgorje'),
   ('izvesn', 'izvjesn'),
   ('menjač', 'mjenjač'),
   ('nalepi', 'nalijepi'),
   ('nalepn', 'naljepn'),
   ('namešt', 'namješt'),
   ('nasled', 'naslijed'),
   ('nasmeš', 'nasmiješ'),
   ('nedelj', 'nedjelj'),
   ('nemošć', 'nijemošć'),
   ('neretk', 'nerijetk'),
   ('neuspe', 'neuspje'),
   ('nevest', 'nevjest'),
   ('obelež', 'obiljež'),
   ('odeven', 'odjeven'),
   ('pešačk', 'pješačk'),
   ('pobedi', 'pobijedi'),
   ('pobegl', 'pobjegl'),
   ('podela', 'podjela'),
   ('podseć', 'podsjeć'),
   ('pomera', 'pomijera'),
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
   ('pridev', 'pridjev'),
   ('primen', 'primjen'),
   ('primer', 'primjer'),
   ('procen', 'procjen'),
   ('proleć', 'proljeć'),
   ('promen', 'promjen'),
   ('prosek', 'prosijek'),
   ('proseč', 'prosječ'),
   ('prosle', 'proslije'),
   ('proter', 'protjer'),
   ('prover', 'provjer'),
   ('rascep', 'rascjep'),
   ('razmen', 'razmijen'),
   ('razmer', 'razmjer'),
   ('razreš', 'razriješ'),
   ('razume', 'razumije'),
   ('razume', 'razumje'),
   ('razume', 'razumije'),
   ('reklam', 'reklam'),
   ('rešenj', 'rješenj'),
   ('saposl', 'zaposlj'),
   ('savest', 'savjest'),
   ('smatra', 'smatra'),
   ('smejat', 'smijat'),
   ('stalež', 'stalež'),
   ('strelj', 'strijelj'),
   ('svetlo', 'svjetlo'),
   ('svetsk', 'svjetsk'),
   ('svugde', 'svugdje'),
   ('unapre', 'unaprije'),
   ('uživel', 'uživjel'),
   ('vaspit', 'vaspit'),
   ('venčal', 'vjenčal'),
   ('venčan', 'vjenčan'),
   ('verova', 'vjerova'),
   ('vremen', 'vremen'),
   ('zahtev', 'zahtjev'),
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
   ('delov', 'djelov'),
   ('detet', 'djetet'),
   ('devet', 'devet'),
   ('devoj', 'djevoj'),
   ('dečač', 'dječač'),
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
   ('lečeć', 'liječeć'),
   ('mesec', 'mjesec'),
   ('mešav', 'mješav'),
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
   ('pesam', 'pjesam'),
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
   ('svesn', 'svjesn'),
   ('svide', 'svidje'),
   ('ubeđe', 'ubijeđe'),
   ('ucena', 'ucjena'),
   ('ucene', 'ucjene'),
   ('uceni', 'ucijeni'),
   ('ucenu', 'ucjenu'),
   ('umere', 'umjere'),
   ('umest', 'umjest'),
   ('umeti', 'umjeti'),
   ('umetn', 'umjetn'),
   ('usled', 'usljed'),
   ('uspeh', 'uspjeh'),
   ('uspev', 'uspijev'),
   ('uvežb', 'uvježb'),
   ('uvide', 'uvidje'),
   ('venac', 'vijenac'),
   ('veruj', 'vjeruj'),
   ('vetar', 'vjetar'),
   ('vežba', 'vježba'),
   ('videl', 'vidjel'),
   ('videt', 'vidjet'),
   ('volel', 'voljel'),
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
   ('dečj', 'dječij'),
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
   ('meša', 'miješa'),
   ('mlek', 'mlijek'),
   ('nemc', 'njemc'),
   ('nežn', 'nježn'),
   ('ocen', 'ocjen'),
   ('odel', 'odijel'),
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
   ('smeš', 'smiješ'),
   ('sneg', 'snijeg'),
   ('sten', 'stijen'),
   ('svež', 'svjež'),
   ('teme', 'tjeme'),
   ('tera', 'tjera'),
   ('tesn', 'tijesn'),
   ('ubed', 'ubijed'),
   ('ubeđ', 'ubjeđ'),
   ('ubeđ', 'ubijeđ'),
   ('unel', 'unijel'),
   ('unet', 'unijet'),
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
   ('det', 'dijet'),
   ('deč', 'dječ'),
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
   ('usp', 'uspj'),
   ('vek', 'vijek'),
   ('več', 'vječ'),
   ('čov', 'čovj'),

]


EXACT_DICT = {k.lower(): v for k, v in EXACT}
STEMS_DICT = {k.lower(): v for k, v in STEMS}

# Sortiranje po dužini zbog pohlepnog poklapanja korijena
STEMS_SORTED = sorted(STEMS_DICT.keys(), key=len, reverse=True)

IMENA_IZUZECI_KORIJENI = ['vera', 'veri', 'veru', 'sedić', 'seden', 'sedlar', 'slep', 'unesk']
IZUZECI_VELIKO_SLOVO = {'Nemci', 'Nemcima', 'Nemaca'}
T_IMENA = {'vera', 'veri', 'veru'}
K_PREZ = ['sedić', 'seden', 'sedlar', 'razbolović', 'slepčević']
T_IZUZ = ['telefon', 'televiz', 'telegram', 'telefons', 'televizij', 'teleskop']

KONTEKST_MAPE = [
    {
        'ekavski': {'sedela', 'sedeli', 'sedeo', 'sedio', 'sede', 'sedu', 'sedi', 'sedog', 'sedoh', 'sedeti'},
        'kljucevi1': ['kos', 'brad', 'zalisc', 'star', 'godin', 'glav', 'vlas', 'obrv', 'mrsi'],
        'kljucevi2': ['stolic', 'fotelj', 'klup', 'mest', 'sto', 'sof', 'park', 'sati', 'mirn', 'prozor', 'pod', 'kuć', 'ispred'],
        'mape_grupa1': {'sedela': 'sijedila', 'sedeli': 'sijedili', 'sedeo': 'sijedio', 'sedio': 'sijedio', 'sede': 'sijede', 'sedu': 'sijedu', 'sedi': 'sijedi', 'sedog': 'sijedog', 'sedoh': 'sijedoh', 'sedeti': 'sijedjeti'},
        'mape_grupa2': {'sedela': 'sjedjela', 'sedeli': 'sjedjeli', 'sedeo': 'sjedio', 'sedio': 'sjedio', 'sede': 'sjede', 'sedu': 'sjedu', 'sedi': 'sjedi', 'sedog': 'sjedog', 'sedoh': 'sjedoh', 'sedeti': 'sjedjeti'}
    },
    {
        'ekavski': {'svet', 'sveta', 'svetu', 'svetom', 'svetovi', 'svetova', 'svetovima'},
        'kljucevi1': ['bog', 'crkv', 'otac', 'duh', 'krst', 'ikona', 'svešten', 'vjera', 'knji', 'vidi'],
        'kljucevi2': ['zemlj', 'planet', 'ljud', 'narod', 'putov', 'obid', 'držav'],
        'mape_grupa1': {'svet': 'svet', 'sveta': 'sveta', 'svetu': 'svetu', 'svetom': 'svetom', 'svetovi': 'svetovi', 'svetova': 'svetova', 'svetovima': 'svetovima'},
        'mape_grupa2': {'svet': 'svijet', 'sveta': 'svijeta', 'svetu': 'svijetu', 'svetom': 'svijetom', 'svetovi': 'svjetovi', 'svetova': 'svjetova', 'svetovima': 'svjetovima'},
    },
    {
        'ekavski': {'bela', 'bele', 'belo', 'belog', 'belom', 'belu', 'beli', 'belih', 'belim'},
        'kljucevi1': ['boj', 'papir', 'košulj', 'snijeg', 'haljin', 'zid', 'platn'],
        'kljucevi2': ['pladn', 'dan', 'zabel', 'platn', 'košulj', 'zid', 'boj'],
        'mape_grupa1': {'bela': 'bijela', 'bele': 'bijele', 'belo': 'bijelo', 'belog': 'bijelog', 'belom': 'bijelom', 'belu': 'bijelu', 'beli': 'bijeli', 'belih': 'bijelih', 'belim': 'bijelim'},
        'mape_grupa2': {'bela': 'bjelila', 'bele': 'bjelile', 'belo': 'bjelilo', 'belog': 'bjelilog', 'belom': 'bjelilom', 'belu': 'bjelilu', 'beli': 'bjelili', 'belih': 'bjelilih', 'belim': 'bjelilim'}
    },
    {
        'ekavski': {'selo', 'sela', 'selu', 'selom', 'selima'},
        'kljucevi2': ['mjest', 'mesto', 'livad', 'životinj', 'krav', 'ovc', 'babi', 'ded', 'djed', 'imanj', 'prirod', 'oranic'],
        'kljucevi1': ['stolic', 'fotelj', 'klup', 'mest', 'sto', 'sof', 'park', 'sati', 'mirn', 'prozor', 'pod', 'kuć', 'ispred', 'ptica', 'dete', 'dijete'],
        'mape_grupa2': {'selo': 'selo', 'sela': 'sela', 'selu': 'selu', 'selom': 'selom', 'selima': 'selima'},
        'mape_grupa1': {'selo': 'sjelo', 'sela': 'sjela', 'selu': 'sjelu', 'selom': 'sjelom', 'selima': 'sjelima'}
    },
    {
        'ekavski': {'dela', 'delu', 'delo', 'delima', 'delom', 'velika dela'},
        'kljucevi1': ['značajn', 'sabran', 'knjig', 'pisac', 'umetnik', 'umjetnik', 'stvor', 'autor', 'opus', 'bibliotek'],
        'kljucevi2': ['kuć', 'poslovn', 'prostor', 'imovin', 'zemljišt', 'plac', 'soba', 'sprat', 'zgrad', 'dvorišt', 'ispit', 'prijemn'],
        'mape_grupa1': {'dela': 'djela', 'delu': 'djelu', 'delo': 'djelo', 'delima': 'djelima', 'delom': 'djelom'},
        'mape_grupa2': {'dela': 'dijela', 'delu': 'dijelu', 'delo': 'dijelo', 'delima': 'dijelovima', 'delom': 'dijelom'}
    },
    {
        'ekavski': {'veće', 'veća', 'veću', 'većim', 'većeg', 'većoj'},
        'kljucevi1': ['glomazn', 'gabarit', 'velik', 'poras', 'poveć', 'broj', 'dimenzij', 'tež', 'vis', 'šir', 'manj', 'dupl'],
        'kljucevi2': ['zasijed', 'zasjed', 'odbor', 'sudsk', 'ministarsk', 'gradsk', 'odluk', 'član', 'glasan', 'sastan', 'skupštin', 'savet', 'savjet'],
        'mape_grupa1': {'veće': 'veće', 'veća': 'veća', 'veću': 'veću', 'većim': 'većim', 'većeg': 'većeg', 'većoj': 'većoj'},
        'mape_grupa2': {'veće': 'vijeće', 'veća': 'vijeća', 'veću': 'vijeću', 'većim': 'vijećima', 'većeg': 'vijeća', 'većoj': 'vijeću'}
    },
    {
        'ekavski': {'primene', 'primena', 'primeni', 'primenu', 'primenom', 'primenama'},
        'kljucevi1': ['znanj', 'teorij', 'praks', 'metod', 'zakon', 'pravil', 'sistem', 'funkcij', 'rezultat'],
        'kljucevi2': ['alat', 'oruđ', 'kupil', 'sprem', 'priprem', 'planir', 'kazn', 'mjer', 'mjere', 'sankcij'],
        'mape_grupa1': {'primene': 'primjene', 'primena': 'primjena', 'primeni': 'primjeni', 'primenu': 'primjenu', 'primenom': 'primjenom', 'primenama': 'primjenama'},
        'mape_grupa2': {'primene': 'primijene', 'primena': 'primijene', 'primeni': 'primijene', 'primenu': 'primijene', 'primenom': 'primijene', 'primenama': 'primijene'}
    },
    {
        'ekavski': {'reci', 'recima'},
        'kljucevi1': ['nekom', 'tati', 'bratu', 'prijatelj', 'kaž', 'rekn', 'istinu', 'poruk', 'pism', 'glasn', 'tiho'],
        'kljucevi2': ['približ', 'obali', 'vod', 'tok', 'most', 'pliv', 'brod', 'čam', 'rib', 'jezer', 'mor', 'morsk'],
        'mape_grupa1': {'reci': 'reci', 'recima': 'recima'},
        'mape_grupa2': {'reci': 'rijeci', 'recima': 'riječima'}
    },
    {
        'ekavski': {'preko', 'preka', 'preke', 'preku', 'preki', 'prekog', 'prekom'},
        'kljucevi1': ['ljut', 'pogled', 'mrštit', 'osion', 'gled', 'izraz', 'oko', 'reč', 'riječ', 'narav', 'gnev', 'gnijev', 'prekor', 'hladn'],
        'kljucevi2': ['preć', 'stić', 'doć', 'zakorač', 'most', 'prug', 'šin', 'put', 'ulic', 'rijek', 'potok', 'strana', 'obala', 'granic', 'objav', 'potrebn'],
        'mape_grupa1': {'preko': 'prijeko', 'preka': 'prijeka', 'preke': 'prijeke', 'preku': 'prijeku', 'preki': 'prijeki', 'prekog': 'prijekog', 'prekom': 'prijekom'},
        'mape_grupa2': {'preko': 'preko', 'preka': 'preka', 'preke': 'preke', 'preku': 'preku', 'preki': 'preki', 'prekog': 'prekog', 'prekom': 'prekom'}
    },
    {
        'ekavski': {'slede', 'sledi', 'slediti', 'sledile', 'sledila', 'sledilo', 'sledili'},
        'kljucevi1': ['krv', 'strah', 'užas', 'šok', 'hladnoć', 'mraz', 'led', 'pogled'],
        'kljucevi2': ['primjer', 'uputstv', 'pravil', 'savjet', 'savet', 'korak', 'trag', 'put', 'vođ', 'mentor'],
        'mape_grupa1': {'slede': 'slede', 'sledi': 'sledi', 'slediti': 'slediti', 'sledila': 'sledila', 'sledilo': 'sledilo', 'sledili': 'sledili'},
        'mape_grupa2': {'slede': 'slijede', 'sledi': 'slijedi', 'slediti': 'slijediti', 'sledile': 'slijedile', 'sledila': 'slijedila', 'sledilo': 'slijedilo', 'sledili': 'slijedili'},

    },
    {
        'ekavski': {'sledeća', 'sledeći', 'sledeće', 'sledeću', 'sledećih', 'sledećem', 'sledećog', 'sledećima'},
        'kljucevi1': ['prim', 'uputstv', 'pravil', 'savjet', 'savet', 'korak', 'trag', 'put', 'vođ', 'mentor'],
        'kljucevi2': ['pacijent', 'bolesnik', 'kandidat', 'učenik', 'kupac', 'gost', 'putnik', 'čovjek', 'čovek', 'voz', 'autobus', 'let', 'polazak', 'tokom'],
        'mape_grupa1': {'sledeća': 'slijedeća', 'sledeći': 'slijedeći', 'sledeće': 'slijedeće', 'sledeću': 'slijedeću', 'sledećih': 'slijedećih', 'sledećem': 'slijedećem', 'sledećog': 'slijedećeg', 'sledećima': 'slijedećima'},
        'mape_grupa2': {'sledeća': 'sljedeća', 'sledeći': 'sljedeći', 'sledeće': 'sljedeće', 'sledeću': 'sljedeću', 'sledećih': 'sljedećih', 'sledećem': 'sljedećem', 'sledećog': 'sljedećem', 'sledećima': 'sljedećima'}
    }
,
    {
        'ekavski': {'nema'},
        'kljucevi1': ['ust', 'žen', 'dev', 'djev', 'sved', 'svjed', 'osta', 'posta', 'stoj', 'gled', 'sluš', 'glu', 'slep', 'slijep', 'hlad', 'nepom'],
        'kljucevi2': ['vrem', 'novc', 'prav', 'smisl', 'nad', 'mest', 'mjest', 'izbor', 'nedost', 'ništ', 'niko', 'viš', 'dovolj', 'ničeg'],
        'mape_grupa1': {'nema':'nijema'},
        'mape_grupa2': {'nema': 'nema'}
    }
,
       {
        'ekavski': {'izvesti'},
        'kljucevi1': [ 'doga', 'inform',  'medij', 'program', 'uživo', 'javnost', 'gledaoc', 'narod', 'izvešt', 'izvešt'],
        'kljucevi2': ['izlazak', 'perform', 'predst', 'koncert', 'rest', 'grad', 'večer', 'ručak', 'klub', 'šetnj', 'pić', 'premijer', 'scena', 'pjesm'],
        'mape_grupa1': {'izvesti': 'izvijesti'},
        'mape_grupa2': {'izvesti': 'izvesti'}  
    }

]


def _sacuvaj_velika_slova(izv, zam, suf=""):
    if izv.isupper(): return zam.upper() + suf.upper()
    return zam.capitalize() + suf if izv.istitle() else zam + suf

def obradi_rijec(rijec, is_start, okolni_tekst):
    r_low = rijec.lower()
    if (rijec.istitle() or rijec.isupper()) and any(r_low.startswith(k) for k in IMENA_IZUZECI_KORIJENI):
        return rijec

    if r_low in EXACT_DICT:
        return rijec if (rijec.isupper() and not is_start) else _sacuvaj_velika_slova(rijec, EXACT_DICT[r_low])
        
    for korijen in STEMS_SORTED:
        if r_low.startswith(korijen):
            suf = rijec[len(korijen):]
            if (is_start and r_low in T_IMENA) or any(r_low.startswith(i) for i in T_IZUZ): return rijec
            if rijec.isupper() and not is_start and rijec in IZUZECI_VELIKO_SLOVO: return rijec
            return _sacuvaj_velika_slova(rijec[:len(korijen)], STEMS_DICT[korijen], suf)

    for m in KONTEKST_MAPE:
        if r_low in m['ekavski']:
            skor1 = sum(1 for k in m['kljucevi1'] if k in okolni_tekst)
            skor2 = sum(1 for k in m['kljucevi2'] if k in okolni_tekst)
            baza = m['mape_grupa1'] if skor1 > skor2 else m['mape_grupa2']
            if r_low in baza: return _sacuvaj_velika_slova(rijec, baza[r_low])
        if len(r_low) > 2 and 'e' in r_low[1:-1]:
           print(f"Neprevedena riječ sa unutrašnjim 'e': {rijec}")
                
    return rijec


def procesiraj_recenicu(recenica, predlozak_tekst):
    # Splituje rečenicu na riječi i ne-riječi (interpunkciju/razmake)
    tokeni = re.split(r'([^\W\d_]+)', recenica, flags=re.U)
    okolni_tekst = recenica.lower()
    
    is_start = True # Prva riječ na koju naiđemo biće početak rečenice
    
    for i, tok in enumerate(tokeni):
        if re.match(r'^[^\W\d_]+$', tok): # Ako je riječ
            tokeni[i] = obradi_rijec(tok, is_start, okolni_tekst)
            is_start = False # Sve sledeće riječi u rečenici nisu početak
        elif tok.strip(): 
            # Ako token sadrži interpunkciju koja završava rečenicu unutar ovog bloka
            if any(c in tok for c in ['.', '!', '?', '\n', '"', '„', '(', '[']):
                is_start = True
                
    return "".join(tokeni)

def zamijeni_rijeci(tekst):
    if not tekst: return tekst
    
    linije = tekst.splitlines(keepends=True)
    procesuirane_linije = []
    cirilica_skup = set('АБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЋУФХЦЧЏШабвгдђежзијклљмнњопрстћуфхцчџш')
    
    for linija in linije:
        tekst_strip = linija.strip()
        if not tekst_strip:
            procesuirane_linije.append(linija)
            continue
            
        je_cirilica = tekst_strip[0] in cirilica_skup
        trenutni_tekst = cirilica_u_latinicu(linija) if je_cirilica else linija
        
        # Dijeljenje na rečenice radi tačnog kontekstnog prozora
        recenice = re.split(r'([.!?\n]+)', trenutni_tekst)
        novi_djelovi = []
        
        for dio in recenice:
            if not dio.strip() or re.match(r'^[...!?\n]+$', dio):
                novi_djelovi.append(dio)
            else:
                novi_djelovi.append(procesiraj_recenicu(dio, trenutni_tekst))
                
        tekst_ijekavski = "".join(novi_djelovi)
        
        if je_cirilica:
            procesuirane_linije.append(latinica_u_cirilicu(tekst_ijekavski))
        else:
            procesuirane_linije.append(tekst_ijekavski)
            
    return "".join(procesuirane_linije)

# Pomoćne funkcije za transliteraciju (ostaju iste)
def cirilica_u_latinicu(tekst):
    m = {'Љ':'Lj','Њ':'Nj','Џ':'Dž','љ':'lj','њ':'nj','џ':'dž','А':'A','а':'a','Б':'B','б':'b','В':'V','в':'v','Г':'G','г':'g','Д':'D','д':'d','Ђ':'Đ','ђ':'đ','Е':'E','е':'e','Ж':'Ž','ж':'ž','З':'Z','з':'z','И':'I','и':'i','Ј':'J','ј':'j','К':'K','к':'k','Л':'L','л':'l','М':'M','м':'m','Н':'N','н':'n','О':'O','о':'o','П':'P','п':'p','Р':'R','р':'r','С':'S','с':'s','Т':'T','т':'t','Ћ':'Ć','ћ':'ć','У':'U','у':'u','Ф':'F','ф':'f','Х':'H','х':'h','Ц':'C','ц':'c','Ч':'Č','ч':'č','Ш':'Š','ш':'š'}
    return "".join(m.get(c, c) for c in tekst)

def latinica_u_cirilicu(tekst):
    for l, c in [('lj','љ'),('nj','њ'),('dž','џ'),('Lj','Љ'),('Nj','Њ'),('Dž','Џ'),('LJ','Љ'),('NJ','Њ'),('DŽ','Џ')]: tekst = tekst.replace(l, c)
    m = {'A':'А','a':'а','B':'Б','b':'б','V':'В','v':'в','G':'Г','g':'г','D':'Д','d':'д','Đ':'Ђ','đ':'ђ','E':'Е','e':'е','Ž':'Ж','ž':'ж','Z':'З','z':'з','I':'И','i':'и','J':'Ј','j':'ј','K':'К','k':'к','L':'Л','l':'л','M':'М','m':'м','N':'Н','n':'н','O':'О','o':'о','P':'П','p':'п','R':'Р','r':'р','S':'С','s':'с','T':'Т','t':'т','Ć':'Ћ','ć':'ћ','U':'У','u':'у','F':'Ф','f':'ф','H':'Х','h':'х','C':'Ц','c':'ц','Č':'Ч','č':'ч','Š':'Ш','š':'ш'}
    return "".join(m.get(c, c) for c in tekst)

def obradi_datoteku(ulaz, izlaz):
    if not os.path.isfile(ulaz): print(f"Greška: '{ulaz}'..."); sys.exit(1)
    with open(ulaz, encoding="utf-8") as f: t = f.read()
    with open(izlaz, "w", encoding="utf-8") as f: f.write(zamijeni_rijeci(t))
    print(f"Završeno: '{ulaz}' -> '{izlaz}'")

if __name__ == "__main__":
    if len(sys.argv) == 3: obradi_datoteku(sys.argv[1], sys.argv[2])
