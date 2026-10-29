CUISINE = 'fr'
TEXT = """
Bœuf à la mode | Boeuf a la mode, Französischer Schmorbraten | FL | 0.75 | 1 Portion | rind 250, wein_rot 100, karotte 100, zwiebel 40, speck 20, butter 10, bruehe 100
Tournedos Rossini | Rinderfilet Rossini | HF | 0.85 | 1 Portion | rind_steak 180, foie_gras 40, weissbrot 30, butter 15, likoerwein 30
Steak au poivre | Pfeffersteak, Pepper steak | HF | 0.85 | 1 Portion | rind_steak 200, pfeffer 4, butter 15, sahne 50, weinbrand 15
Entrecôte bordelaise | Entrecote à la bordelaise | HF | 0.85 | 1 Portion | rind_steak 220, wein_rot 60, butter 20, zwiebel 20, bruehe 40
Côte de porc charcutière | Schweinekotelett Charcutière | HF | 0.85 | 1 Portion | schwein_nacken 200, zwiebel 40, gewuerzgurke 30, senf 10, wein_weiss 40, butter 10
Filet mignon de porc à la moutarde | Schweinefilet in Senfsauce | HF | 0.85 | 1 Portion | schwein_mager 200, senf 15, creme_fraiche 50, wein_weiss 30, butter 10
Veau Marengo | Kalb Marengo | HF | 0.8 | 1 Portion | kalb 220, tomaten_dose 120, pilz 60, zwiebel 30, wein_weiss 50, olivenoel 12
Poulet à la crème | Poulet de Bresse à la crème | HG | 0.85 | 1 Portion | hahn 250, sahne 80, pilz 60, wein_weiss 40, butter 10, zwiebel 20
Poulet Vallée d'Auge | Hähnchen mit Cidre und Calvados | HG | 0.85 | 1 Portion | hahn 250, apfelwein 80, creme_fraiche 50, pilz 60, apfel 60, butter 10
Poulet au vinaigre | Poulet au vinaigre lyonnais | HG | 0.85 | 1 Portion | hahn 250, essig 30, tomate 80, wein_weiss 40, butter 15, creme_fraiche 20
Coq au Riesling | Coq au riesling alsacien | HG | 0.85 | 1 Portion | hahn 250, wein_weiss 120, pilz 80, sahne 50, zwiebel 30, butter 10
Fricassée de poulet | Poulet en fricassée, Hühnerfrikassee französisch | HG | 0.85 | 1 Portion | hahn_keule 220, pilz 60, zwiebel 30, sahne 60, mehl 10, butter 10, bruehe 100
Lapin chasseur | Kaninchen Jägerart | HF | 0.8 | 1 Portion | kaninchen 250, pilz 80, tomaten_dose 60, wein_weiss 60, zwiebel 30, olivenoel 12
Potée lorraine | Lothringer Eintopf | E | 0.9 | 1 Teller | kassler 120, speck 30, weisskohl 150, kartoffel 150, karotte 60, ruebe 50, bruehe 150
Saucisson brioché | Saucisson en brioche lyonnais | WU | 0.95 | 1 Stück | mehl 60, butter 20, ei 20, hefe 2, wuerstchen_geraeuchert 80
Pâté lorrain | Tourte lorraine | PZ | 0.9 | 1 Stück | blaetterteig 120, schwein_nacken 80, kalb 40, wein_weiss 20, zwiebel 20, ei 10
Fleischnacka | Fleischschnecken elsässisch | MA | 0.9 | 1 Portion | mehl 80, ei 30, rind 100, zwiebel 30, petersilie 5, bruehe 100, butter 10
Lotte à l'armoricaine | Seeteufel armoricaine | HFi | 0.85 | 1 Portion | fisch_mager 220, tomaten_dose 100, weinbrand 15, wein_weiss 50, butter 15, zwiebel 20, sahne 30
Saumon en papillote | Lachs in Pergament | HFi | 0.9 | 1 Portion | lachs 180, lauch 60, karotte 50, butter 10, zitrone 10, wein_weiss 20
Bourride | Bourride sétoise | S | 0.9 | 1 Teller | fisch_mager 200, kartoffel 120, lauch 50, mayonnaise 30, knoblauch 4, weissbrot 30, bruehe 200, olivenoel 8
Raie au beurre noir | Rochen in brauner Butter | HFi | 0.85 | 1 Portion | fisch_mager 250, butter 30, essig 10, olive 10, petersilie 5
Maquereaux au vin blanc | Makrelen in Weißwein | HFi | 0.9 | 1 Portion | makrele 180, wein_weiss 60, zwiebel 30, karotte 30, essig 10
Homard thermidor | Lobster thermidor | HFi | 0.9 | 1 Portion | hummer 250, sahne 60, butter 15, senf 5, emmentaler 25, wein_weiss 30, mehl 8
Calamars à la provençale | Tintenfisch provenzalisch | HFi | 0.85 | 1 Portion | kalmar 250, tomate 150, olivenoel 15, knoblauch 5, wein_weiss 30, petersilie 5
Tielle sétoise | Tielle | PZ | 0.9 | 1 Stück | mehl 70, olivenoel 15, hefe 2, wasser 30, oktopus 80, tomaten_dose 60, zwiebel 20
Gratin savoyard | Savoyer Kartoffelgratin | AU | 0.85 | 1 Portion | kartoffel 250, bruehe 100, emmentaler 50, butter 15
Pommes Anna | Pommes de terre Anna | B | 0.8 | 1 Portion | kartoffel 250, butter 35
Pommes boulangère | Bäckerinnen-Kartoffeln | B | 0.85 | 1 Portion | kartoffel 250, zwiebel 60, bruehe 120, butter 15
Flageolets | Flageolets à la crème | HH | 0.95 | 1 Portion | bohnen_trocken 70, wasser 160, butter 10, zwiebel 20, creme_fraiche 20
Lentilles du Puy en salade | Salade de lentilles, Linsensalat französisch | SA | 0.95 | 1 Portion | linsen 70, wasser 150, zwiebel 20, senf 5, essig 10, olivenoel 15, petersilie 5
Petits pois à la française | Erbsen französisch | B | 0.9 | 1 Portion | erbsen 200, salat 60, zwiebel 30, butter 20, speck 15
Carottes Vichy | Vichy-Karotten | B | 0.85 | 1 Portion | karotte 250, butter 15, zucker 5, petersilie 5
Champignons à la grecque | Pilze auf griechische Art | V | 0.85 | 1 Portion | pilz 200, tomate 50, olivenoel 20, zitrone 15, wein_weiss 30, zwiebel 20
Endives braisées | Geschmorter Chicorée | B | 0.8 | 1 Portion | xc_chicoree 300, butter 20, zucker 5, zitrone 10
Gratin de chou-fleur | Blumenkohlgratin französisch | AU | 0.9 | 1 Portion | blumenkohl 250, milch 120, mehl 12, butter 12, emmentaler 40
Petits farcis niçois | Farcis niçois | GM | 0.85 | 1 Portion | tomate 120, zucchini 120, zwiebel 60, schwein_hack 70, kalb 30, paniermehl 20, parmesan 15, olivenoel 15
Tomates farcies | Gefüllte Tomaten französisch | GM | 0.85 | 2 Stück | tomate 300, schwein_hack 100, paniermehl 15, ei 15, zwiebel 20, olivenoel 10, reis 20
Tarte à la tomate | Tomatentarte | PZ | 0.9 | 1 Stück | mehl 50, butter 25, senf 10, tomate 120, emmentaler 20, olivenoel 8
Tourte aux blettes | Tourte de blettes niçoise | K | 0.9 | 1 Stück | mehl 50, butter 20, zucker 25, mangold 70, rosinen 15, pinienkerne 8, parmesan 8, ei 15, apfel 30
Quiche au saumon | Lachsquiche | PZ | 0.9 | 1 Stück | mehl 45, butter 22, lachs 50, ei 40, sahne 50, milch 30, spinat 30
Salade piémontaise | Kartoffelsalat französisch | SA | 1.0 | 1 Portion | kartoffel 150, schinken 40, ei 30, tomate 50, gewuerzgurke 20, mayonnaise 30
Omelette jambon fromage | Omelette au jambon et fromage, Schinken-Käse-Omelett | EI | 0.9 | 1 Portion | ei 150, schinken 40, emmentaler 30, butter 10
Pipérade | Piperade basquaise | EI | 0.85 | 1 Portion | paprika 150, paprika_rot 80, tomate 120, zwiebel 50, ei 100, olivenoel 15, rohschinken 20
Potage cultivateur | Gemüsesuppe Bauernart | S | 0.95 | 1 Teller | karotte 60, lauch 50, kartoffel 60, ruebe 40, weisskohl 40, speck 15, butter 8, bruehe 250
Velouté de champignons | Champignoncremesuppe französisch | S | 0.95 | 1 Teller | pilz 180, zwiebel 30, butter 10, sahne 50, bruehe 200
Bisque de homard | Hummersuppe, Lobster bisque | S | 0.95 | 1 Teller | hummer 80, tomatenmark 15, sahne 60, butter 10, weinbrand 10, reis 10, bruehe 220
Soupe au chou | Kohlsuppe französisch | S | 0.95 | 1 Teller | weisskohl 150, kartoffel 80, speck 30, karotte 40, zwiebel 30, bruehe 250
Crème Du Barry | Blumenkohlcremesuppe | S | 0.95 | 1 Teller | blumenkohl 200, kartoffel 50, sahne 50, butter 10, bruehe 200
Velouté d'asperges | Spargelcremesuppe französisch | S | 0.95 | 1 Teller | spargel 180, kartoffel 40, sahne 50, butter 10, bruehe 220
Friand à la viande | Friand | SN | 0.9 | 1 Stück | blaetterteig 80, schwein_hack 60, zwiebel 10, ei 10, petersilie 3
Chausson aux pommes | Apfeltasche französisch | G | 0.95 | 1 Stück | blaetterteig 80, apfel 70, zucker 10, butter 5, ei 5
Pain aux raisins | Rosinenschnecke französisch | G | 0.95 | 1 Stück | mehl 45, butter 20, zucker 10, milch 30, ei 10, rosinen 15, hefe 2
Croissant aux amandes | Mandelcroissant | G | 0.95 | 1 Stück | mehl 40, butter 25, mandel 25, zucker 20, ei 10, milch 10
Pain au lait | Milchbrötchen französisch | BR | 0.9 | 2 Stück | mehl 70, milch 35, butter 10, zucker 8, ei 10, hefe 2
Fougasse | Fougasse provençale | BR | 0.9 | 1 Stück | mehl 100, wasser 60, olivenoel 10, olive 15, hefe 2
Tarte Bourdaloue | Tarte aux poires Bourdaloue, Birnen-Mandel-Tarte | K | 0.95 | 1 Stück | mehl 35, butter 25, zucker 25, mandel 20, ei 15, birne 60
Tarte aux abricots | Aprikosentarte | K | 0.95 | 1 Stück | mehl 45, butter 22, zucker 20, aprikose 100, ei 8
Tarte au chocolat | Schokoladentarte | K | 0.95 | 1 Stück | mehl 35, butter 25, zucker 15, schokolade 35, sahne 35, ei 10
Tarte aux myrtilles | Heidelbeertarte | K | 0.95 | 1 Stück | mehl 45, butter 22, zucker 20, blaubeere 100, ei 8
Tarte normande | Normannische Apfeltarte | K | 0.95 | 1 Stück | mehl 40, butter 20, zucker 20, apfel 90, ei 20, creme_fraiche 30
Gâteau au yaourt | Joghurtkuchen französisch | K | 0.95 | 1 Stück | joghurt 30, mehl 40, zucker 30, ei 25, oel 15
Quatre-quarts | Quatre quarts breton | K | 0.95 | 1 Stück | butter 20, zucker 20, mehl 20, ei 20
Charlotte aux fraises | Erdbeer-Charlotte | D | 1.0 | 1 Stück | x2_biskuit 30, erdbeere 80, sahne 50, zucker 15, gelatine 2, joghurt 30
Mont-Blanc | Mont-Blanc aux marrons, Kastanien-Mont-Blanc | D | 1.0 | 1 Stück | kastanie 80, zucker 25, sahne 50, eiweiss 15
Savarin | Savarin au rhum | K | 0.95 | 1 Stück | mehl 40, butter 12, ei 20, zucker 30, hefe 2, weinbrand 10, wasser 30, sahne 30
Kouglof | Kougelhopf, Gugelhupf elsässisch | K | 0.95 | 1 Stück | mehl 50, butter 18, zucker 12, ei 15, milch 20, rosinen 12, mandel 5, hefe 2
Tarte au sucre | Zuckertarte nordfranzösisch | K | 0.95 | 1 Stück | mehl 50, butter 15, zucker 25, ei 15, milch 15, sahne 15, hefe 2
Poires Belle-Hélène | Birne Helene | D | 1.0 | 1 Portion | birne 150, zucker 20, eis 80, schokolade 25, sahne 20
Pêche Melba | Pfirsich Melba | D | 1.0 | 1 Portion | pfirsich 150, eis 80, himbeere 50, zucker 15, sahne 20
Croquembouche | Croque-en-bouche | D | 0.95 | 1 Portion | mehl 25, butter 20, ei 40, wasser 40, milch 60, zucker 35, vanillepudding_pulver 8
Tarte tropézienne | Tropézienne | K | 0.95 | 1 Stück | mehl 50, butter 18, zucker 22, ei 20, milch 50, sahne 30, hefe 2, staerke 5
Flan pâtissier | Flan parisien | K | 0.95 | 1 Stück | mehl 30, butter 12, milch 120, ei 25, zucker 25, staerke 12
Choux à la crème | Windbeutel französisch | G | 0.95 | 2 Stück | mehl 25, butter 20, ei 40, wasser 40, milch 60, zucker 20, staerke 8
Pommes au four | Bratapfel französisch | D | 0.85 | 1 Stück | apfel 200, butter 10, zucker 15, rosinen 10
Œufs à la neige au caramel | Oeufs a la neige | D | 1.0 | 1 Portion | eiweiss 40, zucker 35, milch 150, ei 30
Pastis | Pastis de Marseille, Anisschnaps mit Wasser | GT | 1.0 | 1 Glas | spirituose 30, zucker 2, wasser 150
Diabolo menthe | Minzlimonade | GT | 1.0 | 1 Glas | x2_limonade 250, zucker 15
Citron pressé | Frisch gepresste Zitronenlimonade | GT | 1.0 | 1 Glas | zitrone 40, zucker 15, wasser 200
Calvados | Calvados du Pays d'Auge | GT | 1.0 | 1 Glas (4 cl) | spirituose 40
Café crème | Cafe creme | GT | 1.0 | 1 Tasse | kaffee 150, milch 50
Kir royal | Kir Royal | GT | 1.0 | 1 Glas | wein_weiss 100, likoer 15
"""
