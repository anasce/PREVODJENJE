import sys
import os
import re

def sortiraj_recnik(d):
    """Sortira rječnik: opadajuća dužina ključa, pa abecedno."""
    sortirani_kljucevi = sorted(d.keys(), key=lambda x: (-len(x), x.lower()))
    return {k: d[k] for k in sortirani_kljucevi}

def formatiraj_za_fajl(ime_recnika, d):
    """Pretvara rječnik u tekstualni format spreman za upis."""
    izlaz = f"{ime_recnika} = {{\n"
    prethodna_duzina = None
    for k, v in d.items():
        if prethodna_duzina is not None and len(k) != prethodna_duzina:
            izlaz += "\n"  # Prazan red između različitih dužina
        izlaz += f"    '{k}': '{v}',\n"
        prethodna_duzina = len(k)
    izlaz += "}"
    return izlaz

def main():
    # 1. TRAŽENJE IMENA FAJLA
    ime_fajla = input("Unesite ime fajla koji ažurirate (npr. kod.py): ").strip()
    if not os.path.exists(ime_fajla):
        print(f"Greška: Fajl '{ime_fajla}' ne postoji!")
        sys.exit(1)

    # 2. ODABIR RJEČNIKA
    print("\nIzaberite rječnik u koji dodajete parove:")
    print("1) EXACT")
    print("2) STEMS")
    print("3) STEM_FRAZE")
    izbor = input("Unesite broj (1, 2 ili 3): ").strip()
    
    mape_izbora = {'1': 'EXACT', '2': 'STEMS', '3': 'STEM_FRAZE'}
    if izbor not in mape_izbora:
        print("Pogrešan unos! Prekidam.")
        sys.exit(1)
    ime_recnika = mape_izbora[izbor]

    # 3. UNOS PAROVA RIJEČI
    novi_parovi = {}
    print(f"\n--- Započinjete unos novih parova za {ime_recnika} ---")
    print("Unesite riječ 'kraj' za završetak unosa.\n")
    
    while True:
        kljuc = input("Unesite originalnu riječ (ključ): ").strip()
        if kljuc.lower() == 'kraj':
            break
        
        vrijednost = input(f"Unesite ijekavsku zamjenu za '{kljuc}': ").strip()
        if vrijednost.lower() == 'kraj':
            break
            
        if kljuc and vrijednost:
            novi_parovi[kljuc] = vrijednost
            print("Pojam je privremeno dodat u listu.\n")
        else:
            print("Unos ne smije biti prazan!\n")

    if not novi_parovi:
        print("Niste unijeli nijedan par. Izlazim bez promjena.")
        sys.exit(0)

    # 4. ČITANJE FAJLA I PARSIRANJE
    with open(ime_fajla, 'r', encoding='utf-8') as f:
        sadrzaj = f.read()

    # Regex koji pronalazi rječnik i sve parove unutar njega
    pattern = rf"{ime_recnika}\s*=\s*\{{(.*?)\}}"
    match = re.search(pattern, sadrzaj, re.DOTALL)
    
    if not match:
        print(f"Greška: Rječnik {ime_recnika} nije pronađen u fajlu!")
        sys.exit(1)
        
    unutrasnjost = match.group(1)
    
    # Izvlačimo postojeće parove iz fajla (ispravljena linija)
    postojeci_parovi = {}
    for k, v in re.findall(r"['\"](.*?)['\"]\s*:\s*['\"](.*?)['\"]", unutrasnjost):
        postojeci_parovi[k] = v

    # Spajamo stare parove sa novim koje si upravo unio
    postojeci_parovi.update(novi_parovi)

    # Sortiramo po tvom pravilu (opadajuća dužina, pa abeceda)
    sortiran_recnik = sortiraj_recnik(postojeci_parovi)
    
    # Pravimo novi tekst rječnika
    novi_recnik_tekst = formatiraj_za_fajl(ime_recnika, sortiran_recnik)
    
    # Zamjenjujemo stari rječnik novim u tekstu fajla
    pun_match = match.group(0)
    sadrzaj = sadrzaj.replace(pun_match, novi_recnik_tekst)

    # Ako je u pitanju STEMS, ažuriramo i STEMS_SORTED listu u fajlu
    if ime_recnika == 'STEMS':
        kljucevi_str = ", ".join([f"'{k}'" for k in sortiran_recnik.keys()])
        nova_lista_linija = f"STEMS_SORTED = [{kljucevi_str}]"
        sadrzaj = re.sub(r"STEMS_SORTED\s*=\s*\[.*?\]", nova_lista_linija, sadrzaj)

    # 5. UPISIVANJE NAZAD U FAJL
    with open(ime_fajla, 'w', encoding='utf-8') as f:
        f.write(sadrzaj)

    print(f"\nUspješno dodato! Fajl '{ime_fajla}' je ažuriran i sortiran.")

if __name__ == "__main__":
    main()
