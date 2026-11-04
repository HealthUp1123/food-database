CUISINE = 'tr'
TEXT = """
Balık Buğulama | Gedünsteter Fisch, Steamed fish | HFi | 0.85 | 1 Portion | fisch_mager 180, tomate 60, sivri 30, zwiebel 25, olivenoel 10, zitrone 8, petersilie 5, wasser 40
Fırında Levrek | Wolfsbarsch aus dem Ofen, Baked sea bass | HFi | 0.8 | 1 Portion | wolfsbarsch 200, kartoffel 80, tomate 50, sivri 25, olivenoel 12, zitrone 8, oregano 1
Kağıtta Levrek | Wolfsbarsch in Pergament, Sea bass in parchment | HFi | 0.8 | 1 Portion | wolfsbarsch 200, tomate 40, sivri 20, olivenoel 8, zitrone 8, petersilie 4, butter 5
Tuzda Balık | Fisch in Salzkruste, Fish in salt crust | HFi | 0.78 | 1 Portion | fisch_mager 200, olivenoel 8, zitrone 8, oregano 1, salz 2
Domates Salatalık | Tomate und Gurke in Scheiben, Sliced tomato and cucumber | SA | 1.0 | 1 Teller | tomate 120, gurke 100, olivenoel 8, zitrone 6
Fıstıklı Yoğurt | Joghurt mit Pistazien, Pistachio yogurt | V | 1.0 | 1 Schälchen | joghurt 120, pistazie 18, honig 8
Dil Salatası | Zungensalat, Tongue salad | SA | 1.0 | 1 Teller | zunge 90, zwiebel 25, petersilie 10, olivenoel 10, zitrone 8, salat 30
Kabak Sıyırma | Zucchini-Joghurt-Meze, Zucchini yogurt meze | V | 0.75 | 1 Schälchen | zucchini 200, joghurt 90, knoblauch 4, dill 4, olivenoel 8
Közlenmiş Biber Yoğurtlu | Geröstete Paprika mit Joghurt, Roasted peppers with yogurt | V | 0.9 | 1 Schälchen | sivri 150, joghurt 80, knoblauch 4, olivenoel 8, tomatenmark 5
Antakya Humusu | Hatay-Hummus, Hatay hummus, Sıcak humus Antakya | V | 1.0 | 1 Schälchen | kichererbsen 100, tahin 18, zitrone 10, knoblauch 4, butter 12, pul_biber 2, kreuzkuemmel 1, olivenoel 6
Kremalı Tavuk Çorbası | Hühnercremesuppe, Cream of chicken soup | S | 0.9 | 1 Schüssel | hahn_brust 50, sahne 35, mehl 10, butter 8, milch 80, karotte 20, wasser 160
Kuzu Kuyruk Çorbası | Lammschwanzsuppe, Lamb tail soup | S | 0.9 | 1 Schüssel | schwanzfett 20, lamm 40, kichererbsen 40, zwiebel 25, knoblauch 3, pul_biber 1, wasser 240
Ekşili Çorba | Saure Linsensuppe, Sour lentil soup | S | 0.9 | 1 Schüssel | rote_linsen 35, bulgur 12, zwiebel 25, zitrone 18, minze_trocken 1, tomatenmark 6, butter 8, wasser 220
Çoban Kavurma | Shepherd's lamb saute, Hirtensauté vom Lamm | HF | 0.75 | 1 Portion | lamm 150, schwanzfett 12, sivri 40, tomate 50, zwiebel 40, pul_biber 1
Salçalı Makarna | Nudeln mit Tomatenmark, Pasta with tomato paste | T | 0.95 | 1 Teller | nudeln 75, tomatenmark 28, oel 12, knoblauch 3, paprikapulver 1, wasser 150
Özbek Pilavı | Usbekischer Pilaw, Uzbek pilaf | RP | 0.95 | 1 Teller | reis 65, lamm 70, karotte 55, zwiebel 30, kichererbsen 30, butter 12, knoblauch 3, wasser 140
Karışık Dolma | Gefülltes Gemüse mit Fleisch, Stuffed vegetables with meat, Karışık dolma etli | DO | 0.85 | 1 Portion | paprika 70, zucchini 60, aubergine 50, tomate 40, hack 55, reis 25, zwiebel 30, tomatenmark 6, olivenoel 10, wasser 50
Dalyan Köfte | Dalyan meatloaf, Gemüseauflauf mit Hack | KF | 0.85 | 1 Portion | hack 110, kartoffel 80, karotte 30, erbsen 25, ei 20, tomatenmark 8, oel 8, wasser 40
Zeytinyağlı Patlıcan | Aubergine in Olivenöl, Eggplant in olive oil | GZ | 0.85 | 1 Portion | aubergine 220, zwiebel 45, tomate 70, knoblauch 4, olivenoel 16, petersilie 5, wasser 40
Zeytinyağlı Havuç | Karotten in Olivenöl, Carrots in olive oil | GZ | 0.88 | 1 Portion | karotte 200, zwiebel 30, reis 15, olivenoel 14, zucker 4, wasser 50
Kaşık Salatası | Löffel-Salat, Spoon salad | SA | 1.0 | 1 Schüssel | tomate 100, gurke 70, zwiebel 25, sivri 30, petersilie 12, sumak_pulver 2, nar_eksisi 8, olivenoel 12
Turşu Salatası | Salat aus Salzgemüse, Pickle salad | SA | 1.0 | 1 Schüssel | gewuerzgurke 120, zwiebel 20, tomate 40, petersilie 8, olivenoel 10, essig 6
Nar Ekşili Salata | Salat mit Granatapfelsirup, Salad with pomegranate dressing | SA | 1.0 | 1 Schüssel | salat 60, tomate 80, gurke 50, zwiebel 20, nar_eksisi 12, olivenoel 12, sumak_pulver 1, walnuss 10
Tavuk İskender | Hähnchen-İskender, Chicken iskender | KB | 0.9 | 1 Teller | hahn_keule 130, ekmek 70, joghurt 70, tomate 55, butter 18, tomatenmark 8, paprika 20
Ali Paşa Kebabı | Ali-Paşa-Kebap, Ali Pasa kebab | KB | 0.85 | 1 Portion | hack 100, aubergine 140, tomate 70, sivri 30, zwiebel 25, joghurt 40, oel 12, tomatenmark 6
Pizza Karışık | Pizza gemischt, Mixed pizza | PZ | 0.92 | 1 Stück | x3_pizzateig 200, tomaten_dose 60, kasar 55, sucuk 35, sivri 25, pilz 30, olivenoel 6
Patso | Pommes im Brot, Fries in bread | SN | 0.9 | 1 Stück | ekmek 70, kartoffel 130, oel 14, ketchup 18, gewuerzgurke 25
Tavuklu Nohutlu Pilav | Reis mit Hähnchen und Kichererbsen, Chicken chickpea rice | RP | 0.95 | 1 Teller | reis 60, hahn_brust 70, kichererbsen 55, butter 10, wasser 130
Etli Nohutlu Pilav | Reis mit Fleisch und Kichererbsen, Beef chickpea rice | RP | 0.95 | 1 Teller | reis 60, rind 60, kichererbsen 55, butter 10, zwiebel 15, wasser 130
Et Haşlama | Gekochtes Rind mit Gemüse, Boiled beef with vegetables | HF | 0.85 | 1 Teller | rind 130, kartoffel 100, karotte 50, zwiebel 30, wasser 100
Sumaklı Soğan | Zwiebeln mit Sumach, Onions with sumac | SA | 1.0 | 1 Schälchen | zwiebel 90, sumak_pulver 4, petersilie 10, pul_biber 1, olivenoel 6
Kadayıflı Karides | Garnelen im Kadayıf, Shrimp in kadayif | SN | 0.85 | 1 Portion | garnele 110, kadayif 30, butter 14, zitrone 8
Pastırmalı Humus | Hummus mit Pastırma, Hummus with pastirma | V | 1.0 | 1 Schälchen | kichererbsen 90, tahin 16, zitrone 10, knoblauch 3, pastirma 30, olivenoel 8, butter 6
Pamuk Şeker | Zuckerwatte, Cotton candy | SN | 1.0 | 1 Portion | zucker 30
Macun Şekeri | Macun, Turkish fruit paste candy | SN | 0.9 | 1 Portion | zucker 32, pekmez 16, zitrone 5, wasser 10
Sultanahmet Köfte | Sultanahmet kofte, Istanbul Köfte | KF | 0.82 | 1 Portion | hack 140, paniermehl 15, zwiebel 20, ei 12, oel 8, tomate 40, sivri 20
Kasap Köfte | Metzger-Köfte, Butcher's kofte | KF | 0.8 | 1 Portion | hack 100, lamm_hack 40, schwanzfett 10, paniermehl 12, zwiebel 15, ei 10, oel 6
Ekşi Mayalı Ekmek | Sauerteigbrot, Sourdough bread | BR | 0.85 | 1 Stück | mehl 90, wasser 60, salz 2
Trabzon Ekmeği | Trabzon-Brot, Trabzon bread | BR | 0.88 | 1 Stück | mehl 100, wasser 58, hefe 2, salz 2, joghurt 15
Vakfıkebir Ekmeği | Vakfikebir-Brot, Vakfikebir bread | BR | 0.86 | 1 Stück | mehl 110, wasser 62, hefe 2, salz 2
Tandır Ekmeği | Tandir-Brot, Tandir bread | BR | 0.88 | 1 Stück | mehl 90, wasser 50, hefe 2, joghurt 20, salz 2
Gilik | Gilik-Fladen, Gilik flatbread | BR | 0.9 | 1 Stück | mehl 70, wasser 42, oel 6, salz 1
Hamursuz | Ungesaeuertes Fladenbrot, Unleavened flatbread | BR | 0.92 | 1 Stück | mehl 80, wasser 42, olivenoel 6, salz 1
Saray Böreği | Palace borek, Palast-Börek | BO | 0.92 | 1 Stück | yufka 70, beyaz_peynir 50, milch 40, ei 20, butter 12
Kandil Kurabiyesi | Kandil-Kekse, Kandil cookies | K | 0.95 | 3 Stück | mehl 40, butter 16, zucker 14, ei 10, sesam 4
Susamlı Kurabiye | Sesamkekse, Sesame cookies | K | 0.95 | 3 Stück | mehl 35, butter 16, zucker 12, sesam 10, ei 8
Kakaolu Kurabiye | Kakaokekse, Cocoa cookies | K | 0.95 | 3 Stück | mehl 35, butter 16, zucker 16, kakao 8, ei 8
Muffin | Muffin mit Vanille, Plain muffin | K | 0.92 | 1 Stück | mehl 40, zucker 18, ei 20, milch 25, oel 12
Çikolatalı Krep | Crepe mit Schokolade, Chocolate crepe | D | 0.9 | 2 Stück | mehl 40, milch 80, ei 30, kakao 8, zucker 12, butter 8, schokolade 15
Soğuk Baklava | Kalte Baklava mit Milch, Cold baklava with milk | SW | 0.95 | 1 Stück | yufka 45, butter 22, pistazie 16, zucker 28, milch 90
Midye Baklava | Muschel-Baklava, Mussel-shaped baklava | SW | 0.9 | 2 Stück | yufka 35, butter 16, pistazie 14, kaymak 18, zucker 22
Yassı Kadayıf | Flat kadayif, Flacher Kadayıf mit Kaymak | SW | 0.95 | 1 Stück | kadayif 45, butter 18, kaymak 25, pistazie 12, zucker 30, wasser 15
Koz Helva | Koz halva, Koz helvasi cevizli, Walnuss-Koz-Helva | SW | 0.92 | 1 Portion | mehl 40, butter 18, zucker 28, walnuss 16, milch 35
Kağıt Helvası | Waffel-Helva, Wafer halva | SW | 0.9 | 1 Portion | staerke 28, zucker 32, oel 10, milch 40
Yaz Helvası | Sommer-Helva, Summer halva | PU | 1.0 | 1 Schälchen | staerke 22, zucker 35, milch 160, kakao 4
Pekmez Helvası | Pekmez-Helva, Molasses halva | SW | 0.92 | 1 Portion | mehl 40, butter 18, pekmez 36, milch 40
Glorya Helvası | Glorya-Helva, Cocoa glorya halva | SW | 0.95 | 1 Portion | keks 40, kakao 10, butter 16, zucker 12, milch 20
Akide Şekeri | Akide-Bonbons, Akide candy | SN | 0.85 | 2 Stück | zucker 40, wasser 14, zitrone 2
Sade Dondurma | Milcheis, Milk ice cream | D | 1.0 | 1 Kugelbecher | milch 80, sahne 40, zucker 18, ei 15
Meyveli Dondurma | Fruchteis, Fruit ice cream | D | 1.0 | 1 Kugelbecher | milch 60, sahne 30, zucker 18, erdbeere 70
Çikolatalı Dondurma | Schokoladeneis, Chocolate ice cream | D | 1.0 | 1 Kugelbecher | milch 70, sahne 35, zucker 16, kakao 8, schokolade 12
Armut Tatlısı | Birne in Sirup, Poached pear | D | 0.9 | 1 Portion | birne 180, zucker 40, wasser 60, walnuss 8
Kaymaklı Lokum | Lokum mit Kaymak, Lokum with clotted cream | SW | 0.85 | 2 Stück | zucker 42, staerke 8, wasser 18, kaymak 20, zitrone 2
Pirinç Unu Muhallebisi | Reismehlpudding, Rice flour pudding | PU | 1.0 | 1 Schälchen | milch 200, reismehl 20, zucker 24
Mısır Unu Helvası | Maismehlhelva, Cornmeal halva | SW | 0.92 | 1 Portion | maismehl 40, butter 20, zucker 30, milch 80
Karalahana Kavurma | Gebratener Schwarzkohl, Sauteed collards | GZ | 0.8 | 1 Portion | karalahana 200, zwiebel 35, oel 14, maismehl 12, pul_biber 1
Kara Bulgur Pilavı | Schwarzer Bulgurpilaw, Dark bulgur pilaf | RP | 0.9 | 1 Teller | bulgur 65, karalahana 90, zwiebel 25, oel 10, tomatenmark 4, wasser 150
Rize Simidi | Rize-Simit, Rize simit | G | 0.9 | 1 Stück | mehl 75, milch 30, ei 15, butter 10, hefe 2, sesam 10, zucker 6
Hamsi Pilakisi | Sardellen-Pilaki, Anchovy pilaki | HFi | 0.85 | 1 Portion | sardelle 160, kartoffel 70, karotte 30, zwiebel 30, tomate 50, olivenoel 12, knoblauch 3, wasser 40
Sütlü Kabak | Kuerbis in Milch, Pumpkin in milk | PU | 0.95 | 1 Schälchen | kuerbis 180, milch 140, zucker 22, staerke 6
Kabak Pastası | Kuerbiskuchen, Pumpkin cake | K | 0.9 | 1 Stück | kuerbis 90, mehl 40, zucker 28, ei 25, oel 12, zimt 1
Bafra Nokulu | Nokul, Bafra walnut roll | G | 0.9 | 1 Stück | mehl 55, walnuss 22, zucker 16, butter 12, pekmez 8, hefe 2, wasser 28
Bandırma Kaz Tiridi | Gaense-Tirit, Goose tirit | HG | 0.9 | 1 Teller | gans 90, ekmek 55, zwiebel 25, butter 8, wasser 50
Kastamonu Banduma | Banduma, Kastamonu chicken with bread | HG | 0.9 | 1 Teller | hahn 100, ekmek 45, walnuss 15, joghurt 50, butter 10, paprikapulver 1, wasser 40
Ekşili Pilav | Saurer Pilaw, Sour pilaf | RP | 0.95 | 1 Teller | reis 60, zitrone 16, dill 6, fruehlingszwiebel 15, butter 8, wasser 130
Sumaklı Köfte | Sumach-Köfte, Sumac meatballs | KF | 0.82 | 1 Portion | hack 120, zwiebel 25, paniermehl 12, sumak_pulver 4, oel 8, petersilie 6
Peynirli İrmik Helvası | Griess-Helva mit Kaese, Cheese semolina halva | SW | 0.92 | 1 Portion | griess 40, lor 40, butter 16, zucker 24, milch 60
Sübye | Mandelmilch, Almond drink | GT | 1.0 | 1 Glas | mandel 30, wasser 200, zucker 12
Bakla Dolması | Gefuellte Dicke Bohnen, Stuffed broad beans | DO | 0.88 | 1 Portion | dicke_bohnen 180, reis 22, zwiebel 25, dill 6, olivenoel 12, zucker 3, wasser 40
Hibeş | Tahin-Dip Antalya, Tahini dip | SD | 1.0 | 1 Schälchen | tahin 45, zitrone 16, knoblauch 4, kreuzkuemmel 2, paprikapulver 2, olivenoel 8, wasser 30
Kerebiç | Kerebic, Mersin kerebic, Mersin Kerebiç | K | 0.95 | 2 Stück | griess 30, mehl 18, butter 14, zucker 20, pistazie 8, kaymak 16
Batırık | Batirik, Bulgur-Salat Tarsus | SA | 1.0 | 1 Portion | bulgur 45, tomate 90, zwiebel 25, petersilie 12, fruehlingszwiebel 15, olivenoel 12, nar_eksisi 8, wasser 35
Karakuş | Karakus, Mersin syrup pastry | SW | 0.95 | 1 Stück | griess 32, mehl 15, ei 18, zucker 36, walnuss 12, oel 8, zitrone 5
Tuzlu Yoğurt | Salzjoghurt, Salted yogurt | V | 0.72 | 1 Schälchen | suzme 170, salz 3
Arabaşı Hamuru | Arabasi-Teig, Arabasi dough | B | 0.95 | 1 Portion | mehl 80, wasser 55, ei 15, salz 1
Şebit | Sebit, Layered flatbread Konya | BR | 0.9 | 1 Stück | mehl 80, wasser 45, butter 14, joghurt 15
Bükme | Bukme, Gefalteter Yufka mit Käse | BO | 0.9 | 1 Stück | yufka 80, beyaz_peynir 50, butter 10, petersilie 5
Hangel | Hangel Erzurum, Teigtaschen Erzurum mit Joghurt | MA | 0.95 | 1 Portion | mehl 70, ei 15, wasser 35, joghurt 80, butter 12, knoblauch 3, tomatenmark 6
Hasuta | Hasuta, Mehlbrei Erzurum | PU | 0.95 | 1 Schälchen | mehl 28, butter 18, zucker 24, wasser 90
Herle | Herle, Bulgur mit Joghurt Erzurum | E | 0.92 | 1 Teller | bulgur 50, joghurt 80, kichererbsen 30, butter 10, wasser 110
Malatya Köftesi | Malatya-Köfte, Malatya kofte | KF | 0.9 | 1 Portion | bulgur 45, hack 50, zwiebel 20, tomatenmark 10, pul_biber 2, oel 8, wasser 40
Pöç | Poc, Lammschwanz geschmort | HF | 0.8 | 1 Portion | lamm 90, schwanzfett 25, zwiebel 40, kichererbsen 40, wasser 70
Gendime | Gendime, Weizenkoerner mit Lamm | E | 0.95 | 1 Teller | xa_weizen 45, lamm 55, kichererbsen_trocken 18, zwiebel 25, butter 8, wasser 170
Şıhtan | Sihtan, Dünnes Fladenbrot Erzurum | PI | 0.9 | 1 Stück | mehl 70, wasser 40, hack 40, zwiebel 15, butter 8
Ciğer Kavurma | Leberpfanne, Liver saute | HF | 0.8 | 1 Portion | leber 160, schwanzfett 15, zwiebel 40, sivri 30, pul_biber 2
Cantık | Cantik, Fleischfladen Kastamonu | PI | 0.9 | 1 Stück | mehl 100, hack 70, zwiebel 25, tomate 30, butter 8, wasser 50
Kestane Şekeri | Kandierte Maronen, Candied chestnuts, Bursa kestane sekeri | D | 0.9 | 1 Portion | kastanie 80, zucker 45, wasser 30
Bilecik Pazarı Köftesi | Bilecik-Köfte, Bilecik kofte | KF | 0.8 | 1 Portion | hack 130, paniermehl 12, zwiebel 20, ei 12, oel 8
Mengen Pilavı | Mengen-Pilaw, Mengen pilaf | RP | 0.95 | 1 Teller | reis 60, hahn 70, karotte 35, sivri 20, butter 12, mandel 8, wasser 130
Mafiş Tatlısı | Mafis, Sirupgebaeck Mafis | SW | 0.85 | 3 Stück | mehl 40, joghurt 18, ei 12, oel 16, zucker 32, wasser 12
"""
