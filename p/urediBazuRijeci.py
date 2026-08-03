import json
import re
import unicodedata

AKCENAT_REGEX = re.compile(r"[\u0300-\u030f]|[àáâãäåèéêëìíîïòóôõöùúûüāēīōū]")
CYRILLIC_REGEX = re.compile(r"[\u0400-\u04FF]")

def ukloni_akcente(tekst):
    nfd = unicodedata.normalize('NFD', tekst)
    cisto = "".join([c for c in nfd if not unicodedata.combining(c)])
    zamjene = {'à':'a', 'á':'a', 'â':'a', 'ã':'a', 'ä':'a', 'å':'a',
               'è':'e', 'é':'e', 'ê':'e', 'ë':'e', 'ì':'i', 'í':'i',
               'î':'i', 'ï':'i', 'ò':'o', 'ó':'o', 'ô':'o', 'õ':'o',
               'ö':'o', 'ù':'u', 'ú':'u', 'û':'u', 'ü':'u', 'ā':'a',
               'ē':'e', 'ī':'i', 'ō':'o', 'ū':'u'}
    for staro, novo in zamjene.items():
        cisto = cisto.replace(staro, novo)
    return cisto

osnovna_mapa = {}
svi_zapisi = []

with open("kaikki.org-dictionary-SerboCroatian.jsonl", "r", encoding="utf-8") as f:
    for linija in f:
        try:
            podaci = json.loads(linija)
            if "word" in podaci:
                glavna = podaci["word"].strip()
                if not CYRILLIC_REGEX.search(glavna):
                    cista_glavna = ukloni_akcente(glavna)
                    if "ije" in cista_glavna or "je" in cista_glavna:
                        osnovna_mapa[cista_glavna.replace("ije", "e").replace("je", "e")] = cista_glavna
            svi_zapisi.append(podaci)
        except json.JSONDecodeError:
            continue

ekavske_sa_akcentom = set()
for podaci in svi_zapisi:
    kandidati = []
    if "word" in podaci: kandidati.append(podaci["word"])
    if "forms" in podaci:
        for forma in podaci["forms"]:
            if "form" in forma: kandidati.append(forma["form"])
            
    for rijec in kandidati:
        rijec = rijec.strip()
        if CYRILLIC_REGEX.search(rijec) or "ije" in rijec or "je" in rijec:
            continue
        if " " in rijec or any(c in rijec.lower() for c in ['x', 'q', 'w']) or any(c.isdigit() for c in rijec):
            continue
        if rijec in ["◌̀", "◌́", "̀", "́", "̂", "̄", "̏"]:
            continue
        if AKCENAT_REGEX.search(rijec):
            ekavske_sa_akcentom.add(rijec)

# Pravljenje rječnika optimizovanog za brzu pretragu
baza_rjecnik = {}
for ekavska_akcentovana in sorted(ekavske_sa_akcentom):
    ekavska_cista = ukloni_akcente(ekavska_akcentovana)
    ijekavska_cista = osnovna_mapa.get(ekavska_cista, None)
    
    baza_rjecnik[ekavska_cista] = {
        "ekavica_akcent": ekavska_akcentovana,
        "ijekavica_cista": ijekavska_cista
    }

# Čuvanje rječnika kao gotovog Python fajla
with open("baza_rijeci.py", "w", encoding="utf-8") as f_out:
    f_out.write("rijeci = " + json.dumps(baza_rjecnik, indent=4, ensure_ascii=False))

print("Fajl 'baza_rijeci.py' je uspješno napravljen!")
