# E2I PREVODILAC - Optimizovan, keširan i 100% kompatibilan sa Anvil/Skulpt okruženjem
import re

try:
    import sys
    import os
    IMA_OS = True
except ImportError:
    IMA_OS = False

EXACT = {
    'anae': 'anaeaa', 'razmenama': 'razmjenama', 'bezgrešan': 'bezgriješan',
    'nesvestan': 'nesvjestan', 'verovatan': 'vjerovatan', 'zahtevima': 'zahtjevima',
    'izvestan': 'izvjestan', 'netrezan': 'netrijezan', 'neutešan': 'neutješan',
    'razmenom': 'razmjenom', 'svetlost': 'svjetlost', 'zasedama': 'zasjedama',
    'nemošću': 'nijemošću', 'preseći': 'presjeći', 'razmena': 'razmjena',
    'razmenu': 'razmjenu', 'senkama': 'sjenkama', 'svestan': 'svjestan',
    'svećama': 'svijećama', 'verzija': 'verzija', 'zahteve': 'zahtjeve',
    'zahtevu': 'zahtjevu', 'zahtevi': 'zahtjevi', 'zavesom': 'zavjesom',
    'belima': 'bijelima', 'celima': 'cijelima', 'dedama': 'djedovima',
    'drugde': 'drugdje', 'grešan': 'griješan', 'gdegod': 'gdjegod',
    'najpre': 'najprije', 'napred': 'naprijed', 'nemima': 'nijemima',
    'oduvek': 'oduvijek', 'peskom': 'pijeskom', 'odseći': 'odsjeći',
    'peškir': 'peškir', 'poseći': 'posjeći', 'prosek': 'prosijek',
    'rečima': 'riječima', 'rekama': 'rijekama', 'senkom': 'sjenkom',
    'smešan': 'smiješan', 'sredom': 'srijedom', 'srećan': 'srećan',
    'svećom': 'svijećom', 'trezan': 'trijezan', 'utešan': 'utješan',
    'zaseći': 'zasjeći', 'zaseda': 'zasjeda', 'zasede': 'zasjede',
    'zasedi': 'zasjedi', 'zasedu': 'zasjedu', 'zahtev': 'zahtjev',
    'zauvek': 'zauvijek', 'zavesa': 'zavjesa', 'zavese': 'zavjese',
    'zavesi': 'zavjesi', 'zavesu': 'zavjesu', 'beloj': 'bijeloj',
    'celoj': 'cijeloj', 'dedom': 'djedom', 'iseći': 'isjeći',
    'nigde': 'nigdje', 'odeća': 'odjeća', 'odeći': 'odjeći',
    'odeću': 'odjeću', 'otpre': 'otprije', 'pesak': 'pijesak',
    'peska': 'pijeska', 'pesku': 'pijesku', 'pevac': 'kokot',
    'rekao': 'rekao', 'rekla': 'rekla', 'rekom': 'rijekom',
    'razne': 'razne', 'rečju': 'riječju', 'senka': 'sjenka',
    'senke': 'sjenke', 'senci': 'sjenci', 'senku': 'sjenku',
    'sreda': 'srijeda', 'sredu': 'srijedu', 'svest': 'svijest',
    'sveća': 'svijeća', 'sveće': 'svijeće', 'sveću': 'svijeću',
    'sveći': 'svijeći', 'svećo': 'svijećo', 'tesan': 'tijesan',
    'vreme': 'vrijeme', 'bela': 'bijela', 'bele': 'bijele',
    'beli': 'bijeli', 'belo': 'bijelo', 'belu': 'bijelu',
    'cela': 'cijela', 'cele': 'cijele', 'celi': 'cijeli',
    'celo': 'cijelo', 'celu': 'cijelu', 'deca': 'djeca',
    'dece': 'djece', 'deci': 'djeci', 'deco': 'djeco',
    'decu': 'djecu', 'deda': 'djed', 'dede': 'djedovi',
    'dedu': 'djedu', 'dedi': 'djedi', 'dele': 'dijele',
    'dete': 'dijete', 'dole': 'dolje', 'hteo': 'htio',
    'igde': 'igdje', 'lepa': 'lijepa', 'lepe': 'lijepe',
    'lepi': 'lijepi', 'lepo': 'lijepo', 'lepu': 'lijepu',
    'leta': 'ljeta', 'leto': 'ljeto', 'mera': 'mjera',
    'mere': 'mjere', 'meri': 'mjeri', 'meru': 'mjeru',
    'neme': 'nijeme', 'nemi': 'nijemi', 'nemo': 'nijemo',
    'nisu': 'nijesu', 'plen': 'plijen', 'reči': 'riječi',
    'reka': 'rijeka', 'reke': 'rijeke', 'reci': 'rijeci',
    'reku': 'rijeku', 'seći': 'sjeći', 'smeo': 'smio',
    'tela': 'tijela', 'telo': 'tijelo', 'telu': 'tijelu',
    'umeo': 'umio', 'uvek': 'uvijek', 'uvid': 'uvid',
    'veka': 'vijeka', 'veku': 'vijeku', 'vide': 'vide',
    'vole': 'vole', 'žele': 'žele', 'beo': 'bijel',
    'bes': 'bijes', 'ceo': 'cio', 'cev': 'cijev',
    'deo': 'dio', 'dev': 'djev', 'dve': 'dvije',
    'gde': 'gdje', 'lek': 'lijek', 'lep': 'lijep',
    'leš': 'leš', 'obe': 'obje', 'pre': 'prije',
    'reč': 'riječ', 'sme': 'smije', 'ume': 'umije',
    'vek': 'vijek',
}

