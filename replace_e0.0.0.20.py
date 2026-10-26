#E2I PREVODILAC
#Konvertor ekavice u ijekavicu
import sys, os, re 
#https://gorgeous-small-dog.anvil.app



EXACT = {

    'razmenama': 'razmjenama',

    'zahtevima': 'zahtjevima',

    'pretrpeo': 'pretrpio',
    'razboleo': 'razbolio',
    'razmenom': 'razmjenom',
    'svetlost': 'svjetlost',
    'zasedama': 'zasjedama',

    'doživeo': 'doživio',
    'nemošću': 'nijemošću',
    'poželeo': 'poželio',
    'razmena': 'razmjena',
    'razmenu': 'razmjenu',
    'verzija': 'verzija',
    'zahteve': 'zahtjeve',
    'zahtevu': 'zahtjevu',
    'zahtevi': 'zahtjevi',

    'belima': 'bijelima',
    'celima': 'cijelima',
    'dedama': 'djedovima',
    'drugde': 'drugdje',
    'najpre': 'najprije',
    'napred': 'naprijed',
    'nemima': 'nijemima',
    'oduvek': 'oduvijek',
    'prosek': 'prosijek',
    'rečima': 'riječima',
    'svideo': 'svidio',
    'uvideo': 'uvidio',
    'zaseda': 'zasjeda',
    'zasede': 'zasjede',
    'zasedi': 'zasjedi',
    'zasedu': 'zasjedu',
    'zahtev': 'zahtjev',

    'celoj': 'cijeloj',
    'doneo': 'donio',
    'iseći': 'isjeći',
    'nigde': 'nigdje',
    'odneo': 'odnio',
    'odeća': 'odjeća',
    'odeći': 'odjeći',
    'odeću': 'odjeću',
    'pevac': 'kokot',
    'rekao': 'rekao',
    'rekla': 'rekla',
    'razne': 'razne',
    'rečju': 'riječju',
    'sreda': 'srijeda',
    'svest': 'svijest',
    'uspeo': 'uspio',
    'voleo': 'volio',
    'vreme': 'vrijeme',
    'želeo': 'želio',
    'žudeo': 'žudio',

    'bela': 'bijela',
    'bele': 'bijele',
    'beli': 'bijeli',
    'belo': 'bijelo',
    'belu': 'bijelu',
    'cela': 'cijela',
    'cele': 'cijele',
    'celi': 'cijeli',
    'celo': 'cijelo',
    'celu': 'cijelu',
    'deca': 'djeca',
    'dece': 'djece',
    'deci': 'djeci',
    'deco': 'djeco',
    'decu': 'djecu',
    'deda': 'djed',
    'dede': 'djedovi',
    'dele': 'dijele',
    'dete': 'dijete',
    'dole': 'dolje',
    'hteo': 'htio',
    'lepa': 'lijepa',
    'lepe': 'lijepe',
    'lepi': 'lijepi',
    'lepo': 'lijepo',
    'lepu': 'lijepu',
    'leta': 'ljeta',
    'leto': 'ljeto',
    'mera': 'mjera',
    'mere': 'mjere',
    'meri': 'mjeri',
    'meru': 'mjeru',
    'neme': 'nijeme',
    'nemi': 'nijemi',
    'nemo': 'nijemo',
    'nisu': 'nijesu',
    'plen': 'plijen',
    'reči': 'riječi',
    'smeo': 'smio',
    'tela': 'tijela',
    'telo': 'tijelo',
    'telu': 'tijelu',
    'umeo': 'umio',
    'uvek': 'uvijek',
    'uvid': 'uvid',
    'veka': 'vijeka',
    'veku': 'vijeku',
    'vera': 'vjera',
    'vere': 'vjere',
    'veri': 'vjeri',
    'veru': 'vjeru',
    'vide': 'vide',
    'vole': 'vole',
    'žele': 'žele',

    
    'beo': 'bijel',
    'bes': 'bijes',
    'ceo': 'cio',
    'cev': 'cijev',
    'deo': 'dio',
    'dev': 'djev',
    'dve': 'dvije',
    'gde': 'gdje',
    'lek': 'lijek',
    'lep': 'lijep',
    'leš': 'leš',
    'obe': 'obje',
    'pre': 'prije',
    'reč': 'riječ',
    'sme': 'smije',
    'ume': 'umije',
    'vek': 'vijek',
}



