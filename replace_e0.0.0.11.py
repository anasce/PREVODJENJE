#E2I PREVODILAC
#Konvertor ekavice u ijekavicu
import sys, os, re 

EXACT = {

    'doprineo': 'doprinio',
    'pretrpeo': 'pretrpio',
    'razboleo': 'razbolio',
    'doživeo': 'doživio',
    'verzija': 'verzija',
    'zamenik': 'zamjenik',
    'celima': 'cijelima',
    'dedama': 'djedovima',
    'drugde': 'drugdje',
    'najpre': 'najprije',
    'napred': 'naprijed',
    'nemima': 'nijemima',
    'prosek': 'prosijek',
    'rečima': 'riječima',
    'svideo': 'svidio',
    'uvideo': 'uvidio',
    'zaseda': 'zasjeda',
    'zasedu': 'zasjedu',
    'zasedi': 'zasjedi',
    'zasede': 'zasjede',
    'zasedama': 'zasjedama',
    'doneo': 'donio',
    'nigde': 'nigdje',
    'pevac': 'kokot',
    'rekao': 'rekao',
    'rekla': 'rekla',
    'rečju': 'riječji',
    'sreda': 'srijeda',
    'svest': 'svijest',
    'uspeo': 'uspio',
    'video': 'vidio',
    'voleo': 'volio',
    'vreme': 'vrijeme',
    'želeo': 'želio',
    'žudeo': 'žudio',
    'deci': 'djeci',
    'deda': 'djed',
    'dede': 'djedovi',
    'dele': 'dijele',
    'dete': 'dijete',
    'hteo': 'htio',
    'leto': 'ljeto',
    'leta': 'ljeta',
    'neme': 'nijeme',
    'nemi': 'nijemi',
    'nemo': 'nijemo',
    'plen': 'plijen',
    'reči': 'riječi',
    'smeo': 'smio',
    'uvek': 'uvijek',
    'uvid': 'uvid',
    'vide': 'vide',
    'vole': 'vole',
    'žele': 'žele',
    'bes': 'bijes',
    'ceo': 'cio',
    'deo': 'dio',
    'dev': 'djev',
    'dve': 'dvije',
    'lek': 'lijek',
    'obe': 'obje',
    'pre': 'prije',
    'reč': 'riječ',
    'sme': 'smije',
}