STEMS = {
    'drugostepen': 'drugostepen', 'međuzvezdan': 'međuzvjezdan', 'predstavnik': 'predstavnik',
    'nepogrešiv': 'nepogrešiv', 'nepoverenj': 'nepovjerenj', 'obaveštenj': 'obavještenj',
    'pretpostav': 'pretpostav', 'najzahtev': 'najzahtjev', 'podrazume': 'podrazumije',
    'pravoverc': 'pravovjern', 'presecanj': 'presijecanj', 'razrešenj': 'razrješenj',
    'snabdeven': 'snabdjeven', 'sprečavanj': 'sprječavanj', 'unapređenj': 'unaprjeđenj',
    'dodeljen': 'dodijeljen', 'doprinos': 'doprinios', 'dragocen': 'dragocjen',
    'izvestan': 'izvjestan', 'opredeli': 'opredijeli', 'opredelj': 'opredjelj',
    'petomese': 'petomjese', 'pomeranj': 'pomjeranj', 'ponedelj': 'ponedjelj',
    'potkolen': 'potkoljen', 'potpreds': 'potpredsj', 'poverenj': 'povjerenj',
    'predvide': 'predvidje', 'pregreja': 'pregrija', 'preteran': 'pretjeran',
    'pretrpel': 'pretrpjel', 'primenju': 'primjenju', 'privredn': 'privredn',
    'prosveti': 'prosvjeti', 'ravnomer': 'ravnomjer', 'sporazum': 'sporazum',
    'svestran': 'svestran', 'verovatn': 'vjerovatn', 'zahtevat': 'zahtijevat',
    'zakasnel': 'zakašnjel', 'zasenjen': 'zasjenjen', 'zastarel': 'zastarjel',
    'zaveštan': 'zavještan', 'bezuspe': 'bezuspje', 'crvenet': 'crvenjet',
    'crvenel': 'crvenjel', 'delegat': 'delegat', 'delikat': 'delikat',
    'doprine': 'doprinije', 'doteran': 'dotjeran', 'doživel': 'doživjel',
    'doživet': 'doživjet', 'izbegav': 'izbjegav', 'leticij': 'leticij',
    'malolet': 'maloljet', 'nadžive': 'nadživje', 'naleplj': 'naljeplj',
    'napredn': 'napredn', 'napredo': 'napredo', 'napretk': 'napretk',
    'nasledn': 'nasljedn', 'neizmer': 'neizmjer', 'neizbež': 'neizbjež',
    'neverov': 'nevjerov', 'obavest': 'obavijest', 'obavešt': 'obavješt',
    'obezbed': 'obezbijed', 'obezbeđ': 'obezbjeđ', 'ocenjen': 'ocijenjen',
    'ocenjiv': 'ocjenjiv', 'odeljak': 'odjeljak', 'osvedoč': 'osvjedoč',
    'osvetli': 'osvijetli', 'osvetlj': 'osvjetlj', 'penelop': 'penelop',
    'podsmeh': 'podsmjeh', 'pogreši': 'pogriješi', 'pogrešk': 'pogrešk',
    'poletet': 'poletjet', 'pomešan': 'pomiješan', 'poverlj': 'povjerlj',
    'povreda': 'povreda', 'povredu': 'povredu', 'prebole': 'prebolje',
    'predlog': 'prijedlog', 'premest': 'premjest', 'premešt': 'premješt',
    'prethod': 'prethod', 'primedb': 'primjedb', 'primeni': 'primijeni',
    'primeno': 'primjeno', 'primenj': 'primijenj', 'primeti': 'primijeti',
    'procena': 'procjena', 'procenj': 'procjenj', 'procenu': 'procjenu',
    'promeni': 'promijeni', 'prosvet': 'prosvjet', 'punolet': 'punoljet',
    'rascepi': 'rascijepi', 'rasejan': 'rasijan', 'razbole': 'razbolje',
    'razmenj': 'razmjenj', 'smešten': 'smješten', 'snabdev': 'snabdijev',
    'telefon': 'telefon', 'tromese': 'tromjese', 'umetnik': 'umjetnik',
    'verenik': 'vjerenik', 'vrednov': 'vrednov', 'zamenic': 'zamjenic',
    'zamenik': 'zamjenik', 'zaplena': 'zapljena', 'zaplene': 'zapljene',
    'zapleni': 'zaplijeni', 'zaplenu': 'zapljenu', 'belešk': 'bilješk',
    'bekstv': 'bjekstv', 'bezbed': 'bezbjed', 'cepnut': 'cjepnut',
    'dedukt': 'dedukt', 'delimi': 'djelimi', 'delima': 'djelima',
    'detalj': 'detalj', 'detinj': 'djetinj', 'dodeli': 'dodijeli',
    'dodelj': 'dodjelj', 'dospel': 'dospjel', 'eksten': 'eksten',
    'gnezdo': 'gnijezdo', 'grejat': 'grijat', 'izgore': 'izgorje',
    'izmena': 'izmjena', 'izvesn': 'izvjesn', 'kolevk': 'kolijevk',
    'lepljiv': 'ljepljiv', 'letarg': 'letarg', 'letimi': 'letimi',
    'medved': 'medvjed', 'menjač': 'mjenjač', 'mleven': 'mljeven',
    'najlep': 'najljep', 'nalepi': 'nalijepi', 'nalepn': 'naljepn',
    'namenj': 'namijenj', 'namešt': 'namješt', 'nasled': 'naslijed',
    'navest': 'navest', 'navode': 'navode', 'nedelj': 'nedjelj',
    'neizbe': 'neizbje', 'neretk': 'nerijetk', 'neuspe': 'neuspje',
    'nevest': 'nevjest', 'odeven': 'odjeven', 'otpeva': 'otpjeva',
    'pesnik': 'pjesnik', 'pesnič': 'pjesnič', 'pesnic': 'pjesnic',
    'pešačk': 'pješačk', 'peščan': 'pješčan', 'pevanj': 'pjevanj',
    'pismen': 'pismen', 'pobedi': 'pobijedi', 'pobegl': 'pobjegl',
    'podela': 'podjela', 'podelj': 'podijelj', 'podseć': 'podsjeć',
    'pomera': 'pomijera', 'porekl': 'porijekl', 'poretk': 'poretk',
    'posled': 'posljed', 'posred': 'posred', 'posvet': 'posvet',
    'potera': 'potjera', 'povest': 'povijest', 'predse': 'predsje',
    'predst': 'predst', 'preduz': 'preduz', 'prenes': 'prenes',
    'presel': 'presel', 'prevar': 'prevar', 'preživ': 'preživj',
    'pridev': 'pridjev', 'primer': 'primjer', 'primet': 'primjet',
    'prispe': 'prispje', 'procen': 'procjen', 'promen': 'promjen',
    'prosek': 'prosijek', 'prosle': 'proslije', 'proter': 'protjer',
    'prover': 'provjer', 'rascep': 'rascjep', 'razmer': 'razmjer',
    'razume': 'razumije', 'redosl': 'redoslj', 'reklam': 'reklam',
    'rešenj': 'rješenj', 'revers': 'revers', 'saposl': 'zaposlj',
    'savest': 'savjest', 'sečenj': 'sječenj', 'sedišt': 'sjedišt',
    'semest': 'semest', 'smatra': 'smatra', 'smejat': 'smijat',
    'stepen': 'stepen', 'strelj': 'strijelj', 'svetlo': 'svjetlo',
    'svetsk': 'svjetsk', 'svećnj': 'svijećnj', 'svugde': 'svugdje',
    'stedet': 'stedjet', 'stidet': 'stidjet', 'stidel': 'stidjel',
    'štedet': 'štedjet', 'štedel': 'štedjel', 'ubeđen': 'ubijeđen',
    'unapre': 'unaprije', 'unešen': 'unešen', 'usmeni': 'usmeni',
    'uživel': 'uživjel', 'vaspit': 'vaspit', 'venčal': 'vjenčal',
    'venčan': 'vjenčan', 'verbal': 'verbal', 'vernic': 'vjernic',
    'verova': 'vjerova', 'volont': 'volont', 'vremen': 'vremen',
    'zabele': 'zabilje', 'zameni': 'zamijeni', 'zamenj': 'zamjenj',
    'zaplen': 'zaplijen', 'zapose': 'zaposje', 'zaposl': 'zapošlj',
    'železn': 'željezn', 'ameri': 'ameri', 'beleg': 'biljeg',
    'belež': 'biljež', 'belil': 'bjelil', 'belog': 'bjelog',
    'bolet': 'boljet', 'bolel': 'boljel', 'cedil': 'cjedil',
    'celin': 'cjelin', 'celob': 'celob', 'celog': 'cijelog',
    'celok': 'celok', 'cenar': 'cenar', 'cenit': 'cijenit',
    'cepan': 'cjepan', 'cepaj': 'cijepaj', 'cveta': 'cvjeta',
    'decem': 'decem', 'delat': 'djelat', 'delim': 'dijelim',
    'delov': 'djelov', 'deluj': 'djeluj', 'detet': 'djetet',
    'devet': 'devet', 'devoj': 'djevoj', 'dečač': 'dječač',
    'dodel': 'dodjel', 'donel': 'donijel', 'dones': 'dones',
    'goret': 'gorjet', 'gorel': 'gorjel', 'greja': 'grija',
    'greši': 'griješi', 'grešn': 'griješn', 'hlepč': 'hljepč',
    'inves': 'inves', 'isten': 'isten', 'izmer': 'izmjer',
    'izned': 'izned', 'iznet': 'iznijet', 'izves': 'izvjes',
    'izveš': 'izvješ', 'kamer': 'kamer', 'karak': 'karak',
    'kolen': 'koljen', 'kolev': 'kolijev', 'koren': 'korijen',
    'kvenc': 'kvenc', 'lekar': 'ljekar', 'lekov': 'ljekov',
    'lepil': 'ljepil', 'lepit': 'lijepit', 'lepoj': 'ljepoj',
    'lepot': 'ljepot', 'lestv': 'ljestv', 'letak': 'letak',
    'letal': 'letal', 'letel': 'letjel', 'letet': 'letjet',
    'letis': 'letis', 'letnj': 'ljetnj', 'leton': 'leton',
    'levic': 'ljevic', 'levič': 'ljevič', 'lečeć': 'liječeć',
    'liter': 'liter', 'menja': 'mijenja', 'meram': 'mjeram',
    'meril': 'mjeril', 'mesec': 'mjesec', 'meseč': 'mjeseč',
    'mešav': 'mješav', 'mlečn': 'mlječn', 'model': 'model',
    'molek': 'molek', 'mrzet': 'mrzjet', 'mrzel': 'mrzjel',
    'namer': 'namjer', 'napad': 'napad', 'nared': 'nared',
    'nasme': 'nasmije', 'nedel': 'nedjel', 'negde': 'negdje',
    'nemac': 'njemac', 'nemač': 'njemač', 'nemoć': 'nemoć',
    'never': 'nevjer', 'numer': 'numer', 'obele': 'obilje',
    'obesh': 'obesh', 'obest': 'obijest', 'obeše': 'obješe',
    'obole': 'obolje', 'oceni': 'ocijeni', 'ocenu': 'ocjenu',
    'ocenj': 'ocjenj', 'odelj': 'odjelj', 'odnel': 'odnijel',
    'odnet': 'odnijet', 'odole': 'odolje', 'opsed': 'opsjed',
    'oseća': 'osjeća', 'osmeh': 'osmjeh', 'osvet': 'osvjet',
    'pesam': 'pjesam', 'pevuš': 'pjevuš', 'pevuc': 'pjevuc',
    'pevač': 'pjevač', 'pobeg': 'pobjeg', 'podel': 'podijel',
    'podne': 'podne', 'pomer': 'pomjer', 'posed': 'posjed',
    'poset': 'posjet', 'poseć': 'posjeć', 'posle': 'poslije',
    'pover': 'povjer', 'povre': 'povrije', 'požel': 'poželj',
    'prene': 'prenije', 'preti': 'prijeti', 'prese': 'presje',
    'preve': 'preve', 'prole': 'prolje', 'prose': 'prosje',
    'rasej': 'rasijan', 'razne': 'raznje', 'razre': 'razrije',
    'rešav': 'rješav', 'rešen': 'riješen', 'saose': 'saosje',
    'savet': 'savjet', 'scena': 'scena', 'scene': 'scene',
    'sceni': 'sceni', 'sceno': 'sceno', 'scenu': 'scenu',
    'sečiv': 'sječiv', 'sedeć': 'śedeć', 'sekir': 'śekir',
    'sever': 'śever', 'sleta': 'slijeta', 'smeni': 'smijeni',
    'smenj': 'smjenj', 'smest': 'smjest', 'smešt': 'smješt',
    'smeši': 'smiješi', 'smeše': 'smiješe', 'smešn': 'smiješn',
    'snešk': 'snješk', 'sneži': 'snježi', 'sneža': 'snježa',
    'spreč': 'spriječ', 'stale': 'stale', 'sutra': 'śutra',
    'svedo': 'svjedo', 'svesn': 'svjesn', 'svest': 'svijest',
    'svetl': 'svijetl', 'sveža': 'svježa', 'sveže': 'svježe',
    'sveži': 'svježi', 'svežu': 'svježu', 'svide': 'svidje',
    'telev': 'telev', 'telim': 'tijelim', 'tešnj': 'tješnj',
    'trezn': 'trijezn', 'trpel': 'trpjel', 'trpet': 'trpjet',
    'ubeđe': 'ubijeđe', 'ubeđu': 'ubjeđu', 'ucena': 'ucjena',
    'ucene': 'ucjene', 'uceni': 'ucijeni', 'ucenu': 'ucjenu',
    'umere': 'umjere', 'umest': 'umjest', 'umeti': 'umjeti',
    'umetn': 'umjetn', 'usled': 'usljed', 'usmen': 'usmen',
    'usmer': 'usmjer', 'uspeh': 'uspjeh', 'uspev': 'uspijev',
    'uvežb': 'uvježb', 'uvide': 'uvidje', 'uvred': 'uvrijed',
    'venac': 'vijenac', 'venča': 'vjenča', 'verid': 'vjerid',
    'veruj': 'vjeruj', 'vetar': 'vjetar', 'vesti': 'vijesti',
    'vežba': 'vježba', 'videl': 'vidjel', 'videt': 'vidjet',
    'videv': 'vidjev', 'vredn': 'vrijedn', 'vređa': 'vrijeđa',
    'vreme': 'vrijeme', 'vrtet': 'vrtjet', 'vrtel': 'vrtjel',
    'zamen': 'zamjen', 'zamer': 'zamjer', 'zapre': 'zaprije',
    'zased': 'zasijed', 'zaver': 'zavjer', 'zaves': 'zavjes',
    'zvezd': 'zvijezd', 'čovek': 'čovjek', 'želel': 'željel',
    'želet': 'željet', 'živel': 'živjel', 'živet': 'živjet',
    'živev': 'živjev', 'žudel': 'žudel', 'žutet': 'žutjet',
    'žutel': 'žutjel', 'wonde': 'wonde', 'beda': 'bijeda',
    'bedn': 'bijedn', 'besk': 'besk', 'besn': 'bijesn',
    'besp': 'besp', 'besv': 'besvj', 'beža': 'bježa',
    'bled': 'blijed', 'bleđ': 'bljeđ', 'breg': 'brijeg',
    'cedi': 'cijedi', 'cena': 'cijena', 'ceni': 'cijeni',
    'cent': 'cent', 'cenu': 'cijenu', 'crev': 'crijev',
    'cvet': 'cvijet', 'cveć': 'cvijeć', 'deci': 'deci',
    'deco': 'djeco', 'deli': 'dijeli', 'dele': 'dijele',
    'deča': 'dječa', 'dečj': 'dječij', 'done': 'donije',
    'dozv': 'dozv', 'dvem': 'dvjem', 'gnev': 'gnjev',
    'greh': 'grijeh', 'hleb': 'hljeb', 'htel': 'htjel',
    'isec': 'isijec', 'izbe': 'izbje', 'koen': 'korijen',
    'leka': 'lijeka', 'leku': 'lijeku', 'lenj': 'lijen',
    'letv': 'letv', 'leva': 'lijeva', 'leve': 'lijeve',
    'levi': 'lijevi', 'levo': 'lijevo', 'levu': 'lijevu',
    'leče': 'liječe', 'leči': 'liječi', 'lešn': 'lješn',
    'mehu': 'mjehu', 'mese': 'mjese', 'mesn': 'mjesn',
    'mest': 'mjest', 'meša': 'miješa', 'mlek': 'mlijek',
    'nemc': 'njemc', 'neme': 'nijeme', 'nega': 'njega',
    'nežn': 'nježn', 'nezi': 'njezi', 'obes': 'objes',
    'ocen': 'ocjen', 'odel': 'odijel', 'odse': 'odsje',
    'onde': 'ondje', 'oset': 'osjet', 'ovde': 'ovdje',
    'over': 'ovjer', 'pesm': 'pjesm', 'pena': 'pjena',
    'peno': 'pjeno', 'peni': 'pjeni', 'pene': 'pjene',
    'penu': 'pjenu', 'peva': 'pjeva', 'peša': 'pješa',
    'peši': 'pješi', 'retk': 'rijetk', 'reči': 'riječi',
    'rečn': 'rječn', 'reši': 'riješi', 'scen': 'scen',
    'sedn': 'śedn', 'seme': 'śeme', 'seti': 'sjeti',
    'slep': 'slijep', 'smeh': 'smijeh', 'smej': 'smij',
    'smel': 'smjel', 'smen': 'smjen', 'smer': 'smjer',
    'smes': 'smjes', 'sneg': 'snijeg', 'sten': 'stijen',
    'teme': 'tjeme', 'tera': 'tjera', 'tesn': 'tijesn',
    'ubed': 'ubijed', 'unel': 'unijel', 'unet': 'unijet',
    'uspe': 'uspje', 'uteh': 'utjeh', 'uver': 'uvjer',
    'čove': 'čovje', 'venc': 'vijenc', 'vers': 'vjers',
    'vera': 'vjera', 'vere': 'vjere', 'veri': 'vjeri',
    'veru': 'vjeru', 'vetr': 'vjetr', 'veći': 'veći',
    'veče': 'veče', 'večn': 'vječn', 'vešt': 'vješt',
    'vode': 'vode', 'vole': 'volje', 'volj': 'volj',
    'vred': 'vrijed', 'zeva': 'zijeva', 'zver': 'zvijer',
    'žele': 'žele',
}