STEMS = {
    'drugostepen': 'drugostepen',
    'međuzvezdan': 'međuzvjezdan',
    'predstavnik': 'predstavnik',

    'nepogrešiv': 'nepogrešiv',
    'obaveštenj': 'obavještenj',
    'pretpostav': 'pretpostav',

    'najzahtev': 'najzahtjev',    
    'podrazume': 'podrazumije',
    'pravoverc': 'pravovjern',
    'presecanj': 'presijecanj',
    'razrešenj': 'razrješenj',
    'snabdeven': 'snabdjeven',
    'sprečavanj': 'sprječavanj',

    'dodeljen': 'dodijeljen',
    'doprinos': 'doprinios',
    'dragocen': 'dragocjen',
    'opredeli': 'opredijeli',
    'opredelj': 'opredjelj',
    'petomese': 'petomjese',
    'pomeranj': 'pomjeranj',
    'ponedelj': 'ponedjelj',
    'potkolen': 'potkoljen',
    'potpreds': 'potpredsj',
    'predvide': 'predvidje',
    'pregreja': 'pregrija',
    'preteran': 'pretjeran',
    'pretrpel': 'pretrpjel',
    'primenju': 'primjenju',
    'privredn': 'privredn',
    'prosveti': 'prosvjeti',
    'ravnomer': 'ravnomjer',
    'sporazum': 'sporazum',
    'svestran': 'svestran',
    'verovatn': 'vjerovatn',
    'zahtevat': 'zahtijevat',
    'zakasnel': 'zakašnjel',
    'zasenjen': 'zasjenjen',
    'zastarel': 'zastarjel',
    'zaveštan': 'zavještan',

    'bezuspe': 'bezuspje',
    'delegat': 'delegat',
    'delikat': 'delikat',
    'doprine': 'doprinije',
    'doteran': 'dotjeran',
    'doživel': 'doživjel',
    'doživet': 'doživjet',
    'izbegav': 'izbjegav',
    'leticij': 'leticij',
    'malolet': 'maloljet',
    'nadžive': 'nadživje',
    'naleplj': 'naljeplj',
    'napredn': 'napredn',
    'napredo': 'napredo',
    'napretk': 'napretk',
    'nasledn': 'nasljedn',
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
    'penelop': 'penelop',
    'podsmeh': 'podsmjeh',
    'pogreši': 'pogriješi',
    'pogrešk': 'pogrešk',
    'poletet': 'poletjet',
    'pomešan': 'pomiješan',
    'poverlj': 'povjerlj',
    'povreda': 'povreda',
    'povredu': 'povredu',
    'prebole': 'prebolje',
    'predlog': 'prijedlog',
    'premest': 'premjest',
    'premešt': 'premješt',
    'prethod': 'prethod',
    'primedb': 'primjedb',
    'primeni': 'primijeni',
    'primeno': 'primjeno',
    'primenj': 'primijenj',
    'primeti': 'primijeti',
    'procena': 'procjena',
    'procenj': 'procjenj',
    'procenu': 'procjenu',
    'promeni': 'promijeni',
    'prosvet': 'prosvjet',
    'punolet': 'punoljet',
    'rascepi': 'rascijepi',
    'rasejan': 'rasijan',
    'razbole': 'razbolje',
    'razmenj': 'razmjenj',
    'smešten': 'smješten',
    'snabdev': 'snabdijev',
    'telefon': 'telefon',
    'tromese': 'tromjese',
    'umetnik': 'umjetnik',
    'verenik': 'vjerenik',
    'vrednov': 'vrednov',
    'zamenic': 'zamjenic',
    'zamenik': 'zamjenik',
    'zaplena': 'zapljena',
    'zaplene': 'zapljene',
    'zapleni': 'zaplijeni',
    'zaplenu': 'zapljenu',

    'belešk': 'bilješk',
    'bekstv': 'bjekstv',
    'bezbed': 'bezbjed',
    'cepnut': 'cjepnut',
    'dedukt': 'dedukt',
    'delimi': 'djelimi',
    'delima': 'djelima',
    'delimi': 'djelimi',
    'detalj': 'detalj',
    'detinj': 'djetinj',
    'dodeli': 'dodijeli',
    'dodelj': 'dodjelj',
    'dospel': 'dospjel',
    'eksten': 'eksten',
    'gnezdo': 'gnijezdo',
    'grejat': 'grijat',
    'izgore': 'izgorje',
    'izmena': 'izmjena',
    'izvesn': 'izvjesn',
    'kolevk': 'kolijevk',
    'letarg': 'letarg',
    'letimi': 'letimi',
    'menjač': 'mjenjač',
    'mleven': 'mljeven',
    'najlep': 'najljep',
    'nalepi': 'nalijepi',
    'nalepn': 'naljepn',
    'namenj': 'namijenj',
    'namešt': 'namješt',
    'nasled': 'naslijed',
    'navest': 'navest',
    'navode': 'navode',
    'nedelj': 'nedjelj',
    'neizbe': 'neizbje',
    'neretk': 'nerijetk',
    'neuspe': 'neuspje',
    'nevest': 'nevjest',
    'odeven': 'odjeven',
    'otpeva': 'otpjeva',
    'pešačk': 'pješačk',
    'pismen': 'pismen',
    'pobedi': 'pobijedi',
    'pobegl': 'pobjegl',
    'podela': 'podjela',
    'podelj': 'podijelj',
    'podseć': 'podsjeć',
    'pomera': 'pomijera',
    'porekl': 'porijekl',
    'poretk': 'poretk',
    'posled': 'posljed',
    'posred': 'posred',
    'posvet': 'posvet',
    'potera': 'potjera',
    'povest': 'povijest',
    'predse': 'predsje',
    'predst': 'predst',
    'preduz': 'preduz',
    'prenes': 'prenes',
    'presel': 'presel',
    'prevar': 'prevar',
    'preživ': 'preživj',
    'pridev': 'pridjev',
    'primer': 'primjer',
    'primet': 'primjet',
    'prispe': 'prispje',
    'procen': 'procjen',
    'promen': 'promjen',
    'prosek': 'prosijek',
    'prosle': 'proslije',
    'proter': 'protjer',
    'prover': 'provjer',
    'rascep': 'rascjep',
    'razmer': 'razmjer',
    'razume': 'razumije',
    'redosl': 'redoslj',
    'reklam': 'reklam',
    'rešenj': 'rješenj',
    'revers': 'revers',
    'saposl': 'zaposlj',
    'savest': 'savjest',
    'sečenj': 'sječenj',
    'sedišt': 'sjedišt',
    'semest': 'semest',
    'smatra': 'smatra',
    'smejat': 'smijat',
    'stepen': 'stepen',
    'strelj': 'strijelj',
    'svetlo': 'svjetlo',
    'svetsk': 'svjetsk',
    'svugde': 'svugdje',
    'ubeđen': 'ubijeđen',
    'unapre': 'unaprije',
    'unešen': 'unešen',
    'usmeni': 'usmeni',
    'uživel': 'uživjel',
    'vaspit': 'vaspit',
    'venčal': 'vjenčal',
    'venčan': 'vjenčan',
    'verbal': 'verbal',
    'vernic': 'vjernic',
    'verova': 'vjerova',
    'volont': 'volont',
    'vremen': 'vremen',
    'zabele': 'zabilje',
    'zameni': 'zamijeni',
    'zamenj': 'zamjenj',
    'zaplen': 'zaplijen',
    'zapose': 'zaposje',
    'zaposl': 'zapošlj',
    'železn': 'željezn',

    'ameri': 'ameri',
    'beleg': 'biljeg',
    'belež': 'biljež',
    'belil': 'bjelil',
    'belog': 'bjelog',
    'cedil': 'cjedil',
    'celin': 'cjelin',
    'celob': 'celob',
    'celog': 'cijelog',
    'celok': 'celok',
    'cenar': 'cenar',
    'cenit': 'cijeniti',
    'cveta': 'cvjeta',
    'decem': 'decem',
    'delat': 'djelat',
    'delim': 'dijelim',
    'delov': 'djelov',
    'deluj': 'djeluj',
    'detet': 'djetet',
    'devet': 'devet',
    'devoj': 'djevoj',
    'dečač': 'dječač',
    'dodel': 'dodjel',
    'donel': 'donijel',
    'dones': 'dones',
    'greja': 'grija',
    'greši': 'griješi',
    'hlepč': 'hljepč',
    'isten': 'isten',
    'izmer': 'izmjer',
    'izned': 'izned',
    'iznet': 'iznijet',
    'izveš': 'izvješ',
    'kamer': 'kamer',
    'karak': 'karak',
    'kolen': 'koljen',
    'kolev': 'kolijev',
    'koren': 'korijen',
    'kvenc': 'kvenc',
    'lekar': 'ljekar',
    'lekov': 'ljekov',
    'lepil': 'ljepil',
    'lepit': 'lijepit',
    'lepoj': 'ljepoj',
    'lepot': 'ljepot',
    'lestv': 'ljestv',
    'letak': 'letak',
    'letal': 'letal',
    'letel': 'letjel',
    'letis': 'letis',
    'letnj': 'ljetnj',
    'leton': 'leton',
    'levic': 'ljevic',
    'levič': 'ljevič',
    'lečeć': 'liječeć',
    'liter': 'liter',
    'menja': 'mijenja',
    'meram': 'mjeram',
    'meril': 'mjeril',
    'mesec': 'mjesec',
    'meseč': 'mjeseč',
    'mešav': 'mješav',
    'model': 'model',
    'molek': 'molek',
    'namer': 'namjer',
    'napad': 'napad',
    'nared': 'nared',
    'nasme': 'nasmije',
    'nedel': 'nedjel',
    'negde': 'negdje',
    'nemac': 'njemac',
    'nemač': 'njemač',
    'nemoć': 'nemoć',
    'never': 'nevjer',
    'numer': 'numer',
    'obele': 'obilje',
    'obesh': 'obesh',
    'obest': 'obijest',
    'obeše': 'obješe',
    'obole': 'obolje',
    'oceni': 'ocijeni',
    'ocenu': 'ocjenu',
    'ocenj': 'ocjenj',
    'odelj': 'odjelj',
    'odnel': 'odnijel',
    'odnet': 'odnijet',
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
    'povre': 'povrije',
    'požel': 'poželj',
    'prene': 'prenije',
    'preti': 'prijeti',
    'prese': 'presje',
    'preve': 'preve',
    'prole': 'prolje',
    'prose': 'prosje',
    'rasej': 'rasijan',
    'razne': 'raznje',
    'razre': 'razrije',
    'rešav': 'rješav',
    'rešen': 'riješen',
    'saose': 'saosje',
    'savet': 'savjet',
    'scena': 'scena',
    'scene': 'scene',
    'sceni': 'sceni',
    'sceno': 'sceno',
    'scenu': 'scenu',
    'sever': 'sjever',
    'sečiv': 'sječiv',
    'sedeć': 'śedeć',
    'sekir': 'śekir',
    'sever': 'śever',
    'sleta': 'slijeta',
    'smeni': 'smijeni',
    'smenj': 'smjenj',
    'smest': 'smjest',
    'smešt': 'smješt',
    'smeši': 'smiješi',
    'smeše': 'smiješe',
    'snešk': 'snješk',
    'sneži': 'sniježi',
    'sneža': 'sniježa',
    'spreč': 'spriječ',
    'stale': 'stale',
    'sutra': 'śutra',
    'svedo': 'svjedo',
    'svesn': 'svjesn',
    'svest': 'svijest',
    'svetl': 'svijetl',
    'sveža': 'svježa',
    'sveže': 'svježe',
    'sveži': 'svježi',
    'svežu': 'svježu',
    'svide': 'svidje',
    'telev': 'telev',
    'telim': 'tijelim',
    'ubeđe': 'ubijeđe',
    'ubeđu': 'ubjeđu',
    'ucena': 'ucjena',
    'ucene': 'ucjene',
    'uceni': 'ucijeni',
    'ucenu': 'ucjenu',
    'umere': 'umjere',
    'umest': 'umjest',
    'umeti': 'umjeti',
    'umetn': 'umjetn',
    'usled': 'usljed',
    'usmen': 'usmen',
    'usmer': 'usmjer',
    'uspeh': 'uspjeh',
    'uspev': 'uspijev',
    'uvežb': 'uvježb',
    'uvide': 'uvidje',
    'uvred': 'uvrijed',
    'venac': 'vijenac',
    'venča': 'vjenča',
    'verid': 'vjerid',
    'veruj': 'vjeruj',
    'vetar': 'vjetar',
    'vesti': 'vijesti',
    'vežba': 'vježba',
    'videl': 'vidjel',
    'videt': 'vidjet',
    'videv': 'vidjev',
    'vredn': 'vrijedn',
    'vređa': 'vrijeđa',
    'vreme': 'vrijeme',
    'zamen': 'zamjen',
    'zamer': 'zamjer',
    'zapre': 'zaprije',
    'zased': 'zasijed',
    'zaver': 'zavjer',
    'zvezd': 'zvijezd',
    'čovek': 'čovjek',
    'želel': 'željel',
    'želet': 'željet',
    'živel': 'živjel',
    'živeo': 'živio',
    'živet': 'živjet',
    'žudel': 'žudel',

    'beda': 'bijeda',
    'bedn': 'bijedn',
    'besk': 'besk',
    'besn': 'bijesn',
    'besp': 'besp',
    'besv': 'besvj',
    'beža': 'bježa',
    'bled': 'blijed',
    'breg': 'brijeg',
    'cedi': 'cijedi',
    'cena': 'cijena',
    'ceni': 'cijeni',
    'cent': 'cent',
    'cenu': 'cijenu',
    'crev': 'crijev',
    'cvet': 'cvijet',
    'deci': 'deci',
    'deco': 'djeco',
    'deli': 'dijeli',
    'dele': 'dijele',
    'deča': 'dječa',
    'dečj': 'dječij',
    'done': 'donije',
    'dozv': 'dozv',
    'dvem': 'dvjem',
    'gnev': 'gnjev',
    'greh': 'grijeh',
    'hleb': 'hljeb',
    'isec': 'isijec',
    'izbe': 'izbje',
    'koen': 'korijen',
    'leka': 'lijeka',
    'leku': 'lijeku',
    'lenj': 'lijen',
    'letv': 'letv',
    'leva': 'lijeva',
    'leve': 'lijeve',
    'levi': 'lijevi',
    'levo': 'lijevo',
    'levu': 'lijevu',
    'leče': 'liječe',
    'leči': 'liječi',
    'lešn': 'lješn',
    'mehu': 'mjehu',
    'mese': 'mjese',
    'mesn': 'mjesn',
    'mest': 'mjest',
    'meša': 'miješa',
    'mlek': 'mlijek',
    'nemc': 'njemc',
    'neme': 'nijemje',
    'nega': 'njega',
    'nežn': 'nježn',
    'nezi': 'njezi',
    'obes': 'objes',
    'ocen': 'ocjen',
    'odel': 'odijel',
    'odse': 'odsje',
    'onde': 'ondje',
    'oset': 'osjet',
    'ovde': 'ovdje',
    'over': 'ovjer',
    'pesm': 'pjesm',
    'pena': 'pjena',
    'peno': 'pjeno',
    'peni': 'pjeni',
    'pene': 'pjene',
    'penu': 'pjenu',
    'peva': 'pjeva',
    'peša': 'pješa',
    'peši': 'pješi',
    'retk': 'rijetk',
    'reči': 'riječi',
    'rečn': 'rječn',
    'reši': 'riješi',
    'scen': 'scen',
    'sedn': 'śedn',
    'seme': 'śeme',
    'seti': 'sjeti',
    'slep': 'slijep',
    'smeh': 'smijeh',
    'smej': 'smij',
    'smel': 'smjel',
    'smen': 'smjen',
    'smer': 'smjer',
    'smes': 'smjes',
    'sneg': 'snijeg',
    'sten': 'stijen',
    'teme': 'tjeme',
    'tera': 'tjera',
    'tesn': 'tijesn',
    'ubed': 'ubijed',
    'unel': 'unijel',
    'unet': 'unijet',
    'uspe': 'uspje',
    'uteh': 'utjeh',
    'uver': 'uvjer',
    'čove': 'čovje',
    'venc': 'vijenc',
    'vers': 'vjers',
    'vetr': 'vjetr',
    'veći': 'veći',
    'veče': 'veče',
    'večn': 'vječn',
    'vešt': 'vješt',
    'vode': 'vode',
    'vole': 'volje',
    'volj': 'volj',
    'vred': 'vrijed',
    'zeva': 'zijeva',
    'zver': 'zvijer',
    'žele': 'žele',

#    'bed': 'bijed',
#    'cep': 'cijep',
#    'cev': 'cijev',
#    'dec': 'djec',
#    'ded': 'djed',
#    'det': 'dijet',
#    'deč': 'dječ',
#   'gde': 'gdje',
#    'hte': 'htje',
#    'len': 'lijen',
#    'les': 'ljesaaa',
#    'lev': 'lijev',
#    'meš': 'mješ',
#    'mle': 'mlje',
#    'pes': 'pijes',
#    'pev': 'pjev',
#    'rek': 'rijek',
#    'ređ': 'rjeđ',
#    'reš': 'rješ',
#    'sen': 'sjen',
#    'seć': 'sjeć',
#    'tel': 'tijel',
#    'ume': 'umje',
#    'čov': 'čovj',
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
    {
        'ekavski': {'sedela', 'sedeli', 'sedeo', 'sedio', 'sede', 'sedu', 'sedi', 'sedog', 'sedoh', 'sedeti'},
        'kljucevi1': ['kos', 'brad', 'zalisc', 'star', 'godin', 'glav', 'vlas', 'obrv', 'mrsi'],
        'kljucevi2': [],
        'mape_grupa1': {'sedela': 'sijedila', 'sedeli': 'sijedili', 'sedeo': 'sijedio', 'sedio': 'sijedio', 'sede': 'sijede', 'sedu': 'sijedu', 'sedi': 'sijedi', 'sedog': 'sijedog', 'sedoh': 'sijedoh', 'sedeti': 'sijedjeti'},
        'mape_grupa2': {'sedela': 'sjedjela', 'sedeli': 'sjedjeli', 'sedeo': 'sjedio', 'sedio': 'sjedio', 'sede': 'sjede', 'sedu': 'sjedu', 'sedi': 'sjedi', 'sedog': 'sjedog', 'sedoh': 'sjedoh', 'sedeti': 'sjedjeti'}
    },
    {
        'ekavski': {'svet', 'sveta', 'svetu', 'svetom', 'svetovi', 'svetova', 'svetovima'},
        'kljucevi1': ['bog', 'crkv', 'otac', 'duh', 'krst', 'ikona', 'svešten', 'vjera', 'knji', 'vidi'],
        'kljucevi2': [],
        'mape_grupa1': {'svet': 'svet', 'sveta': 'sveta', 'svetu': 'svetu', 'svetom': 'svetom', 'svetovi': 'svetovi', 'svetova': 'svetova', 'svetovima': 'svetovima'},
        'mape_grupa2': {'svet': 'svijet', 'sveta': 'svijeta', 'svetu': 'svijetu', 'svetom': 'svijetom', 'svetovi': 'svjetovi', 'svetova': 'svjetova', 'svetovima': 'svjetovima'},
    },
    {
        'ekavski': {'selo', 'sela', 'selu', 'selom', 'selima'},
        'kljucevi1': ['stolic', 'fotelj', 'klup', 'mest', 'sto', 'sof', 'park', 'sati', 'mirn', 'prozor', 'pod', 'kuć', 'ispred', 'ptica', 'dete', 'dijete'],
        'kljucevi2': [],
        'mape_grupa1': {'selo': 'sjelo', 'sela': 'sjela', 'selu': 'sjelu', 'selom': 'sjelom', 'selima': 'sjelima'},
        'mape_grupa2': {'selo': 'selo', 'sela': 'sela', 'selu': 'selu', 'selom': 'selom', 'selima': 'selima'}
    },
    {
        'ekavski': {'dela', 'delu', 'delo', 'delima', 'delom'},
        'kljucevi1': ['kuć', 'poslovn', 'prostor', 'imovin', 'zemljišt', 'plac', 'soba', 'sprat', 'zgrad', 'dvorišt', 'ispit', 'prijemn', 'završn', 'dipl', 'posl', 'centr','donj','ošte'],
        'kljucevi2': [],
        'mape_grupa1': {'dela': 'dijela', 'delu': 'dijelu',  'delovima': 'djelovima', 'delom': 'dijelom'},
        'mape_grupa2': {'dela': 'djela', 'delu': 'djelu', 'delo': 'djelo', 'delima': 'djelima', 'delom': 'djelom'}
    },
    {
        'ekavski': {'veće', 'veća', 'veću', 'većim', 'većeg', 'većoj'},
        'kljucevi1': ['glomazn', 'gabarit', 'velik', 'poras', 'poveć', 'broj', 'dimenzij', 'tež', 'vis', 'šir', 'manj', 'dupl', 'obim'],
        'kljucevi2': [],
        'mape_grupa1': {'veće': 'veće', 'veća': 'veća', 'veću': 'veću', 'većim': 'većim', 'većeg': 'većeg', 'većoj': 'većoj'},
        'mape_grupa2': {'veće': 'vijeće', 'veća': 'vijeća', 'veću': 'vijeću', 'većim': 'vijećima', 'većeg': 'vijeća', 'većoj': 'vijeću'}
    },
    {
        'ekavski': {'primene', 'primena', 'primeni', 'primenu', 'primenom', 'primenama'},
        'kljucevi1': ['alat', 'oruđ', 'kupil', 'sprem', 'priprem', 'planir', 'kazn', 'mjer', 'mjere', 'sankcij'],
        'kljucevi2': [],
        'mape_grupa1': {'primene': 'primijene',  'primeni': 'primijeni'},
        'mape_grupa2': {'primene': 'primjene', 'primena': 'primjena', 'primeni': 'primjeni', 'primenu': 'primjenu', 'primenom': 'primjenom', 'primenama': 'primjenama'}
    },
    {
        'ekavski': {'reci', 'recima'},
        'kljucevi1': ['nekom', 'tati', 'bratu', 'prijatelj', 'kaž', 'rekn', 'istinu', 'poruk', 'pism', 'glasn', 'tiho'],
        'kljucevi2': [],
        'mape_grupa1': {'reci': 'reci', 'recima': 'recima'},
        'mape_grupa2': {'reci': 'rijeci', 'recima': 'riječima'}
    },
    {
        'ekavski': {'preko', 'preka', 'preke', 'preku', 'preki', 'prekog', 'prekom'},
        'kljucevi1': ['ljut', 'pogled', 'mrštit', 'osion', 'gled', 'izraz', 'oči', 'reč', 'riječ', 'narav', 'gnev', 'gnijev', 'prekor', 'hladn'],
        'kljucevi2': [],
        'mape_grupa1': {'preko': 'prijeko', 'preka': 'prijeka', 'preke': 'prijeke', 'preku': 'prijeku', 'preki': 'prijeki', 'prekog': 'prijekog', 'prekom': 'prijekom'},
        'mape_grupa2': {'preko': 'preko', 'preka': 'preka', 'preke': 'preke', 'preku': 'preku', 'preki': 'preki', 'prekog': 'prekog', 'prekom': 'prekom'}
    },
    {
        'ekavski': {'slede', 'sledi', 'slediti', 'sledile', 'sledila', 'sledilo', 'sledili'},
        'kljucevi1': ['krv', 'strah', 'užas', 'šok', 'hladnoć', 'mraz', 'ledu', 'pogled'],
        'kljucevi2': [],
        'mape_grupa1': {'slede': 'slede', 'sledi': 'sledi', 'slediti': 'slediti', 'sledila': 'sledila', 'sledilo': 'sledilo', 'sledili': 'sledili'},
        'mape_grupa2': {'slede': 'slijede', 'sledi': 'slijedi', 'slediti': 'slijediti', 'sledile': 'slijedile', 'sledila': 'slijedila', 'sledilo': 'slijedilo', 'sledili': 'slijedili'},
    },
    {
        'ekavski': {'sledeća', 'sledeći', 'sledeće', 'sledeću', 'sledećih', 'sledećem', 'sledećeg', 'sledećima'},
        'kljucevi1': ['prim', 'uputstv', 'pravil', 'savjet', 'savet', 'korak', 'trag', 'put', 'vođ', 'mentor'],
        'kljucevi2': [],
        'mape_grupa1': {'sledeća': 'slijedeća', 'sledeći': 'slijedeći', 'sledeće': 'slijedeće', 'sledeću': 'slijedeću', 'sledećih': 'slijedećih', 'sledećem': 'slijedećem', 'sledećeg': 'slijedećeg', 'sledećima': 'slijedećima'},
        'mape_grupa2': {'sledeća': 'sljedeća', 'sledeći': 'sljedeći', 'sledeće': 'sljedeće', 'sledeću': 'sljedeću', 'sledećih': 'sljedećih', 'sledećem': 'sljedećem', 'sledećeg': 'sljedećeg', 'sledećima': 'sljedećima'}
    },
    {
        'ekavski': {'nema'},
        'kljucevi1': ['ust',  'sved', 'svjed', 'ostal', 'posta', 'stoj', 'gled', 'sluš', 'glu', 'slep', 'slijep', 'hlad', 'nepom'],
        'kljucevi2': [],
        'mape_grupa1': {'nema': 'nijema'},
        'mape_grupa2': {'nema': 'nema'}
    },
    {
        'ekavski': {'izvesti'},
        'kljucevi1': ['doga', 'inform', 'medij', 'program', 'uživo', 'javnost', 'gledaoc', 'narod', 'izvešt', 'izvešt'],
        'kljucevi2': [],
        'mape_grupa1': {'izvesti': 'izvijesti'},
        'mape_grupa2': {'izvesti': 'izvesti'}
    },
    {
        'ekavski': {'nem'},
        'kljucevi1': ['ust',  'sved', 'svjed', 'ostal', 'posta', 'stoj', 'gled', 'sluš', 'glu', 'slep', 'slijep', 'hlad', 'nepom'],
        'kljucevi2': [],
        'mape_grupa1': {'nem': 'nijem'},
        'mape_grupa2': {'nem': 'njem'}
    },
    {
        'ekavski': {'letu', 'leti'},
        'kljucevi1': ['ptic', 'avio', 'neb', 'heli', 'balo', 'inse', 'pilo', 'eska'],
        'kljucevi2': [],
        'mape_grupa1': {'letu': 'letu', 'leti': 'leti'},
        'mape_grupa2': {'letu': 'ljetu', 'leti': 'ljeti'}
    }
,
     {
        'ekavski': {'zahteva'},  
        'kljucevi1': ['služb', 'zvanič', 'pism', 'opravd', 'neopravd', 'ponovlj', 'skromn', 'pretjer', 'nereal', 'podnij', 'predat', 'odobri', 'prihvat', 'odbi', 'odbac', 'uputi', 'povuć', 'razmotr', 'ispun', 'ugovolj', 'posebn', 'lice', 'rešav', 'rješav', 'izuzeć', 'posebnog', 'podnošenj', 'zaštit', 'dostav', 'podnosioc', 'broj', 'zakon'],
        'kljucevi2': [],      
        'mape_grupa1': {'zahteva': 'zahtjeva'},
        'mape_grupa2': {'zahteva': 'zahtijeva'}  
    },
    {
        'ekavski': {'izmene', 'izmeni'},  
        'kljucevi1': ['potpun', 'koren', 'korijen', 'delimič', 'djelimič', 'značaj', 'bitn', 'minim', 'neznat', 'smest', 'naknad', 'unapre', 'unaprije', 'vrem', 'vrijem', 'dopuni', 'stanj'],
        'kljucevi2': [],
        'mape_grupa1': {'izmene': 'izmijene', 'izmeni': 'izmijeni'},
        'mape_grupa2': {'izmene': 'izmjene', 'izmeni': 'izmjeni'}  
    },
    {
        'ekavski': {'razmene', 'razmeni'},  
        'kljucevi1': ['reč', 'riječ', 'mišlj', 'utisk', 'telefon', 'kontakt', 'adres', 'poklon', 'nežn', 'nježn', 'pogled', 'novac', 'iskustv', 'među', 'brzo', 'srdačno', 'otvoren'],
        'kljucevi2': [],
        'mape_grupa1': {'razmene': 'razmijene', 'razmeni': 'razmijeni'},
        'mape_grupa2': {'razmene': 'razmjene', 'razmeni': 'razmjeni'}  
    },
    {
        'ekavski': {'procene', 'proceni'},  
        'kljucevi1': ['praviln', 'objektiv', 'realn', 'pogrešn', 'brzo', 'odokativ', 'situac', 'rizik', 'štet', 'vredn', 'vrijedn', 'tužil'],
        'kljucevi2': [],
        'mape_grupa1': {'procene': 'procijene', 'proceni': 'procijeni'},
        'mape_grupa2': {'procene': 'procjene', 'proceni': 'procjeni'}  
    },
    {
        'ekavski': {'povrede', 'povredi'},  
        'kljucevi1': ['ljud', 'igrač', 'riječ', 'reč', 'često', 'lako', 'namern', 'namjern', 'slučajn', 'nekog', 'prijatelj', 'ponos', 'osjeć', 'oseć'],
        'kljucevi2': [],
        'mape_grupa1': {'povrede': 'povrijede', 'povredi': 'povrijedi'},
        'mape_grupa2': {'povrede': 'povrede', 'povredi': 'povredi'}  
    },
    {
        'ekavski': {'video'},  
        'kljucevi1': ['nadzo', 'sistem', 'oprem', 'kamer', 'live', 'digit', 'mutan', 'dugi', 'kratki', 'pokrenu', 'pustit', 'premot', 'smini', 'montir', 'skinut', 'snim', 'zapis', 'signal', 'produkc', 'bim', 'strim', 'objekt', 'zgrad', 'ulic', 'bank'],
        'kljucevi2': [],
        'mape_grupa1': {'video': 'video'},
        'mape_grupa2': {'video': 'vidio'}  
    },
    {
        'ekavski': {'vest'},  
        'kljucevi1': ['orindž','orange','palm','bič','beach','virdžin','virgin','point','indi','bank','end','sajd','side','hem','junaj','unite','brom','kany','jerr','tarib'],
        'kljucevi2': [],
        'mape_grupa1': {'vest': 'vest'},
        'mape_grupa2': {'vest': 'vijest'}  
    }

]