STEMS = {
    'četvoromeseč': 'četvoromjeseč',
    'desetomeseč': 'desetomjeseč',
    'devetomeseč': 'devetomjeseč',
    'međuzvezdan': 'međuzvjezdan',
    'predstavnik': 'predstavnik',
    'jednomeseč': 'jednomjeseč',
    'pretpostav': 'pretpostav',
    'sedmomeseč': 'sedmmjeseč',
    'šestomeseč': 'šestomjeseč',
    'najzahtev': 'najzahtjev',
    'osmomeseč': 'osmoomjeseč',
    'petomeseč': 'petomjeseč',
    'podrazume': 'podrazumije',
    'pravoverc': 'pravovjern',
    'presecanj': 'presijecanj',
    'bezuspeš': 'bezuspješ',
    'dodeljen': 'dodijeljen',
    'doprinel': 'doprinijel',
    'doprinos': 'doprinios',
    'dragocen': 'dragocjen',
    'dvomeseč': 'dvomjeseč',
    'opredeli': 'opredijeli',
    'opredelj': 'opredjelj',
    'pomeranj': 'pomjeranj',
    'ponedelj': 'ponedjelj',
    'potkolen': 'potkoljen',
    'potpreds': 'potpredsj',
    'predvide': 'predvidje',
    'pregreja': 'pregrija',
    'preteran': 'pretjeran',
    'pretrpel': 'pretrpjel',
    'prosveti': 'prosvjeti',
    'ravnomer': 'ravnomjer',
    'tromeseč': 'tromjeseč',
    'verovatn': 'vjerovatn',
    'zakasnel': 'zakašnjel',
    'zasenjen': 'zasjenjen',
    'zaveštan': 'zavještan',
    'delegat': 'delegat',
    'delimič': 'djelimič',
    'doprine': 'doprinije',
    'doteran': 'dotjeran',
    'doživel': 'doživjel',
    'doživet': 'doživjet',
    'izbegav': 'izbjegav',
    'leticij': 'leticij',
    'letimič': 'letimič',
    'letarg': 'letarg',
    'nadžive': 'nadživje',
    'najlepš': 'najljepš',
    'naleplj': 'naljeplj',
    'napredn': 'napredn',
    'napredo': 'napredo',
    'nasledn': 'nasljedn',
    'neizbež': 'neizbjež',
    'neizmer': 'neizmjer',
    'obavest': 'obavijest',
    'obavešt': 'obavješt',
    'obezbed': 'obezbijed',
    'obezbeđ': 'obezbjeđ',
    'ocenjen': 'ocijenjen',
    'ocenjiv': 'ocjenjiv',
    'odeljak': 'odjeljak',
    'osvedoč': 'osvjedoč',
    'osvetli': 'osvijetli',
    'osvetlj': 'osvjetlj',
    'podsmeh': 'podsmjeh',
    'pogreši': 'pogriješi',
    'pogrešk': 'pogrešk',
    'poletet': 'poletjet',
    'pomešan': 'pomiješan',
    'poverlj': 'povjerlj',
    'povredi': 'povrijedi',
    'prebole': 'prebolje',
    'predlog': 'prijedlog',
    'premest': 'premjest',
    'premešt': 'premješt',
    'prethod': 'prethod',
    'primedb': 'primjedb',
    'primeni': 'primijeni',
    'primenj': 'primijenj',
    'primeti': 'primijeti',
    'procena': 'procjena',
    'procene': 'procjene',
    'proceni': 'procijeni',
    'procenj': 'procjenj',
    'procenu': 'procjenu',
    'promeni': 'promijeni',
    'prosleđ': 'prosljeđ',
    'prosvet': 'prosvjet',
    'rascepi': 'rascijepi',
    'rasejan': 'rasijan',
    'razbole': 'razbolje',
    'razmenj': 'razmjenj',
    'smešten': 'smješten',
    'telefon': 'telefon',
    'umetnik': 'umjetnik',
    'unapređ': 'unaprjeđ',
    'zabelež': 'zabiljež',
    'zahteva': 'zahtijeva',
    'zaplena': 'zapljena',
    'zaplene': 'zapljene',
    'zapleni': 'zaplijeni',
    'zaplenu': 'zapljenu',
    'bekstv': 'bjekstv',
    'cepnut': 'cjepnut',
    'dedukt': 'dedukt',
    'delima': 'djelima',
    'delimi': 'djelimi',
    'detalj': 'detalj',
    'detinj': 'djetinj',
    'dodeli': 'dodijeli',
    'dodelj': 'dodjelj',
    'dospel': 'dospjel',
    'gnezdo': 'gnijezdo',
    'grejat': 'grijat',
    'izgore': 'izgorje',
    'izvesn': 'izvjesn',
    'kolevk': 'kolijevk',
    'menjač': 'mjenjač',
    'nalepi': 'nalijepi',
    'nalepn': 'naljepn',
    'namešt': 'namješt',
    'nasled': 'naslijed',
    'nasmeš': 'nasmiješ',
    'nedelj': 'nedjelj',
    'nemošć': 'nijemošć',
    'neretk': 'nerijetk',
    'neuspe': 'neuspje',
    'nevest': 'nevjest',
    'obelež': 'obiljež',
    'odeven': 'odjeven',
    'otpeva': 'otpjeva',
    'pešačk': 'pješačk',
    'pobedi': 'pobijedi',
    'pobegl': 'pobjegl',
    'podela': 'podjela',
    'podseć': 'podsjeć',
    'pomera': 'pomijera',
    'porekl': 'porijekl',
    'posled': 'posljed',
    'posred': 'posred',
    'potera': 'potjera',
    'povest': 'povijest',
    'povređ': 'povrijeđ',
    'predse': 'predsje',
    'predst': 'predst',
    'preduz': 'preduz',
    'preseć': 'presjeć',
    'prevar': 'prevar',
    'preživ': 'preživj',
    'pridev': 'pridjev',
    'primen': 'primjen',
    'primer': 'primjer',
    'primet': 'primjet',
    'procen': 'procjen',
    'proleć': 'proljeć',
    'promen': 'promjen',
    'prosek': 'prosijek',
    'proseč': 'prosječ',
    'prosle': 'proslije',
    'proter': 'protjer',
    'prover': 'provjer',
    'rascep': 'rascjep',
    'razmen': 'razmijen',
    'razmer': 'razmjer',
    'razreš': 'razriješ',
    'razume': 'razumije',
    'reklam': 'reklam',
    'rešenj': 'rješenj',
    'saoseć': 'saosjeć',
    'saposl': 'zaposlj',
    'savest': 'savjest',
    'sedišt': 'sjedišt',
    'smatra': 'smatra',
    'smejat': 'smijat',
    'stalež': 'stalež',
    'strelj': 'strijelj',
    'svetlo': 'svjetlo',
    'svetsk': 'svjetsk',
    'svugde': 'svugdje',
    'unapre': 'unaprije',
    'uživel': 'uživjel',
    'vaspit': 'vaspit',
    'venčal': 'vjenčal',
    'venčan': 'vjenčan',
    'verbal': 'verbal',
    'verova': 'vjerova',
    'vremen': 'vremen',
    'zahtev': 'zahtjev',
    'zamenj': 'zamjenj',
    'zaplen': 'zaplijen',
    'zapose': 'zaposje',
    'zaposl': 'zapošlj',
    'zapreć': 'zaprijeć',
    'železn': 'željezn',
    'belil': 'bjelil',
    'beleg': 'biljeg',
    'belež': 'biljež',
    'cedil': 'cjedil',
    'celin': 'cjelin',
    'celob': 'celob',
    'celog': 'cijelog',
    'celok': 'celok',
    'cenit': 'cijeniti',
    'cveta': 'cvjeta',
    'decem': 'decem',
    'delat': 'djelat',
    'deleć': 'dijeleć',
    'delim': 'dijelim',
    'delić': 'djelić',
    'delov': 'djelov',
    'detet': 'djetet',
    'devet': 'devet',
    'devoj': 'djevoj',
    'dečač': 'dječač',
    'dodel': 'dodjel',
    'donel': 'donijel',
    'greja': 'grija',
    'greši': 'griješi',
    'hlepč': 'hljepč',
    'izbeg': 'izbjeg',
    'izmen': 'izmijen',
    'izmer': 'izmjer',
    'izned': 'izned',
    'iznet': 'iznijet',
    'izveš': 'izvješ',
    'kolen': 'koljen',
    'kolev': 'kolijev',
    'koren': 'korijen',
    'lekar': 'ljekar',
    'lepil': 'ljepil',
    'lepit': 'lijepit',
    'lepoj': 'ljepoj',
    'lepot': 'ljepot',
    'lestv': 'ljestv',
    'letak': 'letak',
    'letal': 'letal',
    'letel': 'letjel',
    'letis': 'letis',
    'leton': 'leton',
    'levic': 'ljevic',
    'levič': 'ljevič',
    'lečeć': 'liječeć',
    'mesec': 'mjesec',
    'mešav': 'mješav',
    'namer': 'namjer',
    'napad': 'napad',
    'nared': 'nared',
    'nedel': 'nedjel',
    'negde': 'negdje',
    'nemac': 'njemac',
    'nemač': 'njemač',
    'nemoć': 'nemoć',
    'never': 'nevjer',
    'obole': 'obolje',
    'oceni': 'ocijeni',
    'ocenj': 'ocjenj',
    'obest': 'obijest',
    'odelj': 'odjelj',
    'odole': 'odolje',
    'opsed': 'opsjed',
    'oseća': 'osjeća',
    'osmeh': 'osmjeh',
    'osvet': 'osvjet',
    'pesam': 'pjesam',
    'pobeg': 'pobjeg',
    'podel': 'podijel',
    'podne': 'podne',
    'pomer': 'pomjer',
    'posed': 'posjed',
    'poset': 'posjet',
    'poseć': 'posjeć',
    'posle': 'poslije',
    'pover': 'povjer',
    'prene': 'prenije',
    'preti': 'prijeti',
    'rasej': 'rasijan',
    'savet': 'savjet',
    'sever': 'sjever',
    'sleta': 'slijeta',
    'smeja': 'smija',
    'smeni': 'smijeni',
    'smenj': 'smjenj',
    'smest': 'smjest',
    'smešt': 'smješt',
    'svedo': 'svjedo',
    'svesn': 'svjesn',
    'svest': 'svijest',
    'svide': 'svidje',
    'ubeđe': 'ubijeđe',
    'ucena': 'ucjena',
    'ucene': 'ucjene',
    'uceni': 'ucijeni',
    'ucenu': 'ucjenu',
    'umere': 'umjere',
    'umest': 'umjest',
    'umeti': 'umjeti',
    'umetn': 'umjetn',
    'usled': 'usljed',
    'usmer': 'usmjer',
    'uspeh': 'uspjeh',
    'uspev': 'uspijev',
    'uvežb': 'uvježb',
    'uvide': 'uvidje',
    'venac': 'vijenac',
    'vetar': 'vjetar',
    'vežba': 'vježba',
    'videl': 'vidjel',
    'videt': 'vidjet',
    'videv': 'vidjev',
    'zamen': 'zamijen',
    'zamer': 'zamjer',
    'zased': 'zasijed',
    'zaver': 'zavjer',
    'zvezd': 'zvijezd',
    'čovek': 'čovjek',
    'čoveč': 'čovječ',
    'želel': 'željel',
    'želet': 'željet',
    'živel': 'živjel',
    'živeo': 'živio',
    'živet': 'živjet',
    'žudel': 'žudel',
    'beda': 'bijeda',
    'bedn': 'bijedn',
    'besn': 'bijesn',
    'besk': 'besk',
    'besp': 'besp',
    'besv': 'besvj',
    'beža': 'bježa',
    'bled': 'blijed',
    'breg': 'brijeg',
    'cedi': 'cijedi',
    'cel': 'cijel',
    'cena': 'cijena',
    'ceni': 'cijeni',
    'cent': 'cent',
    'cenu': 'cijenu',
    'cvet': 'cvijet',
    'deli': 'dijeli',
    'deci': 'deci',
    'deča': 'dječa',
    'dečj': 'dječij',
    'done': 'donije',
    'dvem': 'dvjem',
    'gnev': 'gnjev',
    'greh': 'grijeh',
    'hleb': 'hljeb',
    'isec': 'isijec',
    'iseć': 'isjeć',
    'koen': 'korijen',
    'leka': 'lijeka',
    'leko': 'ljeko',
    'leku': 'lijeku',
    'lenj': 'lijen',
    'letv': 'letv',
    'mehu': 'mjehu',
    'meri': 'mjeri',
    'mese': 'mjese',
    'mesn': 'mjesn',
    'mest': 'mjest',
    'meša': 'miješa',
    'mlek': 'mlijek',
    'nemc': 'njemc',
    'nežn': 'nježn',
    'obeš': 'obješ',
    'obes': 'objes',
    'ocen': 'ocjen',
    'odel': 'odijel',
    'odeć': 'odjeć',
    'odne': 'odnije',
    'onde': 'ondje',
    'oset': 'osjet',
    'oseć': 'osjeć',
    'ovde': 'ovdje',
    'pesm': 'pjesm',
    'peva': 'pjeva',
    'peša': 'pješa',
    'retk': 'rijetk',
    'rečn': 'rječn',
    'reša': 'rješa',
    'reši': 'riješi',
    'seti': 'sjeti',
    'slep': 'slijep',
    'smeh': 'smijeh',
    'smel': 'smjel',
    'smen': 'smjen',
    'smer': 'smjer',
    'smeš': 'smiješ',
    'sneg': 'snijeg',
    'sten': 'stijen',
    'svež': 'svjež',
    'teme': 'tjeme',
    'tera': 'tjera',
    'tesn': 'tijesn',
    'ubed': 'ubijed',
    'ubeđ': 'ubijeđ',
    'unel': 'unijel',
    'unet': 'unijet',
    'uneš': 'uneš',
    'uspe': 'uspje',
    'uteh': 'utjeh',
    'uver': 'uvjer',
    'veče': 'veče',
    'večn': 'vječn',
    'venc': 'vijenc',
    'venč': 'vjenč',
    'vers': 'vjers',
    'vest': 'vijest',
    'vetr': 'vjetr',
    'veća': 'veća',
    'veće': 'veće',
    'veći': 'veći',
    'vešt': 'vješt',
    'vole': 'volje',
    'volj': 'volj',
    'vred': 'vrijed',
    'vređ': 'vrijeđ',
    'zver': 'zvijer',
    'žele': 'žele',
    'bed': 'bijed',
    'bel': 'bijel',
    'cep': 'cijep',
    'cev': 'cijev',
    'det': 'dijet',
    'deč': 'dječ',
    'dec': 'djec',
    'ded': 'djed',
    'gde': 'gdje',
    'hte': 'htje',
    'len': 'lijen',
    'lep': 'lijep',
    'les': 'ljes',
    'lev': 'lijev',
    'leč': 'liječ',
    'leš': 'lješ',
    'mer': 'mjer',
    'meš': 'mješ',
    'mle': 'mlje',
    'pes': 'pijes',
    'pev': 'pjev',
    'ređ': 'rjeđ',
    'rek': 'rijek',
    'reš': 'rješ',
    'sen': 'sjen',
    'seć': 'sjeć',
    'tel': 'tijel',
    'vek': 'vijek',
    'ver': 'vjer',
    'čov': 'čovj',
}


