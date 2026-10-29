CUISINE = 'de'
TEXT = """
Apfelkuchen | Versunkener Apfelkuchen, Apple cake German | K | 0.92 | 1 Stück | mehl 50, butter 30, zucker 35, ei 30, apfel 120, milch 15
Gedeckter Apfelkuchen | Apfelkuchen mit Teigdecke, Covered apple pie | K | 0.92 | 1 Stück | mehl 60, butter 35, zucker 35, ei 25, apfel 150, rosinen 10, zimt 1
Apfelstrudel | Apfelstrudel, Apple strudel | K | 0.92 | 1 Stück | yufka 40, apfel 150, butter 15, zucker 20, rosinen 15, semmel 10, zimt 1
Topfenstrudel | Quarkstrudel, Quark strudel | K | 0.92 | 1 Stück | yufka 40, quark 100, ei 25, zucker 25, butter 12, rosinen 10
Bienenstich | Bienenstich, Bee sting cake | K | 0.92 | 1 Stück | mehl 45, butter 25, zucker 30, mandel 20, milch 90, staerke 10, ei 20, sahne 30
Streuselkuchen | Streuselkuchen, Crumble cake | K | 0.92 | 1 Stück | mehl 60, butter 40, zucker 35, hefe 2, milch 30, ei 15
Butterkuchen | Butterkuchen mit Mandeln, Butter cake | K | 0.92 | 1 Stück | mehl 60, butter 40, zucker 25, hefe 2, milch 30, mandel 10, ei 15
Käsekuchen | Käsekuchen, German cheesecake, Quarkkuchen | K | 0.95 | 1 Stück | quark 120, ei 40, zucker 35, butter 20, mehl 30, staerke 8, milch 30
Russischer Zupfkuchen | Zupfkuchen, Russian pluck cake | K | 0.95 | 1 Stück | mehl 40, butter 30, zucker 35, kakao 8, quark 100, ei 35, staerke 8
Schwarzwälder Kirschtorte | Schwarzwälder Kirsch, Black Forest cake | K | 1.0 | 1 Stück | mehl 25, ei 40, zucker 30, kakao 6, sahne 90, sauerkirsche 70, schokolade 10
Sachertorte | Sachertorte, Sacher cake | K | 0.95 | 1 Stück | schokolade 40, butter 30, zucker 35, ei 45, mehl 20, marmelade 25
Frankfurter Kranz | Frankfurter Kranz, Frankfurt crown cake | K | 1.0 | 1 Stück | mehl 30, butter 45, zucker 40, ei 40, haselnuss 15, marmelade 15
Donauwelle | Donauwelle, Danube wave cake | K | 0.95 | 1 Stück | mehl 45, butter 40, zucker 35, ei 40, sauerkirsche 40, milch 60, staerke 10, kakao 6, schokolade 12
Marmorkuchen | Rührkuchen, Marble cake | K | 0.95 | 1 Stück | mehl 50, butter 35, zucker 40, ei 40, milch 15, kakao 6
Sandkuchen | Sandkuchen, Sand cake | K | 0.95 | 1 Stück | mehl 35, staerke 15, butter 40, zucker 40, ei 40
Gugelhupf | Gugelhupf, Bundt cake | K | 0.95 | 1 Stück | mehl 50, butter 35, zucker 40, ei 40, rosinen 15, milch 20
Eierlikörkuchen | Eierlikörkuchen, Egg liqueur cake | K | 0.95 | 1 Stück | mehl 50, ei 40, zucker 40, oel 25, milch 15
Mohnkuchen | Mohnkuchen, Poppy seed cake | K | 0.95 | 1 Stück | mehl 40, butter 25, zucker 35, mohn 35, milch 60, ei 25
Zwetschgenkuchen | Pflaumenkuchen, Plum cake, Zwetschgendatschi | K | 0.92 | 1 Stück | mehl 55, butter 25, zucker 25, hefe 2, milch 20, pflaume 150
Rhabarberkuchen | Rhabarberkuchen mit Baiser, Rhubarb cake | K | 0.95 | 1 Stück | mehl 50, butter 30, zucker 40, ei 40, rhabarber 130
Erdbeerkuchen | Erdbeertorte, Strawberry cake | K | 1.0 | 1 Stück | mehl 30, ei 30, zucker 35, erdbeere 120, staerke 8
Obstkuchen | Obsttorte, Fruit tart | K | 1.0 | 1 Stück | mehl 35, butter 20, zucker 30, ei 25, pfirsich 60, erdbeere 40, staerke 8
Kirschkuchen | Kirschkuchen vom Blech, Cherry cake | K | 0.95 | 1 Stück | mehl 50, butter 30, zucker 35, ei 40, sauerkirsche 100
Nusskuchen | Nusskuchen, Nut cake | K | 0.95 | 1 Stück | mehl 35, haselnuss 30, butter 30, zucker 35, ei 40
Baumkuchen | Baumkuchen, Tree cake | K | 1.0 | 1 Stück | mehl 30, butter 30, zucker 25, ei 40, marzipan 20, schokolade 10
Christstollen | Stollen, Dresdner Stollen, Christmas stollen | K | 0.95 | 1 Scheibe | mehl 50, butter 25, zucker 12, rosinen 30, mandel 10, marzipan 10, zimt 1
Marzipanstollen | Marzipanstollen, Stollen mit Marzipan | K | 0.95 | 1 Scheibe | mehl 45, butter 25, zucker 12, rosinen 25, marzipan 25
Quarkstollen | Quarkstollen, Quark stollen | K | 0.95 | 1 Scheibe | mehl 50, quark 30, butter 25, zucker 20, rosinen 25
Lebkuchen | Nürnberger Lebkuchen, Gingerbread | G | 1.0 | 1 Stück | mehl 20, honig 15, zucker 12, mandel 15, haselnuss 10, lebkuchen_gewuerz 1
Elisenlebkuchen | Elisen Lebkuchen | G | 1.0 | 1 Stück | mandel 20, haselnuss 15, zucker 20, honig 8, ei 10
Spekulatius | Spekulatius, Speculoos | G | 1.0 | 3 Stück | mehl 15, butter 8, zucker 8, zimt 1
Zimtsterne | Zimtsterne, Cinnamon stars | G | 1.0 | 3 Stück | mandel 15, zucker 12, eiweiss 10, zimt 1
Vanillekipferl | Vanillekipferl, Vanilla crescents | G | 1.0 | 3 Stück | mehl 15, butter 10, mandel 7, zucker 7
Butterplätzchen | Plätzchen, Butter cookies | G | 1.0 | 3 Stück | mehl 20, butter 12, zucker 8, ei 3
Kokosmakronen | Kokosmakronen, Coconut macaroons | G | 1.0 | 3 Stück | kokos 20, zucker 15, eiweiss 15
Pfeffernüsse | Pfeffernüsse, Spiced cookies | G | 1.0 | 5 Stück | mehl 15, honig 10, zucker 8, lebkuchen_gewuerz 1
Printen | Aachener Printen | G | 1.0 | 1 Stück | mehl 20, honig 12, zucker 10, lebkuchen_gewuerz 1
Dominosteine | Dominosteine, Domino stones | G | 1.0 | 3 Stück | marzipan 15, marmelade 15, lebkuchen_gewuerz 1, schokolade 20, mehl 15
Linzer Torte | Linzer Torte, Linz tart | K | 0.95 | 1 Stück | mehl 35, butter 30, zucker 20, haselnuss 25, marmelade 40
Marzipankartoffeln | Marzipankartoffeln, Marzipan potatoes | G | 1.0 | 3 Stück | marzipan 35, kakao 3
Berliner | Berliner Pfannkuchen, Krapfen, Doughnut | G | 0.95 | 1 Stück | mehl 55, milch 30, ei 15, butter 10, zucker 15, oel 15, marmelade 20
Krapfen | Faschingskrapfen, Fasnachtsküchle, Doughnut Bavarian | G | 0.95 | 1 Stück | mehl 55, milch 30, ei 15, butter 10, zucker 12, oel 15, marmelade 20
Windbeutel | Windbeutel, Cream puff | G | 1.0 | 1 Stück | mehl 20, butter 15, ei 30, sahne 70, zucker 10
Quarkbällchen | Quarkbällchen, Quark balls | G | 0.9 | 4 Stück | quark 60, mehl 40, ei 25, zucker 20, oel 15
Quarkkeulchen | Quarkkeulchen, Quark pancakes | G | 0.9 | 3 Stück | quark 90, kartoffel 100, mehl 30, ei 25, zucker 15, butter 15, rosinen 10
Hefezopf | Hefezopf, Butterzopf, Sweet braided bread | G | 0.95 | 1 Scheibe | mehl 50, butter 15, zucker 10, milch 25, ei 10, hefe 2, rosinen 10
Rosinenbrötchen | Rosinenbrötchen, Raisin roll | G | 0.95 | 1 Brötchen | mehl 50, milch 25, butter 8, zucker 8, rosinen 20, hefe 2
Franzbrötchen | Franzbrötchen, Hamburg cinnamon roll | G | 0.95 | 1 Stück | mehl 55, butter 22, zucker 15, zimt 2, milch 25, hefe 2
Streuselschnecke | Streuselschnecke, Streusel snail | G | 0.95 | 1 Stück | mehl 55, butter 25, zucker 20, milch 25, hefe 2, ei 10
Mohnschnecke | Mohnschnecke, Poppy seed pastry | G | 0.95 | 1 Stück | mehl 50, mohn 25, butter 15, zucker 20, milch 40, hefe 2
Nussschnecke | Nussschnecke, Nut roll | G | 0.95 | 1 Stück | mehl 50, haselnuss 20, butter 15, zucker 20, milch 25, hefe 2
Puddingbrezel | Puddingbrezel, Custard pretzel | G | 0.95 | 1 Stück | mehl 60, butter 20, zucker 10, milch 60, staerke 8, hefe 2
Amerikaner | Amerikaner, Glazed cake bun | G | 0.95 | 1 Stück | mehl 45, zucker 35, ei 20, milch 20, butter 15, staerke 5
Mandelhörnchen | Mandelhörnchen, Almond croissant cookies | G | 1.0 | 1 Stück | mandel 25, zucker 15, marzipan 10, schokolade 5
Nussecken | Nussecken, Nut triangles | G | 1.0 | 1 Stück | mehl 20, butter 20, zucker 15, haselnuss 20, marmelade 8, schokolade 8
Eierschecke | Eierschecke, Saxon egg cake | K | 0.95 | 1 Stück | mehl 35, butter 30, zucker 35, quark 60, ei 50, milch 60, staerke 10
Schneeballen | Schneeballen, Snowballs pastry | G | 0.9 | 1 Stück | mehl 50, butter 15, ei 20, zucker 15, oel 20
Florentiner | Florentiner, Florentines | G | 1.0 | 2 Stück | mandel 20, zucker 12, sahne 10, schokolade 15, honig 5
Rote Grütze | Rote Grütze mit Vanillesoße, Red berry pudding | PU | 1.0 | 1 Schälchen | himbeere 60, erdbeere 50, sauerkirsche 50, zucker 25, staerke 10, wasser 80
Vanillepudding | Vanillepudding, Vanilla pudding | PU | 1.0 | 1 Schälchen | milch 200, zucker 20, vanillepudding_pulver 15
Schokopudding | Schokoladenpudding, Chocolate pudding German | PU | 1.0 | 1 Schälchen | milch 200, zucker 20, kakao 8, vanillepudding_pulver 12
Grießpudding | Grießpudding, Semolina pudding | PU | 1.0 | 1 Schälchen | milch 200, griess 20, zucker 15, ei 10
Vanillesoße | Vanillesauce, Vanilla sauce | SD | 1.0 | 1 Portion | milch 100, zucker 10, staerke 6, ei 10
Götterspeise | Wackelpudding, Jelly dessert | PU | 1.0 | 1 Schälchen | wasser 150, zucker 20, gelatine 6
Mousse au Chocolat | Schokoladenmousse, Chocolate mousse | PU | 1.0 | 1 Schälchen | schokolade 50, sahne 70, ei 40, zucker 10
Bayerische Creme | Bayerische Crème, Bavarian cream | PU | 1.0 | 1 Schälchen | milch 100, sahne 80, ei 30, zucker 20, gelatine 4
Quarkspeise | Quarkspeise mit Früchten, Quark dessert | PU | 1.0 | 1 Schälchen | quark 150, sahne 30, zucker 20, erdbeere 50
Bratapfel | Bratapfel mit Marzipan, Baked apple | D | 0.9 | 1 Apfel | apfel 200, marzipan 20, rosinen 10, mandel 8, butter 5, zimt 1
Bratapfel mit Vanillesoße | Bratapfel Vanillesoße | D | 0.9 | 1 Apfel | apfel 200, marzipan 15, rosinen 10, butter 5, milch 80, zucker 10, staerke 5
Apfel im Schlafrock | Apfel im Schlafrock, Apple in puff pastry | D | 0.95 | 1 Stück | apfel 120, blaetterteig 70, zucker 10, rosinen 10, ei 8
Armer Ritter | Arme Ritter, German toast | D | 0.9 | 2 Scheiben | weissbrot 70, milch 80, ei 50, butter 15, zucker 15, zimt 1
Semmelschmarrn | Semmelschmarrn, Bread schmarrn | D | 0.9 | 1 Portion | semmel 80, milch 100, ei 60, butter 15, zucker 15, rosinen 15
Germknödel | Germknödel mit Mohn, Yeast dumpling with plum jam | D | 0.95 | 1 Stück | mehl 90, milch 40, hefe 3, butter 15, zucker 10, marmelade 40, mohn 10
Zwetschgenknödel | Pflaumenknödel, Plum dumplings | D | 1.0 | 3 Stück | kartoffel 150, mehl 50, ei 15, pflaume 90, semmel 20, butter 20, zucker 15, zimt 1
Marillenknödel | Marillenknödel, Apricot dumplings | D | 1.0 | 3 Stück | kartoffel 150, mehl 50, ei 15, aprikose 90, semmel 20, butter 20, zucker 15
Topfenknödel | Quarkknödel, Quark dumplings | D | 1.0 | 3 Stück | quark 120, semmel 50, ei 30, butter 20, zucker 15
Hefeklöße mit Vanillesoße | Hefeklöße, Yeast dumplings | D | 0.95 | 2 Stück | mehl 100, milch 50, hefe 3, butter 12, zucker 10, ei 15
Vanilleeis mit heißen Himbeeren | Heiße Liebe, Hot love dessert | D | 1.0 | 1 Portion | milch 70, sahne 50, zucker 20, himbeere 100, staerke 3
Spaghettieis | Spaghetti-Eis, Spaghetti ice cream | D | 1.0 | 1 Portion | milch 80, sahne 60, zucker 25, erdbeere 60, kokos 5
Eisbecher | Eisbecher mit Sahne, Ice cream sundae | D | 1.0 | 1 Becher | milch 100, sahne 80, zucker 25, erdbeere 60
Obstsalat | Obstsalat, Fruit salad | D | 1.0 | 1 Schüssel | apfel 80, banane 60, orange 80, traube 50, zitrone 5
Apfelschorle | Apfelsaftschorle, Apple spritzer | GT | 1.0 | 1 Glas | apfel 125, wasser 125, zucker 5
Apfelsaft | Apfelsaft naturtrüb, Apple juice | GT | 1.0 | 1 Glas | apfel 250, zucker 10
Orangenschorle | Orangensaftschorle | GT | 1.0 | 1 Glas | orange 125, wasser 125
Kirschsaft | Sauerkirschsaft | GT | 1.0 | 1 Glas | sauerkirsche 150, zucker 20, wasser 100
Holundersaft | Holunderblütensirup Getränk, Elderflower drink | GT | 1.0 | 1 Glas | zucker 25, wasser 200, zitrone 5
Spezi | Spezi, Cola-Orange | GT | 1.0 | 1 Glas | zucker 25, wasser 200, orange 20
Colamix | Cola Mix, Cola with orange | GT | 1.0 | 1 Glas | zucker 25, wasser 200
Malzbier | Malzbier, Malt beer | GT | 1.0 | 1 Flasche | zucker 20, wasser 180, hirse 5
Pils | Pils 0,5 l, Pilsner, Bier | GT | 1.0 | 1 Glas | bier 500
Weizenbier | Hefeweizen, Weissbier, Wheat beer | GT | 1.0 | 1 Glas | bier 500
Radler | Radler, Alsterwasser, Shandy | GT | 1.0 | 1 Glas | bier 250, zucker 15, zitrone 10, wasser 250
Kölsch | Kölsch 0,2 l | GT | 1.0 | 1 Stange | bier 200
Weißwein trocken | Weißwein, White wine | GT | 1.0 | 1 Glas | wein_weiss 200
Rotwein trocken | Rotwein, Red wine | GT | 1.0 | 1 Glas | wein_rot 200
Weinschorle | Weinschorle sauer, Wine spritzer | GT | 1.0 | 1 Glas | wein_weiss 125, wasser 125
Glühwein | Glühwein, Mulled wine | GT | 1.0 | 1 Tasse | wein_rot 200, zucker 20, zimt 1, orange 10
Kaffee mit Milch | Milchkaffee, Coffee with milk | GT | 1.0 | 1 Tasse | tee 150, milch 50
Kaffee mit Milch und Zucker | Kaffee Milch Zucker | GT | 1.0 | 1 Tasse | tee 150, milch 30, zucker 8
Latte Macchiato | Latte Macchiato | GT | 1.0 | 1 Glas | milch 200, tee 30
Cappuccino | Cappuccino | GT | 1.0 | 1 Tasse | milch 120, tee 40
Kakao | Heiße Schokolade, Kakao mit Milch, Hot cocoa | GT | 1.0 | 1 Tasse | milch 200, kakao 8, zucker 12
Früchtetee | Früchtetee, Fruit tea | GT | 1.0 | 1 Tasse | tee 250
Pfefferminztee | Pfefferminztee, Peppermint tea | GT | 1.0 | 1 Tasse | tee 250
Kamillentee | Kamillentee, Chamomile tea | GT | 1.0 | 1 Tasse | tee 250
"""
