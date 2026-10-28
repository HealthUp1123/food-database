CUISINE = 'tr'
TEXT = """
Pirinç Pilavı | Tereyağlı Pilav, Turkish rice pilaf, Sade Pilav | RP | 0.95 | 1 Teller | reis 70, butter 10, wasser 140
Şehriyeli Pirinç Pilavı | Reis mit Nudeln, Rice pilaf with vermicelli | RP | 0.95 | 1 Teller | reis 60, nudeln 12, butter 10, wasser 140
Bulgur Pilavı | Bulgur Pilav, Bulgur pilaf | RP | 0.95 | 1 Teller | bulgur 70, butter 8, zwiebel 20, wasser 150
Domatesli Bulgur Pilavı | Bulgur mit Tomaten | RP | 0.95 | 1 Teller | bulgur 70, tomate 60, tomatenmark 8, zwiebel 20, oel 8, wasser 140
Nohutlu Pilav | Reis mit Kichererbsen, Pilaf with chickpeas | RP | 0.95 | 1 Teller | reis 60, kichererbsen 60, butter 10, wasser 130
Nohutlu Bulgur Pilavı | Bulgur mit Kichererbsen | RP | 0.95 | 1 Teller | bulgur 60, kichererbsen 60, butter 8, zwiebel 20, wasser 140
Mercimekli Bulgur Pilavı | Bulgur mit Linsen, Bulgur pilaf with lentils | RP | 0.95 | 1 Teller | bulgur 55, linsen 20, zwiebel 30, oel 10, wasser 170
Perde Pilavı | Siirt Perde Pilavı, Pilaf im Teigmantel, Siirt pilaf | RP | 0.9 | 1 Portion | reis 60, hahn 60, mandel 12, rosinen 10, butter 15, mehl 40, ei 20, wasser 100
İç Pilav | Iç Pilav, Gewürzreis mit Leber und Pinienkernen, Spiced rice with liver | RP | 0.95 | 1 Teller | reis 70, huhn_leber 35, pinienkerne 8, rosinen 8, zwiebel 20, butter 12, zimt 1, wasser 140
Hamsi Pilavı | Reis mit Sardellen, Anchovy pilaf | RP | 0.9 | 1 Teller | reis 60, sardelle 100, zwiebel 40, butter 10, pinienkerne 6, rosinen 6, zimt 1, wasser 120
Midye Pilavı | Reis mit Miesmuscheln, Mussel pilaf | RP | 0.95 | 1 Teller | reis 60, muschel 90, zwiebel 30, pinienkerne 6, rosinen 6, olivenoel 10, wasser 120
Etli Pilav | Reis mit Fleisch, Pilaf with beef | RP | 0.92 | 1 Teller | reis 60, rind 80, butter 10, zwiebel 20, wasser 130
Kavurmalı Pilav | Reis mit Kavurma | RP | 0.92 | 1 Teller | reis 60, rind_fett 70, butter 6, zwiebel 20, wasser 130
Kıymalı Pilav | Reis mit Hack, Pilaf with minced meat | RP | 0.92 | 1 Teller | reis 60, hack 70, zwiebel 25, tomatenmark 6, oel 8, wasser 130
Mantarlı Pilav | Reis mit Champignons | RP | 0.95 | 1 Teller | reis 60, pilz 100, butter 10, wasser 120
Patlıcanlı Pilav | Reis mit Aubergine | RP | 0.92 | 1 Teller | reis 55, aubergine 120, tomate 40, zwiebel 20, oel 20, wasser 110
Sebzeli Pilav | Gemüsereis | RP | 0.95 | 1 Teller | reis 60, karotte 30, erbsen 30, mais 30, paprika 30, butter 10, wasser 130
Domatesli Pirinç Pilavı | Tomatenreis | RP | 0.95 | 1 Teller | reis 65, tomate 60, tomatenmark 8, butter 8, wasser 130
Bezelyeli Pilav | Reis mit Erbsen | RP | 0.95 | 1 Teller | reis 60, erbsen 60, butter 10, wasser 130
Arpa Şehriye Pilavı | Nudelpilaw mit Arpa Şehriye | RP | 0.95 | 1 Teller | nudeln 60, butter 10, bruehe 120
Düğün Pilavı | Hochzeitspilaw, Wedding rice | RP | 0.92 | 1 Teller | reis 60, hahn 60, kichererbsen 30, butter 12, wasser 130
Kuskus Pilavı | Couscous Pilaf | RP | 0.95 | 1 Teller | couscous 60, butter 8, zwiebel 20, wasser 100
Pilav Üstü Kuru Fasulye | Kuru Fasulye mit Reis, White beans with rice | RP | 0.93 | 1 Teller | bohnen_trocken 50, reis 60, zwiebel 25, tomatenmark 8, butter 15, wasser 330
Pilav Üstü Nohut | Kichererbsen auf Reis | RP | 0.93 | 1 Teller | kichererbsen_trocken 45, reis 60, zwiebel 25, tomatenmark 8, butter 15, wasser 300
Pilav Üstü Döner | Döner auf Reis, Doner over rice | KB | 0.88 | 1 Teller | reis 60, lamm 70, hack 60, butter 8, tomate 30, wasser 130
Pilav Üstü Tavuk | Hähnchen auf Reis, Chicken over rice | HG | 0.9 | 1 Teller | reis 60, hahn_brust 110, butter 8, tomate 30, wasser 130
Siirt Büryan | Büryan Siirt, Lamm aus dem Erdofen | HF | 0.65 | 1 Portion | lamm 300, schwanzfett 15, lavas 40
Fırın Makarna | Überbackene Nudeln, Baked pasta Turkish | T | 0.95 | 1 Portion | nudeln 70, kasar 40, ei 25, milch 80, butter 10, wasser 150
Kıymalı Fırın Makarna | Überbackene Nudeln mit Hack | T | 0.93 | 1 Portion | nudeln 70, hack 60, kasar 35, tomatenmark 8, zwiebel 20, milch 40, butter 8, wasser 150
Peynirli Makarna | Nudeln mit Käse | T | 0.95 | 1 Portion | nudeln 75, beyaz_peynir 45, butter 10, wasser 160
Kıymalı Makarna | Nudeln mit Hackfleisch | T | 0.95 | 1 Portion | nudeln 75, hack 60, zwiebel 20, tomatenmark 10, oel 8, wasser 160
Domates Soslu Makarna | Nudeln mit Tomatensoße | T | 0.95 | 1 Portion | nudeln 75, tomate 100, tomatenmark 8, zwiebel 20, oel 10, wasser 150
Yoğurtlu Makarna | Nudeln mit Joghurt und Knoblauch | T | 0.95 | 1 Portion | nudeln 70, joghurt 100, knoblauch 3, butter 10, pul_biber 1, wasser 140
Tavuklu Makarna | Nudeln mit Hähnchen | T | 0.95 | 1 Portion | nudeln 70, hahn_brust 80, sahne 30, paprika 30, zwiebel 20, oel 8, wasser 140
Sebzeli Makarna | Gemüsenudeln | T | 0.95 | 1 Portion | nudeln 70, zucchini 50, paprika 40, tomate 50, zwiebel 20, oel 12, wasser 140
Mantarlı Kremalı Makarna | Nudeln mit Pilzrahmsoße | T | 0.95 | 1 Portion | nudeln 70, pilz 80, sahne 50, zwiebel 15, butter 8, wasser 140
Spagetti Bolonez | Spaghetti Bolognese türkisch | T | 0.95 | 1 Teller | nudeln 80, hack 80, tomate 100, tomatenmark 10, zwiebel 25, oel 10, wasser 160
Cevizli Erişte | Hausnudeln mit Walnuss | T | 0.95 | 1 Portion | nudeln 70, walnuss 25, butter 12, zucker 3, wasser 140
Peynirli Erişte | Hausnudeln mit Käse | T | 0.95 | 1 Portion | nudeln 70, beyaz_peynir 40, butter 12, wasser 140
Yoğurtlu Erişte | Hausnudeln mit Joghurt | T | 0.95 | 1 Portion | nudeln 70, joghurt 90, butter 12, knoblauch 3, wasser 140
Kıymalı Erişte | Hausnudeln mit Hack | T | 0.95 | 1 Portion | nudeln 70, hack 60, zwiebel 20, tomatenmark 8, oel 8, wasser 140
Tirit | Tirit, Brot in Fleischbrühe, Bread with meat and broth | E | 0.95 | 1 Teller | ekmek 100, lamm 70, joghurt 60, butter 12, tomatenmark 6, bruehe 150
Hamsi Tava | Frittierte Sardellen, Fried anchovies | HFi | 0.85 | 1 Portion | sardelle 200, maismehl 30, oel 22, zitrone 5
Hamsi Buğulama | Gedünstete Sardellen | HFi | 0.85 | 1 Portion | sardelle 200, olivenoel 10, zitrone 8, petersilie 5, wasser 40
Hamsi Izgara | Gegrillte Sardellen | HFi | 0.8 | 1 Portion | sardelle 200, oel 6
Levrek Izgara | Gegrillter Wolfsbarsch, Grilled sea bass | HFi | 0.75 | 1 Portion | wolfsbarsch 280, olivenoel 8, zitrone 8, salat 30
Çipura Izgara | Gegrillte Dorade, Grilled sea bream | HFi | 0.75 | 1 Portion | wolfsbarsch 280, olivenoel 8, zitrone 8, salat 30
Levrek Buğulama | Gedünsteter Wolfsbarsch | HFi | 0.8 | 1 Portion | wolfsbarsch 240, wein_weiss 40, olivenoel 8, zitrone 8, petersilie 5
Çipura Fırın | Dorade aus dem Ofen | HFi | 0.75 | 1 Portion | wolfsbarsch 280, kartoffel 100, tomate 40, olivenoel 10, zitrone 6
Alabalık Izgara | Gegrillte Forelle, Grilled trout | HFi | 0.75 | 1 Portion | forelle 260, olivenoel 6, zitrone 6, salat 30
Alabalık Tava | Gebratene Forelle | HFi | 0.8 | 1 Portion | forelle 260, mehl 15, oel 15, zitrone 6
Sardalya Izgara | Gegrillte Sardinen, Grilled sardines | HFi | 0.78 | 1 Portion | sardine 250, olivenoel 6, zitrone 6
Sardalya Tava | Gebratene Sardinen | HFi | 0.8 | 1 Portion | sardine 230, mehl 15, oel 15
Uskumru Izgara | Gegrillte Makrele, Grilled mackerel | HFi | 0.75 | 1 Portion | makrele 260, olivenoel 5, zitrone 6, zwiebel 20
Uskumru Dolma | Gefüllte Makrele, Stuffed mackerel | HFi | 0.75 | 1 Portion | makrele 220, zwiebel 40, walnuss 15, rosinen 8, pinienkerne 6, zimt 1, olivenoel 10
Uskumru Fırın | Makrele aus dem Ofen | HFi | 0.75 | 1 Portion | makrele 260, kartoffel 100, tomate 40, zwiebel 20, olivenoel 8
Lüfer Izgara | Gegrillter Lüfer, Grilled bluefish | HFi | 0.75 | 1 Portion | fisch_fett 280, olivenoel 6, zitrone 6, salat 30
Lüfer Buğulama | Gedünsteter Lüfer | HFi | 0.8 | 1 Portion | fisch_fett 240, olivenoel 8, zitrone 8, petersilie 5, tomate 40
Palamut Izgara | Gegrillter Bonito | HFi | 0.75 | 1 Portion | fisch_fett 280, olivenoel 6, zitrone 6
Palamut Tava | Gebratener Bonito | HFi | 0.8 | 1 Portion | fisch_fett 250, mehl 15, oel 15
Palamut Pilaki | Bonito Pilaki | HFi | 0.85 | 1 Portion | fisch_fett 200, kartoffel 60, karotte 30, zwiebel 30, tomate 50, olivenoel 12, wasser 40
Kalkan Tava | Gebratener Steinbutt, Fried turbot | HFi | 0.8 | 1 Portion | fisch_mager 260, mehl 15, oel 15, zitrone 6
Barbunya Tava | Gebratene Rotbarbe, Fried red mullet | HFi | 0.8 | 1 Portion | fisch_mager 200, mehl 15, oel 15
Barbunya Izgara | Gegrillte Rotbarbe | HFi | 0.78 | 1 Portion | fisch_mager 220, olivenoel 6, zitrone 6
Mezgit Tava | Gebratener Merlan | HFi | 0.8 | 1 Portion | fisch_mager 220, mehl 15, oel 15
İstavrit Tava | Gebratene Holzmakrele | HFi | 0.8 | 1 Portion | fisch_mager 240, mehl 15, oel 15
Kılıç Şiş | Schwertfischspieß, Swordfish skewer | HFi | 0.78 | 1 Portion | schwertfisch 200, paprika 40, tomate 40, zwiebel 20, olivenoel 8, oregano 1
Kılıç Izgara | Gegrillter Schwertfisch | HFi | 0.78 | 1 Portion | schwertfisch 220, olivenoel 6, zitrone 8
Somon Izgara | Gegrillter Lachs, Grilled salmon | HFi | 0.78 | 1 Portion | lachs 200, olivenoel 6, zitrone 8, spargel 80
Somon Fırın | Lachs aus dem Ofen | HFi | 0.78 | 1 Portion | lachs 200, kartoffel 100, brokkoli 80, olivenoel 8, zitrone 8
Karides Güveç | Garnelen im Tontopf, Shrimp guvec | HFi | 0.85 | 1 Tontopf | garnele 150, tomate 60, paprika 30, kasar 30, butter 10, knoblauch 3, pilz 40
Karides Tava | Gebratene Garnelen | HFi | 0.85 | 1 Portion | garnele 180, mehl 15, oel 15, knoblauch 3, zitrone 5
Karides Sote | Garnelen-Sauté | HFi | 0.85 | 1 Portion | garnele 180, paprika 40, tomate 40, butter 12, knoblauch 4
Kalamar Tava | Frittierte Kalmare, Fried calamari | HFi | 0.88 | 1 Portion | kalmar 180, mehl 30, ei 15, oel 22, zitrone 5
Kalamar Izgara | Gegrillte Kalmare | HFi | 0.8 | 1 Portion | kalmar 220, olivenoel 8, zitrone 8, petersilie 4
Ahtapot Salatası | Oktopussalat, Octopus salad | SA | 1.0 | 1 Portion | oktopus 120, olivenoel 10, zitrone 10, zwiebel 20, petersilie 5
Ahtapot Izgara | Gegrillter Oktopus | HFi | 0.8 | 1 Portion | oktopus 220, olivenoel 10, zitrone 8
Balık Köfte | Fischfrikadellen, Fish kofta | HFi | 0.85 | 1 Portion | fisch_mager 150, paniermehl 20, ei 15, zwiebel 20, petersilie 5, oel 15
Balık Güveç | Fisch im Tontopf | HFi | 0.85 | 1 Tontopf | fisch_mager 160, tomate 60, paprika 40, kartoffel 60, zwiebel 20, olivenoel 10, wasser 40
Sazan Tava | Gebratener Karpfen | HFi | 0.8 | 1 Portion | karpfen 250, mehl 15, oel 15
Lakerda | Lakerda, Gesalzener Bonito, Cured bonito | V | 1.0 | 1 Portion | thunfisch 100, zwiebel 20, olivenoel 10, zitrone 5, dill 2
Çiroz | Çiroz, Getrocknete Makrele | V | 1.0 | 1 Portion | makrele 80, olivenoel 8, zwiebel 20
Hamsili Mısır Ekmeği | Hamsili Ekmek, Sardellen-Maisbrot | HFi | 0.9 | 1 Portion | sardelle 120, maismehl 60, zwiebel 20, oel 15, wasser 50
Ton Balıklı Makarna | Nudeln mit Thunfisch | T | 0.95 | 1 Portion | nudeln 70, thunfisch 60, tomate 60, zwiebel 20, olivenoel 10, wasser 140
"""
