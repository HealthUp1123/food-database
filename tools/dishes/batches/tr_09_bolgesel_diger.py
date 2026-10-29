CUISINE = 'tr'
TEXT = """
Papaz Yahnisi | Papaz Yahnisi, Lammeintopf mit Zwiebeln, Priest's stew | HF | 0.7 | 1 Portion | lamm 170, zwiebel 150, tomatenmark 8, oel 15, wasser 80
Bursa Kebabı | Bursa Kebap, Bursa kebab | KB | 0.75 | 1 Portion | lamm 140, tomate 80, butter 20, joghurt 60, lavas 60
Elbasan Tava | Elbasan Tava, Lamm im Joghurt-Eiguss, Elbasan tava | HF | 0.75 | 1 Portion | lamm 150, joghurt 80, ei 30, mehl 12, butter 15
Fırın Kebabı | Ofenkebab, Konya oven kebab | HF | 0.7 | 1 Portion | lamm 200, zwiebel 40, butter 15, tomate 40
Tepsi Kebabı | Hatay Tepsi Kebabı, Tray kebab | KB | 0.8 | 1 Portion | hack 140, tomate 80, sivri 40, zwiebel 40, oel 10, petersilie 5
Kuzu Tandır | Lammtandır, Tandoor lamb | HF | 0.7 | 1 Portion | lamm 280, butter 10, knoblauch 3
Saray Kebabı | Saray Kebap, Palace kebab | KB | 0.85 | 1 Portion | lamm_hack 150, kartoffel 100, butter 15, tomate 60, joghurt 40
Pehlivan Kebabı | Pehlivan Kebabı, Wrestler's kebab | KB | 0.8 | 1 Portion | lamm 170, paprika 60, tomate 60, zwiebel 40, olivenoel 12
Şiş Köfte | Sis Köfte, Skewered kofta | KF | 0.78 | 1 Portion | hack 150, zwiebel 20, petersilie 5, paniermehl 10, salz 1
Soğan Kebabı | Zwiebelkebab, Onion kebab | KB | 0.8 | 1 Portion | hack 120, zwiebel 120, tomatenmark 8, oel 10
Kuşbaşı Kebabı | Kuşbaşı Kebap, Cubed meat kebab | KB | 0.75 | 1 Portion | lamm 170, zwiebel 40, tomate 60, sivri 40, oel 10
Biber Kebabı | Paprika-Kebap | KB | 0.8 | 1 Portion | hack 120, sivri 120, tomate 60, oel 10
Enginar Kebabı | Artischocken-Kebap | KB | 0.8 | 1 Portion | rind 100, artischocke 120, zwiebel 30, tomatenmark 8, oel 12
Kabak Kebabı | Zucchini-Kebap | KB | 0.8 | 1 Portion | hack 120, zucchini 150, tomate 60, oel 12
İslim Kebabı | Islim Kebabı, Aubergine-Fleisch-Kebap | KB | 0.8 | 1 Portion | rind 100, aubergine 150, tomate 60, paprika 40, oel 15
Terbiyeli Köfte | Köfte mit Eigelb-Zitronensauce, Köfte with egg-lemon sauce | KF | 0.9 | 1 Portion | hack 120, reis 15, ei 30, mehl 15, zitrone 15, butter 10, wasser 200
Terbiyeli Tavuk | Hähnchen mit Eigelb-Zitronensauce | HG | 0.85 | 1 Portion | hahn_brust 150, ei 30, mehl 15, zitrone 15, butter 10, karotte 40, wasser 150
Etli Bulgur Köftesi | Gefüllte Bulgurbällchen mit Fleisch | KF | 0.95 | 1 Portion | bulgur 70, hack 70, zwiebel 40, mehl 10, oel 12, paprikamark 8
Yoğurtlu Bulgur Köftesi | Bulgurköfte mit Joghurt | KF | 0.95 | 1 Portion | bulgur 70, joghurt 100, hack 40, zwiebel 20, butter 10
Çibörek | Cibörek, Gefüllte Teigtasche gebraten, Fried meat pie | BO | 0.8 | 1 Stück | mehl 80, hack 80, zwiebel 20, oel 30, wasser 40
Kabak Kalye | Kabak Kalye, Zucchini-Gericht, Squash with tomatoes | GZ | 0.85 | 1 Portion | zucchini 200, tomate 80, zwiebel 30, oel 15
Pazı Kavurma | Mangold-Pfanne, Chard sauté | GZ | 0.85 | 1 Portion | mangold 200, zwiebel 40, reis 10, oel 15, tomatenmark 5
Ispanak Kavurma | Spinat-Pfanne | GZ | 0.85 | 1 Portion | spinat 220, zwiebel 40, oel 15, tomatenmark 5
Lahana Kavurma | Kohl-Pfanne | GZ | 0.85 | 1 Portion | weisskohl 220, zwiebel 40, tomatenmark 8, oel 15
Mercimek Yemeği | Linsengericht, Lentil stew | HH | 0.95 | 1 Portion | linsen 70, zwiebel 40, tomatenmark 8, oel 12, wasser 200
Kırmızı Mercimek Yemeği | Rote Linsen Gericht, Red lentil stew | HH | 0.95 | 1 Portion | rote_linsen 70, zwiebel 40, tomatenmark 8, oel 12, wasser 200
Yeşil Mercimek Yemeği | Grüne Linsen Gericht | HH | 0.95 | 1 Portion | linsen 70, zwiebel 40, tomate 50, oel 12, wasser 200
Etli Mercimek | Linsen mit Fleisch | HH | 0.95 | 1 Portion | linsen 60, rind 60, zwiebel 40, tomatenmark 8, oel 8, wasser 200
Barbunya Yemeği | Borlottibohnen Gericht, Cranberry bean stew | HH | 0.95 | 1 Portion | bohnen_trocken 60, zwiebel 40, tomatenmark 10, oel 12, wasser 250
Börülce Yemeği | Augenbohnen Gericht, Black-eyed pea dish | HH | 0.95 | 1 Portion | gruene_bohnen 120, zwiebel 30, tomate 60, oel 15
Börülce Salatası | Augenbohnensalat, Black-eyed pea salad | SA | 1.0 | 1 Portion | gruene_bohnen 120, zwiebel 20, petersilie 5, olivenoel 12, zitrone 10, knoblauch 2
Nohutlu Ispanak | Spinat mit Kichererbsen, Spinach with chickpeas | HH | 0.9 | 1 Portion | spinat 180, kichererbsen 80, zwiebel 40, tomatenmark 8, oel 12
Nohutlu Tavuk | Hähnchen mit Kichererbsen | HG | 0.9 | 1 Portion | hahn_brust 100, kichererbsen 80, zwiebel 30, tomate 60, oel 10
Bakla Ezmesi | Dicke-Bohnen-Paste | V | 0.95 | 1 Schälchen | dicke_bohnen 140, olivenoel 15, dill 5, zitrone 5, joghurt 30
Kabak Mücveri | Zucchini-Puffer, Zucchini fritters | HV | 0.8 | 4 Stück | zucchini 150, ei 40, mehl 30, beyaz_peynir 30, dill 5, oel 25
Patates Mücveri | Kartoffel-Puffer, Potato fritters | HV | 0.8 | 4 Stück | kartoffel 150, ei 40, mehl 20, zwiebel 20, oel 25
Ispanak Mücveri | Spinat-Puffer | HV | 0.8 | 4 Stück | spinat 150, ei 40, mehl 30, beyaz_peynir 30, oel 25
Havuç Mücveri | Möhren-Puffer | HV | 0.8 | 4 Stück | karotte 150, ei 40, mehl 30, joghurt 20, oel 25
Karnabahar Mücveri | Blumenkohl-Puffer | HV | 0.8 | 4 Stück | blumenkohl 150, ei 40, mehl 30, kasar 20, oel 25
Pırasa Mücveri | Lauch-Puffer | HV | 0.8 | 4 Stück | lauch 150, ei 40, mehl 30, beyaz_peynir 25, oel 25
Mercimek Mücveri | Linsen-Puffer | HV | 0.85 | 4 Stück | linsen 80, ei 30, mehl 20, zwiebel 20, oel 25
Peynirli Mücver | Käse-Puffer | HV | 0.8 | 4 Stück | zucchini 100, beyaz_peynir 60, ei 40, mehl 30, oel 25
Kumpir | Kumpir, Gefüllte Ofenkartoffel, Stuffed baked potato | SN | 0.9 | 1 Portion | kartoffel 350, butter 15, kasar 50, mais 30, gewuerzgurke 25, mayonnaise 15
Kokoreç Ekmek Arası | Kokoreç Sandwich | SN | 0.9 | 1 Sandwich | innereien 120, ekmek 100, tomate 30, oel 5
Köfte Ekmek | Köfte im Brot, Kofta sandwich | SN | 0.9 | 1 Sandwich | hack 100, ekmek 100, tomate 40, zwiebel 20, petersilie 5
Sucuk Ekmek | Sucuk im Brot, Sucuk sandwich | SN | 0.9 | 1 Sandwich | sucuk 80, ekmek 100, tomate 30
Ciğer Dürüm | Leber-Dürüm, Liver wrap | SN | 0.9 | 1 Dürüm | leber 120, lavas 70, zwiebel 30, tomate 30, sumak_pulver 1
Kuzu Şiş Dürüm | Lammspieß-Dürüm | SN | 0.9 | 1 Dürüm | lamm 130, lavas 70, tomate 40, zwiebel 20
Çiğ Köfte Dürüm | Çiğ Köfte Wrap | SN | 1.0 | 1 Dürüm | bulgur 40, tomatenmark 15, zwiebel 20, lavas 60, salat 30, oel 8, wasser 40
Tavuk Pilav | Hähnchen mit Reis Straßenstil, Chicken rice street food | SN | 0.9 | 1 Teller | reis 70, hahn_brust 80, kichererbsen 40, butter 8, wasser 140
Haşlanmış Mısır | Gekochter Mais, Boiled corn on the cob | SN | 1.0 | 1 Kolben | mais 200, butter 5
Közlenmiş Mısır | Gegrillter Mais | SN | 1.0 | 1 Kolben | mais 200
Közlenmiş Kestane | Geröstete Kastanien, Roasted chestnuts | SN | 1.0 | 1 Tüte | kastanie 120
Leblebi | Geröstete Kichererbsen, Roasted chickpeas | SN | 1.0 | 1 Handvoll | kichererbsen_trocken 40
Kaz Kızartması | Kars-Gänsebraten, Kars roast goose | HG | 0.7 | 1 Portion | gans 250, kartoffel 100, zwiebel 20
Keşkek | Keşkek, Weizen-Fleisch-Brei, Wheat and meat porridge | E | 0.95 | 1 Portion | bulgur 70, lamm 80, butter 15, wasser 250
Haşıl | Erzurum Haşıl, Erzurum Mehlsuppe | D | 1.0 | 1 Schüssel | mehl 30, butter 15, zucker 20, wasser 200
Murtuğa | Murtuğa, Van breakfast dish | FR | 0.9 | 1 Portion | mehl 40, butter 20, beyaz_peynir 40, ei 30
Kavut | Kavut, Geröstetes Getreide, Roasted grain porridge | FR | 1.0 | 1 Schüssel | mehl 40, honig 15, butter 8, wasser 100
Meftune | Meftune, Diyarbakır Lammgericht | HF | 0.75 | 1 Portion | lamm 120, aubergine 100, tomate 60, sivri 50, oel 15, zitrone 5
Sembusek | Sembusek, Mardin Teigtaschen | BO | 0.85 | 3 Stück | mehl 60, lamm_hack 60, zwiebel 20, oel 15
Kibbeh Mardin | Mardin-Kibbeh, Mardin kibbeh | KF | 0.85 | 2 Stück | bulgur 60, lamm_hack 70, zwiebel 30, walnuss 10, oel 15
Irok | Irok, Mardin Köfte | KF | 0.85 | 3 Stück | bulgur 60, hack 70, zwiebel 20, oel 15
Herise | Herise, Mardin Weizenbrei, Mardin harissa | E | 0.95 | 1 Portion | bulgur 70, lamm 80, butter 15, wasser 250
Mevlana Çorbası | Mevlana Çorbası, Konya Suppe | S | 0.95 | 1 Schüssel | linsen 25, bulgur 15, zwiebel 20, tomatenmark 8, butter 10, wasser 250
Mısır Çorbası | Maissuppe, Corn soup | S | 0.95 | 1 Schüssel | mais 80, milch 100, butter 10, mehl 12, wasser 150
Kayseri Yağlaması | Yağlama, Kayseri flatbread with meat | PI | 0.9 | 1 Portion | mehl 100, hack 80, zwiebel 30, joghurt 60, butter 15, tomate 40
Laz Böreği | Laz Böreği, Laz pastry dessert | SW | 0.95 | 1 Portion | yufka 40, milch 120, zucker 25, staerke 10, butter 12, ei 15
Mantarlı Tavuk Sote | Hähnchen-Pilz-Sauté | HG | 0.85 | 1 Portion | hahn_brust 140, pilz 100, paprika 40, zwiebel 20, oel 12
Tavuk Kebabı | Hähnchenkebab | HG | 0.8 | 1 Portion | hahn_brust 180, joghurt 30, tomate 40, paprika 40, oel 8
Kremalı Tavuk | Hähnchen in Sahnesauce | HG | 0.85 | 1 Portion | hahn_brust 140, sahne 60, pilz 40, butter 8, zwiebel 15
Tavuk Sarma | Hähnchenröllchen, Chicken rolls | HG | 0.85 | 1 Portion | hahn_brust 150, kasar 30, schinken 25, oel 10
Tavuk Tantuni | Hähnchen-Tantuni | SN | 0.9 | 1 Dürüm | hahn_brust 100, lavas 70, tomate 40, petersilie 5, sumak_pulver 1, oel 10
Tavuk Ciğeri Sote | Hähnchenleber-Sauté | HG | 0.8 | 1 Portion | huhn_leber 150, zwiebel 40, oel 12, paprika 20
Fırında Sebzeli Tavuk | Hähnchen mit Ofengemüse | HG | 0.8 | 1 Portion | hahn_keule 200, kartoffel 100, karotte 50, paprika 40, oel 10
Fırında Patlıcan | Ofenaubergine | GZ | 0.8 | 1 Portion | aubergine 250, olivenoel 12, knoblauch 3, tomate 40
Fırında Kabak | Ofenzucchini | GZ | 0.85 | 1 Portion | zucchini 250, olivenoel 10, knoblauch 3
Fırında Karnabahar | Ofenblumenkohl | GZ | 0.85 | 1 Portion | blumenkohl 250, olivenoel 10, kasar 20
Fırında Brokoli | Ofenbrokkoli | GZ | 0.85 | 1 Portion | brokkoli 250, olivenoel 10, kasar 20
Kaşarlı Mantar | Pilze mit Käse überbacken | GZ | 0.85 | 1 Portion | pilz 200, kasar 50, butter 10
Közlenmiş Patlıcan | Gegrillte Aubergine | GZ | 0.75 | 1 Portion | aubergine 250, olivenoel 8
Közlenmiş Domates Biber | Gegrillte Tomaten und Paprika | GZ | 0.8 | 1 Portion | tomate 150, sivri 100, olivenoel 8
Haşlanmış Sebze | Gekochtes Gemüse | GZ | 1.0 | 1 Portion | karotte 80, brokkoli 80, blumenkohl 80, zucchini 60
Soslu Kabak | Zucchini mit Sauce | GZ | 0.85 | 1 Portion | zucchini 200, joghurt 60, knoblauch 3, oel 10
Kızarmış Patlıcan Domates Soslu | Gebratene Aubergine in Tomatensoße | GZ | 0.8 | 1 Portion | aubergine 200, tomate 100, knoblauch 3, oel 25
Zeytinyağlı Barbunya | Barbunya Pilaki Olivenöl, Barbunya in olive oil | HH | 0.9 | 1 Portion | bohnen_trocken 55, zwiebel 40, karotte 30, tomate 60, olivenoel 15, wasser 200
Zeytinyağlı Nohut | Kichererbsen in Olivenöl | HH | 0.9 | 1 Portion | kichererbsen_trocken 50, zwiebel 40, tomate 60, olivenoel 15, wasser 200
Zeytinyağlı Mercimek | Linsen in Olivenöl | HH | 0.9 | 1 Portion | linsen 60, zwiebel 40, karotte 30, olivenoel 15, wasser 200
"""
