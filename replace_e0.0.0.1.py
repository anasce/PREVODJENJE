import sys
import os
import re

# ─────────────────────────────────────────────────────────────────────────────
# EXACT replacements  (word boundaries on BOTH sides)
# Applied first. List longer / more-specific entries before shorter ones.
# ─────────────────────────────────────────────────────────────────────────────
EXACT = [
    # ── special / user-defined irregulars ──
    ("pevac",               "kokot"),           # rooster: kokot, not pjevac
    ("sutra",               "śutra"),

    # ── compound & longer forms ──
    ("svedočanstvo",        "svjedočanstvo"),
    ("svedočenje",          "svjedočenje"),
    ("nasledništvo",        "nasljedništvo"),
    ("naslednica",          "nasljednica"),
    ("naslednik",           "nasljednik"),
    ("celovitost",          "cjelovitost"),
    ("celovito",            "cjelovito"),
    ("celovit",             "cjelovit"),
    ("vrednost",            "vrijednost"),
    ("vrednovanje",         "vrjednovanje"),
    ("vredan",              "vrijedan"),
    ("verodostojan",        "vjerodostojan"),
    ("verovati",            "vjerovati"),
    ("vernost",             "vjernost"),
    ("verno",               "vjerno"),
    ("veran",               "vjeran"),
    ("bezbednim",           "bezbjednim"),
    ("bezbedna",            "bezbjedna"),
    ("bezbedno",            "bezbjedno"),
    ("rešenja",             "rješenja"),
    ("rešenje",             "rješenje"),
    ("predeo",              "predio"),
    ("zamena",              "zamjena"),
    ("smena",               "smjena"),
    ("promenio",            "promijenio"),
    ("promenila",           "promijenila"),
    ("promenilo",           "promijenilo"),
    ("promene",             "promjene"),
    ("promena",             "promjena"),
    ("izmenio",             "izmijenio"),
    ("zamenio",             "zamjenio"),
    ("menjao",              "mijenjao"),
    ("prisetiti",           "prisjetiti"),
    ("prisećanje",          "prisjećanje"),
    ("neravnomerno",        "neravnomjerno"),
    ("bezbednost",          "bezbjednost"),
    ("predsedništvo",       "predsjedništvo"),
    ("posedovanje",         "posjedovanje"),
    ("povređivanje",        "povrjeđivanje"),   # fixed: povrje-, not povri-
    ("povređen",            "povrijeđen"),
    ("poslepodne",          "poslijepodne"),
    ("poslediplomski",      "posljediplomski"),
    ("posledično",          "posljedično"),
    ("razumevanja",         "razumijevanja"),
    ("unapredite",          "unaprijedite"),
    ("izbegavajte",         "izbjegavajte"),
    ("posećujete",          "posjećujete"),
    ("razgovetno",          "razgovjetno"),
    ("razumeti",            "razumjeti"),
    ("preterano",           "pretjerano"),
    ("promenite",           "promijenite"),
    ("vrednosti",           "vrijednosti"),
    ("smernice",            "smjernice"),
    ("veštine",             "vještine"),
    ("uspešno",             "uspješno"),
    ("sledeći",             "sljedeći"),
    ("umesto",              "umjesto"),
    ("namesto",             "namjesto"),
    ("zahtevati",           "zahtijevati"),
    ("zahteva",             "zahtijeva"),
    ("saveta",              "savjeta"),
    ("saveti",              "savjeti"),
    ("dečaštvo",            "dječaštvo"),
    ("dečija",              "dječija"),
    ("smešan",              "smiješan"),
    ("nepoverenje",         "nepovjerenje"),
    ("nepoverljivo",        "nepovjerljivo"),
    ("nepoverljiv",         "nepovjerljiv"),
    ("poverovati",          "povjerovati"),
    ("poverenje",           "povjerenje"),
    ("devojka",             "djevojka"),
    ("namera",              "namjera"),
    ("nasmešiti",           "nasmiješiti"),
    ("pobediti",            "pobijediti"),
    ("pobeditelj",          "pobjeditelj"),
    ("pobednik",            "pobjednik"),
    ("pobeda",              "pobjeda"),
    ("doneti",              "donijeti"),
    ("grešiti",             "griješiti"),
    # grešnik intentionally omitted — stays grešnik
    ("izmenjivač",          "izmjenjivač"),
    ("menjačnica",          "mjenjačnica"),
    ("menjati",             "mijenjati"),
    ("bežanija",            "bježanija"),
    ("bežati",              "bježati"),
    ("cediljka",            "cjediljka"),
    ("ceđenje",             "cijeđenje"),
    ("cediti",              "cijediti"),
    ("letovanje",           "ljetovanje"),
    ("letovalište",         "ljetovalište"),
    ("odletanje",           "odlijetanje"),
    ("odleteti",            "odletjeti"),
    ("letenje",             "letjenje"),
    ("leteti",              "letjeti"),
    ("odmeren",             "odmjeren"),
    ("odmeriti",            "odmjeriti"),
    ("izmeriti",            "izmjeriti"),
    ("izmeriv",             "izmjeriv"),
    ("merilo",              "mjerilo"),
    ("meriti",              "mjeriti"),
    ("sedeti",              "sjedjeti"),        # fixed: sjedjeti
    ("terati",              "tjerati"),
    ("naterati",            "natjerati"),
    ("videti",              "vidjeti"),
    ("voleti",              "voljeti"),
    ("pevačica",            "pjevačica"),
    ("pevačko",             "pjevačko"),
    ("pevač",               "pjevač"),
    ("pevati",              "pjevati"),
    ("nerešeno",            "neriješeno"),
    ("nerešiv",             "nerješiv"),        # fixed: nerje-, not neri-
    ("odrešen",             "odriješen"),
    ("rešiti",              "riješiti"),
    ("podeliti",            "podijeliti"),
    ("deljenje",            "dijeljenje"),
    ("delimično",           "djelimično"),
    ("deliti",              "dijeliti"),
    ("podela",              "podjela"),
    ("gnezdo",              "gnijezdo"),
    ("kolenica",            "koljenica"),
    ("kolenaст",            "koljenast"),
    ("koleno",              "koljeno"),
    ("cenovnik",            "cjenovnik"),
    ("celoživotni",         "cjeloživotni"),
    ("cenjen",              "cijenjen"),
    ("zvezdica",            "zvjezdica"),
    ("zvezdani",            "zvjezdani"),
    ("zvezda",              "zvijezda"),
    ("svetlo",              "svijetlo"),        # fixed: svije-, not svje-
    ("osvetljenje",         "osvjetljenje"),
    ("osvetliti",           "osvijetliti"),
    ("svetlucati",          "svjetlucati"),
    ("sveća",               "svijeća"),
    ("mesečina",            "mjesečina"),
    ("mesečni",             "mjesečni"),
    ("mesečar",             "mjesečar"),
    ("mestimično",          "mjestimično"),
    ("mesec",               "mjesec"),
    ("osvestiti",           "osvijestiti"),
    ("osvešćenost",         "osvješćenost"),
    ("osvetljenost",        "osvjetljenost"),
    ("obaveštenje",         "obavještenje"),
    ("obavestiti",          "obavijestiti"),
    ("svest",               "svijest"),
    ("pesak",               "pijesak"),
    ("uspešan",             "uspješan"),
    ("uspeh",               "uspjeh"),
    ("vetrenjača",          "vjetrenjača"),
    ("vetar",               "vjetar"),
    ("dečak",               "dječak"),
    ("dečji",               "dječiji"),         # fixed: dječiji
    ("dete",                "dijete"),
    ("deca",                "djeca"),
    ("slepi",               "slijepi"),
    ("seno",                "sijeno"),
    ("sena",                "sjena"),
    ("lekovito",            "ljekovito"),
    ("lekarija",            "ljekarija"),
    ("lekarka",             "ljekarka"),
    ("lečenje",             "liječenje"),
    ("izlečiti",            "izliječiti"),
    ("lekar",               "ljekar"),
    ("lepo",                "lijepo"),
    ("lepota",              "ljepota"),
    ("telesni",             "tjelesni"),
    ("telo",                "tijelo"),
    ("breg",                "brijeg"),
    ("cvetanje",            "cvjetanje"),
    ("cvetić",              "cvjetić"),
    ("cvećar",              "cvjećar"),
    ("cvet",                "cvijet"),
    ("snežan",              "sniježan"),
    ("snežni",              "snježni"),
    ("sneg",                "snijeg"),
    ("zver",                "zvijer"),
    ("gnev",                "gnijev"),
    ("bedan",               "bijedan"),
    ("bedni",               "bijedni"),
    ("beda",                "bijeda"),
    ("zenica",              "zjenica"),
    ("mešalica",            "mješalica"),
    ("mešavina",            "mješavina"),
    ("mešati",              "miješati"),
    ("mera",                "mjera"),
    ("reka",                "rijeka"),
    ("mleko",               "mlijeko"),
    ("leto",                "ljeto"),
    ("cena",                "cijena"),
    ("hleb",                "hljeb"),
    ("vera",                "vjera"),
    ("vreme",               "vrijeme"),
    ("namestiti",           "namjestiti"),
    ("mesto",               "mjesto"),
    ("savet",               "savjet"),
    ("zauvek",              "zauvijek"),
    ("uvek",                "uvijek"),
    ("rečnik",              "rječnik"),
    ("rečica",              "rječica"),
    ("reči",                "riječi"),
    ("pena",                "pjena"),
    ("belo",                "bijelo"),
    ("bela",                "bijela"),
    ("celi",                "cijeli"),
    ("uspeo",               "uspio"),
    ("crep",                "crijep"),
    ("crevo",               "crijevo"),
    ("cev",                 "cijev"),
    ("ceo",                 "cio"),
    ("nedeljni",            "nedjeljni"),
    ("nedelja",             "nedjelja"),
    ("ponedeljkom",         "ponedjeljkom"),
    ("ponedeljak",          "ponedjeljak"),
    ("negde",               "negdje"),
    ("ovde",                "ovdje"),
    ("osmehivati",          "osmjehivati"),
    ("osmehnuti",           "osmjehnuti"),
    ("osmeh",               "osmijeh"),
    ("poslednji",           "posljednji"),
    ("posledica",           "posljedica"),
    ("posednik",            "posjednik"),
    ("posed",               "posjed"),
    ("posle",               "poslije"),
    ("povest",              "povijest"),
    ("delokrug",            "djelokrug"),
    ("delo",                "djelo"),
    ("ogrev",               "ogrjev"),
    ("pešačenje",           "pješačenje"),
    ("pešadija",            "pješadija"),
    ("pešački",             "pješački"),
    ("pešak",               "pješak"),
    ("obešenjak",           "obješenjak"),
    ("obešati",             "obješati"),
    ("obesiti",             "objesiti"),
    ("predsednica",         "predsjednica"),
    ("predsednik",          "predsjednik"),
    ("grehota",             "grjehota"),
    ("greh",                "grijeh"),
    ("blesnuti",            "bljesnuti"),
    ("blesak",              "bljesak"),
    ("neosetljiv",          "neosjetljiv"),
    ("osetljiv",            "osjetljiv"),
    ("osvežavanje",         "osvježavanje"),
    ("izvetriti",           "izvjetriti"),
    ("nežno",               "nježno"),
    ("besan",               "bijesan"),
    ("bes",                 "bijes"),
    ("vek",                 "vijek"),
    ("lek",                 "lijek"),
    ("svet",                "svijet"),
    ("smejati",             "smijati"),
]

