# Zubereitete Grundzutaten OHNE eigenen USDA-Datensatz (quality "estimate").
# Werte werden aus der rohen USDA-Grundzutat (Basis) berechnet, nur mit dokumentierten Faktoren:
#   pro 100 g zubereitet = (roh * Retention + Fettaufnahme) / Ausbeute
#   Ausbeute = Gewicht zubereitet / Gewicht roh, Fettaufnahme = g Öl pro 100 g roh (Rapsöl, USDA-Wert aus der Liste).
# Gibt es für ein Lebensmittel keinen veröffentlichten Faktor, steht es NICHT hier (nicht raten).
#
# Quellen der Faktoren:
#   COFID  = Public Health England (2021): McCance and Widdowson's Composition of Foods Integrated Dataset (CoFID),
#            https://www.gov.uk/government/publications/composition-of-foods-integrated-dataset-cofid
#            (Open Government Licence v3.0). Genutzt werden nur Wasser- und Fettgehalt je Paar roh/zubereitet,
#            daraus die Ausbeute per Massenbilanz (fettfreie Trockenmasse bleibt erhalten):
#            Ausbeute = (100 - Wasser_roh - Fett_roh) / (100 - Wasser_zub - Fett_zub),
#            Fettaufnahme = Ausbeute * Fett_zub - Fett_roh.
#   BOGNAR = Bognár A. (2002): Tables on weight yield of food and retention factors of food constituents for the
#            calculation of nutrient composition of cooked foods (dishes). BFE-R--02-03, Bundesforschungsanstalt für
#            Ernährung, Karlsruhe. https://www.fao.org/uploads/media/bognar_bfe-r-02-03.pdf
#   NLG    = Bergström L. (1994): Nutrient losses and gains in the preparation of foods. NLG Project 1983-1993,
#            Rapport 32/94, Livsmedelsverket; Ausbeutefaktoren veröffentlicht in Phenol-Explorer
#            (Rothwell et al. 2013), http://phenol-explorer.eu/publications/1269
#
# Eintrag: (Name, Kategorie, Zustand, [Synonyme], Basis-Name (Rohware aus base_list.py), Methode)
# Methode: dict(y=Ausbeute, oil=g Rapsöl/100 g roh, ret=Retention {protein,fat,carbs,fiber} (fehlend = 1,0), src=Text)
from base_list import G

def de(x, n=2):
    return f'{x:.{n}f}'.replace('.', ',')

def num(x):
    return str(x).replace('.', ',')

def cofid(raw, cooked, how, fat_added=True):
    """raw/cooked = (Code, Name, Wasser g, Fett g) aus CoFID 2021, Blatt 1.3 Proximates.
    Ohne Fettzugabe (fat_added=False) bleibt die gesamte Trockenmasse erhalten: Ausbeute = (100 - Wasser_roh) / (100 - Wasser_zub)."""
    (rc, rn, rw, rf), (cc, cn, cw, cf) = raw, cooked
    if fat_added:
        y = (100 - rw - rf) / (100 - cw - cf)
        oil = y * cf - rf
        assert oil > 0, (cn, oil)
    else:
        y, oil = (100 - rw) / (100 - cw), 0.0
    src = (f'Ausbeute {de(y)}' + (f' und Fettaufnahme {de(oil, 1)} g Öl/100 g roh' if oil else '') +
           f' per Massenbilanz aus CoFID 2021 (PHE, OGL v3): {rc} {rn} (Wasser {num(rw)} g, Fett {num(rf)} g) -> '
           f'{cc} {cn} (Wasser {num(cw)} g, Fett {num(cf)} g); {how}')
    return dict(y=y, oil=oil, src=src)

def fixed(y, src):
    return dict(y=y, oil=0.0, src=f'Ausbeute {de(y)} aus {src}; Retention der Makronährstoffe 1,0 (nur Wasserverlust)')

# Bognár 2002, Tab. 26/28/30, Spalte "steam", A (Gemüse, essbarer Teil): Protein/Fett/KH 0,95, Ballaststoffe 0,94
STEAM_RET = dict(protein=0.95, fat=0.95, carbs=0.95, fiber=0.94)
def steamed(y, tab, food, rtab):
    return dict(y=y, oil=0.0, ret=STEAM_RET,
                src=f'Ausbeute {de(y)} aus Bognár 2002, Tab. {tab} ("{food}", e(k,p)); Retention Protein/Fett/KH 0,95, '
                    f'Ballaststoffe 0,94 aus Bognár 2002, Tab. {rtab} (steam, A)')