STEM_FRAZE = {
    'Savet za ljudska prava UN': 'Savjet za ljudska prava UN',
    'Savet bezbednosti UN ': 'Savjet bezbjednosti UN',
    'Savet Evropske unije': 'Savjet Evropske unije',
    'Bel kraljic': 'Bijel kraljic',
    'Savet Evrop': 'Savjet Evrop',
    'Deda Mraz': 'Djed Mraz',
    'Snešk Beli': 'Snješk Bijeli',
    'Mlečn put': 'Mlječn put',
    'Već Evrop': 'Vijeć Evrop',
    'Bel kuć': 'Bijel kuć',
}

KONTEKST_MAPE = [
    {'ekavski': {'sedela', 'sedeli', 'sedeo', 'sedio', 'sede', 'sedu', 'sedi', 'sedog', 'sedoh', 'sedeti'},
     'kljucevi1': ('brad', 'zalisc', 'star', 'godin', 'glav', 'vlas', 'obrv', 'mrsi', 'kosa', 'kose', 'kosi', 'kosu', 'kosom'),
     'mape_grupa1': {'sedela': 'sijedila', 'sedeli': 'sijedili', 'sedeo': 'sijedio', 'sedio': 'sijedio', 'sede': 'sijede', 'sedu': 'sijedu', 'sedi': 'sijedi', 'sedog': 'sijedog', 'sedoh': 'sijedoh', 'sedeti': 'sijedjeti'},
     'mape_grupa2': {'sedela': 'sjedjela', 'sedeli': 'sjedjeli', 'sedeo': 'sjedio', 'sedio': 'sjedio', 'sede': 'sjede', 'sedu': 'sjedu', 'sedi': 'sjedi', 'sedog': 'sjedog', 'sedoh': 'sjedoh', 'sedeti': 'sjedjeti'}},
    {'ekavski': {'svet', 'sveta', 'svetu', 'svetom', 'svetovi', 'svetova', 'svetovima'},
     'kljucevi1': ('bog', 'crkv', 'otac', 'duh', 'krst', 'ikona', 'svešten', 'vjera', 'knji', 'vidi'),
     'mape_grupa1': {},
     'mape_grupa2': {'svet': 'svijet', 'sveta': 'svijeta', 'svetu': 'svijetu', 'svetom': 'svijetom', 'svetovi': 'svjetovi', 'svetova': 'svjetova', 'svetovima': 'svjetovima'}},
    {'ekavski': {'selo', 'sela', 'selu', 'selom', 'selima'},
     'kljucevi1': ('stolic', 'fotelj', 'klup', 'mest', 'sto', 'sof', 'park', 'sati', 'mirn', 'prozor', 'pod', 'kuć', 'ispred', 'ptica', 'dete', 'dijete'),
     'mape_grupa1': {'selo': 'sjelo', 'sela': 'sjela', 'selu': 'sjelu', 'selom': 'sjelom', 'selima': 'sjelima'},
     'mape_grupa2': {}},
    {'ekavski': {'dela', 'delu', 'delo', 'delima', 'delom'},
     'kljucevi1': ('kuć', 'poslovn', 'prostor', 'imovin', 'zemljišt', 'plac', 'soba', 'sprat', 'zgrad', 'dvorišt', 'ispit', 'prijemn', 'završn', 'dipl', 'posl', 'centr', 'donj', 'ošte'),
     'mape_grupa1': {'dela': 'dijela', 'delu': 'dijelu', 'delovima': 'djelovima', 'delom': 'dijelom'},
     'mape_grupa2': {'dela': 'djela', 'delu': 'djelu', 'delo': 'djelo', 'delima': 'djelima', 'delom': 'djelom'}},
    {'ekavski': {'veće', 'veća', 'veću', 'većim', 'većeg', 'većoj'},
     'kljucevi1': ('glomazn', 'gabarit', 'velik', 'poras', 'poveć', 'broj', 'dimenzij', 'tež', 'vis', 'šir', 'manj', 'dupl', 'obim'),
     'mape_grupa1': {},
     'mape_grupa2': {'veće': 'vijeće', 'veća': 'vijeća', 'veću': 'vijeću', 'većim': 'vijećima', 'većeg': 'vijeća', 'većoj': 'vijeću'}},
    {'ekavski': {'primene', 'primena', 'primeni', 'primenu', 'primenom', 'primenama'},
     'kljucevi1': ('alat', 'oruđ', 'kupil', 'sprem', 'priprem', 'planir', 'kazn', 'mjer', 'mjere', 'sankcij'),
     'mape_grupa1': {'primene': 'primijene', 'primeni': 'primijeni'},
     'mape_grupa2': {'primene': 'primjene', 'primena': 'primjena', 'primeni': 'primjeni', 'primenu': 'primjenu', 'primenom': 'primjenom', 'primenama': 'primjenama'}},
    {'ekavski': {'reci', 'recima'},
     'kljucevi1': ('nekom', 'tati', 'bratu', 'prijatelj', 'kaž', 'rekn', 'istinu', 'poruk', 'pism', 'glasn', 'tiho'),
     'mape_grupa1': {},
     'mape_grupa2': {'reci': 'rijeci', 'recima': 'riječima'}},
    {'ekavski': {'preko', 'preka', 'preke', 'preku', 'preki', 'prekog', 'prekom'},
     'kljucevi1': ('ljut', 'pogled', 'mrštit', 'osion', 'gled', 'izraz', 'oči', 'reč', 'riječ', 'narav', 'gnev', 'gnijev', 'prekor', 'hladn'),
     'mape_grupa1': {'preko': 'prijeko', 'preka': 'prijeka', 'preke': 'prijeke', 'preku': 'prijeku', 'preki': 'prijeki', 'prekog': 'prijekog', 'prekom': 'prijekom'},
     'mape_grupa2': {}},
    {'ekavski': {'slede', 'sledi', 'slediti', 'sledile', 'sledila', 'sledilo', 'sledili'},
     'kljucevi1': ('krv', 'strah', 'užas', 'šok', 'hladnoć', 'mraz', 'ledu', 'pogled'),
     'mape_grupa1': {},
     'mape_grupa2': {'slede': 'slijede', 'sledi': 'slijedi', 'slediti': 'slijediti', 'sledile': 'slijedile', 'sledila': 'slijedila', 'sledilo': 'slijedilo', 'sledili': 'slijedili'}},
    {'ekavski': {'sledeća', 'sledeći', 'sledeće', 'sledeću', 'sledećih', 'sledećem', 'sledećeg', 'sledećima'},
     'kljucevi1': ('prim', 'uputstv', 'pravil', 'savjet', 'savet', 'korak', 'trag', 'put', 'vođ', 'mentor'),
     'mape_grupa1': {'sledeća': 'slijedeća', 'sledeći': 'slijedeći', 'sledeće': 'slijedeće', 'sledeću': 'slijedeću', 'sledećih': 'slijedećih', 'sledećem': 'slijedećem', 'sledećeg': 'slijedećeg', 'sledećima': 'slijedećima'},
     'mape_grupa2': {'sledeća': 'sljedeća', 'sledeći': 'sljedeći', 'sledeće': 'sljedeće', 'sledeću': 'sljedeću', 'sledećih': 'sljedećih', 'sledećem': 'sljedećem', 'sledećeg': 'sljedećeg', 'sledećima': 'sljedećima'}},
    {'ekavski': {'nema'},
     'kljucevi1': ('ust', 'sved', 'svjed', 'ostal', 'posta', 'stoj', 'gled', 'sluš', 'glu', 'slep', 'slijep', 'hlad', 'nepom'),
     'mape_grupa1': {'nema': 'nijema'},
     'mape_grupa2': {}},
    {'ekavski': {'izvesti'},
     'kljucevi1': ('doga', 'inform', 'medij', 'program', 'uživo', 'javnost', 'gledaoc', 'narod', 'izvešt'),
     'mape_grupa1': {'izvesti': 'izvijesti'},
     'mape_grupa2': {}},
    {'ekavski': {'nem'},
     'kljucevi1': ('ust', 'sved', 'svjed', 'ostal', 'posta', 'stoj', 'gled', 'sluš', 'glu', 'slep', 'slijep', 'hlad', 'nepom'),
     'mape_grupa1': {'nem': 'nijem'},
     'mape_grupa2': {'nem': 'njem'}},
    {'ekavski': {'letu', 'leti'},
     'kljucevi1': ('ptic', 'avio', 'neb', 'heli', 'balo', 'inse', 'pilo', 'eska'),
     'mape_grupa1': {},
     'mape_grupa2': {'letu': 'ljetu', 'leti': 'ljeti'}},
    {'ekavski': {'zahteva'},
     'kljucevi1': ('služb', 'zvanič', 'pism', 'opravd', 'neopravd', 'ponovlj', 'skromn', 'pretjer', 'nereal', 'podnij', 'predat', 'odobri', 'prihvat', 'odbi', 'odbac', 'uputi', 'povuć', 'razmotr', 'ispun', 'ugovolj', 'posebn', 'lice', 'rešav', 'rješav', 'izuzeć', 'posebnog', 'podnošenj', 'zaštit', 'dostav', 'podnosioc', 'broj', 'zakon'),
     'mape_grupa1': {'zahteva': 'zahtjeva'},
     'mape_grupa2': {'zahteva': 'zahtijeva'}},
    {'ekavski': {'izmene', 'izmeni'},
     'kljucevi1': ('potpun', 'koren', 'korijen', 'delimič', 'djelimič', 'značaj', 'bitn', 'minim', 'neznat', 'smest', 'naknad', 'unapre', 'unaprije', 'vrem', 'vrijem', 'dopuni', 'stanj'),
     'mape_grupa1': {'izmene': 'izmijene', 'izmeni': 'izmijeni'},
     'mape_grupa2': {'izmene': 'izmjene', 'izmeni': 'izmjeni'}},
    {'ekavski': {'razmene', 'razmeni'},
     'kljucevi1': ('reč', 'riječ', 'mišlj', 'utisk', 'telefon', 'kontakt', 'adres', 'poklon', 'nežn', 'nježn', 'pogled', 'novac', 'iskustv', 'među', 'brzo', 'srdačno', 'otvoren'),
     'mape_grupa1': {'razmene': 'razmijene', 'razmeni': 'razmijeni'},
     'mape_grupa2': {'razmene': 'razmjene', 'razmeni': 'razmjeni'}},
    {'ekavski': {'procene', 'proceni'},
     'kljucevi1': ('praviln', 'objektiv', 'realn', 'pogrešn', 'brzo', 'odokativ', 'situac', 'rizik', 'štet', 'vredn', 'vrijedn', 'tužil'),
     'mape_grupa1': {'procene': 'procijene', 'proceni': 'procijeni'},
     'mape_grupa2': {'procene': 'procjene', 'proceni': 'procjeni'}},
    {'ekavski': {'povrede', 'povredi'},
     'kljucevi1': ('ljud', 'igrač', 'riječ', 'reč', 'često', 'lako', 'namern', 'namjern', 'slučajn', 'nekog', 'prijatelj', 'ponos', 'osjeć', 'oseć'),
     'mape_grupa1': {'povrede': 'povrijede', 'povredi': 'povrijedi'},
     'mape_grupa2': {}},
    {'ekavski': {'video'},
     'kljucevi1': ('nadzo', 'sistem', 'oprem', 'kamer', 'live', 'digit', 'mutan', 'dugi', 'kratki', 'pokrenu', 'pustit', 'premot', 'snimi', 'montir', 'skinut', 'snim', 'zapis', 'signal', 'produkc', 'bim', 'strim', 'objekt', 'zgrad', 'ulic', 'bank'),
     'mape_grupa1': {},
     'mape_grupa2': {'video': 'vidio'}},
    {'ekavski': {'vest'},
     'kljucevi1': ('orindž', 'orange', 'palm', 'bič', 'beach', 'virdžin', 'virgin', 'point', 'indi', 'bank', 'end', 'sajd', 'side', 'hem', 'junaj', 'unite', 'brom', 'kany', 'jerr', 'tarib'),
     'mape_grupa1': {},
     'mape_grupa2': {'vest': 'vijest'}},
    {'ekavski': {'besan'},
     'kljucevi1': ('noć', 'sati', 'dani', 'zora', 'oči', 'pogled', 'misli', 'umor', 'provesti', 'dočekati', 'jutro', 'muči', 'neispavan', 'budan', 'nesan', 'probdjeve'),
     'mape_grupa1': {'besan': 'bijesan'},
     'mape_grupa2': {'besan': 'bijesan'}},
    {'ekavski': {'srede', 'sredi'},
     'kljucevi1': ('prostor', 'namješ', 'stvar', 'nered', 'temelj', 'hitro', 'vremen', 'general', 'haos', 'papir', 'posprem', 'očisti', 'čist', 'rasprem', 'počist', 'složi', 'sortir', 'raspored', 'organiz'),
     'mape_grupa1': {},
     'mape_grupa2': {'srede': 'srijede', 'sredi': 'srijedi'}}
]

