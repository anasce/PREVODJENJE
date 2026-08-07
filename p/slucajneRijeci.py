import random
import time

def ultra_brzi_izbor(ime_fajla="serbian-words-latin.txt"):
    validne_rijeci = []
    start_time = time.time()
    
    print("Čitam i filtriram fajl, molim sačekaj sekundu...")
    
    try:
        # Otvaramo fajl sa 'rb' (read binary) - ovo drastično ubrzava čitanje sa diska
        with open(ime_fajla, "rb") as fajl:
            for linija in fajl:
                # Čistimo prazne prostore na nivou bajtova
                linija = linija.strip()
                if len(linija) < 3:
                    continue
                    
                # Uzimamo unutrašnjost riječi na nivou bajtova
                unutrasnjost = linija[1:-1]
                
                # Provjera bajtova za slova 'e' (101) i 'E' (69) - najbrža moguća provjera
                if 101 in unutrasnjost or 69 in unutrasnjost:
                    # Tek sada dekodiramo samo onu riječ koja nam stvarno treba
                    rijec = linija.decode("utf-8", errors="ignore")
                    validne_rijeci.append(rijec)
                        
        # Izbor 10 nasumičnih riječi
        if len(validne_rijeci) >= 10:
            izabrane = random.sample(validne_rijeci, 10)
            print("\n--- REZULTAT ---")
            for r in izabrane:
                print(r)
        elif len(validne_rijeci) > 0:
            print(f"\nPronađeno je samo {len(validne_rijeci)} riječi:")
            for r in validne_rijeci:
                print(r)
        else:
            print("\nNijedna riječ ne ispunjava uslov.")
            
        print(f"\nUspješno završeno za: {time.time() - start_time:.2f} sekundi.")
            
    except FileNotFoundError:
        print(f"Greška: Fajl '{ime_fajla}' nije pronađen.")

# Pokreni novi kod
ultra_brzi_izbor()