FRAZE_PATTERNS = []
sve_fraze = {**{k: v for k, v in EXACT.items() if " " in k}, **STEM_FRAZE}
for fraza, zamjena in sorted(sve_fraze.items(), key=lambda x: len(x[0]), reverse=True):
    pattern = re.compile(r"\b" + re.escape(fraza) + r"\b", re.IGNORECASE)
    FRAZE_PATTERNS.append((pattern, fraza, zamjena))  # Popravljeno: pakuje 3 vrijednosti


STEMS_SORTED = sorted(STEMS.keys(), key=len, reverse=True)
IMENA_IZUZECI_KORIJENI = ["vera", "veri", "veru", "vere", "vero", "sedić", "seden", "sedlar", "slepč", "unesk", "cvetk", "penelop", "meri", "penezi", "bela", "beli", "sneža"]
IZUZECI_VELIKO_SLOVO = {"Nemci", "Nemcima", "Nemaca"}
# --- OPTIMIZACIJA 1: INDEXIRANJE KONTEKST_MAPE U O(1) RJEČNIK ---
BRZI_KONTEKST = {}
for m in KONTEKST_MAPE:
    for rjec in m['ekavski']:
        BRZI_KONTEKST[rjec] = {
            'kljucevi1': m['kljucevi1'],
            'grupa1': m['mape_grupa1'],
            'grupa2': m['mape_grupa2']
        }

