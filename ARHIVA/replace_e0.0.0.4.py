import sys, os, re 
EXACT = [
   
  ("prosleđivanje", "prosljeđivanje"),
  ('pre', 'prije'),
]


STEMS = [
    ('pogreši', 'pogriješiti'),
    ('pretpostavk', 'pretpostavk'),
    ('predvide', 'predvidje'),
    ('povredi', 'povrijedi'),
    ('potpreds', 'potpredsj'),
    ('ponedelj', 'ponedjelj'),
    ('obavest', 'obavijest'),
    ('prevar', 'prijevar'),
    ('povest', 'povijest'),
    ('poverlj', 'povjerlj'),
    ('prosle', 'proslije'),
    ('gnezdo', 'gnijezdo'),
    ('unapre', 'unaprije'),
    ('obavešt', 'obavješt'),
    ('nasled', 'naslijed'),
    ('zabelež', 'zabiljež'),
    ('dodeli', 'dodijeli'),
    ('podsmjeh', 'podsmjeh'),
    ('pregreja', 'pregrija'),
    ('prebole', 'prebolje'),
    ('blede', 'blijedje'),
    ('izvest', 'izvijest'),
    ('neizbež', 'neizbjež'),
    ('pobedi', 'pobijedi'),
    ('porekl', 'porijekl'),
    ('razume', 'razumije'),
    ('neizmer', 'neizmjer'),
    ('letelic', 'letjelic'),
    ('nadžive', 'nadživje'),
    ('razume', 'razumje'),
    ('usled', 'uslijed'),
    ('dospel', 'dospjel'),
    ('namešt', 'namješt'),
    ('detinj', 'djetinj'),
    ('posle', 'poslije'),
    ('svugde', 'svugdje'),
    ('greši', 'griješi'),
    ('prene', 'prenije'),
    ('oceni', 'ocijeni'),
    ('savest', 'savjest'),
    ('nalete', 'naletje'),
    ('svetsk', 'svjetsk'),
    ('neuspe', 'neuspje'),
    ('dožive', 'doživje'),
    ('preseć', 'presjeć'),
    ('kolev', 'kolijev'),
    ('podne', 'podnije'),
    ('obelež', 'obiljež'),
    ('izgore', 'izgorje'),
    ('nedelj', 'nedjelj'),
    ('koren', 'korijen'),
    ('razmer', 'razmjer'),
    ('primer', 'primjer'),
    ('menjač', 'mjenjač'),
    ('svetlo', 'svjetlo'),
    ('posled', 'posljed'),
    ('čovek', 'čovjek'),
    ('cveta', 'cvjeta'),
    ('zaver', 'zavjer'),
    ('cvet', 'cvijet'),
    ('savet', 'savjet'),
    ('lekar', 'ljekar'),
    ('slep', 'slijep'),
    ('sede', 'sjedje'),
    ('mesec', 'mjesec'),
    ('posed', 'posjed'),
    ('negde', 'negdje'),
    ('greh', 'grijeh'),
    ('obeša', 'objesa'),
    ('mlek', 'mlijek'),
    ('deli', 'dijeli'),
    ('bled', 'blijed'),
    ('odole', 'odolje'),
    ('sred', 'srijed'),
    ('vrem', 'vrijem'),
    ('preć', 'prijeć'),
    ('pover', 'povjer'),
    ('smeh', 'smijeh'),
    ('dodel', 'dodjel'),
    ('svet', 'svijet'),
    ('svedo', 'svjedo'),
    ('never', 'nevjer'),
    ('leči', 'liječi'),
    ('umest', 'umjest'),
    ('oseća', 'osjeća'),
    ('izmen', 'izmjen'),
    ('zamer', 'zamjer'),
    ('belež', 'biljež'),
    ('osvet', 'osvjet'),
    ('sten', "stijen"),
    ('obole', 'obolje'),
    ('teles', 'tjeles'),
    ('oddel', 'odijel'),
    ('kolen', 'koljen'),
    ('odne', 'odnije'),
    ('uspeh', 'uspjeh'),
    ('preds', 'predsj'),
    ('izmer', 'izmjer'),
    ('izveš', 'izvješ'),
    ('reši', 'riješi'),
    ('lepot', 'ljepot'),
    ('zver', 'zvijer'),
    ('done', 'donije'),
    ('vetar', 'vjetar'),
    ('sever', 'sjever'),
    ('nemač', 'njemač'),
    ('smenj', 'smjenj'),
    ('zvezd', 'zvjezd'),
    ('delat', 'djelat'),
    ('vred', 'vrijed'),
    ('izne', 'iznije'),
    ('devoj', 'djevoj'),
    ('namer', 'namjer'),
    ('rek', 'rijek'),
    ('oseć', 'osjeć'),
    ('lek', 'lijek'),
    ('vešt', 'vješt'),
    ('lev', 'lijev'),
    ('reč', 'riječ'),
    ('peva', 'pjeva'),
    ('već', 'vijeć'),
    ('oset', 'osjet'),
    ('cev', 'cijev'),
    ('cep', 'cijep'),
    ('žele', 'želje'),
    ('hleb', 'hljeb'),
    ('cen', 'cijen'),
    ('gnev', 'gnjev'),
    ('vide', 'vidje'),
    ('uver', 'uvjer'),
    ('mese', 'mjese'),
    ('ocen', 'ocjen'),
    ('pes', 'pijes'),
    ('smer', 'smjer'),
    ('bes', 'bijes'),
    ('pesm', 'pjesm'),
    ('lep', 'lijep'),
    ('ovde', 'ovdje'),
    ('mest', 'mjest'),
    ('greja', 'grija'),
    ('lenj', 'lijen'),
    ('peša', 'pješa'),
    ('onde', 'ondje'),
    ('une', 'unije'),
    ('det', 'dijet'),
    ('sled', 'sljed'),
    ('beža', 'bježa'),
    ('bed', 'bijed'),
    ('smeja', 'smija'),
    ('cel', 'cijel'),
    ('lete', 'letje'),
    ('uspe', 'uspje'),
    ('odel', 'odjel'),
    ('dec', 'djec'),
    ('ded', 'djed'),
    ('de', 'dije'),
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
    ('seć', 'sjeć')
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

def replace_words(text):
    return _apply_stems(_apply_exact(text))

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
