# -*- coding: utf-8 -*-
"""Quell-Anker der Rezeptzutaten (tools/dishes/ingredients.json) für gesättigte Fettsäuren und Salz.

Jede Zutat zeigt auf ein Lebensmittel einer freien Quelle:
  'BLS:<Code>'  = BLS 4.0,  'SRN:<Beschreibung>' = USDA SR Legacy (per Name), 'CH:<ID>' = Schweizer NWDB,
  'AVG:a|b'     = Mittelwert zweier Anker,  'VEG' / 'FRUIT' = Median aller rohen BLS-Gemüse- bzw. Obst-Lebensmittel,
  'ZERO'        = enthält weder Fett noch nennenswert Salz (Wasser, Essig, Spirituosen ohne Fett).
Verwendet wird nur der ANTEIL gesättigter Fettsäuren am Gesamtfett (sfa/fat) und der Salzgehalt (g/100 g).
Zweites Tupel-Element: False = Salzwert des Ankers ist für diese Zutat nicht belastbar (z. B. Pastırma ist
stärker gesalzen als das BLS-Trockenfleisch, Sucuk/Chorizo nur über Salami angenähert) -> Gericht bekommt dann
KEINEN Salzwert. Proxy-Anker (ähnliches Lebensmittel) sind mit '# Proxy' markiert.
None = keine passende freie Quelle -> Gericht bekommt weder sat_fat noch salt.
"""
A = {
 'Rinderhackfleisch': ('BLS:U010100', True), 'Lammhackfleisch': ('SRN:Lamb, ground, raw', True),
 'Rindfleisch (Schmor/Gulasch)': ('BLS:U281100', True), 'Rindfleisch (Steak/Filet/Lende)': ('BLS:U284100', True),
 'Rindfleisch fett (Brust/Querrippe)': ('BLS:U255100', True), 'Lammfleisch': ('BLS:U861100', True), 'Lammkotelett': ('BLS:U727100', True),
 'Leber (Rind/Lamm)': ('BLS:V531100', True), 'Innereien (Lamm, gemischt)': ('BLS:V544100', True), 'Rinderzunge': ('BLS:V591100', True),
 'Lammschwanzfett': ('BLS:U807100', True), 'Sucuk (Knoblauchwurst)': ('BLS:W149300', False),  # Proxy Salami
 'Pastırma': ('BLS:U101400', False),  # Proxy Trockenfleisch
 'Hähnchenbrust': ('BLS:V416100', True), 'Hähnchenkeule (ohne Knochen)': ('CH:26', True), 'Hähnchen mit Haut (ohne Knochen)': ('BLS:V414100', True),
 'Putenbrust': ('BLS:V486100', True), 'Hühnerleber': ('BLS:V634100', True), 'Ente': ('BLS:V464100', True), 'Gans': ('BLS:V474100', True),
 'Schweineschnitzel/-filet': ('BLS:U611100', True), 'Schweinenacken': ('BLS:U632100', True), 'Schweinebauch': ('BLS:U642100', True),
 'Schweinshaxe (ausgelöst)': ('SRN:Pork, fresh, leg (ham), rump half, separable lean and fat, raw', True), 'Schweinehackfleisch': ('BLS:U020100', True),
 'Hackfleisch gemischt': ('AVG:BLS:U010100|BLS:U020100', True), 'Kochschinken': ('BLS:W424000', True), 'Bauchspeck geräuchert': ('BLS:W415000', True),
 'Kasseler': ('BLS:W510000', True), 'Bratwurst': ('BLS:W222600', True), 'Bockwurst': ('BLS:W211100', True), 'Weißwurst': ('BLS:W224000', True),
 'Leberwurst': ('BLS:W880100', True), 'Leberkäse': ('BLS:W256000', True), 'Mettwurst': ('BLS:W331000', True), 'Salami': ('BLS:W149300', True),
 'Blutwurst': ('BLS:W343000', True), 'Lachs': ('BLS:T410100', True), 'Forelle': ('BLS:T422100', True), 'Karpfen': ('BLS:T501100', True),
 'Hering': ('BLS:T102100', True), 'Makrele': ('BLS:T107100', True), 'Sardelle (Hamsi)': ('BLS:T104100', True), 'Sardine': ('BLS:T105100', True),
 'Wolfsbarsch/Dorade': ('SRN:Fish, sea bass, mixed species, raw', True), 'Kabeljau': ('BLS:T204100', True), 'Seelachs': ('BLS:T207100', True),
 'Thunfisch': ('BLS:T121100', True), 'Schwertfisch': ('BLS:T612100', True), 'Fisch fettreich (Lüfer, Palamut, Bonito)': ('BLS:T121100', True),  # Proxy Thunfisch
 'Fisch mager (Weißfisch)': ('BLS:T603100', True), 'Aal': ('BLS:T041100', True), 'Garnelen': ('BLS:T753100', True), 'Miesmuscheln': ('BLS:T792100', True),
 'Kalmar': ('BLS:T020100', True), 'Oktopus': ('SRN:Mollusks, octopus, common, raw', True), 'Ei': ('BLS:E111100', True), 'Eiweiß': ('BLS:E113100', True),
 'Vollmilch': ('BLS:M111300', True), 'Milch 1,5%': ('BLS:M111200', True), 'Joghurt (3,5%)': ('BLS:M141300', True),
 'Strained Yogurt (Süzme)': ('BLS:M141500', True),  # Proxy Sahnejoghurt 10 %
 'Ayran': ('BLS:M2S8300', True), 'Schlagsahne': ('BLS:M173900', True), 'Crème fraîche': ('BLS:M176800', True), 'Schmand': ('BLS:M172700', True),
 'Magerquark': ('BLS:M713100', True), 'Speisequark 40%': ('BLS:M713500', True), 'Frischkäse': ('BLS:M710800', True), 'Mascarpone': ('BLS:M7A6800', True),
 'Butter': ('BLS:Q611000', True), 'Kaymak': ('BLS:M173900', True),  # Proxy Sahne
 'Beyaz Peynir (Schafskäse)': ('BLS:M012200', True), 'Kaşar': ('BLS:M402600', True),  # Proxy Gouda
 'Tulum Peyniri': ('BLS:M012200', False), 'Lor Peyniri': ('BLS:M741600', True), 'Hellim/Halloumi': ('BLS:M524500', True), 'Mozzarella': ('BLS:M032100', True),
 'Parmesan': ('BLS:M306400', True), 'Gouda': ('BLS:M402600', True), 'Emmentaler/Bergkäse': ('BLS:M304600', True), 'Camembert': ('BLS:M602600', True),
 'Weinblätter (eingelegt)': ('SRN:Grape leaves, canned', True), 'Weiße Bohnen (trocken)': ('SRN:Beans, white, mature seeds, raw', True),
 'Kichererbsen (trocken)': ('BLS:G770400', True), 'Kichererbsen (gekocht)': ('BLS:G770432', True), 'Rote Linsen (trocken)': ('BLS:H730000', True),
 'Grüne/Braune Linsen (trocken)': ('BLS:H725100', True), 'Dicke Bohnen (Bakla)': ('BLS:G730100', True), 'Tomatenmark': ('BLS:R160000', True),
 'Paprikamark (Biber Salçası)': ('BLS:G898400', False), 'Tomaten (Dose)': ('BLS:G568900', True), 'Reis (trocken)': ('BLS:C352000', True),
 'Bulgur': ('BLS:C119100', True), 'Couscous': ('BLS:C119200', True), 'Nudeln/Şehriye (trocken)': ('BLS:E401000', True), 'Weizenmehl': ('BLS:C214200', True),
 'Grieß': ('BLS:C219300', True), 'Speisestärke': ('BLS:C446000', True), 'Reismehl': ('BLS:C453000', True), 'Haferflocken': ('BLS:C133000', True),
 'Paniermehl': ('BLS:B821000', True), 'Brötchen/Semmel': ('BLS:B511000', True), 'Weißbrot/Toast': ('BLS:B311000', True), 'Vollkornbrot': ('BLS:B121000', True),
 'Roggenmischbrot': ('BLS:B271000', True), 'Türkisches Brot (Ekmek)': ('BLS:B311000', True), 'Lavaş/Wrap-Fladen': ('BLS:B783012', True),
 'Yufka/Filoteig': ('SRN:Phyllo dough', True), 'Tel Kadayıf': ('SRN:Phyllo dough', False), 'Blätterteig': ('BLS:D072000', True), 'Hefe': ('BLS:R459000', True),
 'Maismehl/Polenta': ('BLS:C346000', True), 'Hirse': ('BLS:C332000', True), 'Tarhana (trocken)': None, 'Kastanie': ('BLS:H230100', True),
 'Zucker': ('BLS:S111000', True), 'Honig': ('BLS:S120000', True), 'Pekmez/Traubensirup': ('BLS:S157000', True), 'Marmelade/Konfitüre': ('BLS:S132000', True),
 'Tahin': ('BLS:Q901000', True), 'Tahin-Halva': ('SRN:Candies, halavah, plain', True), 'Walnüsse': ('BLS:H120100', True), 'Mandeln': ('BLS:H210100', True),
 'Haselnüsse': ('BLS:H130100', True), 'Pistazien': ('BLS:H250600', True), 'Erdnüsse': ('BLS:H110600', True), 'Pinienkerne': ('BLS:H320100', True),
 'Kokosraspeln': ('BLS:H150400', True), 'Sesam': ('BLS:H420100', True), 'Sonnenblumenkerne': ('BLS:H430100', True), 'Kürbiskerne': ('BLS:H310100', True),
 'Mohn': ('BLS:H450100', True), 'Zitronensaft': ('BLS:F601600', True), 'Granatapfelsirup (Nar Ekşisi)': ('FRUIT', True), 'Preiselbeerkompott': ('BLS:F4A1900', True),
 'Sonnenblumenöl': ('BLS:Q320000', True), 'Olivenöl': ('BLS:Q120000', True), 'Butterschmalz': ('BLS:Q683000', True), 'Schweineschmalz': ('BLS:Q860000', True),
 'Margarine': ('SRN:Margarine, regular, 80% fat, composite, stick, with salt', True), 'Salz': ('BLS:R114000', True),
 'Pfeffer': ('BLS:R258100', True), 'Paprikapulver': ('SRN:Spices, paprika', True), 'Pul Biber (Chiliflocken)': ('SRN:Spices, paprika', False),
 'Kreuzkümmel': ('SRN:Spices, cumin seed', True), 'Zimt': ('SRN:Spices, cinnamon, ground', True), 'Oregano/Thymian/Majoran (trocken)': ('SRN:Spices, oregano, dried', True),
 'Minze getrocknet': ('SRN:Spearmint, dried', True), 'Gewürzmischung (Sumak, Muskat, Kurkuma usw.)': ('SRN:Spices, oregano, dried', False),
 'Kakaopulver': ('BLS:S711000', True), 'Zartbitterschokolade': ('BLS:S570000', True), 'Vollmilchschokolade': ('BLS:S539900', True), 'Gelatine': ('BLS:R468000', True),
 'Senf': ('BLS:R132000', True), 'Ketchup': ('BLS:R141100', True), 'Mayonnaise': ('BLS:Q991000', True), 'Essig': ('ZERO', True), 'Rotwein': ('BLS:P253000', True),
 'Weißwein': ('BLS:P210000', True), 'Bier': ('BLS:P163000', True), 'Brühe': ('AVG:BLS:X411243|BLS:X416243', True), 'Wasser': ('BLS:N110000', True),
 'Tee/Kaffee (ungesüßt)': ('BLS:N410100', True), 'Sauerkraut': ('BLS:G345902', True), 'Gewürzgurke': ('BLS:G520802', True), 'Oliven': ('BLS:H510802', True),
 'Sumak': ('SRN:Spices, oregano, dried', False), 'Kalbfleisch (Schnitzel/Keule)': ('BLS:U482100', True), 'Wildfleisch (Reh/Hirsch)': ('BLS:V212100', True),
 'Wildschweinfleisch': ('BLS:V250100', True), 'Kaninchenfleisch': ('BLS:V132100', True), 'Meerrettich': ('BLS:G630100', True), 'Marzipan': ('BLS:S421000', True),
 'Graupen (Gerste)': ('BLS:C148000', True), 'Erbsen getrocknet': ('BLS:G760400', True), 'Lebkuchengewürz/Zimt-Nelke': ('SRN:Spices, cinnamon, ground', True),
 'Speisequark 20 % Fett': ('BLS:M713300', True), 'Puddingpulver': ('BLS:R481100', True), 'Sauerrahm (10 % Fett)': ('BLS:M172700', True),
 'Rotkohl (gegart, Glas)': ('BLS:G341900', True), 'Ricotta': ('BLS:M741600', True), 'Pecorino': ('BLS:M306400', False),  # Proxy Parmesan
 'Rohschinken (Prosciutto/Jamón)': ('BLS:W441000', True), 'Chorizo': ('BLS:W149300', False), 'Stockfisch/Bacalao (gewässert)': ('BLS:T800200', False),
 'Schnecken': ('BLS:V050100', True), 'Krabbe/Krebsfleisch': ('SRN:Crustaceans, crab, blue, raw', True), 'Hummer/Langustine': ('BLS:T730100', True),
 'Blauschimmelkäse (Gorgonzola)': ('BLS:M5B1600', True), 'Ziegenkäse': ('BLS:M6A9600', True), 'Buttermilch': ('BLS:M150000', True),
 'Knäckebrot': ('BLS:B6A2000', True), 'Speiseeis': ('BLS:S243000', True), 'Butterkeks': ('BLS:D630400', True), 'Spirituose 40 %': ('BLS:P712000', True),
 'Sherry/Portwein/Likörwein': ('BLS:P431000', True), 'Likör': ('ZERO', True), 'Apfelwein/Cider': ('BLS:P353100', True), 'Kaffee (aufgebrüht)': ('BLS:N410100', True),
 'Kondensmilch gezuckert': ('BLS:M181400', True), 'Pflaumenmus': ('BLS:S161000', True), 'Fladenbrot/Pita': ('BLS:B311000', True),  # Proxy Weißbrot
 'Räucherwürstchen/Kielbasa': ('BLS:W217000', True), 'Quittenbrot': ('FRUIT', True), 'Weinbrand/Rum': ('BLS:P741000', True), 'Foie gras': None, 'Haggis': None,
 'Kutteln (Rindermagen, gegart)': ('BLS:V551100', True), 'Löffelbiskuit': ('BLS:D710200', True), 'Spekulatius-Aufstrich (Biscoff-Art)': None,
 'Limonade/Bitter-Orangen-Limonade': ('BLS:N314000', True), 'Pizzateig (roh)': ('BLS:X9A6030', True), 'Buchweizen (Graupen/Mehl)': ('BLS:C322000', True),
 'Roggenmehl Type 1370': ('BLS:C223400', True), 'Seetang/Purpurtang (Laver), gegart': ('SRN:Seaweed, laver, raw', True), 'Erdmandeln (Tigernüsse)': None,
 'Weizenkörner (Dövme/Aşurelik, trocken)': ('BLS:C111000', True), 'Sulguni/Imeruli (Salzlakenkäse, mild)': ('BLS:M012200', False),
 'Koriandergrün frisch': ('VEG', True), 'Traubensaft': ('BLS:F310600', True), 'Tkemali (saure Pflaumensauce)': None,
 'Hartkäse Schaf/Kuh (Kefalotyri/Kashkaval)': ('BLS:M302600', False), 'Rote Kidneybohnen (trocken)': ('BLS:H742100', True),
 'Frischer Salzkäse (Sirene/Brynza/Bryndza)': ('BLS:M012200', True), 'Apfelsaft': ('BLS:F110600', True), 'Orangensaft': ('BLS:F603600', True),
 'Cola/Limonade (gezuckert)': ('BLS:N330000', True), 'Zuckerrübensirup/Golden Syrup/Sirup': ('SRN:Syrup, Cane', True), 'Räucherlachs': ('BLS:T410600', True),
 'Matjeshering': ('BLS:T811100', True), 'Cheddar': ('BLS:M303700', True), 'Rindernierenfett (Suet)': ('BLS:Q890000', True), 'Grünkern/Dinkel (Korn)': ('BLS:C236000', True),
 'Beerenmischung (rot)': ('BLS:F092100', True), 'Lebkuchen/Honigkuchen': ('BLS:D650600', True), 'Kichererbsenmehl': ('BLS:H720400', True),
 'Mais': ('BLS:G570100', True), 'Rosinen/Sultaninen': ('FRUIT', True), 'Aprikosen getrocknet': ('FRUIT', True), 'Datteln': ('FRUIT', True),
 'Feigen getrocknet': ('FRUIT', True), 'Pflaumen getrocknet': ('FRUIT', True),
}
VEG = ['Zwiebel', 'Knoblauch', 'Tomate', 'Paprika grün', 'Paprika rot', 'Spitzpaprika (Sivri Biber)', 'Chilischote', 'Aubergine', 'Zucchini', 'Gurke',
 'Kartoffel', 'Süßkartoffel', 'Karotte', 'Knollensellerie', 'Lauch/Porree', 'Spinat', 'Weißkohl', 'Rotkohl', 'Blumenkohl', 'Brokkoli', 'Grüne Bohnen',
 'Grüne Erbsen', 'Rote Bete', 'Rettich/Rübe', 'Kürbis', 'Okra', 'Weiße Rübe', 'Artischocke', 'Spargel', 'Champignons', 'Blattsalat (Romana/Eisberg)',
 'Rucola', 'Petersilie', 'Dill', 'Minze frisch', 'Frühlingszwiebel', 'Schwarzkohl', 'Mangold', 'Portulak', 'Wildkräuter (Otlar)', 'Rhabarber', 'Rosenkohl',
 'Grünkohl', 'Kohlrabi', 'Fenchel', 'Pastinake/Petersilienwurzel', 'Schwarzwurzel', 'Steckrübe', 'Fenchel (Knolle)', 'Chicorée/Endivie']
FRUIT = ['Aprikose', 'Apfel', 'Birne', 'Quitte', 'Banane', 'Orange', 'Granatapfel', 'Weintraube', 'Erdbeere', 'Kirsche', 'Sauerkirsche/Vişne',
 'Pflaume/Zwetschge', 'Pfirsich', 'Wassermelone', 'Zuckermelone', 'Himbeere', 'Blaubeere', 'Maulbeere', 'Ananas', 'Johannisbeere (rot/schwarz)', 'Stachelbeere']
for n in VEG: A[n] = ('VEG', True)
for n in FRUIT: A[n] = ('FRUIT', True)
