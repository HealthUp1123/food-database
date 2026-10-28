CUISINE = 'tr'
TEXT = """
Su Böreği | Su Böreği Peynirli, Wasserbörek, Water borek | BO | 0.92 | 1 Stück | mehl 60, ei 30, beyaz_peynir 60, butter 20, milch 30, petersilie 4, oel 8
Sigara Böreği | Zigarettenbörek, Cigar borek, Peynirli Sigara Böreği | BO | 0.9 | 1 Portion (4 Stück) | yufka 70, beyaz_peynir 60, ei 15, petersilie 5, oel 28
Kıymalı Sigara Böreği | Zigarettenbörek mit Hack | BO | 0.9 | 1 Portion (4 Stück) | yufka 70, hack 60, zwiebel 20, ei 10, oel 28
Kol Böreği (Ispanaklı) | Ispanaklı Kol Böreği, Spinatbörek | BO | 0.9 | 1 Stück | yufka 90, spinat 120, beyaz_peynir 30, zwiebel 20, ei 25, butter 12, oel 10
Kol Böreği (Peynirli) | Peynirli Kol Böreği, Käsebörek | BO | 0.9 | 1 Stück | yufka 90, beyaz_peynir 80, ei 30, petersilie 5, butter 12, oel 10
Kol Böreği (Kıymalı) | Kıymalı Kol Böreği, Hackbörek | BO | 0.9 | 1 Stück | yufka 90, hack 70, zwiebel 30, ei 25, butter 12, oel 10
Kol Böreği (Patatesli) | Patatesli Kol Böreği, Kartoffelbörek | BO | 0.9 | 1 Stück | yufka 90, kartoffel 120, zwiebel 20, ei 25, butter 12, oel 10
Tepsi Böreği | Blechbörek, Tray borek | BO | 0.9 | 1 Stück | yufka 80, hack 60, zwiebel 20, ei 30, milch 40, oel 20, butter 8
Peynirli Tepsi Böreği | Käse-Blechbörek | BO | 0.9 | 1 Stück | yufka 80, beyaz_peynir 70, ei 30, milch 40, oel 20, butter 8, petersilie 4
Ispanaklı Tepsi Böreği | Spinat-Blechbörek | BO | 0.9 | 1 Stück | yufka 80, spinat 120, beyaz_peynir 30, ei 30, milch 30, oel 20
Patatesli Tepsi Böreği | Kartoffel-Blechbörek | BO | 0.9 | 1 Stück | yufka 80, kartoffel 120, zwiebel 20, ei 30, milch 30, oel 20
Paçanga Böreği | Paçanga, Pastırma-Käse-Börek | BO | 0.88 | 1 Portion (3 Stück) | yufka 60, pastirma 40, kasar 40, tomate 40, sivri 15, oel 28
Talaş Böreği | Talaş Börek, Sägemehl-Börek | BO | 0.9 | 1 Stück | blaetterteig 70, hack 60, zwiebel 20, ei 15, butter 5
Gül Böreği | Rosenbörek, Rose borek | BO | 0.9 | 1 Stück | yufka 80, hack 60, zwiebel 20, oel 15, ei 20
Rulo Börek | Rollbörek | BO | 0.9 | 1 Stück | yufka 80, beyaz_peynir 60, petersilie 5, ei 25, oel 15, butter 8
Muska Böreği | Muska Börek, Dreiecksbörek | BO | 0.9 | 1 Portion (3 Stück) | yufka 70, beyaz_peynir 50, petersilie 5, ei 15, oel 25
Çıtır Börek | Knusperbörek | BO | 0.9 | 1 Portion | yufka 80, beyaz_peynir 50, petersilie 5, oel 25
Bohça Böreği | Bohça Börek, Bündelbörek | BO | 0.9 | 1 Portion | yufka 80, hack 50, zwiebel 20, kartoffel 40, oel 22
Mantarlı Börek | Champignonbörek | BO | 0.9 | 1 Stück | yufka 90, pilz 120, beyaz_peynir 30, ei 25, butter 12, oel 10
Kabaklı Börek | Zucchinibörek | BO | 0.9 | 1 Stück | yufka 90, zucchini 150, beyaz_peynir 40, ei 25, oel 15
Pırasalı Börek | Lauchbörek | BO | 0.9 | 1 Stück | yufka 90, lauch 150, beyaz_peynir 30, ei 25, oel 15
Çiğ Börek | Çiğ Börek Kırım, Çibörek, Fried meat pastry crimean | BO | 0.88 | 1 Stück | mehl 90, hack 80, zwiebel 30, ei 10, oel 30
Arnavut Böreği | Albanian Borek | BO | 0.9 | 1 Stück | yufka 80, hack 60, zwiebel 20, ei 25, butter 10, oel 10
Tatar Böreği | Tatar Böreği, Kochteig-Hack-Börek | MA | 0.95 | 1 Portion | mehl 70, hack 60, zwiebel 25, joghurt 80, butter 10, tomatenmark 5, wasser 100
Peynirli Poğaça | Poğaça mit Käse, Cheese poğaça | G | 0.9 | 1 Stück | mehl 60, beyaz_peynir 30, butter 15, joghurt 15, ei 12, oel 8
Sade Poğaça | Poğaça, Einfache Poğaça | G | 0.9 | 1 Stück | mehl 60, butter 15, joghurt 20, ei 12, oel 12
Patatesli Poğaça | Poğaça mit Kartoffel | G | 0.9 | 1 Stück | mehl 55, kartoffel 40, butter 12, joghurt 15, ei 12, oel 8
Kıymalı Poğaça | Poğaça mit Hack | G | 0.9 | 1 Stück | mehl 55, hack 30, zwiebel 10, butter 12, joghurt 15, ei 12, oel 8
Zeytinli Poğaça | Poğaça mit Oliven | G | 0.9 | 1 Stück | mehl 55, olive 20, butter 12, joghurt 15, ei 12, oel 8
Açma | Açma, Weiches Hefegebäck, Turkish soft roll | G | 0.9 | 1 Stück | mehl 70, milch 20, butter 12, zucker 5, hefe 3, ei 8, oel 5
Simit | Simit, Sesamring, Turkish bagel | G | 0.92 | 1 Stück | mehl 90, sesam 12, pekmez 6, hefe 2, wasser 50
Gevrek | Gevrek Ankara, Sesamring knusprig | G | 0.9 | 1 Stück | mehl 75, sesam 10, pekmez 5, wasser 40
Kandil Simidi | Kandil Simit, Ring mit Gewürzen | G | 0.9 | 1 Stück | mehl 80, butter 12, zucker 5, gewuerz 1, sesam 8
Haşhaşlı Çörek | Mohnschnecke, Poppy seed bun | G | 0.9 | 1 Stück | mehl 80, mohn 20, butter 12, zucker 10, milch 25, hefe 3
Tahinli Çörek | Tahin-Schnecke, Tahini bun | G | 0.9 | 1 Stück | mehl 80, tahin 20, zucker 15, butter 8, milch 25, hefe 3
Çörek | Çörek, Hefezopf türkisch, Turkish sweet bread | G | 0.9 | 1 Stück | mehl 80, butter 15, zucker 10, ei 12, milch 25, hefe 3
Pişi | Pişi, Frittierte Hefeteigbällchen | G | 0.9 | 1 Portion (3 Stück) | mehl 80, hefe 3, joghurt 20, oel 28, wasser 30
Boyoz | Boyoz İzmir, Spanish-Jewish pastry | G | 0.9 | 1 Stück | mehl 90, oel 20, tahin 6
Bazlama | Bazlama, Fladenbrot Pfanne | BR | 0.93 | 1 Stück | mehl 100, joghurt 20, hefe 2, wasser 50
Katmer (Tuzlu) | Katmer herzhaft, Savory katmer | G | 0.9 | 1 Stück | mehl 80, kaymak 25, butter 20, pistazie 15, zucker 5
Mantı (Kayseri) | Kayseri Mantısı, Türkische Maultaschen mit Joghurt, Manti | MA | 0.95 | 1 Portion | mehl 70, hack 50, zwiebel 20, joghurt 100, butter 15, knoblauch 3, tomatenmark 4, pul_biber 1, wasser 60
Kıymalı Mantı | Mantı mit Hackfleisch, Meat manti | MA | 0.95 | 1 Portion | mehl 75, hack 55, zwiebel 20, joghurt 100, butter 12, tomatenmark 5, wasser 70
Çıtır Mantı | Gebackene Mantı, Crispy baked manti | MA | 0.88 | 1 Portion | mehl 70, hack 55, zwiebel 20, butter 15, tomatenmark 8, joghurt 50, oel 8, wasser 70
Su Mantısı | Gekochte Mantı, Boiled manti | MA | 0.95 | 1 Portion | mehl 75, hack 50, zwiebel 20, butter 12, joghurt 80, wasser 70
Peynirli Mantı | Mantı mit Käse | MA | 0.95 | 1 Portion | mehl 75, beyaz_peynir 50, petersilie 4, butter 12, joghurt 80, wasser 70
Kabak Mantısı | Mantı mit Zucchini | MA | 0.95 | 1 Portion | mehl 75, zucchini 80, beyaz_peynir 20, butter 12, joghurt 80, wasser 70
Ispanaklı Mantı | Mantı mit Spinat | MA | 0.95 | 1 Portion | mehl 75, spinat 80, beyaz_peynir 20, butter 12, joghurt 80, wasser 70
Hingel | Hingel Karadeniz, Türkische Teigtaschen Schwarzmeer | MA | 0.95 | 1 Portion | mehl 90, walnuss 20, butter 20, kasar 20, wasser 60
Gaziantep Mantısı (Katıklı Ekşili) | Antep Mantısı, Mantı mit Sauerampfer-Joghurt | MA | 0.95 | 1 Portion | mehl 70, lamm_hack 45, kichererbsen 25, joghurt 80, zitrone 10, butter 10, minze_trocken 1, wasser 100
Tokat Mantısı | Tokat Mantı | MA | 0.95 | 1 Portion | mehl 75, hack 50, zwiebel 20, joghurt 80, butter 12, wasser 70
Kuru Mantı | Getrocknete Mantı | MA | 0.95 | 1 Portion | mehl 80, hack 45, zwiebel 20, butter 12, joghurt 80, wasser 70
Cevizli Mantı | Mantı mit Walnuss | MA | 0.95 | 1 Portion | mehl 75, walnuss 30, zucker 5, butter 12, joghurt 60, wasser 60
Kıymalı Pide | Pide mit Hack, Turkish pide with minced meat | PI | 0.9 | 1 Pide | mehl 150, hack 100, zwiebel 30, tomate 30, sivri 20, butter 12, oel 8, wasser 70
Kuşbaşılı Pide | Pide mit Fleischwürfeln | PI | 0.9 | 1 Pide | mehl 150, rind 100, zwiebel 30, tomate 30, sivri 20, butter 12, oel 8, wasser 70
Kaşarlı Pide | Pide mit Käse, Cheese pide | PI | 0.9 | 1 Pide | mehl 150, kasar 100, butter 12, oel 5, wasser 70
Peynirli Pide | Pide mit Schafskäse | PI | 0.9 | 1 Pide | mehl 150, beyaz_peynir 100, petersilie 5, butter 12, wasser 70
Karışık Pide | Gemischte Pide, Mixed pide | PI | 0.9 | 1 Pide | mehl 150, hack 60, kasar 50, sucuk 30, ei 25, butter 12, wasser 70
Kaşarlı Yumurtalı Pide | Pide mit Käse und Ei | PI | 0.9 | 1 Pide | mehl 150, kasar 70, ei 50, butter 12, wasser 70
Yumurtalı Pide | Pide mit Ei | PI | 0.9 | 1 Pide | mehl 150, ei 100, butter 12, wasser 70
Sucuklu Pide | Pide mit Sucuk | PI | 0.9 | 1 Pide | mehl 150, sucuk 80, kasar 40, butter 8, wasser 70
Pastırmalı Pide | Pide mit Pastırma | PI | 0.9 | 1 Pide | mehl 150, pastirma 70, kasar 40, ei 25, butter 8, wasser 70
Kavurmalı Pide | Pide mit Kavurma | PI | 0.9 | 1 Pide | mehl 150, rind_fett 90, kasar 30, butter 8, wasser 70
Ispanaklı Pide | Pide mit Spinat | PI | 0.9 | 1 Pide | mehl 150, spinat 150, beyaz_peynir 50, butter 12, wasser 70
Tavuklu Pide | Pide mit Hähnchen | PI | 0.9 | 1 Pide | mehl 150, hahn_brust 100, kasar 40, paprika 30, butter 8, wasser 70
Mantarlı Pide | Pide mit Champignons | PI | 0.9 | 1 Pide | mehl 150, pilz 120, kasar 50, butter 10, wasser 70
Sebzeli Pide | Gemüsepide | PI | 0.9 | 1 Pide | mehl 150, paprika 40, tomate 50, pilz 50, mais 30, kasar 50, butter 8, wasser 70
Hamsili Pide | Pide mit Sardellen, Anchovy pide | PI | 0.9 | 1 Pide | mehl 150, sardelle 120, tomate 40, zwiebel 20, oel 12, wasser 70
Bafra Pidesi | Bafra Pide, Samsun Pide | PI | 0.9 | 1 Stück | mehl 140, butter 20, kasar 40, wasser 60
Trabzon Pidesi | Karadeniz Pide, Black Sea pide | PI | 0.9 | 1 Pide | mehl 150, kasar 70, ei 30, butter 20, wasser 70
Kapalı Pide | Geschlossene Pide | PI | 0.9 | 1 Pide | mehl 150, hack 80, kasar 40, zwiebel 20, butter 10, wasser 70
Lahmacun | Lahmacun, Türkische Pizza, Turkish pizza | PI | 0.88 | 1 Stück | mehl 80, lamm_hack 60, zwiebel 20, tomate 25, paprika 15, tomatenmark 6, petersilie 5, oel 5, wasser 40
Fındık Lahmacun | Mini Lahmacun, Small lahmacun | PI | 0.88 | 1 Portion (4 Stück) | mehl 80, lamm_hack 55, zwiebel 20, tomate 25, tomatenmark 6, petersilie 5, oel 5, wasser 40
Lahmacun Dürüm | Lahmacun Wrap, Lahmacun-Rolle mit Salat | PI | 0.9 | 1 Dürüm | mehl 80, lamm_hack 60, zwiebel 20, tomate 25, tomatenmark 6, salat 20, petersilie 10, zitrone 8
Antep Lahmacunu | Gaziantep Lahmacun | PI | 0.88 | 1 Stück | mehl 80, lamm_hack 65, zwiebel 20, tomate 25, paprikamark 8, petersilie 5, oel 5, wasser 40
Peynirli Gözleme | Gözleme mit Käse, Turkish crepe with cheese | PI | 0.9 | 1 Stück | mehl 90, beyaz_peynir 70, petersilie 5, oel 12, wasser 50
Patatesli Gözleme | Gözleme mit Kartoffeln | PI | 0.9 | 1 Stück | mehl 90, kartoffel 120, zwiebel 20, oel 12, wasser 50
Ispanaklı Gözleme | Gözleme mit Spinat | PI | 0.9 | 1 Stück | mehl 90, spinat 120, beyaz_peynir 30, zwiebel 15, oel 12, wasser 50
Kıymalı Gözleme | Gözleme mit Hack | PI | 0.9 | 1 Stück | mehl 90, hack 80, zwiebel 25, oel 12, wasser 50
Karışık Gözleme | Gemischte Gözleme | PI | 0.9 | 1 Stück | mehl 90, kartoffel 60, beyaz_peynir 40, spinat 40, oel 12, wasser 50
Kabaklı Gözleme | Gözleme mit Zucchini | PI | 0.9 | 1 Stück | mehl 90, zucchini 130, beyaz_peynir 30, oel 12, wasser 50
Sucuklu Gözleme | Gözleme mit Sucuk | PI | 0.9 | 1 Stück | mehl 90, sucuk 60, kasar 40, oel 8, wasser 50
Sac Böreği | Sac Böreği, Blechbörek vom Sac | BO | 0.9 | 1 Stück | mehl 90, beyaz_peynir 60, petersilie 5, butter 12, wasser 50
Peynirli Açma | Açma mit Käse | G | 0.9 | 1 Stück | mehl 70, beyaz_peynir 30, butter 12, ei 10, oel 5
Ramazan Pidesi | Pide-Brot, Ramadan flatbread | BR | 0.9 | 1 Stück | mehl 120, hefe 3, sesam 4, wasser 70
Tırnaklı Pide | Tırnaklı Pide, Fingernagel-Pide | BR | 0.9 | 1 Stück | mehl 130, hefe 3, wasser 80
Sandviç Tost | Karışık Tost, Turkish toasted sandwich | SN | 0.92 | 1 Tost | weissbrot 90, kasar 45, sucuk 30, tomate 20, butter 8
Kaşarlı Tost | Käsetoast | SN | 0.92 | 1 Tost | weissbrot 90, kasar 60, butter 8
Ayvalık Tostu | Ayvalık Tost, Ayvalik toast | SN | 0.92 | 1 Tost | ekmek 120, sucuk 40, salami 30, kasar 40, tomate 30, gewuerzgurke 20, ketchup 10, mayonnaise 10
Balık Ekmek | Fischbrötchen Istanbul, Fish sandwich Istanbul | SN | 0.95 | 1 Brot | ekmek 110, makrele 110, salat 20, zwiebel 20, zitrone 5, oel 6
Islak Hamburger | Nasser Burger, Wet burger Taksim | SN | 0.95 | 1 Burger | semmel 70, hack 60, tomatenmark 10, knoblauch 3, butter 5, zwiebel 10
Tantuni | Tantuni Mersin, Tantuni-Wrap | SN | 0.85 | 1 Wrap | lavas 90, rind 90, tomate 30, zwiebel 20, petersilie 5, oel 15, sumak_pulver 2
Midye Tava | Frittierte Muscheln, Fried mussels | SN | 0.9 | 1 Portion | muschel 120, mehl 25, bier 20, oel 22, mehl 10
"""
