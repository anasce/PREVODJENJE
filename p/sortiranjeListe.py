
sortirana_lista = sorted(EXACT, key=lambda x: (-len(str(x[0])), str(x[0]).lower()))
    
# Upis u fajl sa UTF-8 enkodingom zbog naših slova (č, ć, š, đ, ž)
with open('sortirani_parovi.txt', 'w', encoding='utf-8') as f:
        f.write("EXACT = [\n")
        for tpl in sortirana_lista:
            f.write(f"    {tpl},\n")
        f.write("]\n")