# Sortiranje po dužini zbog pohlepnog poklapanja korijena
STEMS_SORTED = sorted(STEMS.keys(), key=len, reverse=True)

IMENA_IZUZECI_KORIJENI = ['vera', 'veri', 'veru', 'sedić', 'seden', 'sedlar', 'slep', 'unesk','cvetk']
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
        'ekavski': {'selo', 'sela', 'selu', 'selom', 'selima'},
        'kljucevi2': ['mjest', 'mesto', 'livad', 'životinj', 'krav', 'ovc', 'babi', 'ded', 'djed', 'imanj', 'prirod', 'oranic'],
        'kljucevi1': ['stolic', 'fotelj', 'klup', 'mest', 'sto', 'sof', 'park', 'sati', 'mirn', 'prozor', 'pod', 'kuć', 'ispred', 'ptica', 'dete', 'dijete'],
        'mape_grupa2': {'selo': 'selo', 'sela': 'sela', 'selu': 'selu', 'selom': 'selom', 'selima': 'selima'},
        'mape_grupa1': {'selo': 'sjelo', 'sela': 'sjela', 'selu': 'sjelu', 'selom': 'sjelom', 'selima': 'sjelima'}
    },
    {
        'ekavski': {'dela', 'delu', 'delo', 'delima', 'delom',  'delvima'},
        'kljucevi2': ['značajn', 'sabran', 'knjig', 'pisac', 'umetnik', 'umjetnik', 'stvor', 'autor', 'opus', 'bibliotek', 'kažnj'],
        'kljucevi1': ['kuć', 'poslovn', 'prostor', 'imovin', 'zemljišt', 'plac', 'soba', 'sprat', 'zgrad', 'dvorišt', 'ispit', 'prijemn'],
        'mape_grupa2': {'dela': 'djela', 'delu': 'djelu', 'delo': 'djelo', 'delima': 'djelima', 'delom': 'djelom'},
        'mape_grupa1': {'dela': 'dijela', 'delu': 'dijelu',  'delovima': 'djelovima', 'delom': 'dijelom'}
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
,
       {
        'ekavski': {'nem'},  
        'kljucevi1': [ '(', '.'],
        'kljucevi2': [  'sved', 'svjed', 'osta', 'posta', 'stoj', 'gled', 'sluš', 'glu', 'slep', 'slijep', 'hlad', 'nepom'],
        'mape_grupa1': {'nem': 'njem'},
        'mape_grupa2': {'nem': 'nijem'}  
    }
,
       {
        'ekavski': {'letu','leti'},  
        'kljucevi1': [ 'ptic', 'avio', 'neb', 'heli', 'balo', 'inse', 'pilo', 'eska'],
        'kljucevi2': [  'sunc', 'vruć', 'mor', 'vrel', 'odmo', 'plaž', 'žeg'],
        'mape_grupa1': {'letu': 'letu','leti': 'leti'},
        'mape_grupa2': {'letu': 'ljetu','leti': 'ljeti'}  
    }

]