STEMS_SORTED = sorted(STEMS.keys(), key=len, reverse=True)

# --- OPTIMIZACIJA 2: MASOVNI REGEX ZA KORIJENE (IZBJEGAVANJE PETLJE) ---
DOPUŠTENI_KORIJENI = [k for k in STEMS_SORTED if len(k) >= 4 or k in STEMS]
KORIJENI_REGEX = re.compile(r'(' + '|'.join(re.escape(k) for k in DOPUŠTENI_KORIJENI) + r')')

def skini_dz(tekst):
    mape = {'č':'c', 'ć':'c', 'š':'s', 'ž':'z', 'đ':'d', 
            'Č':'C', 'Ć':'C', 'Š':'S', 'Ž':'Z', 'Đ':'D', 'Ś':'S', 'ś':'s'}
    return "".join(mape.get(c, c) for c in tekst)

def napravi_fleksibilan_regex(riječ):
            rezultat = ""
            mape_slova = {
                'c': '[cčć]', 's': '[sšś]', 'z': '[zž]', 'd': '[dđ]',
                'C': '[CČĆ]', 'S': '[SŠŚ]', 'Z': '[ZŽ]', 'D': '[DĐ]', 'Ś': '[SŠŚ]', 'ś': '[sšś]'
            }
            for c in riječ:
                c_cisto = skini_dz(c)
                rezultat += mape_slova.get(c_cisto, re.escape(c))
            return rezultat

