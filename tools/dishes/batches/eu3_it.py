CUISINE = 'it'
TEXT = """
Pasta alla norcina | Rigatoni alla norcina, Pasta mit Wurst-Sahne-Sauce | NA | 0.95 | 1 Teller | nudeln 90, wasser 120, schwein_hack 70, sahne 50, zwiebel 20, pecorino 10, olivenoel 8
Spaghetti alla carrettiera | Carrettiera | NA | 0.95 | 1 Teller | nudeln 90, wasser 120, tomate 120, olivenoel 15, knoblauch 5, chili 2, pecorino 12, petersilie 5
Pesto alla trapanese | Busiate al pesto trapanese, Trapani pesto pasta | NA | 0.95 | 1 Teller | nudeln 90, wasser 120, tomate 100, mandel 20, olivenoel 15, pecorino 10, knoblauch 4
Tagliatelle ai funghi porcini | Tagliatelle mit Steinpilzen | NA | 0.95 | 1 Teller | nudeln 90, wasser 120, pilz 150, olivenoel 12, butter 8, knoblauch 4, petersilie 5, parmesan 10
Fettuccine alla papalina | Fettuccine papalina | NA | 0.95 | 1 Teller | nudeln 90, wasser 120, schinken 40, erbsen 40, sahne 50, ei 20, parmesan 12, butter 8, zwiebel 15
Penne alla boscaiola | Pasta boscaiola | NA | 0.95 | 1 Teller | nudeln 90, wasser 120, pilz 80, schwein_hack 50, erbsen 30, sahne 40, tomaten_dose 40, olivenoel 8
Pasta e piselli | Pasta mit Erbsen | NA | 0.95 | 1 Teller | nudeln 80, wasser 180, erbsen 100, speck 20, zwiebel 30, olivenoel 10, parmesan 10
Pasta e broccoli | Pasta mit Brokkoli | NA | 0.95 | 1 Teller | nudeln 90, wasser 140, brokkoli 150, olivenoel 15, knoblauch 4, chili 2, pecorino 10
Pasta alla zozzona | Rigatoni alla zozzona | NA | 0.95 | 1 Teller | nudeln 90, wasser 120, schwein_hack 50, speck 30, tomaten_dose 100, ei 30, pecorino 15
Spaghetti alle cozze | Spaghetti mit Miesmuscheln | NA | 0.9 | 1 Teller | nudeln 90, wasser 120, muschel 250, tomate 80, olivenoel 15, knoblauch 4, petersilie 5
Linguine all'astice | Linguine mit Hummer, Lobster linguine | NA | 0.9 | 1 Teller | nudeln 90, wasser 120, hummer 150, tomate 120, olivenoel 15, knoblauch 4, wein_weiss 30
Lasagne alla napoletana | Neapolitan lasagna | AU | 0.95 | 1 Stück | nudeln 70, wasser 50, hack 80, ricotta 80, mozzarella 50, tomaten_dose 150, ei 20, parmesan 15, olivenoel 10
Vincisgrassi | Vincisgrassi marchigiani | AU | 0.95 | 1 Stück | nudeln 70, wasser 50, hack 60, huhn_leber 30, milch 120, butter 20, mehl 15, tomaten_dose 60, parmesan 15
Timballo alla teramana | Timballo teramano | AU | 0.95 | 1 Stück | mehl 50, ei 50, milch 60, hack 60, mozzarella 50, tomaten_dose 100, parmesan 15, olivenoel 8
Crespelle alla fiorentina | Crespelle ricotta e spinaci | AU | 0.95 | 2 Stück | mehl 40, ei 40, milch 80, ricotta 80, spinat 100, butter 15, parmesan 15, milch_fettarm 60
Cannelloni di carne | Cannelloni mit Fleisch | AU | 0.95 | 1 Portion | nudeln 70, wasser 50, hack 100, tomaten_dose 120, milch 100, butter 15, mehl 12, parmesan 15, zwiebel 20
Tortellini alla panna | Tortellini panna e prosciutto | NA | 0.95 | 1 Teller | mehl 80, ei 30, schwein_hack 30, schinken 30, sahne 80, parmesan 15, wasser 40
Cappelletti in brodo | Cappelletti romagnoli | S | 0.95 | 1 Teller | mehl 60, ei 25, ricotta 30, parmesan 15, hahn_brust 20, bruehe 350
Anolini in brodo | Anolini parmigiani | S | 0.95 | 1 Teller | mehl 60, ei 25, rind 30, paniermehl 10, parmesan 15, bruehe 350
Pansoti con salsa di noci | Pansotti alla genovese | MA | 0.95 | 1 Teller | mehl 80, ei 25, ricotta 60, mangold 60, walnuss 30, sahne 30, parmesan 10, olivenoel 8, wasser 40
Tortelli di zucca | Tortelli di zucca mantovani, Kürbistortelli | MA | 0.95 | 1 Teller | mehl 80, ei 25, kuerbis 120, keks 15, parmesan 15, butter 20, wasser 40
Gnocchi al pesto | Gnocchi mit Pesto | KN | 0.95 | 1 Teller | kartoffel 250, mehl 70, ei 15, olivenoel 20, pinienkerne 10, parmesan 15, knoblauch 3, petersilie 10
Gnudi toscani | Gnudi ricotta e spinaci | KN | 0.95 | 1 Portion | ricotta 150, spinat 150, mehl 30, ei 25, parmesan 20, butter 20
Risotto alla zucca | Kürbisrisotto, Pumpkin risotto | RP | 0.95 | 1 Teller | reis 90, bruehe 280, kuerbis 150, zwiebel 30, butter 15, parmesan 15, wein_weiss 20
Risotto alla salsiccia | Risotto con salsiccia | RP | 0.95 | 1 Teller | reis 90, bruehe 280, bratwurst 80, zwiebel 30, butter 10, parmesan 15, wein_weiss 20
Risotto al Barolo | Rotweinrisotto | RP | 0.95 | 1 Teller | reis 90, bruehe 220, wein_rot 80, zwiebel 30, butter 15, parmesan 15
Riso alla pilota | Risotto alla pilota | RP | 0.95 | 1 Teller | reis 90, wasser 180, schwein_hack 70, butter 15, parmesan 15
Minestra maritata | Neapolitan wedding soup | S | 0.95 | 1 Teller | weisskohl 120, mangold 80, schwein_nacken 60, wuerstchen_geraeuchert 30, bruehe 300, parmesan 8
Ciuppin | Zuppa di pesce ligure, Ligurische Fischsuppe | S | 0.95 | 1 Teller | fisch_mager 180, tomate 120, zwiebel 30, olivenoel 15, wein_weiss 30, weissbrot 40, bruehe 200
Vellutata di zucca | Kürbiscremesuppe italienisch | S | 0.95 | 1 Teller | kuerbis 250, kartoffel 60, zwiebel 30, olivenoel 10, bruehe 150, parmesan 8
Pancotto | Pancotto pugliese | S | 0.95 | 1 Teller | weissbrot 70, kartoffel 80, mangold 80, olivenoel 15, knoblauch 4, wasser 250
Polenta taragna | Polenta taragna valtellinese | KN | 0.9 | 1 Teller | maismehl 50, x4_buchweizen 30, wasser 350, butter 20, emmentaler 60
Pollo alla romana | Pollo con peperoni alla romana | HG | 0.85 | 1 Portion | hahn 250, paprika_rot 150, tomaten_dose 100, olivenoel 15, wein_weiss 30, zwiebel 30
Carne alla pizzaiola | Bistecca alla pizzaiola | HF | 0.85 | 1 Portion | rind_steak 180, tomaten_dose 150, olivenoel 12, knoblauch 4, oregano 1, olive 10
Braciole napoletane | Involtini al ragù, Braciole al sugo | HF | 0.8 | 1 Portion | rind 180, pecorino 15, pinienkerne 8, rosinen 8, tomaten_dose 200, olivenoel 12, wein_rot 30
Peposo dell'Impruneta | Peposo | HF | 0.75 | 1 Portion | rind 250, wein_rot 150, knoblauch 6, pfeffer 3, tomatenmark 10
Stinco di maiale al forno | Stinco di maiale | FL | 0.75 | 1 Portion | schwein_haxe 350, wein_weiss 50, olivenoel 10, kartoffel 150, zwiebel 30
Cotoletta alla bolognese | Cotoletta petroniana | HF | 0.9 | 1 Portion | kalb 150, ei 25, paniermehl 30, butter 20, rohschinken 20, parmesan 20, bruehe 40
Fegato alla veneziana | Liver Venetian style, Leber venezianisch | HF | 0.8 | 1 Portion | leber 180, zwiebel 200, butter 15, olivenoel 10, wein_weiss 20, petersilie 5
Arrosto di vitello | Kalbsbraten italienisch | FL | 0.75 | 1 Portion | kalb 220, wein_weiss 50, butter 10, olivenoel 10, karotte 30, zwiebel 30
Agnello cacio e ova | Agnello cacio e uova | HF | 0.8 | 1 Portion | lamm 220, ei 50, pecorino 20, olivenoel 12, wein_weiss 30, zitrone 10
Arrosticini | Arrosticini abruzzesi, Lammspießchen | KB | 0.75 | 10 Spieße | lamm 200, olivenoel 8, salz 2
Bombette pugliesi | Bombette | FL | 0.8 | 4 Stück | schwein_nacken 180, emmentaler 40, speck 20, petersilie 5
Salsiccia e fagioli | Salsicce e fagioli | WU | 0.9 | 1 Portion | bratwurst 150, bohnen_trocken 60, wasser 150, tomaten_dose 100, olivenoel 10, knoblauch 4
Orata al forno | Orata al cartoccio | HFi | 0.8 | 1 Portion | wolfsbarsch 300, kartoffel 150, olivenoel 15, zitrone 15, tomate 60, petersilie 5
Branzino al sale | Wolfsbarsch in Salzkruste | HFi | 0.75 | 1 Portion | wolfsbarsch 350, olivenoel 10, zitrone 10, salz 3
Baccalà alla livornese | Stockfisch Livorneser Art | HFi | 0.85 | 1 Portion | stockfisch 200, tomaten_dose 150, mehl 15, olivenoel 20, knoblauch 4, petersilie 5
Seppie con piselli | Tintenfisch mit Erbsen | HFi | 0.85 | 1 Portion | kalmar 220, erbsen 120, tomaten_dose 80, olivenoel 15, zwiebel 30, wein_weiss 30
Polpo alla luciana | Polipo alla luciana | HFi | 0.8 | 1 Portion | oktopus 300, tomaten_dose 120, olive 15, olivenoel 15, knoblauch 4, petersilie 5
Alici marinate | Marinierte Sardellen | V | 0.95 | 1 Portion | sardelle 120, zitrone 40, olivenoel 15, knoblauch 3, petersilie 5
Cozze gratinate | Gratinierte Miesmuscheln | V | 0.9 | 1 Portion | muschel 250, paniermehl 25, parmesan 10, olivenoel 15, petersilie 5, knoblauch 3
Calamari ripieni | Calamari imbottiti | HFi | 0.85 | 1 Portion | kalmar 220, paniermehl 30, ei 20, parmesan 10, tomaten_dose 120, olivenoel 15, petersilie 5
Triglie alla livornese | Rotbarben livornese | HFi | 0.85 | 1 Portion | fisch_mager 220, tomaten_dose 150, olivenoel 15, knoblauch 4, petersilie 5
Parmigiana di zucchine | Zucchini-Parmigiana | AU | 0.9 | 1 Portion | zucchini 250, tomaten_dose 150, mozzarella 70, parmesan 20, mehl 15, oel 20
Zucchine alla scapece | Scapece, Zucchine marinate | V | 0.85 | 1 Portion | zucchini 200, oel 20, essig 15, minze 5, knoblauch 3
Melanzane a funghetto | Melanzane trifolate | GZ | 0.8 | 1 Portion | aubergine 250, tomate 80, olivenoel 25, knoblauch 4, petersilie 5
Peperoni ripieni | Peperoni ripieni al forno, Gefüllte Paprika italienisch | GM | 0.85 | 2 Stück | paprika_rot 250, hack 80, paniermehl 25, parmesan 15, ei 20, olive 10, olivenoel 12
Fave e cicoria | Fave e cicorie, Ackerbohnenpüree mit Zichorie | HH | 0.95 | 1 Portion | dicke_bohnen 80, wasser 180, xc_chicoree 150, olivenoel 20, knoblauch 3
Cianfotta | Ciambotta, Italienischer Gemüseeintopf | GZ | 0.85 | 1 Portion | aubergine 100, zucchini 100, paprika 80, kartoffel 100, tomate 100, olivenoel 20, zwiebel 30
Puntarelle alla romana | Puntarelle con le alici | SA | 1.0 | 1 Portion | xc_chicoree 150, sardelle 10, olivenoel 15, essig 8, knoblauch 3
Patate al forno con rosmarino | Italienische Ofenkartoffeln | B | 0.75 | 1 Portion | kartoffel 300, olivenoel 20, knoblauch 4, salz 2
Funghi trifolati | Champignons trifolati | B | 0.75 | 1 Portion | pilz 250, olivenoel 15, knoblauch 4, petersilie 8
Zucchine ripiene | Gefüllte Zucchini italienisch | GM | 0.85 | 2 Hälften | zucchini 250, hack 70, paniermehl 20, parmesan 15, ei 20, tomaten_dose 80, olivenoel 10
Pomodori ripieni di riso | Pomodori col riso, Reisgefüllte Tomaten | GZ | 0.85 | 2 Stück | tomate 300, reis 50, kartoffel 100, olivenoel 20, petersilie 5, knoblauch 3
Bagna càuda | Bagna cauda | SD | 0.9 | 1 Portion | olivenoel 40, sardelle 25, knoblauch 20, butter 10, paprika_rot 80, karotte 60, xc_fenchel 60
Insalata di finocchi | Fenchelsalat | SA | 1.0 | 1 Portion | xc_fenchel 150, olivenoel 12, zitrone 10, parmesan 10
Finocchi gratinati | Fenchel überbacken | AU | 0.85 | 1 Portion | xc_fenchel 250, milch 80, butter 10, mehl 8, parmesan 20
Pizza fritta | Pizza fritta napoletana | PZ | 0.95 | 1 Stück | x3_pizzateig 180, ricotta 60, schinken 30, tomaten_dose 40, oel 25
Panzerotti | Panzerotti pugliesi | SN | 0.95 | 2 Stück | x3_pizzateig 160, mozzarella 60, tomaten_dose 40, oel 25
Crocchè di patate | Panzarotti di patate, Kartoffelkroketten neapolitanisch | SN | 0.9 | 3 Stück | kartoffel 200, ei 30, parmesan 15, mozzarella 30, paniermehl 25, oel 25
Frittatina di pasta | Frittatine napoletane | SN | 0.9 | 1 Stück | nudeln 40, wasser 50, milch 50, butter 10, mehl 10, schinken 20, erbsen 15, paniermehl 15, ei 15, oel 20
Olive ascolane | Olive all'ascolana | SN | 0.9 | 8 Stück | olive 60, hack 50, parmesan 10, ei 25, paniermehl 25, mehl 10, oel 25
Sfincione | Sfincione palermitano | PZ | 0.9 | 1 Stück | x3_pizzateig 180, tomaten_dose 80, zwiebel 50, sardelle 10, pecorino 15, paniermehl 10, olivenoel 15
Focaccia di Recco | Focaccia col formaggio | PZ | 0.9 | 1 Stück | mehl 70, wasser 40, olivenoel 15, frischkaese 80
Erbazzone | Erbazzone reggiano | PZ | 0.9 | 1 Stück | mehl 60, schmalz 10, mangold 150, spinat 50, parmesan 25, ei 20, speck 15, zwiebel 20
Torta al testo | Crescia al testo, Torta al testo con salumi | BR | 0.9 | 1 Stück | mehl 100, wasser 55, olivenoel 8, rohschinken 40, gouda 30
Tramezzino tonno e uova | Tramezzino | SN | 1.0 | 2 Stück | weissbrot 80, thunfisch 40, ei 30, mayonnaise 20, salat 10
Pizza ai funghi | Pizza Funghi | PZ | 0.9 | 1 Pizza | x3_pizzateig 250, tomaten_dose 80, mozzarella 100, pilz 80, olivenoel 10
Pizza tonno e cipolla | Pizza Tonno | PZ | 0.9 | 1 Pizza | x3_pizzateig 250, tomaten_dose 80, mozzarella 90, thunfisch 70, zwiebel 40, olivenoel 10
Pizza Romana | Pizza Napoli, Pizza mit Sardellen | PZ | 0.9 | 1 Pizza | x3_pizzateig 250, tomaten_dose 80, mozzarella 100, sardelle 20, olive 10, oregano 1, olivenoel 10
Pizza Salsiccia e friarielli | Pizza mit Salsiccia | PZ | 0.9 | 1 Pizza | x3_pizzateig 250, mozzarella 80, bratwurst 60, brokkoli 80, olivenoel 10
Pizza Ortolana | Pizza Vegetariana, Gemüsepizza | PZ | 0.9 | 1 Pizza | x3_pizzateig 250, tomaten_dose 80, mozzarella 90, zucchini 50, aubergine 50, paprika_rot 50, olivenoel 12
Crostata di ricotta | Crostata ricotta e cioccolato | K | 0.95 | 1 Stück | mehl 45, butter 20, zucker 25, ei 20, ricotta 70, schokolade 8
Bomboloni | Bombolone alla crema | G | 0.95 | 1 Stück | mehl 50, milch 20, ei 10, butter 8, zucker 15, hefe 2, oel 12, milch_fettarm 40, vanillepudding_pulver 5
Maritozzi con la panna | Maritozzo | G | 0.95 | 1 Stück | mehl 50, milch 20, ei 10, butter 8, zucker 12, hefe 2, sahne 50
Cartellate | Cartellate pugliesi | G | 0.9 | 3 Stück | mehl 50, olivenoel 15, wein_weiss 15, oel 15, honig 25
Baci di dama | Baci di dama piemontesi | G | 0.95 | 4 Stück | haselnuss 20, mehl 20, butter 20, zucker 20, schokolade 8
Brutti ma buoni | Nussbaiser italienisch | G | 0.95 | 4 Stück | haselnuss 30, eiweiss 25, zucker 30
Ricciarelli | Ricciarelli di Siena | G | 0.95 | 3 Stück | mandel 40, zucker 35, eiweiss 15
Chiacchiere | Crostoli, Bugie | G | 0.9 | 1 Portion | mehl 50, ei 15, zucker 8, butter 5, wein_weiss 8, oel 15, zucker 10
Castagnole | Castagnole romagnole | G | 0.9 | 6 Stück | mehl 50, ei 20, zucker 15, butter 8, oel 15, zucker 8
Torta tenerina | Torta tenerina ferrarese | K | 0.95 | 1 Stück | schokolade 35, butter 25, zucker 25, ei 35, mehl 10
Torta paradiso | Torta Paradiso | K | 0.95 | 1 Stück | mehl 15, staerke 15, butter 25, zucker 25, ei 30
Gelato al pistacchio | Pistazieneis | D | 1.0 | 2 Kugeln | eis 100, pistazie 15
Granita al caffè con panna | Granita di caffè | D | 1.0 | 1 Glas | kaffee 150, zucker 25, sahne 40
Biancomangiare | Biancomangiare siciliano | PU | 1.0 | 1 Portion | milch 150, mandel 20, zucker 20, staerke 15
Budino al cioccolato | Italienischer Schokoladenpudding | PU | 1.0 | 1 Portion | milch 150, kakao 10, zucker 20, staerke 12, schokolade 10
Delizia al limone | Delizie al limone | D | 0.95 | 1 Stück | mehl 25, ei 30, zucker 30, sahne 50, milch 50, zitrone 20, staerke 8
Limoncello | Limoncello di Sorrento | GT | 1.0 | 1 Glas (40 ml) | spirituose 25, zucker 12, wasser 5
Negroni | Cocktail Negroni | GT | 1.0 | 1 Glas | spirituose 30, likoer 30, likoerwein 30
Bellini | Bellini veneziano | GT | 1.0 | 1 Glas | pfirsich 50, wein_weiss 100
Caffè corretto | Espresso corretto | GT | 1.0 | 1 Tasse | kaffee 30, spirituose 15, zucker 5
Caffè shakerato | Shakerato | GT | 1.0 | 1 Glas | kaffee 60, zucker 10
"""