def _sacuvaj_velika_slova(izv, zam, suf=""):
    if izv.isupper(): return zam.upper() + suf.upper()
    return zam.capitalize() + suf if izv.istitle() else zam + suf

def a_rijec(rijec, is_start, okolni_tekst):
    r_low = rijec.lower()
    if (rijec.istitle() or rijec.isupper()) and any(r_low.startswith(k) for k in IMENA_IZUZECI_KORIJENI):
        return rijec

    # Koristi rječnik EXACT direktno
    if r_low in EXACT:
        return rijec if (rijec.isupper() and not is_start) else _sacuvaj_velika_slova(rijec, EXACT[r_low])
        
    for korijen in STEMS_SORTED:
        if r_low.startswith(korijen):
            suf = rijec[len(korijen):]
            if (is_start and r_low in T_IMENA) or any(r_low.startswith(i) for i in T_IZUZ): return rijec
            if rijec.isupper() and not is_start and rijec in IZUZECI_VELIKO_SLOVO: return rijec
            # Koristi rječnik STEMS direktno
            return _sacuvaj_velika_slova(rijec[:len(korijen)], STEMS[korijen], suf)

    for m in KONTEKST_MAPE:
        if r_low in m['ekavski']:
            skor1 = sum(1 for k in m['kljucevi1'] if k in okolni_tekst)
            skor2 = sum(1 for k in m['kljucevi2'] if k in okolni_tekst)
            baza = m['mape_grupa1'] if skor1 > skor2 else m['mape_grupa2']
            if r_low in baza: return _sacuvaj_velika_slova(rijec, baza[r_low])
        #if len(r_low) > 2 and 'e' in r_low[1:-1]:
         #  print(f"Neprevedena riječ sa unutrašnjim 'e': {rijec}")
                
    return rijec