# --- OPTIMIZACIJA 3: PRE-KOMPAJLOVANJE FRAZA VAN PETLJE ---
# --- GLOBALNA INICIJALIZACIJA NA DNU KODA (IZVAN SVIH FUNKCIJA) ---
PREKOMPAJLOVANE_FRAZE = []
sve_fraze = {**{k: v for k, v in EXACT.items() if " " in k}, **STEM_FRAZE}
for fraza, zamjena in sorted(sve_fraze.items(), key=lambda x: len(x), reverse=True):
    djelovi = fraza.split()
    regex_djelovi = []
    for d in djelovi:
        cisto = skini_dz(d)
        varijante = [re.escape(d)]
        if cisto != d:
            varijante.append(re.escape(cisto))
        regex_djelovi.append("(" + "|".join(varijante) + ")")
    
    if fraza in STEM_FRAZE:
        pattern_str = r"\b" + r"([a-zA-ZčćžšđČĆŽŠĐ\u0400-\u04FF]*) ".join(regex_djelovi) + r"([a-zA-ZčćžšđČĆŽŠĐ\u0400-\u04FF]*)\b"
    else:
        pattern_str = r"\b" + r"([a-zA-ZčćžšđČĆŽŠĐ\u0400-\u04FF]*)".join(regex_djelovi) + r"\b"
    PREKOMPAJLOVANE_FRAZE.append((re.compile(pattern_str, re.IGNORECASE), fraza, zamjena))