# --- REGEX MAPE ZA ANVIL/SKULPT KOMPATIBILNOST ---
SKINI_DZ_MAPA = {
    'č': 'c', 'ć': 'c', 'š': 's', 'ž': 'z', 'đ': 'd',
    'Č': 'C', 'Ć': 'C', 'Š': 'S', 'Ž': 'Z', 'Đ': 'D',
    'Ś': 'S', 'ś': 's'
}
SKINI_DZ_REGEX = re.compile(r'[čćšžđČĆŠŽĐŚś]')

CIR_U_LAT_MAPA = {
    'Љ': 'Lj', 'Њ': 'Nj', 'Џ': 'Dž', 'љ': 'lj', 'њ': 'nj', 'џ': 'dž',
    'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v', 'Г': 'G', 'г': 'g',
    'Д': 'D', 'д': 'd', 'Ђ': 'Đ', 'ђ': 'đ', 'Е': 'E', 'е': 'e', 'Ж': 'Ž', 'ж': 'ž',
    'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'Ј': 'J', 'ј': 'j', 'К': 'K', 'к': 'k',
    'Л': 'L', 'л': 'l', 'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o',
    'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r', 'С': 'S', 'с': 's', 'Т': 'T', 'т': 't',
    'Ћ': 'Ć', 'ћ': 'ć', 'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'H', 'х': 'h',
    'Ц': 'C', 'ц': 'c', 'Ч': 'Č', 'ч': 'č', 'Ш': 'Š', 'ш': 'š', 'С́': 'Ś', 'с́': 'ś'
}
CIR_U_LAT_REGEX = re.compile('|'.join(re.escape(k) for k in CIR_U_LAT_MAPA))