def procesiraj_recenicu(recenica, predlozak_tekst):
    tokeni = re.split(r'([^\W\d_]+)', recenica, flags=re.U)
    okolni_tekst = recenica.lower()
    is_start = True
    
    for i, tok in enumerate(tokeni):
        if re.match(r'^[^\W\d_]+$', tok):
            tokeni[i] = a_rijec(tok, is_start, okolni_tekst)
            is_start = False
        elif tok.strip(): 
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

def cirilica_u_latinicu(tekst):
    m = {'Љ':'Lj','Њ':'Nj','Џ':'Dž','љ':'lj','њ':'nj','џ':'dž','А':'A','а':'a','Б':'B','б':'b','В':'V','в':'v','Г':'G','г':'g','Д':'D','д':'d','Ђ':'Đ','ђ':'đ','Е':'E','е':'e','Ж':'Ž','ж':'ž','З':'Z','з':'z','И':'I','и':'i','Ј':'J','ј':'j','К':'K','к':'k','Л':'L','л':'l','М':'M','м':'m','Н':'N','н':'n','О':'O','о':'o','П':'P','п':'p','Р':'R','р':'r','С':'S','с':'s','Т':'T','т':'t','Ћ':'Ć','ћ':'ć','У':'U','у':'u','Ф':'F','ф':'f','Х':'H','х':'h','Ц':'C','ц':'c','Ч':'Č','ч':'č','Ш':'Š','ш':'š'}
    return "".join(m.get(c, c) for c in tekst)

