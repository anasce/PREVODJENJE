import sys, os, re 
EXACT = [
  
  ('razboleo', 'razbolio'),
  ('sledeći', 'slijedeći'), 
  ('zamenik', 'zamjenik'),
  ('svideo', 'svidio'),
  ('uvideo', 'uvidio'),
  ('pevac', 'kokot'),
  ('video', 'vidio'),
  ('hteo', 'htio'),
  ('uvid', 'uvid'),
  ('žele', 'žele'),
  ('sme', 'smije'),
  ('smeo', 'smio'),
  ('dve', 'dvije'),
 

]


STEMS = [
    ('pretpostavk', 'pretpostavk'),
    ('presecanj', 'presijecanj'),
    ('predvide', 'predvidje'),
    ('potpreds', 'potpredsj'),
    ('opredeli', 'opredijeli'),
    ('ponedelj', 'ponedjelj'),
    ('opredelj', 'opredjelj'),
    ('pregreja', 'pregrija'),
    ('povredi', 'povrijedi'),
    ('obavest', 'obavijest'),
    ('izbegav', 'izbjegav'),
    ('poverlj', 'povjerlj'),
    ('obavešt', 'obavješt'),
    ('zabelež', 'zabiljež'),
    ('podsmeh', 'podsmjeh'),
    ('prebole', 'prebolje'),
    ('premešt', 'premješt'),
    ('premest', 'premjest'),
    ('odeljak', 'odjeljak'),
    ('doprine', 'doprinije'),
    ('neizbež', 'neizbjež'),
    ('neizmer', 'neizmjer'),
    ('letelic', 'letjelic'),
    ('nadžive', 'nadživje'),
    ('prosleđ', 'prosljeđ'),
    ('osvetli', 'osvijetli'),
    ('osvetlj', 'osvjetlj'),
    ('prevar', 'prijevar'),
    ('povest', 'povijest'),
    ('sredst', 'sredst'),
    ('prosle', 'proslije'),
    ('gnezdo', 'gnijezdo'),
    ('unapre', 'unaprije'),
    ('razbol', 'razbolj'),
    ('proter', 'protjer'),
    ('nasled', 'naslijed'),
    ('pogreš', 'pogriješ'),
    ('dodeli', 'dodijeli'),
    ('izvesn', 'izvjesn'),
    ('izvest', 'izvijest'),
    ('pobedi', 'pobijedi'),
    ('porekl', 'porijekl'),
    ('posled', 'posljed'),
    ('razume', 'razumije'),
    ('razume', 'razumje'),
    ('dospel', 'dospjel'),
    ('pešačk', 'pješačk'),
    ('namešt', 'namješt'),
    ('detinj', 'djetinj'),
    ('svugde', 'svugdje'),
    ('savest', 'savjest'),
    ('nalete', 'naletje'),
    ('svetsk', 'svjetsk'),
    ('povređ', 'povrijeđ'),
    ('neuspe', 'neuspje'),
    ('vaspit', 'vaspit'),
    ('podela', 'podjela'),
    ('smatra', 'smatra'),
    ('dožive', 'doživje'),
    ('preseć', 'presjeć'),
    ('preduz', 'preduz'),
    ('stalež', 'stalež'),
    ('obelež', 'obiljež'),
    ('izgore', 'izgorje'),
    ('nedelj', 'nedjelj'),
    ('razmer', 'razmjer'),
    ('primer', 'primjer'),
    ('menjač', 'mjenjač'),
    ('svetlo', 'svjetlo'),
    ('posled', 'posljed'),
    ('vremen', 'vremen'),
    ('usled', 'usljed'),
    ('posle', 'poslije'),
    ('greši', 'griješi'),
    ('prene', 'prenije'),
    ('oceni', 'ocijeni'),
    ('kolev', 'kolijev'),
    ('podne', 'podnije'),
    ('koren', 'korijen'),
    ('svide', 'svidje'),
    ('čovek', 'čovjek'),
    ('cveta', 'cvjeta'),
    ('zaver', 'zavjer'),
    ('savet', 'savjet'),
    ('podel', 'podijel'),
    ('lekar', 'ljekar'),
    ('zamen', 'zamijen'),
    ('mesec', 'mjesec'),
    ('levic', 'ljevic'),
    ('levič', 'ljevič'),
    ('posed', 'posjed'),
    ('poset', 'posjet'),
    ('poseć', 'posjeć'),
    ('negde', 'negdje'),
    ('živet', 'živjet'),
    ('živel', 'živjel'),
    ('živeo', 'živio'),
    ('obeša', 'objesa'),
    ('odole', 'odolje'),
    ('uvide', 'uvidje'),
    ('pover', 'povjer'),
    ('dodel', 'dodjel'),
    ('svedo', 'svjedo'),
    ('never', 'nevjer'),
    ('venac', 'vijenac'),
    ('umest', 'umjest'),
    ('oseća', 'osjeća'),
    ('izmen', 'izmijen'),
    ('zamer', 'zamjer'),
    ('belež', 'biljež'),
    ('osvet', 'osvjet'),
    ('obole', 'obolje'),
    ('teles', 'tjeles'),
    ('kolen', 'koljen'),
    ('uspeh', 'uspjeh'),
    ('preds', 'predsj'),
    ('izmer', 'izmjer'),
    ('izveš', 'izvješ'),
    ('lepot', 'ljepot'),
    ('vetar', 'vjetar'),
    ('sever', 'sjever'),
    ('nemač', 'njemač'),
    ('napad', 'napad'),
    ('izved', 'izved'),
    ('nared', 'nared'),
    ('smenj', 'smjenj'),
    ('zvezd', 'zvjezd'),
    ('delat', 'djelat'),
    ('devoj', 'djevoj'),
    ('beleg', 'biljeg'),
    ('zased', 'zasijed'),
    ('namer', 'namjer'),
    ('želet', 'željet'),
    ('želet', 'željet'),
    ('ocenj', 'ocijenj'),
    ('greja', 'grija'),
    ('smeja', 'smija'),
    ('cvet', 'cvijet'),
    ('slep', 'slijep'),
    ('sede', 'sjedje'),
    ('greh', 'grijeh'),
    ('mlek', 'mlijek'),
    ('deli', 'dijeli'),
    ('besv', 'besvj'),
    ('bled', 'blijed'),
    ('sred', 'srijed'),
    ('vrem', 'vrijem'),
    ('bled', 'blijed'),
    ('ubed', 'ubijed'),
    ('preć', 'prijeć'),
    ('smeh', 'smijeh'),
    ('svet', 'svijet'),
    ('sten', 'stijen'),
    ('odel', 'odijel'),
    ('odne', 'odnije'),
    ('reši', 'riješi'),
    ('zver', 'zvijer'),
    ('done', 'donije'),
    ('vred', 'vrijed'),
    ('izne', 'iznije'),
    ('delo', 'djelo'),
    ('oseć', 'osjeć'),
    ('vešt', 'vješt'),
    ('peva', 'pjeva'),
    ('venc', 'vijenc'),
    ('cent', 'cent'),
    ('ubeđ', 'ubjeđ'),
    ('nežn', 'nježn'),
    ('mesn', 'mjesn'),
    ('oset', 'osjet'),
    ('hleb', 'hljeb'),
    ('gnev', 'gnjev'),
    ('tera', 'tjera'),
    ('vide', 'vidje'),
    ('vest', 'vijest'),
    ('dvem', 'dvjem'),
    ('uver', 'uvjer'),
    ('mese', 'mjese'),
    ('ocen', 'ocjen'),
    ('smer', 'smjer'),
    ('pesm', 'pjesm'),
    ('ovde', 'ovdje'),
    ('mest', 'mjest'),
    ('lenj', 'lijen'),
    ('peša', 'pješa'),
    ('onde', 'ondje'),
    ('sled', 'sljed'),
    ('beža', 'bježa'),
    ('breg', 'brijeg'),
    ('lete', 'letje'),
    ('uspe', 'uspje'),
    ('done', 'donije'),
    ('odel', 'odjel'),
    ('smel', 'smjel'),
    ('leč', 'liječ'),
    ('rek', 'rijek'),
    ('lek', 'lijek'),
    ('lev', 'lijev'),
    ('vol', 'volj'),
    ('reč', 'riječ'),
    ('već', 'vijeć'),
    ('cev', 'cijev'),
    ('cep', 'cijep'),
    ('pes', 'pijes'),
    ('bes', 'bijes'),
    ('lep', 'lijep'),
    ('une', 'unije'),
    ('det', 'dijet'),
    ('bed', 'bijed'),
    ('cel', 'cijel'),
    ('dec', 'djec'),
    ('ded', 'djed'),
    ('det', 'dijet'),
    ('reš', 'rješ'),
    ('ver', 'vjer'),
    ('mle', 'mlje'),
    ('ređ', 'rjeđ'),
    ('več', 'vječ'),
    ('leš', 'lješ'),
    ('meš', 'mješ'),
    ('let', 'ljet'),
    ('mer', 'mjer'),
    ('dev', 'djev'),
    ('les', 'ljes'),
    ('pev', 'pjev'),
    ('del', 'djel'),
    ('gde', 'gdje'),
    ('sen', 'sjen'),
    ('seć', 'sjeć'),
    ('hte', 'htje'),
    ('cen', 'cijen'),
    ('pre', 'prije'),
    ('bel', 'bijel'),
]