# ─────────────────────────────────────────────────────────────────────────────
# STEM replacements  (word boundary on LEFT side only — prefix match)
# Applied AFTER EXACT. Automatically covers all morphological variants
# of a root. Pattern: (?<![^\W\d_])EKAVstem(\w*) → IJEKAVstem + suffix
#
# Example: ("oseć", "osjeć") matches
#   osećati, osećaj, osećaji, osećaju, osećajima,
#   osećanje, osećanja, osećanjima, osećanjem …
# ─────────────────────────────────────────────────────────────────────────────
STEMS = [
    # osećaj / osećanje / osećati family
    ("oseć",        "osjeć"),

    # sećanje / sećati / sećao family (to remember — distinct from oseć "to feel")
    ("seć",         "sjeć"),

    # pevati / pevač / pevanje (pevac already handled above as kokot)
    ("pev",         "pjev"),

    # menjač / menjačnica
    ("menjač",      "mjenjač"),

    # leteti / letenje / letanje — longer prefix to stay safe
    ("letan",       "lijetan"),
    ("leteć",       "leteć"),   # letećih etc — no jat change here, skip
]


# ─────────────────────────────────────────────────────────────────────────────
# Compile patterns
# ─────────────────────────────────────────────────────────────────────────────

def _exact_pattern(word: str) -> re.Pattern:
    """Full word-boundary match (no partial)."""
    return re.compile(
        r'(?<![^\W\d_])' + re.escape(word) + r'(?![^\W\d_])',
        re.UNICODE
    )