FRAZE_SORTIRANE = sorted(sve_fraze.items(), key=lambda x: len(x[0]), reverse=True)


# BRZO: Jedan prolaz kroz tekst za sve korijene
STEMS_REGEX = re.compile(r'(' + '|'.join(re.escape(k) for k in STEMS_SORTED) + r')')







def _sacuvaj_velika_slova(izv, zam):
    if not izv or not zam: return zam
    if izv.isupper(): return zam.upper()
    return "".join(zam[i].upper() if izv[i if i < len(izv) else -1].isupper() else zam[i].lower() for i in range(len(zam)))


def stabilno_sjecenje_kvačica(rijec, idx, korijen_len, zamjena):
    # Pravi Python na serveru ovdje savršeno računa poziciju slova š, č, ć, ž
    sufiks = rijec[idx + korijen_len:]
    return rijec[:idx] + zamjena + sufiks

def a_rijec(rijec, is_start, okolni_tekst):
    r_low = rijec.lower()
    if "e" not in r_low: return rijec

    if (rijec.istitle() or rijec.isupper()) and any(r_low.startswith(k) for k in IMENA_IZUZECI_KORIJENI):
        if not is_start: return rijec
        if r_low not in STEMS:
            je_u_stems = False
            for l in range(5, min(12, len(r_low) + 1)):
                if r_low[:l] in STEMS:
                    je_u_stems = True; break
            if not je_u_stems: return rijec

    if r_low in EXACT:
        return rijec if (rijec.isupper() and not is_start) else _sacuvaj_velika_slova(rijec, EXACT[r_low])
        
    if r_low in STEMS:
        if rijec.isupper() and not is_start and rijec in IZUZECI_VELIKO_SLOVO: return rijec
        return _sacuvaj_velika_slova(rijec, STEMS[r_low])

    if r_low in BRZI_KONTEKST:
        m = BRZI_KONTEKST[r_low]
        baza = m['grupa1'] if any(k in okolni_tekst for k in m['kljucevi1']) else m['grupa2']
        return _sacuvaj_velika_slova(rijec, baza[r_low]) if r_low in baza else rijec

    # --- DRASTIČNO UBRZANJE: Izbjegavanje KORIJENI_REGEX.search ---
    prefiksi = [ 'raz', 'pri', 'pre', 'pro', 'nad', 'pod', 'ob', 'za', 'do', 'na', 'iz', 'su', 'od']
    r_low_obradjena = r_low
    odseceni_prefiks = ""
    
    for p in prefiksi:
        if r_low.startswith(p) and len(r_low) > len(p) + 2:
            odseceni_prefiks = r_low[:len(p)]
            r_low_obradjena = r_low[len(p):]
            break

    korijen = None
    for k in STEMS_SORTED:
        if k in r_low:
            korijen = k
            break
            
    if korijen:
        idx = r_low.find(korijen)
        if rijec.isupper() and not is_start and rijec in IZUZECI_VELIKO_SLOVO: 
            return rijec
            
        prefiks_komplet = rijec[:idx]
        sufiks = rijec[idx + len(korijen):]
        sufiks_low = r_low[idx + len(korijen):]
        zamjena = STEMS[korijen]
        
        # Logika za pretrp-eo -> pretrp-io
        if korijen.endswith("e") and zamjena.endswith("e") and sufiks_low.startswith("o"):
            baza = zamjena
            for kraj in ["ije", "je"]:
                if baza.endswith(kraj): 
                    baza = baza[:-len(kraj)]
                    break
            sufiks = _sacuvaj_velika_slova(rijec[idx + len(korijen):idx + len(korijen) + 1], "io") + rijec[idx + len(korijen) + 1:]
            return prefiks_komplet + _sacuvaj_velika_slova(rijec[idx:idx + len(korijen)], baza) + sufiks
            
        return prefiks_komplet + _sacuvaj_velika_slova(rijec[idx:idx + len(korijen)], zamjena) + sufiks

    return rijec