LAT_U_CIR_MAPA = {
    'lj': 'љ', 'nj': 'њ', 'dž': 'џ', 'Lj': 'Љ', 'Nj': 'Њ', 'Dž': 'Џ', 'LJ': 'Љ', 'NJ': 'Њ', 'DŽ': 'Џ',
    'A': 'А', 'a': 'а', 'B': 'Б', 'b': 'б', 'V': 'В', 'v': 'в', 'G': 'Г', 'g': 'г', 'D': 'Д', 'd': 'д',
    'Đ': 'Ђ', 'đ': 'ђ', 'E': 'Е', 'e': 'е', 'Ž': 'Ж', 'ž': 'ж', 'Z': 'З', 'z': 'з', 'I': 'И', 'i': 'и',
    'J': 'Ј', 'j': 'ј', 'K': 'К', 'k': 'к', 'L': 'Л', 'l': 'л', 'M': 'М', 'm': 'м', 'N': 'Н', 'n': 'н',
    'O': 'О', 'o': 'о', 'P': 'П', 'p': 'п', 'R': 'Р', 'r': 'р', 'S': 'С', 's': 'с', 'T': 'Т', 't': 'т',
    'Ć': 'Ћ', 'ć': 'ћ', 'U': 'У', 'u': 'у', 'F': 'Ф', 'f': 'ф', 'H': 'Х', 'h': 'х', 'C': 'Ц', 'c': 'ц',
    'Č': 'Ч', 'č': 'ч', 'Š': 'Ш', 'š': 'ш', 'Ś': 'С́', 'ś': 'с́', 'w': 'w'
}
LAT_U_CIR_REGEX = re.compile('|'.join(re.escape(k) for k in LAT_U_CIR_MAPA))

