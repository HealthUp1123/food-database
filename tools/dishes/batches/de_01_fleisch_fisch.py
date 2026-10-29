CUISINE = 'de'
TEXT = """
Wiener Schnitzel | Schnitzel vom Kalb, Wiener Schnitzel veal, Kalbsschnitzel | HF | 0.85 | 1 Schnitzel | kalb 160, paniermehl 20, ei 20, mehl 10, schmalz 20
Schweineschnitzel Wiener Art | Schnitzel Wiener Art, Schweineschnitzel paniert, Pork schnitzel | HF | 0.85 | 1 Schnitzel | schwein_mager 160, paniermehl 20, ei 20, mehl 10, oel 20
Jägerschnitzel | Jaegerschnitzel, Schnitzel mit Pilzrahmsoße | HF | 0.85 | 1 Schnitzel | schwein_mager 150, paniermehl 15, ei 15, mehl 10, pilz 60, sahne 40, zwiebel 15, oel 20
Zigeunerschnitzel | Schnitzel mit Paprikasoße, Paprika schnitzel | HF | 0.85 | 1 Schnitzel | schwein_mager 150, paniermehl 15, ei 15, mehl 10, paprika 60, tomatenmark 10, zwiebel 20, oel 25
Rahmschnitzel | Schnitzel in Rahmsoße | HF | 0.85 | 1 Schnitzel | schwein_mager 160, sahne 50, mehl 8, zwiebel 15, butter 10, bruehe 40
Holsteiner Schnitzel | Schnitzel mit Spiegelei, Holstein schnitzel | HF | 0.85 | 1 Schnitzel | schwein_mager 150, paniermehl 15, ei 70, mehl 8, butter 15, oel 15
Cordon bleu | Cordon Bleu, Gefülltes Schnitzel | HF | 0.85 | 1 Stück | schwein_mager 150, schinken 30, emmentaler 30, paniermehl 20, ei 25, mehl 10, oel 25
Putenschnitzel paniert | Putenschnitzel, Turkey schnitzel | HG | 0.85 | 1 Schnitzel | pute 160, paniermehl 20, ei 20, mehl 10, oel 20
Hähnchenschnitzel paniert | Hühnerschnitzel, Chicken schnitzel | HG | 0.85 | 1 Schnitzel | hahn_brust 160, paniermehl 20, ei 20, mehl 10, oel 20
Pariser Schnitzel | Schnitzel Pariser Art | HF | 0.85 | 1 Schnitzel | schwein_mager 150, ei 40, mehl 20, oel 20, zitrone 5
Putenbrust in Rahmsoße | Putenbrust mit Sahnesauce | HG | 0.85 | 1 Portion | pute 160, sahne 50, zwiebel 20, butter 8, bruehe 40
Rinderrouladen | Rouladen, Rinderroulade, Beef roulade | FL | 0.7 | 1 Roulade | rind 170, speck 20, zwiebel 25, gewuerzgurke 20, senf 10, mehl 8, bruehe 100, oel 8
Sauerbraten | Rheinischer Sauerbraten, Marinated pot roast | FL | 0.65 | 1 Portion | rind 220, essig 30, zwiebel 40, rosinen 10, zucker 5, mehl 8, bruehe 100
Schweinebraten | Schweinebraten mit Soße, Roast pork | FL | 0.7 | 1 Portion | schwein_nacken 200, zwiebel 40, bruehe 100, schmalz 8, mehl 5
Krustenbraten | Schweinekrustenbraten, Crackling roast pork | FL | 0.7 | 1 Portion | schwein_bauch 150, schwein_nacken 100, zwiebel 40, bier 50, bruehe 80
Kassler Braten | Kasseler Braten, Smoked pork loin | FL | 0.8 | 1 Portion | kassler 220, zwiebel 20, bruehe 50
Kassler mit Sauerkraut | Kasseler mit Sauerkraut | FL | 0.9 | 1 Portion | kassler 150, sauerkraut 200, zwiebel 20, schmalz 5, wein_weiss 30
Rindergulasch | Gulasch, Beef goulash, Gulasch Rind | HF | 0.7 | 1 Portion | rind 200, zwiebel 100, paprika 40, tomatenmark 15, paprikapulver 3, oel 10, mehl 8, bruehe 150
Schweinegulasch | Gulasch Schwein | HF | 0.7 | 1 Portion | schwein_nacken 200, zwiebel 90, paprika 40, tomatenmark 15, paprikapulver 3, oel 10, bruehe 150
Szegediner Gulasch | Szegediner, Sauerkraut goulash | HF | 0.8 | 1 Portion | schwein_nacken 150, sauerkraut 200, zwiebel 50, paprikapulver 3, sahne 30, oel 10, bruehe 100
Pilzgulasch | Champignon Gulasch | HV | 0.8 | 1 Portion | pilz 250, zwiebel 60, paprika 40, tomatenmark 15, oel 12, sahne 30
Wildgulasch | Hirschgulasch, Venison goulash | HF | 0.7 | 1 Portion | wild 200, zwiebel 70, wein_rot 80, tomatenmark 12, mehl 8, oel 10, bruehe 100
Hackbraten | Falscher Hase, Meatloaf | HF | 0.85 | 1 Scheibe | gemischtes_hack 150, semmel 25, ei 25, zwiebel 20, senf 5, paniermehl 5
Frikadellen | Buletten, Fleischpflanzerl, Fleischküchle | KF | 0.8 | 2 Stück | gemischtes_hack 150, semmel 25, ei 20, zwiebel 20, senf 5, oel 12
Königsberger Klopse | Königsberger Klopse, Meatballs in caper sauce | KF | 0.9 | 1 Portion | gemischtes_hack 150, semmel 25, ei 25, zwiebel 20, butter 12, mehl 12, bruehe 120, sahne 30, zitrone 5
Hackepeter | Mett, Thüringer Mett, Raw minced pork | SN | 1.0 | 1 Brötchenhälfte | schwein_hack 100, zwiebel 15, salz 1, pfeffer 1
Mettbrötchen | Mettbroetchen, Mett roll | SN | 1.0 | 1 Brötchen | semmel 60, schwein_hack 100, zwiebel 15
Kalbshaxe | Gebratene Kalbshaxe | HF | 0.65 | 1 Portion | kalb 400, zwiebel 40, karotte 40, wein_weiss 60, bruehe 100
Schweinshaxe | Schweinshaxn, Haxe, Roasted pork knuckle | HF | 0.6 | 1 Portion | schwein_haxe 380, zwiebel 40, bier 100, bruehe 100
Eisbein | Eisbein mit Sauerkraut, Boiled pork knuckle | HF | 0.7 | 1 Portion | schwein_haxe 330, sauerkraut 150, zwiebel 20
Schäufele | Fränkisches Schäufele, Pork shoulder Franconian | HF | 0.65 | 1 Portion | schwein_nacken 300, zwiebel 40, bier 60
Leberkäse mit Spiegelei | Leberkäse Spiegelei, Meatloaf with fried egg | WU | 0.95 | 1 Portion | leberkaese 150, ei 60, butter 8
Leberkäse im Brötchen | Leberkässemmel, Leberkaesbroetchen | WU | 1.0 | 1 Brötchen | leberkaese 100, semmel 60, senf 10
Currywurst | Currywurst, Curry sausage | WU | 0.95 | 1 Portion | bratwurst 180, ketchup 40, paprikapulver 1, oel 5
Currywurst mit Pommes | Currywurst Pommes | WU | 0.9 | 1 Teller | bratwurst 180, ketchup 40, kartoffel 150, oel 12
Bratwurst | Grillwurst, Bratwurst gebraten | WU | 0.9 | 1 Wurst | bratwurst 150, oel 3
Bratwurst im Brötchen | Bratwurstsemmel, Bratwurst roll | WU | 0.95 | 1 Brötchen | bratwurst 120, semmel 60, senf 10
Bockwurst | Bockwurst mit Brötchen, Bockwurst with bun | WU | 1.0 | 1 Wurst | bockwurst 125, semmel 50, senf 10
Weißwurst | Münchner Weißwurst, Weisswurst, Bavarian white sausage | WU | 1.0 | 2 Würste | weisswurst 160, senf 20, semmel 50
Nürnberger Rostbratwürstchen | Nürnberger Bratwürste, Nuremberg sausages | WU | 0.92 | 6 Stück | bratwurst 180, senf 10, meerrettich 10
Thüringer Rostbratwurst | Thüringer Bratwurst, Thuringian sausage | WU | 0.92 | 1 Wurst | bratwurst 150, senf 10, semmel 50
Blutwurst gebraten | Blutwurst mit Zwiebeln, Fried blood sausage | WU | 0.95 | 1 Portion | blutwurst 150, zwiebel 30, schmalz 8
Leberwurst Brot | Leberwurstbrot, Liverwurst sandwich | SN | 1.0 | 2 Scheiben | roggenbrot 80, leberwurst 40, butter 10
Presssack | Presskopf, Schwartenmagen, Head cheese | WU | 1.0 | 1 Portion | leberwurst 100, gelatine 5
Sülze | Fleischsülze, Aspic | WU | 1.0 | 1 Portion | schwein_mager 80, gelatine 8, essig 10, gewuerzgurke 20, karotte 20
Saure Nierchen | Saure Nieren, Sour kidneys | HF | 0.8 | 1 Portion | innereien 200, zwiebel 40, mehl 10, essig 20, butter 10, bruehe 100
Kalbsleber Berliner Art | Leber Berliner Art, Berlin style liver | HF | 0.85 | 1 Portion | leber 180, apfel 80, zwiebel 50, mehl 10, butter 15
Leber mit Zwiebeln | Leber mit Äpfeln und Zwiebeln | HF | 0.85 | 1 Portion | leber 180, zwiebel 60, mehl 10, butter 12
Tafelspitz | Tafelspitz mit Meerrettich, Boiled beef Austrian | HF | 0.7 | 1 Portion | rind 220, karotte 50, sellerie 40, meerrettich 15, bruehe 100
Zwiebelrostbraten | Zwiebelrostbraten, Swabian onion roast | HF | 0.75 | 1 Portion | rind_steak 200, zwiebel 80, mehl 15, butter 12, bruehe 60
Rumpsteak mit Kräuterbutter | Rumpsteak, Steak herb butter | HF | 0.75 | 1 Steak | rind_steak 220, butter 20, petersilie 5, oel 5
Rinderschmorbraten | Schmorbraten, Pot roast | FL | 0.65 | 1 Portion | rind 220, zwiebel 40, karotte 40, sellerie 30, tomatenmark 10, wein_rot 60, bruehe 100
Wildschweinbraten | Wild boar roast | FL | 0.7 | 1 Portion | wildschwein 220, zwiebel 40, wein_rot 60, bruehe 100, preiselbeeren 15
Hirschbraten | Hirsch, Venison roast | FL | 0.7 | 1 Portion | wild 220, zwiebel 40, wein_rot 60, bruehe 100, speck 20
Rehrücken | Rehbraten, Roast saddle of venison | FL | 0.75 | 1 Portion | wild 200, butter 15, sahne 40, preiselbeeren 15
Hasenpfeffer | Hase im Topf, Jugged hare | FL | 0.7 | 1 Portion | kaninchen 220, speck 25, wein_rot 80, zwiebel 40, bruehe 100
Kaninchen in Senfsoße | Kaninchen in Senfsauce | FL | 0.75 | 1 Portion | kaninchen 220, senf 15, sahne 50, wein_weiss 40, zwiebel 20
Gänsebraten | Martinsgans, Roast goose, Weihnachtsgans | HG | 0.65 | 1 Portion | gans 300, apfel 40, zwiebel 30, bruehe 80
Entenbraten | Ente mit Rotkohl, Roast duck | HG | 0.65 | 1 Portion | ente 300, apfel 40, zwiebel 30, bruehe 80
Brathähnchen halb | Halbes Hähnchen, Roast chicken half, Hendl | HG | 0.7 | 1 halbes Hähnchen | hahn 450, butter 10, paprikapulver 2
Backhendl | Backhähnchen, Fried chicken Austrian | HG | 0.8 | 1 Portion | hahn_keule 250, mehl 20, ei 30, paniermehl 30, schmalz 25
Hühnerfrikassee | Frikassee, Chicken fricassee | HG | 0.95 | 1 Portion | hahn_brust 120, pilz 50, erbsen 30, sahne 50, butter 12, mehl 12, bruehe 120, zitrone 5
Kalbsfrikassee | Kalbsragout, Veal fricassee | HF | 0.95 | 1 Portion | kalb 120, pilz 50, erbsen 30, sahne 50, butter 12, mehl 12, bruehe 120
Hähnchenbrust in Currysoße | Hähnchen Curry mild | HG | 0.9 | 1 Portion | hahn_brust 150, sahne 50, zwiebel 20, oel 8, bruehe 100
Matjes Hausfrauenart | Matjesfilets Hausfrauen Art, Herring house style | HFi | 1.0 | 1 Portion | hering 120, apfel 40, zwiebel 20, joghurt 50, schmand 40, gewuerzgurke 20
Bismarckhering | Bismarck herring, Pickled herring | HFi | 1.0 | 1 Portion | hering 120, zwiebel 30, essig 10, senf 3
Rollmops | Rollmops, Rolled pickled herring | HFi | 1.0 | 1 Stück | hering 100, gewuerzgurke 15, zwiebel 15, essig 8
Backfisch | Gebackener Fisch, Fried fish German | HFi | 0.85 | 1 Portion | kabeljau 180, mehl 20, ei 20, paniermehl 20, oel 22
Fischstäbchen | Fischstaebchen, Fish fingers | HFi | 0.95 | 5 Stück | kabeljau 80, paniermehl 30, oel 10
Forelle Müllerin | Forelle nach Müllerin Art, Trout miller style | HFi | 0.8 | 1 Forelle | forelle 300, mehl 15, butter 20, zitrone 10, petersilie 5
Forelle blau | Blaue Forelle, Poached trout | HFi | 0.9 | 1 Forelle | forelle 300, essig 10, butter 15
Karpfen blau | Karpfen blau mit Meerrettich | HFi | 0.9 | 1 Portion | karpfen 300, essig 10, butter 15
Karpfen gebacken | Gebackener Karpfen, Fried carp | HFi | 0.85 | 1 Portion | karpfen 250, ei 20, paniermehl 25, oel 25
Zander gebraten | Zanderfilet gebraten, Pan fried pike-perch | HFi | 0.85 | 1 Portion | fisch_mager 200, mehl 10, butter 15, zitrone 10
Scholle Finkenwerder Art | Scholle mit Speck, Plaice with bacon | HFi | 0.85 | 1 Portion | fisch_mager 220, speck 30, butter 12, mehl 10
Rotbarsch gebraten | Rotbarschfilet | HFi | 0.85 | 1 Portion | fisch_mager 200, mehl 10, butter 15
Seelachsfilet paniert | Seelachs paniert | HFi | 0.85 | 1 Portion | seelachs 180, paniermehl 20, ei 20, mehl 8, oel 20
Lachs mit Dillsoße | Lachsfilet Dill, Salmon dill sauce | HFi | 0.85 | 1 Portion | lachs 180, sahne 50, dill 5, butter 8, zitrone 10
Labskaus | Labskaus, Hamburg corned beef hash | HF | 0.95 | 1 Portion | rind 100, kartoffel 150, rote_bete 50, zwiebel 30, gewuerzgurke 25, schmalz 10, ei 50
Bratheringe | Bratheringe, Fried pickled herring | HFi | 0.9 | 1 Portion | hering 150, mehl 15, essig 20, zwiebel 40, oel 20
Heringsstipp | Heringsstipp, Herring in cream | HFi | 1.0 | 1 Portion | hering 100, schmand 50, joghurt 40, apfel 40, zwiebel 20
Aal grün | Grüner Aal, Eel in herb sauce | HFi | 0.85 | 1 Portion | aal 200, butter 15, petersilie 10, sahne 40, mehl 8
Fischfrikadellen | Fischbuletten | KF | 0.85 | 2 Stück | fisch_mager 150, semmel 25, ei 20, zwiebel 20, oel 15
Strammer Max | Strammer Max, Open sandwich with ham and egg | FR | 0.95 | 1 Portion | roggenbrot 80, schinken 50, ei 60, butter 15
Bauernfrühstück | Bauernfruehstueck, Farmer's breakfast | PF | 0.9 | 1 Pfanne | kartoffel 200, ei 100, speck 40, zwiebel 30, oel 15
Rührei mit Speck | Ruehrei mit Speck, Scrambled eggs bacon | FR | 0.9 | 1 Portion | ei 150, speck 40, butter 10, milch 20
Kartoffelpuffer mit Apfelmus | Reibekuchen, Kartoffelpuffer, Potato pancakes | KN | 0.8 | 3 Stück | kartoffel 250, ei 30, mehl 15, zwiebel 20, oel 30, apfel 80, zucker 5
Himmel und Erde | Himmel un Ääd, Blood sausage with apples and potatoes | KN | 0.95 | 1 Portion | kartoffel 200, apfel 100, blutwurst 120, zwiebel 30, butter 12, milch 40
Grünkohl mit Pinkel | Grünkohl mit Pinkelwurst, Kale with sausage | E | 0.9 | 1 Portion | gruenkohl 250, mettwurst 80, schwein_bauch 60, zwiebel 30, schmalz 10, haferflocken 8, bruehe 100
Grünkohl mit Kassler | Grünkohl und Kassler | E | 0.9 | 1 Portion | gruenkohl 250, kassler 100, zwiebel 30, schmalz 10, haferflocken 8, bruehe 100
"""