def procesiraj_recenicu(recenica, predlozak_tekst):
    # Eksplicitno dodata naša slova sa dijakritičkim znacima u regex
    pattern = r'([a-zA-ZčćžšđČĆŽŠĐ]+)'
    
    tokeni = re.split(pattern, recenica)
    sve_rijeci = [t.lower() for t in tokeni if re.match(r'^[a-zA-ZčćžšđČĆŽŠĐ]+$', t)]
    
    is_start, idx = True, 0
    for i, tok in enumerate(tokeni):
        if re.match(r'^[a-zA-ZčćžšđČĆŽŠĐ]+$', tok):
            kontekst = " ". join(sve_rijeci[max(0, idx - 4): min(len(sve_rijeci), idx + 5)])
            tokeni[i] = a_rijec(tok, is_start, kontekst)
            is_start, idx = False, idx + 1
        elif tok.strip() and any(c in tok for c in ['.', '!', '?', '\n']):
            is_start = True
            
    return "".join(tokeni)



def _zamijeni_frazu_match(match, korijen_ekavski, korijen_ijekavski):
    pronadjeno = match.group(0)
    ekavski_words = korijen_ekavski.split()
    ijekavski_words = korijen_ijekavski.split()
    novi_djelovi = []
    tokeni_meca = re.split(r'([a-zA-ZčćžšđČĆŽŠĐ]+)', pronadjeno)
    w_brojac = 0

    for tok in tokeni_meca:
        if re.match(r'^[a-zA-ZčćžšđČĆŽŠĐ]+$', tok) and w_brojac < len(ekavski_words):
            izv_w, ek_w, ij_w = tok, ekavski_words[w_brojac], ijekavski_words[w_brojac]
            ek_cisto = skini_dz(ek_w)
            nastavak = izv_w[len(ek_cisto):] if len(izv_w) >= len(ek_cisto) else ""
            rezultujuca_rijec = ij_w + nastavak
            
            if izv_w.isupper():
                zamjena = rezultujuca_rijec.upper()
            elif izv_w.islower():
                zamjena = rezultujuca_rijec.lower()
            elif izv_w.istitle():
                zamjena = rezultujuca_rijec.capitalize()
            else:
                zamjena = "".join(rezultujuca_rijec[i].upper() if i < len(izv_w) and izv_w[i].isupper() else rezultujuca_rijec[i].lower() for i in range(len(rezultujuca_rijec)))
                
            novi_djelovi.append(zamjena)
            w_brojac += 1
        else:
            novi_djelovi.append(tok)
            
    return "".join(novi_djelovi)
        # Mapiranje karaktera za fleksibilan regex koji ignoriše kvačice




# --- NOVA OPTIMIZACIJA 4: MAPIRANJE SVIH KORIJENA U BRZI RJEČNIK ZA O(1) PRETRAGU ---
# Umjesto pretrage petljom kroz STEMS_SORTED, pravimo rječnik gdje je ključ korijen.
# Za korijene u sredini riječi, pravimo jedan zajednički regex.
KORIJENI_ZA_SREDINU_REGEX = re.compile(r'(' + '|'.join(re.escape(k) for k in STEMS_SORTED) + r')')

# Pravimo jedinstveni regex koji hvata sve riječi (i latinicu i ćirilicu sa kvačicama)
# Ovaj regex će odjednom izdvojiti sve tokene koji su riječi.
RIJECI_REGEX = re.compile(r'([a-zA-ZčćžšđČĆŽŠĐ\u0400-\u04FF]+)')

