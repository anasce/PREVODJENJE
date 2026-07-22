import sys
import os
import re

# Word replacements: ekavian -> ijekavian
# Longer/more specific words listed before shorter ones to avoid false matches
REPLACEMENTS = [
    # --- Compound & longer forms first ---
    ("neravnomerno",    "neravnomjerno"),
    ("bezbednost",      "bezbjednost"),
    ("osvešćenost",     "osvješćenost"),
    ("osvetljenost",    "osvjetljenost"),
    ("predsedništvo",   "predsjedništvo"),
    ("posedovanje",     "posjedovanje"),
    ("povređivanje",    "povrijeđivanje"),
    ("poslepodne",      "poslijepodne"),
    ("poslediplomski",  "posljediplomski"),
    ("posledično",      "posljedično"),
    ("razumevanja",     "razumijevanja"),
    ("osećanjima",      "osjećanjima"),
    ("unapredite",      "unaprijedite"),
    ("izbegavajte",     "izbjegavajte"),
    ("posećujete",      "posjećujete"),
    ("razgovetno",      "razgovjetno"),
    ("razumeti",        "razumjeti"),
    ("preterano",       "pretjerano"),
    ("promenite",       "promijenite"),
    ("vrednosti",       "vrijednosti"),
    ("smernice",        "smjernice"),
    ("veštine",         "vještine"),
    ("uspešno",         "uspješno"),
    ("sledeći",         "sljedeći"),
    ("umesto",          "umjesto"),
    ("namesto",         "namjesto"),
    ("zahteva",         "zahtijeva"),
    ("zahtevati",       "zahtijevati"),
    ("osećate",         "osjećate"),
    ("osećaj",          "osjećaj"),
    ("saveta",          "savjeta"),
    ("saveti",          "savjeti"),
    ("dečija",          "dječija"),
    ("dečaštvo",        "dječaštvo"),
    ("smešan",          "smiješan"),
    ("poverenje",       "povjerenje"),
    ("nepoverenje",     "nepovjerenje"),
    ("nepoverljivo",    "nepovjerljivo"),
    ("nepoverljiv",     "nepovjerljiv"),
    ("poverovati",      "povjerovati"),
    ("devojka",         "djevojka"),
    ("namera",          "namjera"),
    ("smejati",         "smijati"),
    ("nasmešiti",       "nasmiješiti"),
    ("pobediti",        "pobijediti"),
    ("pobednik",        "pobjednik"),
    ("pobeditelj",      "pobjeditelj"),
    ("pobeda",          "pobjeda"),
    ("doneti",          "donijeti"),
    ("grešiti",         "griješiti"),
    ("grešnik",         "grješnik"),
    ("menjati",         "mijenjati"),
    ("izmenjivač",      "izmjenjivač"),
    ("menjačnica",      "mjenjačnica"),
    ("bežati",          "bježati"),
    ("bežanija",        "bježanija"),
    ("cediti",          "cijediti"),
    ("cediljka",        "cijediljka"),
    ("ceđenje",         "cijeđenje"),
    ("leteti",          "letjeti"),
    ("letenje",         "letjenje"),
    ("letovanje",       "ljetovanje"),
    ("letovalište",     "ljetovalište"),
    ("odletanje",       "odlijetanje"),
    ("odleteti",        "odletjeti"),
    ("meriti",          "mjeriti"),
    ("merilo",          "mjerilo"),
    ("odmeren",         "odmjeren"),
    ("odmeriti",        "odmjeriti"),
    ("izmeriti",        "izmjeriti"),
    ("izmeriv",         "izmjeriv"),
    ("sedeti",          "sjediti"),
    ("terati",          "tjerati"),
    ("naterati",        "natjerati"),
    ("videti",          "vidjeti"),
    ("voleti",          "voljeti"),
    ("pevati",          "pjevati"),
    ("pevač",           "pjevač"),
    ("pevačica",        "pjevačica"),
    ("pevačko",         "pjevačko"),
    ("pevac",           "pjevac"),
    ("rešiti",          "riješiti"),
    ("nerešeno",        "neriješeno"),
    ("nerešiv",         "neriješiv"),
    ("odrešen",         "odriješen"),
    ("deliti",          "dijeliti"),
    ("podeliti",        "podijeliti"),
    ("deljenje",        "dijeljenje"),
    ("podela",          "podjela"),
    ("delimično",       "djelimično"),
    ("gnezdo",          "gnijezdo"),
    ("koleno",          "koljeno"),
    ("kolenica",        "koljenica"),
    ("kolenaст",        "koljenast"),
    ("cenjen",          "cijenjen"),
    ("cenovnik",        "cjenovnik"),
    ("celoživotni",     "cjeloživotni"),
    ("zvezda",          "zvijezda"),
    ("zvezdani",        "zvjezdani"),
    ("zvezdara",        "zvjezdara"),
    ("zvezdica",        "zvjezdica"),
    ("svetlo",          "svjetlo"),
    ("osvetliti",       "osvjetliti"),
    ("osvetljenje",     "osvjetljenje"),
    ("svetlucati",      "svjetlucati"),
    ("sveća",           "svijeća"),
    ("mesec",           "mjesec"),
    ("mesečina",        "mjesečina"),
    ("mesečni",         "mjesečni"),
    ("mesečar",         "mjesečar"),
    ("mestimično",      "mjestimično"),
    ("svest",           "svijest"),
    ("osvestiti",       "osvijestiti"),
    ("obavestiti",      "obavijestiti"),
    ("obaveštenje",     "obaviještenje"),
    ("pesak",           "pijesak"),
    ("uspeh",           "uspjeh"),
    ("uspešan",         "uspješan"),
    ("vetar",           "vjetar"),
    ("vetrenjača",      "vjetrenjača"),
    ("mleko",           "mlijeko"),
    ("dete",            "dijete"),
    ("deca",            "djeca"),
    ("dečak",           "dječak"),
    ("dečji",           "dječji"),
    ("slepi",           "slijepi"),
    ("seno",            "sijeno"),
    ("sena",            "sjena"),
    ("lepo",            "lijepo"),
    ("lepota",          "ljepota"),
    ("lečenje",         "liječenje"),
    ("izlečiti",        "izliječiti"),
    ("lekovito",        "ljekovito"),
    ("lekar",           "ljekar"),
    ("lekarija",        "ljekarija"),
    ("lekarka",         "ljekarka"),
    ("telo",            "tijelo"),
    ("telesni",         "tjelesni"),
    ("breg",            "brijeg"),
    ("brežuljak",       "brežuljak"),
    ("cvet",            "cvijet"),
    ("cvetanje",        "cvjetanje"),
    ("cvetić",          "cvjetić"),
    ("cvećar",          "cvjećar"),
    ("sneg",            "snijeg"),
    ("snežan",          "snježan"),
    ("snežni",          "snježni"),
    ("zver",            "zvijer"),
    ("gnev",            "gnjev"),
    ("beda",            "bijeda"),
    ("bedni",           "bijedni"),
    ("bedan",           "bijedan"),
    ("zenica",          "zjenica"),
    ("mera",            "mjera"),
    ("mešati",          "miješati"),
    ("mešalica",        "mješalica"),
    ("mešavina",        "mješavina"),
    ("reka",            "rijeka"),
    ("leto",            "ljeto"),
    ("cena",            "cijena"),
    ("hleb",            "hljeb"),
    ("vera",            "vjera"),
    ("vreme",           "vrijeme"),
    ("mesto",           "mjesto"),
    ("namestiti",       "namjestiti"),
    ("savet",           "savjet"),
    ("uvek",            "uvijek"),
    ("zauvek",          "zauvijek"),
    ("reči",            "riječi"),
    ("rečica",          "rječica"),
    ("rečnik",          "rječnik"),
    ("pena",            "pjena"),
    ("bela",            "bijela"),
    ("belo",            "bijelo"),
    ("celi",            "cijeli"),
    ("uspeo",           "uspio"),
    ("ceo",             "cio"),
    ("crep",            "crijep"),
    ("crevo",           "crijevo"),
    ("cev",             "cijev"),
    ("ovde",            "ovdje"),
    ("negde",           "negdje"),
    ("nedelja",         "nedjelja"),
    ("nedeljni",        "nedjeljni"),
    ("ponedeljak",      "ponedjeljak"),
    ("ponedeljkom",     "ponedjeljkom"),
    ("osmeh",           "osmijeh"),
    ("osmehnuti",       "osmjehnuti"),
    ("osmehivati",      "osmjehivati"),
    ("posle",           "poslije"),
    ("poslednji",       "posljednji"),
    ("posledica",       "posljedica"),
    ("posed",           "posjed"),
    ("posednik",        "posjednik"),
    ("povest",          "povijest"),
    ("povređen",        "povrijeđen"),
    ("delo",            "djelo"),
    ("delokrug",        "djelokrug"),
    ("ogrev",           "ogrjev"),
    ("pešak",           "pješak"),
    ("pešački",         "pješački"),
    ("pešačenje",       "pješačenje"),
    ("pešadija",        "pješadija"),
    ("obešati",         "obješati"),
    ("obesiti",         "objesiti"),
    ("obešenjak",       "obješenjak"),
    ("predsednica",     "predsjednica"),
    ("predsednik",      "predsjednik"),
    ("greh",            "grijeh"),
    ("grehota",         "grjehota"),
    ("blesak",          "bljesak"),
    ("blesnuti",        "bljesnuti"),
    ("neosetljiv",      "neosjetljiv"),
    ("osetljiv",        "osjetljiv"),
    ("nežno",           "nježno"),
    ("osvežavanje",     "osvježavanje"),
    ("izvetriti",       "izvjetriti"),
    ("neopevan",       "neopjevan"),
    ("lek",             "lijek"),
    ("bes",             "bijes"),
    ("besan",           "bijesan"),
    ("vek",             "vijek"),
    ("svet",            "svijet"),
]

