CUISINE = 'tr'
TEXT = """
Fıstıklı Baklava | Baklava mit Pistazien, Pistachio baklava | SW | 0.95 | 1 Stück | yufka 14, butter 11, pistazie 12, zucker 14
Cevizli Baklava | Baklava mit Walnuss, Walnut baklava | SW | 0.95 | 1 Stück | yufka 14, butter 11, walnuss 12, zucker 14
Kuru Baklava | Trockene Baklava, Dry baklava | SW | 0.95 | 1 Stück | yufka 15, butter 12, walnuss 10, zucker 8
Havuç Dilimi Baklava | Möhrenscheiben Baklava, Carrot slice baklava | SW | 0.95 | 1 Stück | yufka 14, butter 11, walnuss 10, pistazie 5, zucker 14
Şöbiyet | Sobiyet, Gaziantep Şöbiyet, Cream-filled baklava | SW | 0.95 | 1 Stück | yufka 14, butter 11, kaymak 15, pistazie 8, zucker 14
Sütlü Nuriye | Sütlü Nuriye, Milk baklava | SW | 0.95 | 1 Stück | yufka 14, butter 8, milch 30, walnuss 10, zucker 15
Burma Kadayıf | Burma Kadayif, Rolled kadayif | SW | 0.95 | 1 Stück | kadayif 20, butter 12, pistazie 12, zucker 14
Tel Kadayıf | Kadayif Tel, Shredded wheat dessert | SW | 0.95 | 1 Portion | kadayif 40, butter 25, walnuss 20, zucker 35
Ekmek Kadayıfı | Ekmek Kadayifi, Bread kadayif with kaymak | SW | 0.95 | 1 Portion | weissbrot 70, zucker 35, kaymak 40, pistazie 5
Peynirli Künefe | Künefe, Kunafa with cheese, Kunefe | SW | 0.95 | 1 Portion | kadayif 70, butter 30, hellim 70, zucker 40, pistazie 8
Şekerpare | Sekerpare, Syrup cookies | SW | 0.95 | 1 Stück | mehl 14, griess 8, butter 8, ei 6, zucker 24
Revani | Revani, Grießkuchen mit Sirup, Semolina cake | SW | 0.95 | 1 Stück | griess 30, mehl 15, ei 25, zucker 45, joghurt 20, oel 5, zitrone 5
Sütlü Revani | Revani mit Milch | SW | 0.95 | 1 Stück | griess 30, mehl 15, ei 25, zucker 40, milch 50, oel 5
Tulumba | Tulumba, Fried dough in syrup | SW | 0.85 | 3 Stück | mehl 30, ei 20, butter 5, wasser 40, oel 18, zucker 40
Lokma | Lokma, Teigbällchen in Sirup, Fried dough balls | SW | 0.85 | 5 Stück | mehl 45, hefe 2, wasser 60, oel 20, zucker 40
Hanım Göbeği | Hanim Gobegi, Lady's navel | SW | 0.85 | 3 Stück | mehl 30, ei 20, butter 8, griess 5, oel 15, zucker 40
Dilber Dudağı | Dilber Dudagi, Lady's lips | SW | 0.85 | 3 Stück | mehl 30, ei 20, butter 8, oel 15, zucker 40
Kemalpaşa Tatlısı | Kemalpasa, Cheese dumpling dessert | SW | 0.9 | 3 Stück | lor 50, griess 20, mehl 10, ei 20, zucker 50
Ekmek Tatlısı | Brotpudding mit Kaymak, Bread pudding Turkish | SW | 0.95 | 1 Portion | weissbrot 70, zucker 40, kaymak 40, walnuss 8
Kazandibi | Kazandibi, Karamellisierter Milchpudding | PU | 1.0 | 1 Portion | milch 200, zucker 30, staerke 15, reismehl 5, butter 3
Tavuk Göğsü | Tavuk Gogsu, Hühnerbrust-Pudding, Chicken breast pudding | PU | 1.0 | 1 Portion | milch 200, hahn_brust 15, zucker 30, reismehl 12, zimt 1
Sütlaç | Sütlac, Milchreis türkisch, Rice pudding | PU | 1.0 | 1 Schälchen | milch 200, reis 15, zucker 25, staerke 5
Fırın Sütlaç | Gebackener Milchreis, Baked rice pudding | PU | 1.0 | 1 Schälchen | milch 200, reis 15, zucker 25, staerke 5, ei 10
Muhallebi | Muhallebi, Milchpudding, Milk pudding | PU | 1.0 | 1 Schälchen | milch 200, zucker 25, staerke 14, reismehl 4
Keşkül | Keskül, Mandelpudding, Almond pudding | PU | 1.0 | 1 Schälchen | milch 200, mandel 20, zucker 25, staerke 10, kokos 5
Supangle | Süpangle, Schokoladenpudding, Chocolate pudding | PU | 1.0 | 1 Schälchen | milch 200, kakao 12, zucker 25, staerke 14, butter 5
Aşure | Asure, Noah's pudding | PU | 1.0 | 1 Schälchen | bulgur 25, kichererbsen 15, bohnen_trocken 10, zucker 25, rosinen 10, aprikose_tr 10, feige_tr 10, walnuss 8, wasser 150
Zerde | Zerde, Safranreis-Dessert, Saffron rice dessert | PU | 1.0 | 1 Schälchen | reis 25, zucker 30, staerke 5, rosinen 8, pinienkerne 5, wasser 180
İrmik Helvası | Irmik Helvasi, Grießhelva, Semolina halva | SW | 0.92 | 1 Portion | griess 40, butter 22, zucker 30, milch 80, pinienkerne 5
Un Helvası | Un Helvasi, Mehl-Halva, Flour halva | SW | 0.92 | 1 Portion | mehl 40, butter 25, zucker 30, milch 80
Peynir Helvası | Peynir Helvasi, Käsehalva | SW | 0.92 | 1 Portion | mehl 40, butter 20, zucker 25, kasar 30, milch 60
Kabak Tatlısı | Kürbisdessert, Pumpkin dessert | SW | 1.0 | 1 Portion | kuerbis 200, zucker 50, walnuss 15, tahin 10
Ayva Tatlısı | Quittendessert, Quince dessert | SW | 1.0 | 1 Portion | quitte 200, zucker 45, kaymak 30, walnuss 8
Elma Tatlısı | Apfeldessert, Apple dessert | SW | 1.0 | 1 Portion | apfel 200, zucker 30, zimt 1, walnuss 10
İncir Tatlısı | Feigendessert, Fig dessert | SW | 1.0 | 1 Portion | feige_tr 120, zucker 20, walnuss 15, kaymak 20
Balkabağı Tatlısı | Balkabagi Tatlisi, Pumpkin sweet | SW | 1.0 | 1 Portion | kuerbis 200, zucker 45, walnuss 10
Pişmaniye | Pismaniye, Turkish cotton candy | SW | 1.0 | 1 Portion | mehl 15, butter 15, zucker 30, sesam 3
Lokum | Türkischer Honig, Turkish delight, Rahat Lokum | SW | 1.0 | 1 Stück | zucker 12, staerke 3, wasser 8
Fıstıklı Lokum | Lokum mit Pistazien | SW | 1.0 | 1 Stück | zucker 12, staerke 3, pistazie 4, wasser 8
Cevizli Sucuk | Walnuss-Sucuk, Churchkhela | SW | 1.0 | 1 Stück | walnuss 40, traube 60, mehl 10, zucker 5
Pestil | Pestil, Fruchtleder, Fruit leather | SW | 1.0 | 1 Stück | traube 80, mehl 10, walnuss 10
Cezerye | Cezerye, Möhrenkonfekt, Carrot confection | SW | 1.0 | 1 Stück | karotte 80, zucker 40, walnuss 15, kokos 5
Höşmerim | Hosmerim, Cheese dessert | SW | 0.95 | 1 Portion | lor 50, griess 20, zucker 40, butter 5
Güllaç | Gullac, Rosenblätter-Milchdessert, Ramadan dessert | PU | 1.0 | 1 Portion | mehl 25, milch 150, zucker 20, walnuss 15, granatapfel 20
Maraş Dondurması | Maras Dondurma, Maraş Eis, Maras ice cream | PU | 1.0 | 1 Kugel | milch 80, zucker 15, staerke 2, sahne 30
Trileçe | Trilece, Three milk cake | K | 1.0 | 1 Stück | ei 40, mehl 20, zucker 40, milch 80, sahne 30, kakao 3
Profiterol | Profiteroles, Profiterole | K | 1.0 | 1 Portion | mehl 25, ei 40, butter 20, milch 80, zucker 20, schokolade 25
Magnolia | Magnolia, Banana pudding dessert | PU | 1.0 | 1 Schälchen | milch 150, sahne 30, zucker 20, staerke 12, banane 40, weissbrot 10
Islak Kek | Islak Kek, Nasser Schokokuchen, Wet chocolate cake | K | 0.95 | 1 Stück | mehl 35, zucker 40, ei 30, milch 60, oel 20, kakao 8
Havuçlu Kek | Möhrenkuchen, Carrot cake | K | 0.9 | 1 Stück | mehl 40, karotte 40, zucker 30, ei 30, oel 25, walnuss 10, zimt 1
Portakallı Kek | Orangenkuchen, Orange cake | K | 0.9 | 1 Stück | mehl 45, zucker 30, ei 30, oel 20, orange 40
Limonlu Kek | Zitronenkuchen, Lemon cake | K | 0.9 | 1 Stück | mehl 45, zucker 30, ei 30, oel 20, zitrone 15
Elmalı Kek | Apfelkuchen türkisch, Apple cake Turkish | K | 0.9 | 1 Stück | mehl 40, apfel 60, zucker 30, ei 30, oel 20, zimt 1
Muzlu Kek | Bananenkuchen, Banana cake | K | 0.9 | 1 Stück | mehl 40, banane 60, zucker 30, ei 30, oel 20
Cevizli Kek | Walnusskuchen | K | 0.9 | 1 Stück | mehl 40, walnuss 20, zucker 30, ei 30, oel 20
Kakaolu Kek | Kakaokuchen, Cocoa cake | K | 0.9 | 1 Stück | mehl 40, kakao 8, zucker 35, ei 30, oel 22, milch 30
Browni | Brownie | K | 0.95 | 1 Stück | schokolade 30, butter 20, zucker 30, ei 25, mehl 20
Un Kurabiyesi | Mehlkekse, Flour cookies, Kurabiye | G | 0.95 | 2 Stück | mehl 25, butter 15, zucker 8
Pastane Kurabiyesi | Pastane-Kekse | G | 0.95 | 2 Stück | mehl 25, butter 15, zucker 8, mandel 4
Cevizli Kurabiye | Walnusskekse | G | 0.95 | 2 Stück | mehl 25, butter 15, zucker 8, walnuss 8
Fındıklı Kurabiye | Haselnusskekse | G | 0.95 | 2 Stück | mehl 25, butter 15, zucker 8, haselnuss 8
Sufle | Schokoladensoufflé, Chocolate souffle | K | 0.9 | 1 Portion | schokolade 40, butter 20, ei 40, zucker 20, mehl 10
Tahin Helvası | Tahin-Halva, Tahini halva | SW | 1.0 | 1 Portion | helva 50
Türk Çayı | Schwarzer Tee, Turkish tea, Cay | GT | 1.0 | 1 Tulpenglas | tee 100
Şekerli Çay | Tee mit Zucker | GT | 1.0 | 1 Glas | tee 100, zucker 8
Türk Kahvesi | Mokka, Turkish coffee | GT | 1.0 | 1 Tasse | tee 60
Şekerli Türk Kahvesi | Türkischer Kaffee mit Zucker | GT | 1.0 | 1 Tasse | tee 60, zucker 5
Sütlü Türk Kahvesi | Türkischer Kaffee mit Milch | GT | 1.0 | 1 Tasse | tee 60, milch 60, zucker 5
Salep | Sahlep, Salep drink, Hot sahlep | GT | 1.0 | 1 Tasse | milch 200, zucker 12, staerke 6, zimt 1
Boza | Boza, Fermentiertes Hirsegetränk | GT | 1.0 | 1 Glas | hirse 25, zucker 20, wasser 180
Ayran Glas | Ayran, Joghurtgetränk, Yogurt drink | GT | 1.0 | 1 Glas | joghurt 100, wasser 100, salz 1
Şalgam Suyu | Salgam, Fermentierter Rübensaft, Turnip juice | GT | 1.0 | 1 Glas | rote_bete 30, wasser 170, salz 2
Limonata | Limonade, Lemonade | GT | 1.0 | 1 Glas | zitrone 40, zucker 25, wasser 200
Ihlamur | Lindenblütentee, Linden tea | GT | 1.0 | 1 Tasse | tee 200
Adaçayı | Salbeitee, Sage tea | GT | 1.0 | 1 Tasse | tee 200
Kuşburnu Çayı | Hagebuttentee, Rosehip tea | GT | 1.0 | 1 Tasse | tee 200
Elma Çayı | Apfeltee, Apple tea | GT | 1.0 | 1 Glas | tee 200, zucker 15
Sıcak Çikolata | Heiße Schokolade, Hot chocolate | GT | 1.0 | 1 Tasse | milch 200, kakao 10, zucker 15
Vişne Suyu | Sauerkirschsaft, Sour cherry juice | GT | 1.0 | 1 Glas | sauerkirsche 100, zucker 20, wasser 130
Nar Suyu | Granatapfelsaft, Pomegranate juice | GT | 1.0 | 1 Glas | granatapfel 250
Portakal Suyu | Orangensaft, Orange juice | GT | 1.0 | 1 Glas | orange 250
Kefir | Kefir | GT | 1.0 | 1 Glas | joghurt 150, milch 50
Hoşaf | Hosaf, Trockenfrucht-Kompott | GT | 1.0 | 1 Schälchen | aprikose_tr 40, pflaume_tr 20, zucker 20, wasser 200
Meyan Şerbeti | Lakritz-Sherbet | GT | 1.0 | 1 Glas | zucker 15, wasser 200
Dibek Kahvesi | Dibek Kahvesi, Pistaziankaffee | GT | 1.0 | 1 Tasse | tee 60, milch 30, pistazie 6, zucker 5
Menengiç Kahvesi | Menengic Kahvesi, Terebinthenkaffee | GT | 1.0 | 1 Tasse | milch 150, pistazie 10, zucker 8
Beyaz Ekmek | Weißbrot türkisch, Turkish white bread | BR | 0.85 | 1 Scheibe | mehl 40, wasser 25, hefe 1, salz 1
Tam Buğday Ekmeği | Vollkornbrot türkisch, Whole wheat bread | BR | 0.85 | 1 Scheibe | mehl 15, vollkornbrot 30, wasser 20
Çavdar Ekmeği | Roggenbrot türkisch | BR | 0.95 | 1 Scheibe | roggenbrot 50
Lavaş Ekmeği | Lavash bread | BR | 1.0 | 1 Stück | lavas 60
Mısır Ekmeği | Maisbrot, Corn bread | BR | 0.9 | 1 Stück | maismehl 60, mehl 20, wasser 70, salz 1
Pide Ekmeği | Ramadan-Pide, Pide bread | BR | 0.9 | 1 Stück | mehl 100, wasser 60, hefe 2, sesam 3, ei 5
Yufka Ekmeği | Yufka-Fladen | BR | 1.0 | 1 Stück | yufka 60
Sac Ekmeği | Saç Ekmeği, Saj bread | BR | 1.0 | 1 Stück | mehl 80, wasser 50, salz 1
"""