def _stem_pattern(stem: str) -> re.Pattern:
    """Left-boundary prefix match; captures the rest of the word."""
    return re.compile(
        r'(?<![^\W\d_])(' + re.escape(stem) + r')(\w*)',
        re.UNICODE
    )

_EXACT_COMPILED = [
    (_exact_pattern(ekav), ekav, ijekav)
    for ekav, ijekav in EXACT
]

_STEM_COMPILED = [
    (_stem_pattern(ekav_stem), ekav_stem, ijekav_stem)
    for ekav_stem, ijekav_stem in STEMS
]


# ─────────────────────────────────────────────────────────────────────────────
# Replacement helpers
# ─────────────────────────────────────────────────────────────────────────────

def _apply_exact(text: str) -> str:
    for pattern, ekav, ijekav in _EXACT_COMPILED:
        # lowercase
        text = pattern.sub(ijekav, text)
        # Capitalised
        cap_p = _exact_pattern(ekav.capitalize())
        text = cap_p.sub(ijekav.capitalize(), text)
        # ALL CAPS
        up_p = _exact_pattern(ekav.upper())
        text = up_p.sub(ijekav.upper(), text)
    return text


def _apply_stems(text: str) -> str:
    for pattern, ekav_stem, ijekav_stem in _STEM_COMPILED:
        def _repl(m: re.Match, ije=ijekav_stem) -> str:
            matched_stem = m.group(1)
            suffix = m.group(2)
            # Preserve original capitalisation of the stem part
            if matched_stem.isupper():
                return ije.upper() + suffix
            if matched_stem[0].isupper():
                return ije.capitalize() + suffix
            return ije + suffix
        text = pattern.sub(_repl, text)
    return text


def replace_words(text: str) -> str:
    text = _apply_exact(text)
    text = _apply_stems(text)
    return text


# ─────────────────────────────────────────────────────────────────────────────
# File processing
# ─────────────────────────────────────────────────────────────────────────────

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
        print("Usage: python3.11 replace_e.py <input_file.txt> <output_file.txt>")
        sys.exit(1)

    process_file(sys.argv[1], sys.argv[2])