# Pre-compile patterns for word-boundary matching (handles Unicode/Slavic letters)
def _make_pattern(word: str) -> re.Pattern:
    return re.compile(
        r'(?<![^\W\d_])' + re.escape(word) + r'(?![^\W\d_])',
        re.UNICODE
    )

_COMPILED = [
    (_make_pattern(ekav), ekav, ijekav)
    for ekav, ijekav in REPLACEMENTS
]


def replace_words(text: str) -> str:
    for pattern, ekav, ijekav in _COMPILED:
        text = pattern.sub(ijekav, text)
        cap_pat = _make_pattern(ekav.capitalize())
        text = cap_pat.sub(ijekav.capitalize(), text)
        upper_pat = _make_pattern(ekav.upper())
        text = upper_pat.sub(ijekav.upper(), text)
    return text


def process_file(input_path: str, output_path: str) -> None:
    if not os.path.isfile(input_path):
        print(f"Error: input file '{input_path}' not found.")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    modified = replace_words(text)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(modified)

    print(f"Done! '{input_path}' -> '{output_path}'")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python replace_e.py <input_file.txt> <output_file.txt>")
        sys.exit(1)

    process_file(sys.argv[1], sys.argv[2])


change code to replace similar words. for examle, if osećanjima->osjećanjima, then it can replace also osećanja,osećati, osećaj, osećaji,osećaju
replace pevac with kokot, not pjevac; add sutra->śutra;set "povređivanje" to  "povrjeđivanje" not  "povrijeđivanje";
replace ("grešnik",  with       "grešnik"),   ("sedeti",   with       "sjedjeti"),   ("nerešiv",    with     "nerješiv"),,    ("svetlo",     with     "svijetlo"),    ("dečji",  with          "dječiji"),

