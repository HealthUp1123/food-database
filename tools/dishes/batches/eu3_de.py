CUISINE = 'de'
TEXT = """
Weißwürste mit Brezel und süßem Senf | Weisswurst mit Brezn, Weißwurst-Brotzeit | WU | 1.0 | 2 Würste + 1 Brezel | weisswurst 160, semmel 80, senf 25, zucker 3
Schweinebraten mit Kartoffelknödel und Krautsalat | Schweinsbraten bayerisch mit Krautsalat | FL | 0.8 | 1 Teller | schwein_nacken 220, kartoffel 200, staerke 10, weisskohl 120, essig 10, oel 8, speck 10, zwiebel 30, bruehe 100
Ochsenbackerl in Rotweinsoße | Ochsenbacken geschmort, Rinderbäckchen | FL | 0.75 | 1 Portion | rind_fett 220, wein_rot 80, zwiebel 40, karotte 40, sellerie 30, tomatenmark 15, oel 10, bruehe 150
Kalbsrahmgulasch | Kalbsgulasch mit Rahm | HF | 0.8 | 1 Portion | kalb 200, zwiebel 60, sahne 50, paprikapulver 3, mehl 8, butter 10, bruehe 120
Böfflamott | Boeuf à la mode bayerisch, Bayerischer Sauerbraten | FL | 0.75 | 1 Portion | rind 220, wein_rot 60, essig 15, zwiebel 40, karotte 40, sellerie 25, oel 10, mehl 8, bruehe 100
Kronfleisch | Kronfleisch mit Meerrettich | HF | 0.8 | 1 Portion | rind 200, meerrettich 25, bruehe 100, semmel 60
Brezenknödel | Brezelknödel, Laugenknödel | KN | 1.0 | 2 Knödel | semmel 120, milch 100, ei 50, zwiebel 30, butter 10, petersilie 5
Prinzregenten-Schnitzel | Schnitzel mit Prinzregentensoße | HF | 0.85 | 1 Portion | schwein_mager 180, mehl 10, ei 25, paniermehl 25, oel 20, pilz 60, sahne 40
Krautkrapfen | Allgäuer Krautkrapfen | MA | 0.9 | 1 Portion | mehl 100, ei 50, sauerkraut 150, speck 40, zwiebel 30, butterschmalz 15, bruehe 80
Fränkisches Schäufele mit Kloß | Schäufele mit Kloß und Soße | FL | 0.8 | 1 Teller | schwein_nacken 260, kartoffel 220, staerke 15, bruehe 150, zwiebel 30, mehl 8
Fränkische Karpfen gebacken mit Kartoffelsalat | Karpfen blau fränkisch Kartoffelsalat | HFi | 0.85 | 1 Teller | karpfen 220, mehl 20, schmalz 25, kartoffel 200, zwiebel 30, essig 15, oel 12, bruehe 40
Schwäbischer Zwiebelrostbraten mit Spätzle | Rostbraten mit Spätzle | FL | 0.85 | 1 Teller | rind_steak 200, zwiebel 80, mehl 70, ei 40, oel 15, butter 10, bruehe 80
Ofenschlupfer | Scheiterhaufen schwäbisch | AU | 0.95 | 1 Portion | weissbrot 90, apfel 120, milch 120, ei 50, zucker 25, rosinen 15, butter 10
Pfitzauf | Schwäbischer Pfitzauf | G | 0.9 | 2 Stück | mehl 50, milch 120, ei 50, butter 15, zucker 5
Seelen | Schwäbische Seelen, Seele mit Kümmel und Salz | BR | 0.9 | 1 Stück | mehl 90, wasser 65, hefe 2, salz 2
Kartoffelschnitz und Spätzle | Gaisburger Spätzle Kartoffeln | KN | 0.95 | 1 Teller | kartoffel 200, mehl 80, ei 40, butter 15, zwiebel 40, bruehe 80
Badische Schneckensuppe | Schneckensüppchen | S | 0.95 | 1 Teller | schnecke 70, sahne 60, wein_weiss 40, butter 10, mehl 8, bruehe 200, petersilie 4
Brägele | Badische Bratkartoffeln | B | 0.85 | 1 Portion | kartoffel 250, speck 20, zwiebel 40, oel 15
Schwarzwälder Schinkenplatte | Schwarzwälder Vesper, Schinkenvesper | V | 1.0 | 1 Teller | rohschinken 80, roggenbrot 80, butter 15, gewuerzgurke 30
Ochsenmaulsalat | Ochsenmaul-Salat | SA | 1.0 | 1 Teller | zunge 120, zwiebel 40, essig 20, oel 15, wasser 20, roggenbrot 50
Pfälzer Leberknödel mit Sauerkraut | Lewwerknepp mit Kraut | KN | 0.95 | 1 Teller | leber 80, schwein_hack 60, semmel 50, ei 25, zwiebel 30, sauerkraut 200, kartoffel 150
Pfälzer Teller | Saumagen Bratwurst Leberknödel Teller | FL | 0.9 | 1 Teller | schwein_hack 100, bratwurst 80, leber 50, semmel 30, sauerkraut 150, kartoffel 150, oel 10
Grumbeersupp mit Quetschekuche | Kartoffelsuppe mit Zwetschgenkuchen | S | 0.95 | 1 Teller + 1 Stück | kartoffel 200, karotte 40, lauch 40, sahne 20, bruehe 250, mehl 40, pflaume 100, zucker 15, butter 8
Hoorische | Pfälzer Kartoffelklöße, Hoorige Knepp | KN | 0.9 | 1 Portion | kartoffel 280, mehl 20, ei 20, speck 30, sahne 40
Gefillde | Saarländische gefüllte Klöße | KN | 0.9 | 2 Klöße | kartoffel 250, schwein_hack 80, semmel 20, ei 20, zwiebel 20, speck 20, sahne 40
Lyoner Pfanne | Lyonerpfanne mit Kartoffeln | PF | 0.85 | 1 Portion | bockwurst 130, kartoffel 220, zwiebel 50, paprika 50, oel 15
Schwenkbraten | Saarländischer Schwenker | FL | 0.8 | 1 Steak | schwein_nacken 220, zwiebel 40, oel 15
Rheinischer Muscheltopf | Muscheln rheinische Art | HFi | 0.6 | 1 Topf | muschel 600, wein_weiss 80, zwiebel 50, karotte 40, lauch 40, butter 10, roggenbrot 60
Kölsche Kaviar | Flönz mit Zwiebeln, Blutwurst mit Röggelchen | V | 1.0 | 1 Portion | blutwurst 100, roggenbrot 70, zwiebel 30, senf 10, butter 10
Düsseldorfer Senfrostbraten | Senfrostbraten | FL | 0.8 | 1 Portion | rind_steak 200, senf 30, paniermehl 10, butter 10, zwiebel 30, oel 10
Westfälisches Blindhuhn | Blindhuhn, Bohnen-Birnen-Eintopf westfälisch | E | 0.95 | 1 Teller | gruene_bohnen 150, bohnen_trocken 30, kartoffel 100, karotte 50, apfel 60, birne 60, speck 40, bruehe 200
Pfefferpotthast | Westfälischer Potthast | E | 0.85 | 1 Teller | rind 200, zwiebel 120, paniermehl 15, pfeffer 2, bruehe 200, gewuerzgurke 30
Westfälischer Pickert | Lippischer Pickert, Kastenpickert | BR | 0.85 | 2 Scheiben | kartoffel 100, mehl 70, ei 25, milch 30, rosinen 15, oel 15, hefe 2
Möppkenbrot | Westfälische Blutwurst mit Speck | WU | 0.9 | 2 Scheiben | blutwurst 100, roggenbrot 30, speck 20, oel 10, apfel 60
Westfälischer Schinken mit Pumpernickel | Knochenschinken mit Pumpernickel | V | 1.0 | 1 Teller | rohschinken 70, vollkornbrot 80, butter 15
Westfälische Quarkspeise mit Pumpernickel | Westfälische Götterspeise | D | 1.0 | 1 Schälchen | quark 120, sahne 40, sauerkirsche 80, zucker 20, vollkornbrot 25, schokolade 5
Ahle Wurscht auf Brot | Nordhessische Ahle Wurst Brot | V | 1.0 | 1 Portion | mettwurst 60, roggenbrot 80, butter 10
Grie Soß mit Tafelspitz | Grüne Soße mit Rindfleisch | HF | 0.95 | 1 Teller | rind 160, kartoffel 200, schmand 40, joghurt 60, ei 30, petersilie 15, dill 5, gurke 20
Ebbelwoi | Äppelwoi, Apfelwein hessisch, Stöffche | GT | 1.0 | 0,3 l | apfelwein 300
Sauergespritzter | Apfelwein gespritzt sauer | GT | 1.0 | 0,3 l | apfelwein 200, wasser 100
Frankfurter Schnitzel mit Grüner Soße | Schnitzel mit Grie Soß | HF | 0.9 | 1 Teller | schwein_mager 170, mehl 10, ei 25, paniermehl 25, oel 20, kartoffel 180, schmand 30, joghurt 40, petersilie 10
Hessischer Kartoffelkuchen | Kartoffelkuchen Vogelsberg | KN | 0.85 | 1 Stück | kartoffel 200, speck 30, zwiebel 30, ei 25, mehl 10, oel 10
Kasseler Weckewerk | Weckewerk, Wurstebrei nordhessisch | WU | 0.9 | 1 Portion | schwein_hack 100, semmel 50, bruehe 80, zwiebel 20, kartoffel 150, gewuerzgurke 30
Thüringer Mutzbraten | Mutzbraten | FL | 0.8 | 1 Portion | schwein_nacken 220, zwiebel 20, gewuerz 2, roggenbrot 40, sauerkraut 100
Thüringer Blechkuchen mit Mohn | Mohnblechkuchen | K | 0.95 | 1 Stück | mehl 40, milch 50, mohn 30, zucker 25, butter 10, ei 10, griess 8
Leipziger Allerlei | Allerlei mit Flusskrebsen | GZ | 0.95 | 1 Portion | karotte 60, erbsen 50, spargel 60, blumenkohl 50, krabbe 40, butter 15, mehl 5, bruehe 60, pilz 30
Leipziger Lerche | Lerchengebäck Leipzig | G | 1.0 | 1 Stück | mehl 30, butter 18, zucker 15, marzipan 20, kirsche 15, ei 5
Sächsische Kartoffelsuppe | Kartoffelsuppe sächsisch mit Wiener | S | 0.95 | 1 Teller | kartoffel 200, karotte 40, sellerie 30, lauch 30, bockwurst 60, bruehe 250, butter 8, mehl 5
Sächsischer Sauerbraten mit Rosinen | Sauerbraten sächsische Art | FL | 0.8 | 1 Portion | rind 200, essig 20, wein_rot 40, rosinen 15, xb_lebkuchen 15, zwiebel 30, karotte 30, oel 10, bruehe 100
Sächsische Plinsen | Plinse, Eierplinsen | FR | 0.9 | 2 Stück | mehl 70, milch 120, ei 50, zucker 10, oel 12
Erzgebirgische Buttermilchgetzen | Buttermilchgetzen | KN | 0.8 | 1 Portion | kartoffel 250, buttermilch 60, mehl 20, speck 20, oel 15, zwiebel 20
Lausitzer Leinöl mit Quark und Kartoffeln | Quark mit Leinöl Lausitzer Art | HV | 1.0 | 1 Teller | kartoffel 280, quark_mager 150, oel 15, zwiebel 20, fruehlingszwiebel 10
Spreewälder Gurkensalat | Spreewaldgurken-Salat | SA | 1.0 | 1 Portion | gewuerzgurke 120, zwiebel 30, schmand 30, dill 3
Teltower Rübchen | Teltower Rübchen glasiert | B | 0.9 | 1 Portion | ruebe 180, butter 15, zucker 8, bruehe 50
Berliner Eisbein mit Erbspüree | Eisbein Berliner Art mit Sauerkraut und Erbspüree | FL | 0.8 | 1 Teller | schwein_haxe 300, erbsen_trocken 60, wasser 150, sauerkraut 150, speck 10, zwiebel 20
Kalter Hund | Kalte Schnauze, Lukullus | K | 1.0 | 1 Stück | keks 30, schokolade 25, kokos 10, zucker 10, ei 8
Ketwurst | DDR-Hotdog Ketwurst | SN | 1.0 | 1 Stück | bockwurst 100, semmel 70, ketchup 30
Snuten un Poten | Schnauze und Pfoten, Schweinsfüße mit Sauerkraut | FL | 0.8 | 1 Teller | schwein_haxe 250, sauerkraut 200, kartoffel 200, senf 10
Mecklenburger Rippenbraten | Rippenbraten mit Äpfeln und Pflaumen | FL | 0.8 | 1 Portion | schwein_bauch 220, apfel 80, pflaume_tr 30, zwiebel 20, bruehe 80, mehl 5
Plum un Klüten | Pflaumen und Klöße mecklenburgisch | D | 0.95 | 1 Teller | pflaume 200, zucker 25, staerke 8, mehl 80, milch 60, ei 25, butter 10
Rindfleisch mit Rosinensoße | Rindfleisch in Rosinensauce mecklenburgisch | HF | 0.85 | 1 Portion | rind 200, rosinen 25, mehl 12, butter 10, essig 10, zucker 8, bruehe 150, kartoffel 180
Holsteiner Sauerfleisch | Sauerfleisch mit Bratkartoffeln | HF | 0.9 | 1 Teller | schwein_mager 180, gelatine 5, essig 20, zwiebel 20, kartoffel 220, oel 15, bruehe 100
Schwarzsauer | Swattsuer, Schwarzsauer mit Klößen | S | 0.95 | 1 Teller | blutwurst 80, schwein_bauch 60, essig 15, zucker 10, pflaume_tr 20, mehl 40, ei 15, bruehe 250
Fliederbeersuppe mit Grießklößchen | Holunderbeersuppe | S | 0.95 | 1 Teller | blaubeere 150, zucker 25, staerke 10, apfel 60, wasser 150, griess 25, milch 60, ei 10
Bremer Knipp | Knipp mit Bratkartoffeln | WU | 0.85 | 1 Teller | schwein_hack 100, haferflocken 40, bruehe 60, kartoffel 200, oel 15, gewuerzgurke 30
Pluckte Finken | Bremer Pluckte Finken | E | 0.95 | 1 Teller | rind 120, speck 30, bohnen_trocken 30, karotte 80, kartoffel 120, apfel 60, bruehe 250
Heidschnuckenbraten | Heidschnuckenkeule, Lüneburger Lammbraten | FL | 0.75 | 1 Portion | lamm 220, zwiebel 40, bruehe 100, sahne 30, mehl 5
Buchweizentorte | Lüneburger Heide Buchweizentorte | K | 1.0 | 1 Stück | x4_buchweizen 20, ei 25, zucker 25, sahne 60, preiselbeeren 40
Stint gebraten | Gebratener Stint, Elbstint | HFi | 0.85 | 1 Portion | fisch_fett 220, mehl 20, oel 20, kartoffel 200, gurke 50
Büsumer Krabbenrührei | Krabben-Rührei auf Schwarzbrot | EI | 0.9 | 1 Portion | ei 120, krabbe 70, butter 10, milch 20, vollkornbrot 60, fruehlingszwiebel 5
Kieler Sprotten auf Brot | Kieler Sprotten mit Schwarzbrot | V | 1.0 | 1 Portion | sardine 80, vollkornbrot 70, butter 10, zitrone 5
Holsteiner Katenschinken mit Bratkartoffeln | Katenschinken Teller | HF | 0.9 | 1 Teller | rohschinken 80, kartoffel 250, oel 15, zwiebel 30, ei 50
Matjestatar | Matjes-Tatar auf Schwarzbrot | V | 1.0 | 1 Portion | xb_matjes 80, zwiebel 20, apfel 30, gewuerzgurke 20, schmand 20, vollkornbrot 60
Nordseekrabbensuppe | Krabbensuppe norddeutsch | S | 0.95 | 1 Teller | krabbe 60, sahne 50, wein_weiss 30, karotte 30, lauch 30, butter 10, mehl 10, bruehe 250
Hamburger Schnüüsch | Schnüüsch, Gemüseeintopf mit Milch | E | 0.95 | 1 Teller | gruene_bohnen 100, erbsen 60, karotte 60, kartoffel 120, milch 150, butter 15, schinken 40, mehl 8
Steckrübenmus | Wruken-Mus, Steckrübenpüree | B | 0.9 | 1 Portion | xb_steckruebe 180, kartoffel 100, butter 15, milch 40
Mecklenburger Buttermilchsuppe | Buttermilchsuppe mit Klüten | S | 0.95 | 1 Teller | buttermilch 300, mehl 35, ei 15, zucker 20, rosinen 10
Rumtopf mit Vanilleeis | Rumtopf-Früchte mit Eis | D | 1.0 | 1 Schälchen | xb_rote_gruetze_beeren 80, zucker 20, weinbrand 15, eis 80
Bremer Klaben | Klaben, Bremer Rosinenklaben | K | 1.0 | 1 Scheibe | mehl 40, butter 12, rosinen 25, zucker 6, milch 12, hefe 1, mandel 3
Pharisäer | Kaffee mit Rum und Sahnehaube | GT | 1.0 | 1 Tasse | kaffee 150, weinbrand 20, zucker 8, sahne 30
Tote Tante | Kakao mit Rum und Sahne | GT | 1.0 | 1 Tasse | milch 200, kakao 10, zucker 15, weinbrand 20, sahne 25
Lumumba | Heiße Schokolade mit Rum | GT | 1.0 | 1 Tasse | milch 200, kakao 10, zucker 15, weinbrand 20
Rumgrog | Norddeutscher Grog | GT | 1.0 | 1 Glas | spirituose 40, wasser 160, zucker 10, zitrone 5
Eierpunsch | Eierpunsch mit Weißwein | GT | 1.0 | 1 Tasse | wein_weiss 150, ei 20, zucker 20, sahne 20, likoer 10
Maibowle | Waldmeisterbowle | GT | 1.0 | 1 Glas | wein_weiss 150, zucker 8, wasser 30
Kalte Ente | Kalte Ente Bowle | GT | 1.0 | 1 Glas | wein_weiss 180, zitrone 5, zucker 5
Diesel | Krefelder, Bier mit Cola, Colabier | GT | 1.0 | 0,5 l | bier 250, xb_cola 250
Russ | Russn, Weißbier mit Zitronenlimo | GT | 1.0 | 0,5 l | bier 250, x2_limonade 250
Goaßmaß | Goassmass, Bier mit Cola und Kirschlikör | GT | 1.0 | 1 Maß | bier 500, xb_cola 300, likoer 40
Altbier | Alt, Düsseldorfer Alt | GT | 1.0 | 0,25 l | bier 250
Helles | Bayerisches Helles, Helles Bier | GT | 1.0 | 0,5 l | bier 500
Schwarzbier | Schwarzes Bier | GT | 1.0 | 0,5 l | bier 500
Kiba | Kirsch-Banane-Saft, KiBa | GT | 1.0 | 1 Glas | kirsche 80, banane 50, wasser 120, zucker 10
Eisschokolade | Eisschokolade mit Sahne | GT | 1.0 | 1 Glas | milch 200, kakao 10, zucker 12, eis 80, sahne 30
Bananenmilch | Bananenmilch selbstgemacht, Bananenshake | GT | 1.0 | 1 Glas | milch 220, banane 100, zucker 5
Erdbeermilch | Erdbeershake selbstgemacht | GT | 1.0 | 1 Glas | milch 220, erdbeere 100, zucker 10
Johannisbeerschorle | Johannisbeersaftschorle | GT | 1.0 | 0,4 l | xb_johannisbeere 100, zucker 15, wasser 300
Eierlikör | Eierlikör selbstgemacht | GT | 1.0 | 1 Glas (4 cl) | likoer 40
Apfelpunsch | Heißer Apfelpunsch alkoholfrei | GT | 1.0 | 1 Tasse | xb_apfelsaft 200, xb_orangensaft 50, zimt 1
Heißer Apfelwein | Heißer Ebbelwoi, Apfelwein warm mit Zimt | GT | 1.0 | 1 Glas | apfelwein 250, zucker 10, zimt 1
Laugenstange | Brezelstange | BR | 1.0 | 1 Stück | semmel 80, butter 5
Laugencroissant | Laugen-Croissant | BR | 1.0 | 1 Stück | mehl 35, butter 18, milch 12, zucker 2, hefe 1
Käsestange | Blätterteig-Käsestange | KR | 1.0 | 1 Stück | blaetterteig 60, emmentaler 25, ei 5
Schweineohr | Schweineohren Gebäck, Palmier | G | 1.0 | 1 Stück | blaetterteig 60, zucker 15
Quarktasche | Quarktaschen, Quarkplunder | G | 1.0 | 1 Stück | blaetterteig 60, quark 50, zucker 15, ei 8, vanillepudding_pulver 4
Kirschtasche | Kirschplunder, Kirschteilchen | G | 1.0 | 1 Stück | blaetterteig 60, sauerkirsche 50, zucker 12, staerke 4
Rosinenschnecke | Rosinen-Plunderschnecke, Puddingschnecke | G | 1.0 | 1 Stück | mehl 45, butter 15, milch 15, zucker 12, rosinen 15, vanillepudding_pulver 5, ei 5
Kameruner | Kameruner Spritzgebäck DDR | G | 1.0 | 1 Stück | mehl 40, milch 15, ei 8, butter 5, zucker 10, hefe 2, oel 12
Spritzkuchen | Spritzkuchen mit Zuckerguss | G | 1.0 | 1 Stück | mehl 20, ei 20, butter 10, wasser 25, oel 10, zucker 15
Kaiserbrötchen | Kaisersemmel, Kaiserweck | BR | 1.0 | 1 Stück | semmel 60
Mohnbrötchen | Mohnsemmel | BR | 1.0 | 1 Stück | semmel 60, mohn 5
Sesambrötchen | Sesamsemmel | BR | 1.0 | 1 Stück | semmel 60, sesam 5
Kürbiskernbrötchen | Kürbiskernsemmel | BR | 1.0 | 1 Stück | mehl 40, x4_roggenmehl 10, wasser 30, kuerbiskerne 10, hefe 1
Dinkelbrötchen | Dinkelsemmel, Dinkelweckerl | BR | 1.0 | 1 Stück | mehl 45, wasser 35, sonnenblumenkerne 5, hefe 1
Roggenbrötchen | Roggensemmel | BR | 1.0 | 1 Stück | roggenbrot 65
Kartoffelbrot | Kartoffelbrot vom Bäcker | BR | 1.0 | 2 Scheiben | mehl 40, kartoffel 30, wasser 25, hefe 1
Sonnenblumenkernbrot | Sonnenblumenbrot | BR | 1.0 | 2 Scheiben | x4_roggenmehl 30, mehl 25, sonnenblumenkerne 10, wasser 40, hefe 1
Dinkelvollkornbrot | Dinkelbrot | BR | 1.0 | 2 Scheiben | vollkornbrot 90
Rosinenstuten | Stuten, Westfälischer Rosinenstuten | BR | 1.0 | 2 Scheiben | mehl 45, milch 20, butter 8, rosinen 15, zucker 6, hefe 1
Pizzabrötchen | Pizza-Brötchen überbacken | SN | 0.95 | 1 Stück | semmel 70, tomatenmark 15, salami 20, gouda 30, oregano 1
Schinken-Käse-Croissant | Croissant mit Schinken und Käse | SN | 1.0 | 1 Stück | mehl 40, butter 20, milch 12, schinken 30, gouda 20, hefe 1
Belegtes Brötchen mit Ei | Eibrötchen, Brötchen mit Ei und Remoulade | SN | 1.0 | 1 Stück | semmel 60, ei 50, mayonnaise 10, salat 10, tomate 15
Prasselkuchen | Sächsischer Prasselkuchen | K | 1.0 | 1 Stück | blaetterteig 60, mehl 15, butter 12, zucker 15, marmelade 10
Liegnitzer Bombe | Liegnitzer Bomben | K | 1.0 | 1 Stück | mehl 25, honig 15, zucker 10, ei 10, rosinen 10, mandel 10, schokolade 15, butter 5
Pulsnitzer Pfefferkuchen | Pulsnitzer Lebkuchen | G | 1.0 | 2 Stück | mehl 25, honig 15, zucker 5, lebkuchen_gewuerz 1, schokolade 10
Magenbrot | Magenbrot vom Jahrmarkt | G | 1.0 | 1 Tüte (100 g) | mehl 50, honig 20, zucker 20, schokolade 10, kakao 3, lebkuchen_gewuerz 1
Bärentatzen | Bärentatzen Plätzchen | G | 1.0 | 3 Stück | mehl 15, butter 10, zucker 10, mandel 8, kakao 2, schokolade 8, ei 5
Heidesand | Heidesand-Plätzchen | G | 1.0 | 4 Stück | mehl 25, butter 18, zucker 12
Husarenkrapfen | Engelsaugen, Kulleraugen | G | 1.0 | 3 Stück | mehl 20, butter 12, zucker 8, ei 5, marmelade 8, mandel 3
Terrassenplätzchen | Spitzbuben gestapelt, Terrassen-Plätzchen | G | 1.0 | 2 Stück | mehl 22, butter 14, zucker 10, marmelade 10
Schwarz-Weiß-Gebäck | Schwarz-Weiß-Kekse, Schachbrettkekse | G | 1.0 | 4 Stück | mehl 25, butter 15, zucker 10, kakao 2
Springerle | Springerle Anisgebäck | G | 1.0 | 2 Stück | mehl 30, zucker 25, ei 10
Anisplätzchen | Anisbrötle | G | 1.0 | 4 Stück | mehl 25, zucker 25, ei 12
Gebrannte Mandeln | Gebrannte Mandeln vom Weihnachtsmarkt | SN | 1.0 | 1 Tüte (100 g) | mandel 65, zucker 35, zimt 1
Paradiesapfel | Liebesapfel, Kandierter Apfel | SN | 1.0 | 1 Stück | apfel 150, zucker 40
Schokofrüchte | Schokobanane, Schokofrüchte vom Markt | SN | 1.0 | 1 Spieß | banane 60, erdbeere 40, schokolade_milch 30
Schmalzkuchen | Mutzen, Mutzenmandeln, Schmalzgebäck | G | 1.0 | 1 Tüte (100 g) | mehl 45, quark 15, ei 10, zucker 15, oel 15
Senfeier | Eier in Senfsoße, Senfeier mit Kartoffeln | EI | 0.95 | 1 Teller | ei 120, senf 25, mehl 15, butter 15, milch 150, bruehe 80, kartoffel 220
Tote Oma | Grützwurst mit Sauerkraut und Kartoffeln | WU | 0.9 | 1 Teller | blutwurst 120, sauerkraut 150, kartoffel 200, zwiebel 30, oel 10
Jägerschnitzel mit Jagdwurst | Jagdwurstschnitzel paniert | HF | 0.9 | 1 Teller | bockwurst 130, ei 25, paniermehl 25, mehl 10, oel 20, nudeln 80, tomatenmark 20, ketchup 20, wasser 160
Grützwurst | Thüringer Grützwurst warm | WU | 0.95 | 1 Portion | blutwurst 150, graupen 20, zwiebel 20, oel 5, wasser 30
Krakauer mit Pommes | Krakauer Wurst mit Pommes | SN | 0.9 | 1 Teller | wuerstchen_geraeuchert 150, kartoffel 200, oel 20, ketchup 30
Schaschlik | Imbiss-Schaschlik mit Soße, Schaschlikspieß | KB | 0.85 | 1 Spieß | schwein_nacken 150, speck 20, zwiebel 50, paprika 50, ketchup 40, tomatenmark 10, oel 10
Steak im Brötchen | Nackensteak im Brötchen, Steakbrötchen | SN | 0.9 | 1 Stück | schwein_nacken 140, semmel 70, zwiebel 30, oel 8, senf 10
Pommes Spezial | Pommes mit Ketchup, Mayo und Zwiebeln | SN | 0.9 | 1 Portion | kartoffel 220, oel 20, ketchup 25, mayonnaise 25, zwiebel 20
Pommes mit Mayo | Pommes weiß, Pommes Mayo | SN | 0.9 | 1 Portion | kartoffel 220, oel 20, mayonnaise 30
Schranke Currywurst | Currywurst Pommes Schranke | SN | 0.9 | 1 Teller | bockwurst 130, kartoffel 200, oel 20, ketchup 40, mayonnaise 25, gewuerz 2
Bratkartoffeln mit Spiegelei | Spiegeleier mit Bratkartoffeln | EI | 0.9 | 1 Teller | kartoffel 250, oel 20, zwiebel 30, speck 20, ei 100
Bratkartoffeln mit Sülze und Remoulade | Sülze mit Bratkartoffeln | HF | 0.9 | 1 Teller | kartoffel 250, oel 20, zwiebel 30, schinken 100, gelatine 5, mayonnaise 25, gewuerzgurke 15
Hühnerfrikassee mit Reis | Frikassee mit Reis | HG | 0.95 | 1 Teller | hahn_brust 150, reis 75, wasser 160, pilz 40, spargel 40, erbsen 30, butter 15, mehl 12, sahne 30, bruehe 120
Hähnchenkeule mit Reis und Gemüse | Hähnchenschenkel mit Reis | HG | 0.85 | 1 Teller | hahn 250, reis 75, wasser 160, erbsen 50, karotte 50, oel 10, paprikapulver 2
Milchnudeln | Nudeln in Milch, Milchsuppe mit Nudeln | D | 0.95 | 1 Teller | nudeln 60, milch 300, zucker 15, zimt 1
Grießauflauf mit Kirschen | Grießauflauf | AU | 0.95 | 1 Portion | griess 50, milch 250, ei 40, zucker 25, sauerkirsche 80, butter 10
Quarkauflauf | Quarkauflauf mit Obst | AU | 0.95 | 1 Portion | quark_mager 200, ei 50, griess 25, zucker 25, apfel 80, butter 8
Schweinegeschnetzeltes mit Reis | Geschnetzeltes vom Schwein mit Reis | HF | 0.9 | 1 Teller | schwein_mager 170, pilz 60, zwiebel 30, sahne 50, oel 10, reis 75, wasser 160, bruehe 50
Fischfilet mit Senfsoße und Kartoffeln | Seelachs in Senfsoße | HFi | 0.95 | 1 Teller | seelachs 180, senf 20, mehl 10, butter 15, milch 120, kartoffel 220
Gemüsereis mit Hähnchen | Reispfanne mit Hähnchen | RP | 0.95 | 1 Teller | reis 80, wasser 180, hahn_brust 120, erbsen 40, karotte 40, paprika 40, mais 30, oel 12
Kohlrabigemüse in Rahmsoße | Rahmkohlrabi, Kohlrabi in heller Soße | GZ | 0.95 | 1 Portion | xb_kohlrabi 250, butter 12, mehl 10, milch 80, sahne 20
Schwarzwurzelgemüse | Schwarzwurzeln in Rahmsoße | GZ | 0.95 | 1 Portion | xb_schwarzwurzel 200, butter 10, mehl 8, milch 60, sahne 20
Fenchelgemüse | Geschmorter Fenchel | GZ | 0.9 | 1 Portion | xb_fenchel 250, butter 10, bruehe 50, parmesan 10
Rote-Bete-Gemüse | Rote Bete warm | GZ | 0.9 | 1 Portion | rote_bete 220, butter 10, essig 8, zucker 5, zwiebel 20
Spitzkohl in Rahm | Rahmspitzkohl | GZ | 0.85 | 1 Portion | weisskohl 250, sahne 40, butter 10, zwiebel 20
Rahmwirsing mit Kartoffeln und Würstchen | Wirsing mit Bockwurst | GM | 0.9 | 1 Teller | weisskohl 220, sahne 40, kartoffel 180, bockwurst 100, butter 10
Wirsingeintopf | Wirsingsuppe mit Hack | E | 0.95 | 1 Teller | weisskohl 200, kartoffel 120, gemischtes_hack 80, zwiebel 30, karotte 30, bruehe 300, oel 8
Kohlrabisuppe | Kohlrabicremesuppe | S | 0.95 | 1 Teller | xb_kohlrabi 200, kartoffel 60, sahne 30, butter 8, bruehe 250
Pastinakensuppe | Pastinakencremesuppe | S | 0.95 | 1 Teller | xb_pastinake 180, kartoffel 50, sahne 30, butter 8, bruehe 250
Bärlauchsuppe | Bärlauchcremesuppe | S | 0.95 | 1 Teller | wildkraut 50, kartoffel 120, sahne 40, butter 10, bruehe 250
Grünkernsuppe | Badische Grünkernsuppe | S | 0.95 | 1 Teller | xb_gruenkern 45, karotte 40, lauch 30, sahne 25, butter 8, bruehe 300
Brotsuppe | Bayerische Brotsuppe | S | 0.95 | 1 Teller | roggenbrot 60, zwiebel 40, butter 10, bruehe 300, fruehlingszwiebel 5
Buchstabensuppe | Nudelsuppe mit Buchstaben | S | 0.95 | 1 Teller | nudeln 30, karotte 30, sellerie 20, lauch 20, bruehe 300
Deutsche Hochzeitssuppe | Hochzeitssuppe mit Eierstich und Fleischklößchen | S | 0.95 | 1 Teller | bruehe 300, gemischtes_hack 50, ei 30, milch 20, spargel 30, karotte 20, nudeln 15
Ochsenschwanzsuppe gebunden | Deutsche Ochsenschwanzsuppe | S | 0.9 | 1 Teller | rind_fett 100, karotte 30, sellerie 20, tomatenmark 10, mehl 10, wein_rot 20, bruehe 300
Graupensuppe mit Rauchfleisch | Graupeneintopf mit Rauchfleisch | E | 0.95 | 1 Teller | graupen 50, kassler 80, karotte 40, sellerie 30, kartoffel 80, lauch 30, bruehe 300
Feldsalat mit Speck und Croutons | Rapunzelsalat, Ackersalat mit Speck | SA | 1.0 | 1 Portion | salat 80, speck 30, weissbrot 20, oel 15, essig 8, zwiebel 10
Löwenzahnsalat mit Speck | Bettseicherssalat, Pfälzer Löwenzahnsalat | SA | 1.0 | 1 Portion | wildkraut 80, speck 30, ei 25, oel 12, essig 10, zwiebel 10
Endiviensalat | Endiviensalat mit Kartoffeldressing | SA | 1.0 | 1 Portion | salat 120, kartoffel 40, oel 12, essig 10, zwiebel 10
Kohlrabisalat | Kohlrabi-Rohkost | SA | 1.0 | 1 Portion | xb_kohlrabi 150, apfel 50, joghurt 40, oel 8
Rindfleischsalat | Rindfleischsalat mit Kürbiskernöl | SA | 1.0 | 1 Teller | rind 120, zwiebel 30, gewuerzgurke 30, essig 15, oel 15, ei 25
Geflügelsalat | Geflügelsalat mit Mandarinen | SA | 1.0 | 1 Portion | hahn_brust 100, mayonnaise 30, joghurt 30, orange 50, ananas 30
Matjes in Sahnesoße | Matjes in Sahne mit Apfel und Zwiebel | HFi | 1.0 | 1 Teller | xb_matjes 120, sahne 40, joghurt 40, apfel 50, zwiebel 30, kartoffel 200
Räucherlachs mit Reibekuchen und Meerrettich | Lachs auf Kartoffelrösti | V | 0.9 | 1 Teller | xb_lachs_geraeuchert 80, kartoffel 200, ei 25, oel 25, meerrettich 15, schmand 20
Krautwickel bayerisch | Krautwickel | DO | 0.85 | 2 Stück | weisskohl 200, gemischtes_hack 150, semmel 20, ei 20, zwiebel 30, speck 20, bruehe 100
"""