def latinica_u_cirilicu(tekst):
    for l, c in [('lj','љ'),('nj','њ'),('dž','џ'),('Lj','Љ'),('Nj','Њ'),('Dž','Џ'),('LJ','Љ'),('NJ','Њ'),('DŽ','Џ')]: tekst = tekst.replace(l, c)
    m = {'A':'А','a':'а','B':'Б','b':'б','V':'В','v':'в','G':'Г','g':'г','D':'Д','d':'д','Đ':'Ђ','đ':'ђ','E':'Е','e':'е','Ž':'Ж','ž':'ж','Z':'З','z':'з','I':'И','i':'и','J':'Ј','j':'ј','K':'К','k':'к','L':'Л','l':'л','M':'М','m':'м','N':'Н','n':'н','O':'О','o':'о','P':'П','p':'п','R':'Р','r':'р','S':'С','s':'с','T':'Т','t':'т','Ć':'Ћ','ć':'ћ','U':'У','u':'у','F':'Ф','f':'ф','H':'Х','h':'х','C':'Ц','c':'ц','Č':'Ч','č':'ч','Š':'Ш','š':'ш'}
    return "".join(m.get(c, c) for c in tekst)

def a_datoteku(ulaz, izlaz):
    if not os.path.isfile(ulaz): print(f"Greška: '{ulaz}'..."); sys.exit(1)
    with open(ulaz, encoding="utf-8") as f: t = f.read()
    with open(izlaz, "w", encoding="utf-8") as f: f.write(zamijeni_rijeci(t))
    print(f"Završeno: '{ulaz}' -> '{izlaz}'")

if __name__ == "__main__":
    if len(sys.argv) == 3: a_datoteku(sys.argv[1], sys.argv[2])