CIR_DETEKCIJA = re.compile(r'[\u0400-\u04FF]')
DZ_DETEKCIJA = re.compile(r'[čćžšđČĆŽŠĐ]')

def skini_kvacice(tekst):
    return SKINI_DZ_REGEX.sub(lambda m: SKINI_DZ_MAPA[m.group(0)], tekst)

def cirilica_u_latinicu(tekst):
    return CIR_U_LAT_REGEX.sub(lambda m: CIR_U_LAT_MAPA[m.group(0)], tekst)

def latinica_u_cirilicu(tekst):
    return LAT_U_CIR_REGEX.sub(lambda m: LAT_U_CIR_MAPA[m.group(0)], tekst)

# --- INDEKSIRANJE I PREKOMPAJLOVANJE ---
BRZI_KONTEKST = {
    rjec: (m['kljucevi1'], m['mape_grupa1'], m['mape_grupa2'])
    for m in KONTEKST_MAPE for rjec in m['ekavski']
}

STEMS_SORTED = sorted(STEMS.keys(), key=len, reverse=True)
STEMS_REGEX = re.compile('(' + '|'.join(re.escape(k) for k in STEMS_SORTED) + ')')
RIJECI_REGEX = re.compile(r'([a-zA-ZčćžšđČĆŽŠĐ\u0400-\u04FF]+)')
WORD_ONLY_REGEX = re.compile(r'^[a-zA-ZčćžšđČĆŽŠĐ]+$')