def _wb(word):
    return re.compile(r'(?<![^\W\d_])' + re.escape(word) + r'(?![^\W\d_])', re.UNICODE)

def _stem(stem):
    return re.compile(r'(?<![^\W\d_])(' + re.escape(stem) + r')(\w*)', re.UNICODE | re.IGNORECASE)

_EXACT = [(_wb(e), e, i) for e, i in EXACT]
_STEMS = [(_stem(e), e, i) for e, i in STEMS]


def _apply_exact(text):
    for pat, e, i in _EXACT:
        text = pat.sub(i, text)
        text = _wb(e.capitalize()).sub(i.capitalize(), text)
        text = _wb(e.upper()).sub(i.upper(), text)
    return text

def _apply_stems(text):
    for pat, e, i in _STEMS:
        def _r(m, ije=i):
            s, suf = m.group(1), m.group(2)
            if s.isupper(): return ije.upper() + suf
            if s[0].isupper(): return ije.capitalize() + suf
            return ije + suf
        text = pat.sub(_r, text)
    return text
def replace_words1(text):
    return _apply_stems(_apply_exact(text))
def replace_words(text):
    # Prvo sortiramo STEMS od najduže do najkraće ekavske osnove
    # Ovo garantuje da će se 'cent' poklopiti prije nego 'cen'
    sorted_stems = sorted(STEMS, key=lambda x: len(x[0]), reverse=True)

    def process_token(match):
        word = match.group(0)
        word_lower = word.lower()

        # 1. Provjera za EXACT listu (traži se cijelo poklapanje riječi)
        for e, i in EXACT:
            if word_lower == e:
                if word.isupper(): return i.upper()
                if word[0].isupper(): return i.capitalize()
                return i

        # 2. Provjera za STEMS listu (od najduže ka najkraćoj osnovi)
        for e, i in sorted_stems:
            if word_lower.startswith(e):
                sufix = word[len(e):]  # Uzimamo ostatak reči (sufiks)
                
                # Zadržavanje originalnog velikog/malog slova osnove
                if word[:len(e)].isupper():
                    return i.upper() + sufix
                if word[0].isupper():
                    return i.capitalize() + sufix
                return i + sufix

        # Ako riječ ne ispunjava nijedan uslov, vraća se nepromijenjena
        return word

    # Ovaj regex dijeli tekst na riječi (\w+) i sve ostale karaktere/interpunkciju ([^\w])
    return re.sub(r'\w+|[^\w]', process_token, text, flags=re.UNICODE)


def process_file(inp, out):
    if not os.path.isfile(inp):
        print(f"Error: '{inp}' not found."); sys.exit(1)
    with open(inp, encoding="utf-8") as f: text = f.read()
    with open(out, "w", encoding="utf-8") as f: f.write(replace_words(text))
    print(f"Done: '{inp}' -> '{out}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3.11 replace_e.py <input.txt> <output.txt>"); sys.exit(1)
    process_file(sys.argv[1], sys.argv[2])