def zamijeni_rijeci(tekst):
    if not tekst: return tekst
    
    trenutna = tekst
    # 1. Prolaz kroz fraze (već prekompajlirano)
    for pattern, fraza, zamjena in PREKOMPAJLOVANE_FRAZE:
        def _sub_fraza_precizno(match):
            izv = match.group(0)
            je_cir = any('\u0400' <= c <= '\u04FF' for c in izv)
            ima_dz_izv = any(c in izv for c in 'čćžšđČĆŽŠĐ')
            
            lat_zam = _zamijeni_frazu_match(match, fraza, zamjena)
            if je_cir: 
                return latinica_u_cirilicu(lat_zam)
            return lat_zam if ima_dz_izv else skini_dz(lat_zam)
            
        trenutna = pattern.sub(_sub_fraza_precizno, trenutna)
            
    nova_linija_djelovi = []
    is_start = True
    
    # Koristimo prekompajlirani regex za split umjesto dinamičkog stringa
    for dio in RIJECI_REGEX.split(trenutna):
        if not dio:
            continue
            
        # Provjera da li je token riječ
        if not RIJECI_REGEX.match(dio):
            nova_linija_djelovi.append(dio)
            if any(c in dio for c in ['.', '!', '?', '\n']):
                is_start = True
            continue
            
        je_cirilica = any('\u0400' <= c <= '\u04FF' for c in dio)
        ima_dz = any(c in dio for c in 'čćžšđČĆŽŠĐ')
        
        rijec_lat = cirilica_u_latinicu(dio) if je_cirilica else dio
        r_low = rijec_lat.lower()
        
        if "e" not in r_low:
            nova_linija_djelovi.append(dio)
            is_start = False
            continue
            
        if rijec_lat.istitle() or dio.istitle():
            if r_low in IMENA_IZUZECI_KORIJENI:
                nova_linija_djelovi.append(dio)
                is_start = False
                continue
            # --- OVDJE JE SPAS ZA VEROVATNO / VEROVAO ---
            # Dozvoljavamo blokadu preko startswith izuzetaka SAMO ako riječ NIJE verovatno/verovao/veruje
            if not is_start and not r_low.startswith("verova") and not r_low.startswith("veruj"):
                if any(r_low.startswith(k) for k in IMENA_IZUZECI_KORIJENI):
                    nova_linija_djelovi.append(dio)
                    is_start = False
                    continue

            



            
        if rijec_lat.istitle() or dio.istitle():
            if r_low in IMENA_IZUZECI_KORIJENI:
                nova_linija_djelovi.append(dio)
                is_start = False
                continue
            if not is_start and any(r_low.startswith(k) for k in IMENA_IZUZECI_KORIJENI):
                nova_linija_djelovi.append(dio)
                is_start = False
                continue
        
        # --- OPTIMIZOVANA PRETRAGA U O(1) ---
        if r_low in EXACT:
            tekst_ijekavski = _sacuvaj_velika_slova(rijec_lat, EXACT[r_low])
        elif r_low in STEMS:
            tekst_ijekavski = _sacuvaj_velika_slova(rijec_lat, STEMS[r_low])
        elif r_low in BRZI_KONTEKST:
            tekst_ijekavski = _sacuvaj_velika_slova(rijec_lat, BRZI_KONTEKST[r_low]['grupa2'][r_low])
        else:
            # --- JEDINSTVENO, BRZO I SIGURNO RJEŠENJE ZA PC I ANVIL ---
            # Umjesto nesigurnog for l in range bloka koji miješa 'vera' i 'verovatno',
            # koristimo prekompajlirani STEMS_REGEX koji precizno i u jednom koraku nalazi ispravan korijen.
            match_korijen = STEMS_REGEX.search(r_low)
            
            if match_korijen:
                korijen = match_korijen.group(1)
                idx = r_low.find(korijen)
                prefiks = rijec_lat[:idx]
                sufiks = rijec_lat[idx + len(korijen):]
                zamjena = STEMS[korijen]
                
                # Zadržavamo Vašu originalnu logiku za pretrp-eo -> pretrp-io koja je već radila
                sufiks_low = r_low[idx + len(korijen):]
                if korijen.endswith("e") and zamjena.endswith("e") and sufiks_low.startswith("o"):
                    baza = zamjena
                    for kraj in ["ije", "je"]:
                        if baza.endswith(kraj): 
                            baza = baza[:-len(kraj)]
                            break
                    sufiks = _sacuvaj_velika_slova(rijec_lat[idx + len(korijen):idx + len(korijen) + 1], "io") + rijec_lat[idx + len(korijen) + 1:]
                    tekst_ijekavski = prefiks + _sacuvaj_velika_slova(rijec_lat[idx:idx + len(korijen)], baza) + sufiks
                else:
                    tekst_ijekavski = prefiks + _sacuvaj_velika_slova(rijec_lat[idx:idx + len(korijen)], zamjena) + sufiks
            else:
                tekst_ijekavski = rijec_lat
                
            # --- NA SAMOM KRAJU: ANVIL UKROTITELJ REGEXA ZA PREZIMENA ---
            # Ako je riječ preživjela sve i klijentski JS u browseru se sprema da je pošalje 
            # na KORIJENI_ZA_SREDINU_REGEX, ovdje presrećemo Slepčevića ako u sebi sadrži izuzetak.
            if any(izuzetak in r_low for izuzetak in IMENA_IZUZECI_KORIJENI) and not r_low.startswith("verova") and not r_low.startswith("veruj"):
                # Ako je PC u pitanju, riječ je već ispravno prevedena iznad kroz STEMS_REGEX, 
                # pa provjeravamo da li je ostala neprevedena (Slepčević). Ako jeste, branimo je.
                if r_low == rijec_lat.lower():
                    tekst_ijekavski = rijec_lat


                
        izlaz = latinica_u_cirilicu(tekst_ijekavski) if je_cirilica else (skini_dz(tekst_ijekavski) if not ima_dz else tekst_ijekavski)
        nova_linija_djelovi.append(izlaz)
        is_start = False
        
    return "".join(nova_linija_djelovi)

      
          





# --- OPTIMIZACIJA PREVODA PISMA (JEDAN PROLAZ REGEKSA) ---
CIR_U_LAT_MAPA = {'Љ':'Lj','Њ':'Nj','Џ':'Dž','љ':'lj','њ':'nj','џ':'dž','А':'A','а':'a','Б':'B','б':'b','В':'V','в':'v','Г':'G','г':'g','Д':'D','д':'d','Ђ':'Đ','ђ':'đ','Е':'E','е':'e','Ж':'Ž','ж':'ž','З':'Z','з':'z','И':'I','и':'i','Ј':'J','ј':'j','К':'K','к':'k','Л':'L','л':'l','М':'M','м':'m','Н':'N','н':'n','О':'O','о':'o','П':'P','п':'p','Р':'R','р':'r','С':'S','с':'s','Т':'T','т':'t','Ћ':'Ć','ћ':'ć','У':'U','у':'u','Ф':'F','ф':'f','Х':'H','х':'h','Ц':'C','ц':'c','Ч':'Č','ч':'č','Ш':'Š','ш':'š','С́':'Ś','с́':'ś'}
LAT_U_CIR_MAPA = {
    'lj':'љ','nj':'њ','dž':'џ','Lj':'Љ','Nj':'Њ','Dž':'Џ','LJ':'Љ','NJ':'Њ','DŽ':'Џ',
    'A':'А','a':'а','B':'Б','b':'б','V':'В','v':'в','G':'Г','g':'г','D':'Д','d':'д',
    'Đ':'Ђ','đ':'ђ','E':'Е','e':'е','Ž':'Ж','ž':'ж','Z':'З','z':'з','I':'И','i':'и',
    'J':'Ј','j':'ј','K':'К','k':'к','L':'Л','l':'л','M':'М','m':'м','N':'Н','n':'н',
    'O':'О','o':'о','P':'П','p':'п','R':'Р','r':'р','S':'С','s':'с','T':'Т','t':'т',
    'Ć':'Ћ','ć':'ћ','U':'У','u':'у','F':'Ф','f':'ф','H':'Х','h':'х','C':'Ц','c':'ц',
    'Č':'Ч','č':'ч','Š':'Ш','š':'ш','Ś':'С́','ś':'с́','w':'w'
}


CIR_U_LAT_REGEX = re.compile('|'.join(re.escape(k) for k in CIR_U_LAT_MAPA.keys()))
LAT_U_CIR_REGEX = re.compile('|'.join(re.escape(k) for k in LAT_U_CIR_MAPA.keys()))


def cirilica_u_latinicu(tekst):
    return CIR_U_LAT_REGEX.sub(lambda m: CIR_U_LAT_MAPA[m.group(0)], tekst)

def latinica_u_cirilicu(tekst):
    return LAT_U_CIR_REGEX.sub(lambda m: LAT_U_CIR_MAPA[m.group(0)], tekst)

def a_datoteku(ulaz, izlaz):
    if not os.path.isfile(ulaz): print(f"Greška: '{ulaz}'..."); sys.exit(1)
    with open(ulaz, encoding="utf-8") as f: t = f.read()
    with open(izlaz, "w", encoding="utf-8") as f: f.write(zamijeni_rijeci(t))
    print(f"Završeno: '{ulaz}' -> '{izlaz}'")

if __name__ == "__main__":
    if len(sys.argv) == 3: a_datoteku(sys.argv[1], sys.argv[2])