EO_IZUZECI = {"pepeo", "video", "stereo", "rodeo", "cameo", "kameo", "paleo", "neo", "geodeo", "seo", "sedeo"}

# Vlastita imena i prezimena
IMENA_IZUZECI_REGEX = re.compile(
    r'^(?:vera|veri|veru|vere|vero|verom|'
    r'lepa|lepe|lepi|lepu|lepo|lepom|'
    r'sneža|sneže|sneži|snežu|snežo|snežom|sneza|sneze|snezi|snezu|snezo|snezom|snežan|snezan|'
    r'bela|bele|beli|belo|belu|belom|'
    r'slepč|slepc|sedić|sedic|seden|sedlar|unesk|cvetk|penelop|meri|penezi|'
    r'neven|vedran|vesn|svetlan|predrag|nenad|nebojš|nebojs|dejan|petar|petr|'
    r'veljk|velimir|veric|veroljub|veselin|zvezdan|sreten|sredoje|desimir|desank|'
    r'jelena|jelen|jelic|jelisavet|jeremij|jevt|jezdimir)'
)
DOZVOLJENI_VELIKO_REGEX = re.compile(r'^(?:nemci|nemcima|nemaca|verova|belil)')

PREKOMPAJLOVANE_FRAZE = []
sve_fraze = {**{k: v for k, v in EXACT.items() if " " in k}, **STEM_FRAZE}
for fraza, zamjena in sorted(sve_fraze.items(), key=lambda x: len(x[0]), reverse=True):
    regex_djelovi = []
    for d in fraza.split():
        cisto = skini_kvacice(d)
        varijante = [re.escape(d), re.escape(cisto)] if cisto != d else [re.escape(d)]
        regex_djelovi.append("(" + "|".join(varijante) + ")")
    
    slova_pat = r"([a-zA-ZčćžšđČĆŽŠĐ\u0400-\u04FF]*)"
    spojnica = f"{slova_pat} " if fraza in STEM_FRAZE else slova_pat
    pattern_str = r"\b" + spojnica.join(regex_djelovi) + slova_pat + r"\b"
    PREKOMPAJLOVANE_FRAZE.append((re.compile(pattern_str, re.IGNORECASE), fraza.split(), zamjena.split()))

# --- KEŠ MEMORIJA ZA BEZKONTEKSTNE RIJEČI ---
RIJEC_KES = {}
MAX_KES_VELICINA = 15000

def _sacuvaj_velika_slova(izv, zam):
    if not izv or not zam:
        return zam
    if izv.isupper():
        return zam.upper()
    if izv.islower():
        return zam.lower()
    if izv.istitle():
        return zam.capitalize()
    last_upper = izv[-1].isupper()
    len_izv = len(izv)
    return "".join(
        c.upper() if (izv[i].isupper() if i < len_izv else last_upper) else c.lower()
        for i, c in enumerate(zam)
    )

def _zamijeni_frazu_match(match, ekavski_words, ijekavski_words):
    izv = match.group(0)
    je_cir = bool(CIR_DETEKCIJA.search(izv))
    ima_dz_izv = bool(DZ_DETEKCIJA.search(izv))
    
    novi_djelovi = []
    w_brojac = 0
    for tok in re.split(r'([a-zA-ZčćžšđČĆŽŠĐ]+)', izv):
        if WORD_ONLY_REGEX.match(tok) and w_brojac < len(ekavski_words):
            ek_cisto = skini_kvacice(ekavski_words[w_brojac])
            nastavak = tok[len(ek_cisto):] if len(tok) >= len(ek_cisto) else ""
            novi_djelovi.append(_sacuvaj_velika_slova(tok, ijekavski_words[w_brojac] + nastavak))
            w_brojac += 1
        else:
            novi_djelovi.append(tok)
            
    lat_zam = "".join(novi_djelovi)
    if je_cir:
        return latinica_u_cirilicu(lat_zam)
    return lat_zam if ima_dz_izv else skini_kvacice(lat_zam)