NLG = 'Bergström 1994 (NLG-Projekt), veröffentlicht in Phenol-Explorer, http://phenol-explorer.eu/publications/1269'
ROAST = 'im Ofen mit wenig Rapsöl geröstet; Retention der Makronährstoffe 1,0; Öl mit USDA-Werten von Rapsöl'
FRY = 'in der Pfanne in Rapsöl gebraten; Retention der Makronährstoffe 1,0; Öl mit USDA-Werten von Rapsöl'
TOM = ('13-517', 'Tomatoes, standard, raw', 94.6, 0.1)
ASP = ('13-157', 'Asparagus, raw', 91.4, 0.6)
AUB = ('13-161', 'Aubergine, raw', 92.9, 0.4)
COU = ('13-627', 'Courgette, raw', 95.0, 0.2)

E = [
# ---------------- gegrillt (ohne Fett) ----------------
("Tomate, gegrillt",G,"grilled",["gegrillte Tomate","gegrillte Tomaten","Tomaten gegrillt","Grilltomate"],"Tomate, roh",
 cofid(TOM, ('13-518', 'Tomatoes, standard, grilled, flesh and seeds only', 93.3, 0.2),
       'ohne Fett 6-9 min gegrillt; Retention der Makronährstoffe 1,0 (nur Wasserverlust)', fat_added=False)),
("Spargel grün, gegrillt",G,"grilled",["gegrillter Spargel","Spargel gegrillt","grüner Spargel gegrillt"],"Spargel grün, roh",
 cofid(ASP, ('13-639', 'Asparagus, grilled', 90.9, 0.4), 'ohne Fett gegrillt; Retention der Makronährstoffe 1,0 (nur Wasserverlust)', fat_added=False)),
("Aubergine, gegrillt",G,"grilled",["gegrillte Aubergine","Aubergine vom Grill","Melanzani gegrillt"],"Aubergine, roh",
 fixed(0.40, f'{NLG} ("Aubergine grilled")')),
("Paprika rot, gegrillt",G,"grilled",["rote Paprika gegrillt","gegrillte rote Paprika","gegrillte Paprika","Paprika gegrillt"],"Paprika rot, roh",
 fixed(0.93, f'{NLG} ("Pepper capsicum grilled")')),
("Paprika gelb, gegrillt",G,"grilled",["gelbe Paprika gegrillt","gegrillte gelbe Paprika"],"Paprika gelb, roh",
 fixed(0.93, f'{NLG} ("Pepper capsicum grilled")')),
("Paprika grün, gegrillt",G,"grilled",["grüne Paprika gegrillt","gegrillte grüne Paprika"],"Paprika grün, roh",
 fixed(0.93, f'{NLG} ("Pepper capsicum grilled")')),
# ---------------- im Ofen ----------------
("Zucchini, im Ofen geröstet (mit Öl)",G,"baked",["Ofenzucchini","Zucchini aus dem Ofen","Zucchini geröstet","geröstete Zucchini"],"Zucchini, roh",
 cofid(COU, ('13-629', 'Courgette, roasted in rapeseed oil', 90.7, 1.9), ROAST)),
("Aubergine, im Ofen geröstet (mit Öl)",G,"baked",["Ofenaubergine","Aubergine aus dem Ofen","Aubergine geröstet","geröstete Aubergine"],"Aubergine, roh",
 cofid(AUB, ('13-669', 'Aubergine, flesh and skin, roasted in rapeseed oil', 83.9, 3.8), ROAST)),
("Spargel grün, im Ofen geröstet (mit Öl)",G,"baked",["Ofenspargel","Spargel aus dem Ofen","Spargel geröstet"],"Spargel grün, roh",
 cofid(ASP, ('13-640', 'Asparagus, roasted in rapeseed oil', 89.8, 1.5), ROAST)),
("Lauch, im Ofen geröstet (mit Öl)",G,"baked",["Ofenlauch","Lauch aus dem Ofen","Porree aus dem Ofen","Lauch geröstet"],"Lauch, roh",
 cofid(('13-624', 'Leeks, raw', 90.7, 0.2), ('13-626', 'Leeks, roasted in rapeseed oil', 87.9, 1.9), ROAST)),
("Pastinake, im Ofen geröstet (mit Öl)",G,"baked",["Ofenpastinaken","Pastinaken aus dem Ofen","Pastinake geröstet","geröstete Pastinaken"],"Pastinake, roh",
 cofid(('13-312', 'Parsnip, raw', 79.3, 1.1), ('13-632', 'Parsnip, roasted in rapeseed oil', 58.6, 4.5), ROAST)),
("Zwiebel, im Ofen gebacken",G,"baked",["Ofenzwiebel","Zwiebel aus dem Ofen","gebackene Zwiebel"],"Zwiebel, roh",
 fixed(0.80, 'CoFID 2021 (PHE, OGL v3), 13-589 Onions, baked: "using weight loss of 20%, baked for 90 minutes at 180C" (ohne Fett)')),
# ---------------- in Öl gebraten ----------------
("Zucchini, in Öl gebraten",G,"fried",["Zucchini gebraten","gebratene Zucchini","Zucchini angebraten"],"Zucchini, roh",
 cofid(COU, ('13-587', 'Courgette, fried in rapeseed oil', 86.8, 4.8), FRY)),
("Aubergine, in Öl gebraten",G,"fried",["Aubergine gebraten","gebratene Aubergine","Melanzani gebraten"],"Aubergine, roh",
 cofid(AUB, ('13-577', 'Aubergine, fried in rapeseed oil', 59.5, 31.9), FRY)),
("Champignons, in Öl gebraten",G,"fried",["Champignons gebraten","Champignon gebraten","Pilze gebraten"],"Champignons, roh",
 cofid(('13-505', 'Mushrooms, white, raw', 92.9, 0.2), ('13-507', 'Mushrooms, white, fried in rapeseed oil', 79.1, 11.0), FRY)),
("Tomate, in Öl gebraten",G,"fried",["Tomate gebraten","gebratene Tomate","gebratene Tomaten","Tomaten gebraten"],"Tomate, roh",
 cofid(TOM, ('13-602', 'Tomatoes, standard, fried in rapeseed oil', 84.4, 7.7), FRY)),
# ---------------- gedämpft (Dampf, ohne Fett) ----------------
("Karotte, gedämpft",G,"cooked",["Karotte gedämpft","Möhre gedämpft","Karotten gedämpft","Karotte dampfgegart"],"Karotte, roh",
 steamed(0.90, 17, 'Carrot, steamed', 26)),
("Kohlrabi, gedämpft",G,"cooked",["Kohlrabi gedämpft","Kohlrabi dampfgegart"],"Kohlrabi, roh",
 steamed(0.90, 17, 'Kohlrabi, peeled, steamed', 26)),
("Brokkoli, gedämpft",G,"cooked",["Brokkoli gedämpft","Broccoli gedämpft","Brokkoli dampfgegart"],"Brokkoli, roh",
 steamed(1.04, 19, 'Broccoli, steamed', 28)),
("Blumenkohl, gedämpft",G,"cooked",["Blumenkohl gedämpft","Karfiol gedämpft","Blumenkohl dampfgegart"],"Blumenkohl, roh",
 steamed(0.95, 19, 'Cauliflower, steamed', 28)),
("Grüne Bohnen, gedämpft",G,"cooked",["grüne Bohnen gedämpft","Brechbohnen gedämpft","Bohnen dampfgegart"],"Grüne Bohnen, roh",
 steamed(0.91, 20, 'Green beans, steamed', 28)),
("Erbsen grün, gedämpft",G,"cooked",["Erbsen gedämpft","grüne Erbsen gedämpft"],"Erbsen grün, roh",
 steamed(0.87, 20, 'Green peas, steamed', 28)),
("Spargel grün, gedämpft",G,"cooked",["Spargel gedämpft","grüner Spargel gedämpft"],"Spargel grün, roh",
 steamed(1.00, 17, 'Asparagus, boiled, steamed', 28)),
("Rosenkohl, gedämpft",G,"cooked",["Rosenkohl gedämpft","Kohlsprossen gedämpft"],"Rosenkohl, roh",
 steamed(1.04, 18, 'Brussels sprouts, steamed', 28)),
("Spinat, gedämpft",G,"cooked",["Spinat gedämpft","Blattspinat gedämpft"],"Spinat, roh",
 steamed(0.76, 18, 'Spinach, steamed', 30)),
("Weißkohl, gedämpft",G,"cooked",["Weißkohl gedämpft","Weißkraut gedämpft"],"Weißkohl, roh",
 steamed(1.00, 18, 'White cabbage, steamed', 30)),
("Wirsing, gedämpft",G,"cooked",["Wirsing gedämpft","Wirsingkohl gedämpft"],"Wirsing, roh",
 steamed(0.99, 18, 'Savoy cabbage, steamed', 30)),
]
