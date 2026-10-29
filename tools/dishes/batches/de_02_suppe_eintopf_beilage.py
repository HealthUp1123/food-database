CUISINE = 'de'
TEXT = """
Kartoffelsuppe | Kartoffelsuppe mit Würstchen, Potato soup | S | 1.0 | 1 Teller | kartoffel 150, karotte 40, sellerie 30, lauch 30, zwiebel 20, butter 8, bockwurst 40, bruehe 250
Gulaschsuppe | Gulaschsuppe, Goulash soup | S | 1.0 | 1 Teller | rind 80, zwiebel 60, paprika 50, kartoffel 60, tomatenmark 15, paprikapulver 2, oel 8, bruehe 250
Linsensuppe | Linsensuppe mit Würstchen, Lentil soup | S | 1.0 | 1 Teller | linsen 50, karotte 40, sellerie 30, kartoffel 40, zwiebel 20, bockwurst 40, essig 5, bruehe 250
Erbsensuppe | Erbsensuppe mit Speck, Pea soup | S | 1.0 | 1 Teller | erbsen_trocken 50, kartoffel 40, karotte 30, zwiebel 20, speck 20, bockwurst 40, bruehe 250
Flädlesuppe | Pfannkuchensuppe, Frittatensuppe, Pancake soup | S | 1.0 | 1 Teller | mehl 30, ei 30, milch 40, butter 6, bruehe 250
Grießnockerlsuppe | Grießnockerlsuppe, Semolina dumpling soup | S | 1.0 | 1 Teller | griess 25, ei 25, butter 12, bruehe 250
Leberknödelsuppe | Leberknödelsuppe, Liver dumpling soup | S | 1.0 | 1 Teller | semmel 40, leber 40, ei 20, zwiebel 10, butter 8, bruehe 250
Hühnersuppe | Hühnersuppe mit Nudeln, Chicken noodle soup | S | 1.0 | 1 Teller | hahn_keule 60, nudeln 25, karotte 40, sellerie 20, lauch 20, bruehe 250
Rindfleischsuppe | Rinderbrühe mit Einlage, Beef broth | S | 1.0 | 1 Teller | rind 50, karotte 40, sellerie 30, lauch 30, nudeln 15, bruehe 250
Spargelcremesuppe | Spargelsuppe, Cream of asparagus soup | S | 1.0 | 1 Teller | spargel 120, sahne 40, butter 10, mehl 10, bruehe 200
Kürbissuppe | Kürbiscremesuppe, Pumpkin soup | S | 1.0 | 1 Teller | kuerbis 150, kartoffel 40, zwiebel 20, sahne 30, butter 8, bruehe 200
Tomatensuppe | Tomatencremesuppe, Tomato soup | S | 1.0 | 1 Teller | tomaten_dose 150, zwiebel 25, sahne 30, butter 8, mehl 8, bruehe 150
Zwiebelsuppe | Zwiebelsuppe überbacken, Onion soup | S | 0.95 | 1 Teller | zwiebel 150, butter 15, weissbrot 25, emmentaler 30, wein_weiss 30, bruehe 250
Champignoncremesuppe | Pilzcremesuppe, Cream of mushroom soup | S | 1.0 | 1 Teller | pilz 120, sahne 50, butter 10, mehl 10, zwiebel 20, bruehe 200
Brokkolicremesuppe | Brokkolisuppe, Broccoli cream soup | S | 1.0 | 1 Teller | brokkoli 130, kartoffel 40, sahne 40, zwiebel 15, bruehe 200
Möhrensuppe | Karottensuppe, Carrot soup | S | 1.0 | 1 Teller | karotte 150, kartoffel 40, zwiebel 20, sahne 30, butter 8, bruehe 200
Bohnensuppe | Weiße Bohnensuppe, Bean soup | S | 1.0 | 1 Teller | bohnen_trocken 50, karotte 30, kartoffel 40, zwiebel 20, speck 20, bruehe 250
Kohlsuppe | Weißkohlsuppe, Cabbage soup | S | 1.0 | 1 Teller | weisskohl 150, karotte 30, kartoffel 40, zwiebel 20, hack 40, bruehe 250
Sauerkrautsuppe | Sauerkrautsuppe, Sauerkraut soup | S | 1.0 | 1 Teller | sauerkraut 120, kartoffel 40, zwiebel 20, speck 20, bockwurst 40, bruehe 250
Biersuppe | Biersuppe, Beer soup | S | 1.0 | 1 Teller | bier 150, milch 60, ei 25, butter 8, zucker 8, mehl 10
Gerstensuppe | Graupensuppe, Barley soup | S | 1.0 | 1 Teller | graupen 40, karotte 40, sellerie 30, lauch 30, speck 20, bruehe 250
Schwäbische Maultaschensuppe | Maultaschen in Brühe, Maultaschen soup | S | 1.0 | 1 Teller | mehl 40, hack 40, spinat 30, semmel 15, ei 15, bruehe 250
Kaltschale | Buttermilchkaltschale, Cold fruit soup | S | 1.0 | 1 Schüssel | erdbeere 100, joghurt 100, zucker 10, milch 50
Obstsuppe | Fruchtsuppe, Fruit soup | S | 1.0 | 1 Schüssel | apfel 80, birne 60, pflaume 40, zucker 20, staerke 8, wasser 200
Hamburger Aalsuppe | Aalsuppe, Hamburg eel soup | S | 1.0 | 1 Teller | aal 60, pflaume_tr 20, birne 40, karotte 30, essig 8, zucker 5, bruehe 250
Erbseneintopf | Pea stew | E | 1.0 | 1 Teller | erbsen_trocken 70, kartoffel 100, karotte 50, speck 30, bockwurst 60, bruehe 300
Linseneintopf | Linseneintopf, Lentil stew with sausage | E | 1.0 | 1 Teller | linsen 70, kartoffel 100, karotte 40, speck 25, bockwurst 60, essig 5, bruehe 300
Steckrübeneintopf | Steckrübeneintopf, Rutabaga stew | E | 1.0 | 1 Teller | ruebe 200, kartoffel 100, schwein_bauch 70, zwiebel 20, bruehe 250
Hammeleintopf | Lamm-Kohl-Eintopf, Lamb stew German | E | 1.0 | 1 Teller | lamm 100, weisskohl 100, kartoffel 100, zwiebel 20, bruehe 250
Weißkohleintopf | Kohleintopf, Cabbage stew | E | 1.0 | 1 Teller | weisskohl 200, kartoffel 100, hack 70, zwiebel 20, bruehe 250
Möhreneintopf | Karotteneintopf, Carrot stew | E | 1.0 | 1 Teller | karotte 200, kartoffel 100, bockwurst 60, zwiebel 20, bruehe 250
Pichelsteiner Eintopf | Pichelsteiner, Bavarian stew | E | 1.0 | 1 Teller | rind 60, schwein_mager 60, lamm 40, kartoffel 100, karotte 40, weisskohl 50, lauch 30, bruehe 250
Bohneneintopf | Grüne Bohnen Eintopf | E | 1.0 | 1 Teller | gruene_bohnen 150, kartoffel 100, hack 60, zwiebel 20, bruehe 250
Gaisburger Marsch | Gaisburger Marsch, Swabian beef stew | E | 1.0 | 1 Teller | rind 100, kartoffel 100, nudeln 40, karotte 30, zwiebel 20, bruehe 250
Kohlrouladen | Kohlrouladen mit Soße, Cabbage rolls German | KF | 0.85 | 2 Stück | weisskohl 200, gemischtes_hack 150, semmel 20, ei 20, zwiebel 20, bruehe 100, oel 10
Spätzle | Eierspätzle, Swabian egg noodles | NA | 1.0 | 1 Portion | mehl 90, ei 40, wasser 40, butter 10
Käsespätzle | Kässpätzle, Cheese spaetzle | NA | 0.95 | 1 Portion | mehl 90, ei 50, emmentaler 60, zwiebel 40, butter 20, wasser 40
Linsen mit Spätzle | Linsen und Spätzle, Lentils with spaetzle | E | 1.0 | 1 Teller | linsen 60, mehl 70, ei 30, bockwurst 60, speck 20, zwiebel 20, essig 5, wasser 200
Maultaschen | Schwäbische Maultaschen, Swabian dumplings | NA | 0.95 | 3 Stück | mehl 70, ei 30, hack 60, spinat 40, semmel 20, zwiebel 20, butter 5
Geschmelzte Maultaschen | Maultaschen mit Zwiebeln, Fried maultaschen | NA | 0.95 | 1 Portion | mehl 70, ei 30, hack 60, spinat 40, semmel 20, zwiebel 40, butter 15
Schupfnudeln | Schupfnudeln gebraten, Potato noodles | NA | 0.9 | 1 Portion | kartoffel 200, mehl 60, ei 20, butter 15
Schupfnudeln mit Sauerkraut | Schupfnudeln Sauerkraut | NA | 0.9 | 1 Portion | kartoffel 150, mehl 45, ei 15, sauerkraut 120, speck 20, butter 10
Dampfnudeln | Dampfnudeln mit Vanillesoße | D | 0.95 | 1 Stück | mehl 80, milch 40, hefe 3, butter 15, zucker 10, ei 15
Spaghetti Bolognese | Bolognese, Spaghetti Bolo | NA | 1.0 | 1 Teller | nudeln 90, gemischtes_hack 90, tomaten_dose 100, zwiebel 30, karotte 20, tomatenmark 10, olivenoel 10, wasser 200
Nudelauflauf | Nudelauflauf mit Schinken, Pasta bake | NA | 0.95 | 1 Portion | nudeln 80, schinken 50, sahne 60, emmentaler 50, ei 25, wasser 160
Schinkennudeln | Schinkennudeln Pfanne, Ham noodles | NA | 0.95 | 1 Portion | nudeln 80, schinken 60, ei 50, butter 10, wasser 160
Kartoffelknödel | Kartoffelklöße, Klöße, Potato dumplings | KN | 1.0 | 2 Stück | kartoffel 250, staerke 30, ei 15, semmel 10, salz 1
Kartoffelklöße halb und halb | Halb und halb Klöße, Half-and-half dumplings | KN | 1.0 | 2 Stück | kartoffel 250, staerke 25, ei 15, salz 1
Thüringer Klöße | Thüringer Klöße, Thuringian dumplings | KN | 1.0 | 2 Stück | kartoffel 250, staerke 25, semmel 15, butter 8
Semmelknödel | Brötchenknödel, Bread dumplings | KN | 1.0 | 2 Stück | semmel 100, milch 80, ei 40, zwiebel 20, butter 10, petersilie 3
Serviettenknödel | Serviettenknödel, Napkin dumpling | KN | 1.0 | 1 Scheibe | semmel 100, milch 80, ei 40, butter 10
Speckknödel | Tiroler Speckknödel, Bacon dumplings | KN | 1.0 | 2 Stück | semmel 100, milch 70, ei 40, speck 40, zwiebel 20, butter 10
Leberknödel | Leberknödel mit Sauerkraut, Liver dumplings | KN | 1.0 | 2 Stück | semmel 60, leber 80, ei 30, zwiebel 20, butter 10, milch 30
Käseknödel | Tiroler Käseknödel | KN | 1.0 | 2 Stück | semmel 100, milch 80, ei 40, emmentaler 70, butter 10
Grießklöße | Grießknödel, Semolina dumplings | KN | 1.0 | 3 Stück | griess 50, milch 120, ei 30, butter 10
Kartoffelpüree | Kartoffelbrei, Stampfkartoffeln, Mashed potatoes | KN | 1.0 | 1 Portion | kartoffel 250, milch 50, butter 15
Salzkartoffeln | Salzkartoffeln, Boiled potatoes | KN | 1.0 | 1 Portion | kartoffel 250, salz 1
Pellkartoffeln mit Quark | Pellkartoffeln Kräuterquark, Jacket potatoes with quark | KN | 1.0 | 1 Portion | kartoffel 250, quark 100, petersilie 5, milch 20
Bratkartoffeln | Bratkartoffeln mit Zwiebeln, Fried potatoes | KN | 0.85 | 1 Portion | kartoffel 280, zwiebel 40, speck 20, oel 15
Kartoffelgratin | Kartoffelgratin, Potato gratin | KN | 0.95 | 1 Portion | kartoffel 250, sahne 80, milch 40, emmentaler 40, knoblauch 3
Kartoffelsalat schwäbisch | Schwäbischer Kartoffelsalat, Swabian potato salad | SA | 1.0 | 1 Portion | kartoffel 220, zwiebel 30, bruehe 40, essig 15, oel 12, senf 5
Kartoffelsalat mit Mayonnaise | Kartoffelsalat Mayo, Potato salad with mayo | SA | 1.0 | 1 Portion | kartoffel 200, mayonnaise 40, gewuerzgurke 30, ei 40, zwiebel 20, joghurt 20
Rösti | Kartoffelrösti, Swiss rosti | KN | 0.85 | 1 Portion | kartoffel 250, butterschmalz 20, zwiebel 20
Kartoffelecken | Kartoffelspalten, Potato wedges | KN | 0.8 | 1 Portion | kartoffel 300, oel 15, paprikapulver 2
Pommes frites | Pommes, French fries | KN | 0.55 | 1 Portion | kartoffel 280, oel 25
Kroketten | Kartoffelkroketten, Potato croquettes | KN | 0.95 | 6 Stück | kartoffel 200, ei 20, paniermehl 20, oel 20, milch 15, butter 5
Reibekuchen | Reibekuchen, Rheinische Reibekuchen | KN | 0.8 | 3 Stück | kartoffel 250, ei 30, zwiebel 20, mehl 15, oel 30
Rotkohl | Blaukraut, Apfelrotkohl, Red cabbage | B | 0.9 | 1 Portion | rotkohl 200, apfel 40, zwiebel 20, zucker 8, essig 10, schmalz 8
Sauerkraut | Sauerkraut gekocht, Cooked sauerkraut | B | 0.9 | 1 Portion | sauerkraut 200, zwiebel 20, schmalz 8
Weißkohlgemüse | Gedünsteter Weißkohl | B | 0.9 | 1 Portion | weisskohl 220, zwiebel 20, butter 8
Rosenkohl | Rosenkohl mit Butter, Brussels sprouts | B | 1.0 | 1 Portion | rosenkohl 200, butter 10
Rahmwirsing | Wirsing in Sahne, Creamed savoy cabbage | B | 0.95 | 1 Portion | weisskohl 200, sahne 50, zwiebel 20, butter 8
Rahmspinat | Spinat mit Rahm, Creamed spinach | B | 0.95 | 1 Portion | spinat 220, sahne 40, zwiebel 15, butter 8
Blumenkohl mit Sauce Hollandaise | Blumenkohl Hollandaise | B | 0.95 | 1 Portion | blumenkohl 250, butter 30, ei 20, zitrone 5
Spargel mit Sauce Hollandaise | Spargel Hollandaise, Asparagus with hollandaise | B | 0.95 | 1 Portion | spargel 300, butter 35, ei 25, zitrone 5, kartoffel 150
Spargel mit Schinken | Spargel Schinken, Asparagus with ham | HG | 0.95 | 1 Portion | spargel 300, schinken 80, butter 25, kartoffel 150
Karottengemüse | Möhrengemüse, Glazed carrots | B | 0.95 | 1 Portion | karotte 200, butter 10, zucker 3, petersilie 3
Erbsen und Möhren | Erbsen mit Möhren, Peas and carrots | B | 1.0 | 1 Portion | erbsen 100, karotte 100, butter 8
Buttergemüse | Gemüsemix mit Butter | B | 1.0 | 1 Portion | karotte 80, blumenkohl 80, brokkoli 80, butter 10
Grüne Bohnen mit Speck | Bohnen im Speckmantel, Green beans with bacon | B | 0.95 | 1 Portion | gruene_bohnen 200, speck 30, zwiebel 15, butter 5
Rahmchampignons | Champignons in Rahm, Mushrooms in cream sauce | B | 0.85 | 1 Portion | pilz 200, sahne 50, zwiebel 20, butter 10
Gebratene Champignons | Pilze gebraten, Pan fried mushrooms | B | 0.7 | 1 Portion | pilz 250, butter 12, zwiebel 20
Pfifferlinge in Rahmsoße | Rahmpfifferlinge, Chanterelles in cream | B | 0.85 | 1 Portion | pilz 200, sahne 60, zwiebel 20, butter 10
Gemüsepfanne | Gemüse-Pfanne, Vegetable stir fry | HV | 0.85 | 1 Portion | zucchini 80, paprika 60, karotte 50, pilz 60, zwiebel 30, oel 12
Linsen süßsauer | Linsengemüse süß-sauer | B | 1.0 | 1 Portion | linsen 60, zwiebel 20, essig 10, zucker 5, speck 15, bruehe 150
Apfelmus | Apfelmus selbstgemacht, Applesauce | B | 1.0 | 1 Schälchen | apfel 200, zucker 15, zitrone 5
Erbspüree | Erbspüree, Pea puree | B | 1.0 | 1 Portion | erbsen_trocken 60, butter 10, zwiebel 20, bruehe 150
Bratensoße | Bratensauce, Gravy | SD | 1.0 | 1 Portion | bruehe 120, mehl 8, butter 8, zwiebel 10
Rahmsoße | Sahnesoße, Cream sauce | SD | 1.0 | 1 Portion | sahne 60, bruehe 60, mehl 6, butter 5
Pilzrahmsoße | Pilzsoße, Mushroom cream sauce | SD | 1.0 | 1 Portion | pilz 60, sahne 50, bruehe 40, butter 6, zwiebel 10
Jägersoße | Jägersauce, Hunter's sauce | SD | 1.0 | 1 Portion | pilz 50, speck 10, bruehe 80, tomatenmark 8, mehl 6, wein_rot 20
Senfsoße | Senfsauce, Mustard sauce | SD | 1.0 | 1 Portion | senf 25, sahne 40, bruehe 60, butter 5, mehl 5
Meerrettichsoße | Meerrettich-Sahne, Horseradish sauce | SD | 1.0 | 1 Portion | meerrettich 25, sahne 50, bruehe 40, mehl 5
Kräuterquark | Kräuterquark, Herb quark | SD | 1.0 | 1 Portion | quark 100, joghurt 30, petersilie 5, dill 3, zwiebel 5
Sauce Hollandaise | Hollandaise | SD | 1.0 | 1 Portion | butter 40, ei 25, zitrone 5
"""