def zamijeni_rijeci(tekst):
    if not tekst:
        return tekst

    trenutna = tekst
    for pattern, ek_words, ij_words in PREKOMPAJLOVANE_FRAZE:
        trenutna = pattern.sub(lambda m, ew=ek_words, iw=ij_words: _zamijeni_frazu_match(m, ew, iw), trenutna)

    tokeni = RIJECI_REGEX.split(trenutna)
    GRANICNICI_KONTEKSTA = {'.', ';', '!', '?', '\n'}
    nova_linija_djelovi = []
    num_tokeni = len(tokeni)

    for i, dio in enumerate(tokeni):
        if not dio:
            continue

        if i % 2 == 0:
            nova_linija_djelovi.append(dio)
            continue

        # 1. Brza provjera keša (sadrži samo bezkontekstne riječi)
        if dio in RIJEC_KES:
            nova_linija_djelovi.append(RIJEC_KES[dio])
            continue

        je_cirilica = bool(CIR_DETEKCIJA.search(dio))
        ima_dz = bool(DZ_DETEKCIJA.search(dio))
        rijec_lat = cirilica_u_latinicu(dio) if je_cirilica else dio
        r_low = rijec_lat.lower()

        if "e" not in r_low:
            if len(RIJEC_KES) < MAX_KES_VELICINA:
                RIJEC_KES[dio] = dio
            nova_linija_djelovi.append(dio)
            continue

        je_pocetno_veliko = rijec_lat[0].isupper()
        if je_pocetno_veliko:
            je_dozvoljeno_veliko = bool(DOZVOLJENI_VELIKO_REGEX.match(r_low))
            if not je_dozvoljeno_veliko and not r_low.startswith("veruj") and IMENA_IZUZECI_REGEX.match(r_low):
                if len(RIJEC_KES) < MAX_KES_VELICINA:
                    RIJEC_KES[dio] = dio
                nova_linija_djelovi.append(dio)
                continue

        je_kontekstna = False

        if r_low in EXACT:
            tekst_ijekavski = _sacuvaj_velika_slova(rijec_lat, EXACT[r_low])
        elif r_low in STEMS:
            tekst_ijekavski = _sacuvaj_velika_slova(rijec_lat, STEMS[r_low])
        elif r_low in BRZI_KONTEKST:
            je_kontekstna = True
            kljucevi1, grupa1, grupa2 = BRZI_KONTEKST[r_low]
            prozor = []
            
            for j in range(i - 2, -1, -2):
                if j + 1 < num_tokeni and any(c in GRANICNICI_KONTEKSTA for c in tokeni[j + 1]):
                    break
                tok = tokeni[j]
                if tok:
                    prozor.append((cirilica_u_latinicu(tok) if CIR_DETEKCIJA.search(tok) else tok).lower())
                    if len(prozor) == 4:
                        break

            desno_count = 0
            for j in range(i + 2, num_tokeni, 2):
                if any(c in GRANICNICI_KONTEKSTA for c in tokeni[j - 1]):
                    break
                tok = tokeni[j]
                if tok:
                    prozor.append((cirilica_u_latinicu(tok) if CIR_DETEKCIJA.search(tok) else tok).lower())
                    desno_count += 1
                    if desno_count == 4:
                        break

            ima_kontekst_1 = any(w.startswith(k) for w in prozor for k in kljucevi1)
            baza = grupa1 if ima_kontekst_1 else grupa2
            tekst_ijekavski = _sacuvaj_velika_slova(rijec_lat, baza.get(r_low, rijec_lat))
        else:
            if r_low.endswith("eo") and len(r_low) > 3 and r_low not in EO_IZUZECI:
                osnova = rijec_lat[:-2]
                match_osnova = STEMS_REGEX.search(osnova.lower())
                if match_osnova:
                    korijen = match_osnova.group(1)
                    idx = match_osnova.start()
                    osnova = (
                        osnova[:idx]
                        + _sacuvaj_velika_slova(osnova[idx:idx + len(korijen)], STEMS[korijen])
                        + osnova[idx + len(korijen):]
                    )
                tekst_ijekavski = osnova + _sacuvaj_velika_slova(rijec_lat[-2:], "io")
            else:
                match_korijen = STEMS_REGEX.search(r_low)
                if match_korijen:
                    korijen = match_korijen.group(1)
                    idx = match_korijen.start()
                    prefiks = rijec_lat[:idx]
                    sufiks = rijec_lat[idx + len(korijen):]
                    zamjena = STEMS[korijen]

                    if korijen.endswith("e") and zamjena.endswith("e") and sufiks.lower().startswith("o"):
                        baza = zamjena[:-3] if zamjena.endswith("ije") else (zamjena[:-2] if zamjena.endswith("je") else zamjena)
                        sufiks = _sacuvaj_velika_slova(sufiks[:1], "io") + sufiks[1:]
                        tekst_ijekavski = prefiks + _sacuvaj_velika_slova(rijec_lat[idx:idx + len(korijen)], baza) + sufiks
                    else:
                        tekst_ijekavski = prefiks + _sacuvaj_velika_slova(rijec_lat[idx:idx + len(korijen)], zamjena) + sufiks
                else:
                    tekst_ijekavski = rijec_lat

        izlaz = latinica_u_cirilicu(tekst_ijekavski) if je_cirilica else (tekst_ijekavski if ima_dz else skini_kvacice(tekst_ijekavski))

        # Upis u keš samo ako riječ ne zavisi od konteksta
        if not je_kontekstna and len(RIJEC_KES) < MAX_KES_VELICINA:
            RIJEC_KES[dio] = izlaz

        nova_linija_djelovi.append(izlaz)

    return "".join(nova_linija_djelovi)

if IMA_OS:
    def a_datoteku(ulaz, izlaz):
        if not os.path.isfile(ulaz):
            print(f"Greška: '{ulaz}'...")
            sys.exit(1)
        with open(ulaz, encoding="utf-8") as f:
            t = f.read()
        with open(izlaz, "w", encoding="utf-8") as f:
            f.write(zamijeni_rijeci(t))
        print(f"Završeno: '{ulaz}' -> '{izlaz}'")

    if __name__ == "__main__":
        if len(sys.argv) == 3:
            a_datoteku(sys.argv[1], sys.argv[2])
