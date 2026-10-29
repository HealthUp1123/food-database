CUISINE = 'pl'
TEXT = """
Zupa jarzynowa | Polnische Gemüsesuppe | S | 0.95 | 1 Teller | kartoffel 80, karotte 50, sellerie 30, blumenkohl 50, erbsen 30, gruene_bohnen 30, sahne 20, bruehe 280
Kartoflanka | Zupa ziemniaczana, Polnische Kartoffelsuppe | S | 0.95 | 1 Teller | kartoffel 180, karotte 40, speck 20, zwiebel 30, sauerrahm 30, bruehe 250
Zupa fasolowa | Polnische Bohnensuppe | S | 0.95 | 1 Teller | bohnen_trocken 50, wasser 150, kartoffel 60, karotte 30, wuerstchen_geraeuchert 40, bruehe 150
Krem z dyni | Polnische Kürbiscremesuppe | S | 0.95 | 1 Teller | kuerbis 250, kartoffel 50, sahne 30, butter 8, bruehe 150, kuerbiskerne 8
Schab pieczony | Polnischer Schweinebraten | FL | 0.8 | 1 Portion | schwein_mager 200, oel 10, oregano 1, knoblauch 4, zwiebel 40, kartoffel 150
Karkówka z grilla | Gegrillter Schweinenacken polnisch | HF | 0.8 | 1 Portion | schwein_nacken 220, zwiebel 30, oel 8, senf 10
Pulpety w sosie koperkowym | Fleischbällchen in Dillsauce | KF | 0.9 | 1 Portion | gemischtes_hack 150, ei 20, semmel 20, sahne 40, mehl 8, dill 8, bruehe 120, kartoffel 150
Gulasz wieprzowy | Polnisches Schweinegulasch | E | 0.85 | 1 Portion | schwein_nacken 180, zwiebel 50, paprika_rot 50, mehl 8, tomatenmark 10, oel 10, bruehe 120
Kotlet de volaille | De volaille | HG | 0.9 | 1 Stück | hahn_brust 160, butter 20, ei 25, paniermehl 30, mehl 10, oel 20
Kluski na parze | Pampuchy, Dampfnudeln polnisch | G | 0.95 | 2 Stück | mehl 80, milch 40, ei 15, zucker 10, hefe 3, butter 8, blaubeere 40, sahne 30
Łazanki z kapustą | Lazanki mit Kraut | NA | 0.9 | 1 Teller | nudeln 80, wasser 100, sauerkraut 100, weisskohl 80, speck 30, zwiebel 30, pilz 40
Pierogi z serem na słodko | Süße Quark-Piroggen | MA | 0.95 | 8 Stück | mehl 100, wasser 50, quark 120, ei 15, zucker 20, sauerrahm 30, butter 10
Pierogi ze szpinakiem | Spinatpiroggen | MA | 0.95 | 8 Stück | mehl 100, wasser 50, spinat 120, beyaz_peynir 50, knoblauch 3, butter 10
Krokiety z kapustą i grzybami | Krokiety | SN | 0.9 | 2 Stück | mehl 50, milch 80, ei 40, sauerkraut 80, pilz 40, paniermehl 25, oel 20
Pasztet | Polnische Pastete | V | 0.9 | 1 Portion | schwein_nacken 60, leber 30, speck 20, semmel 10, ei 10
Kiszka ziemniaczana | Kiszka | KN | 0.85 | 1 Portion | kartoffel 250, speck 40, zwiebel 30, schmalz 10
Gzik z ziemniakami | Pyry z gzikiem | KN | 1.0 | 1 Portion | kartoffel 250, quark_mager 120, sauerrahm 40, zwiebel 20, butter 8
Knedle ze śliwkami | Polnische Zwetschgenknödel | KN | 0.95 | 4 Stück | kartoffel 200, mehl 70, ei 15, pflaume 120, butter 15, paniermehl 15, zucker 15
Dorsz smażony | Gebratener Dorsch polnisch | HFi | 0.85 | 1 Portion | kabeljau 180, mehl 15, ei 25, paniermehl 15, oel 20, kartoffel 150
Pstrąg pieczony | Gebackene Forelle polnisch | HFi | 0.8 | 1 Portion | forelle 250, butter 15, zitrone 10, dill 5
Karp w galarecie | Karpfen in Aspik | V | 1.0 | 1 Portion | karpfen 150, karotte 30, gelatine 5, bruehe 120
Buraczki zasmażane | Gebratene Rote Bete | B | 0.9 | 1 Portion | rote_bete 200, butter 10, mehl 8, zitrone 10, zucker 5
Surówka z kiszonej kapusty | Sauerkrautsalat polnisch | SA | 1.0 | 1 Portion | sauerkraut 150, karotte 40, apfel 50, oel 10, zwiebel 10
Kapusta z grochem | Kraut mit Erbsen | HH | 0.95 | 1 Portion | sauerkraut 150, erbsen_trocken 50, wasser 100, zwiebel 30, oel 10
Jagodzianki | Heidelbeerbrötchen | G | 0.95 | 1 Stück | mehl 60, milch 25, ei 10, butter 10, zucker 15, hefe 2, blaubeere 40
Rogal świętomarciński | Martinshörnchen Posen | G | 0.95 | 1 Stück | mehl 50, butter 25, mohn 25, zucker 25, mandel 10, rosinen 10, ei 10
Karpatka | Polnische Karpatenkuchen | K | 0.95 | 1 Stück | mehl 25, butter 25, ei 25, milch 100, zucker 25, staerke 10
Placek z kruszonką | Drożdżowe ciasto z kruszonką | K | 0.95 | 1 Stück | mehl 60, milch 20, ei 10, butter 20, zucker 20, hefe 2
Kogel-mogel | Kogel mogel | D | 1.0 | 1 Glas | ei 40, zucker 20
Ryż z jabłkami | Reis mit Äpfeln polnisch | AU | 0.9 | 1 Portion | reis 60, milch 150, apfel 150, zucker 20, butter 10, zimt 1
Sękacz | Baumkuchen polnisch | K | 0.95 | 1 Stück | butter 20, zucker 20, ei 25, mehl 12, staerke 8
Grzaniec galicyjski | Polnischer Glühwein | GT | 1.0 | 1 Tasse | wein_rot 200, zucker 15, honig 5, orange 10
Miód pitny | Met, Polnischer Honigwein | GT | 1.0 | 1 Glas (100 ml) | likoerwein 60, honig 20, wasser 20
"""
