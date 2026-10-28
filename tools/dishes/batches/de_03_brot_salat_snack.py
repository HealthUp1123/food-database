CUISINE = 'de'
TEXT = """
Brötchen | Semmel, Schrippe, Weckle, Bread roll | BR | 1.0 | 1 Brötchen | semmel 55
Laugenbrezel | Brezel, Breze, Pretzel | BR | 1.0 | 1 Brezel | mehl 70, wasser 40, butter 3, salz 2
Laugenbrötchen | Laugenweckle, Pretzel roll | BR | 1.0 | 1 Brötchen | mehl 60, wasser 35, salz 2
Roggenbrot | Roggenmischbrot, Rye bread | BR | 1.0 | 1 Scheibe | roggenbrot 50
Vollkornbrot | Vollkornbrot, Wholegrain bread | BR | 1.0 | 1 Scheibe | vollkornbrot 50
Pumpernickel | Pumpernickel, Westphalian rye | BR | 1.0 | 1 Scheibe | roggenbrot 50, wasser 5
Weißbrot | Toastbrot, White bread | BR | 1.0 | 1 Scheibe | weissbrot 30
Bauernbrot | Bauernbrot, Farmer's bread | BR | 1.0 | 1 Scheibe | roggenbrot 50
Mehrkornbrot | Mehrkornbrot, Multigrain bread | BR | 1.0 | 1 Scheibe | vollkornbrot 40, sonnenblumenkerne 5, sesam 3
Körnerbrötchen | Körnerbrötchen, Seed roll | BR | 1.0 | 1 Brötchen | semmel 55, sonnenblumenkerne 6, sesam 3, mohn 2
Butterbrezel | Butterbrezel, Buttered pretzel | BR | 1.0 | 1 Brezel | mehl 70, wasser 40, butter 10, salz 2
Brot mit Butter und Käse | Käsebrot, Bread with cheese | SN | 1.0 | 2 Scheiben | roggenbrot 80, butter 10, gouda 40
Brot mit Schinken | Schinkenbrot, Ham sandwich | SN | 1.0 | 2 Scheiben | roggenbrot 80, butter 10, schinken 40
Käsebrötchen | Brötchen mit Käse, Cheese roll | SN | 1.0 | 1 Brötchen | semmel 60, butter 8, gouda 30
Brötchen mit Marmelade | Marmeladenbrötchen, Roll with jam | FR | 1.0 | 1 Brötchen | semmel 60, butter 10, marmelade 25
Brötchen mit Honig | Honigbrötchen | FR | 1.0 | 1 Brötchen | semmel 60, butter 10, honig 20
Brötchen mit Nuss-Nougat-Creme | Nutellabrötchen, Hazelnut spread roll | FR | 1.0 | 1 Brötchen | semmel 60, schokolade_milch 15, haselnuss 5, butter 5
Leberwurstbrötchen | Brötchen mit Leberwurst | SN | 1.0 | 1 Brötchen | semmel 60, leberwurst 30, butter 5
Salamibrötchen | Brötchen mit Salami | SN | 1.0 | 1 Brötchen | semmel 60, salami 25, butter 8
Fischbrötchen | Matjesbrötchen, Bismarckhering Brötchen, Fish roll | SN | 1.0 | 1 Brötchen | semmel 60, hering 70, zwiebel 15, gewuerzgurke 15
Matjesbrötchen | Matjes im Brötchen | SN | 1.0 | 1 Brötchen | semmel 60, hering 70, zwiebel 20
Backfischbrötchen | Fischbrötchen mit Backfisch | SN | 1.0 | 1 Brötchen | semmel 60, kabeljau 80, paniermehl 10, ei 10, oel 10, salat 10
Krabbenbrötchen | Krabbenbrot, Shrimp roll | SN | 1.0 | 1 Brötchen | semmel 60, garnele 60, mayonnaise 20
Räucherlachsbrötchen | Brötchen mit Räucherlachs | SN | 1.0 | 1 Brötchen | semmel 60, lachs 50, frischkaese 25, salat 10
Frühstücksei | Weich gekochtes Ei, Soft boiled egg | FR | 1.0 | 1 Ei | ei 60
Eier im Glas | Eier im Glas, Eggs in a glass | FR | 1.0 | 2 Eier | ei 110, butter 3
Rührei | Rührei natur, Scrambled eggs | FR | 0.9 | 1 Portion | ei 120, milch 20, butter 10
Spiegelei auf Brot | Spiegelei Brot | FR | 1.0 | 1 Portion | ei 60, roggenbrot 50, butter 10
Müsli mit Milch | Müsli, Muesli with milk | FR | 1.0 | 1 Schüssel | haferflocken 40, milch 150, apfel 50, rosinen 10, haselnuss 5
Bircher Müsli | Birchermüsli, Bircher muesli | FR | 1.0 | 1 Schüssel | haferflocken 40, joghurt 100, apfel 80, milch 50, haselnuss 5, zitrone 5
Haferbrei | Haferflockenbrei, Porridge | FR | 1.0 | 1 Schüssel | haferflocken 50, milch 200, honig 10
Milchreis mit Zimt und Zucker | Milchreis, Rice pudding German | PU | 1.0 | 1 Portion | reis 50, milch 250, zucker 15, zimt 1
Grießbrei | Grießbrei mit Zimt, Semolina porridge | PU | 1.0 | 1 Portion | griess 30, milch 200, zucker 15, butter 3
Quark mit Früchten | Fruchtquark, Quark with fruit | FR | 1.0 | 1 Schüssel | quark 150, erdbeere 60, zucker 8, milch 30
Pfannkuchen | Eierkuchen, Palatschinken, Pancakes German, Crêpes | FR | 0.9 | 2 Stück | mehl 80, ei 50, milch 150, butter 12, zucker 10
Pfannkuchen mit Apfelmus | Eierkuchen mit Apfelmus | FR | 0.9 | 2 Stück | mehl 80, ei 50, milch 150, butter 12, apfel 100, zucker 12
Apfelpfannkuchen | Apfelpfannkuchen, Apple pancake | FR | 0.9 | 1 Pfannkuchen | mehl 70, ei 50, milch 130, apfel 120, butter 12, zucker 10, zimt 1
Kaiserschmarrn | Kaiserschmarrn, Shredded pancake | D | 0.9 | 1 Portion | mehl 80, ei 70, milch 120, butter 20, zucker 25, rosinen 20
Heringssalat | Heringssalat, Herring salad | SA | 1.0 | 1 Portion | hering 60, rote_bete 40, apfel 30, gewuerzgurke 30, zwiebel 15, mayonnaise 25, joghurt 20
Fleischsalat | Fleischsalat, Meat salad | SA | 1.0 | 1 Portion | leberkaese 60, gewuerzgurke 40, mayonnaise 50, ei 30, joghurt 20
Wurstsalat | Schweizer Wurstsalat, Sausage salad | SA | 1.0 | 1 Portion | bockwurst 80, gewuerzgurke 30, zwiebel 20, essig 15, oel 12
Schweizer Wurstsalat | Wurstsalat mit Käse, Sausage cheese salad | SA | 1.0 | 1 Portion | bockwurst 70, emmentaler 40, zwiebel 20, gewuerzgurke 25, essig 12, oel 12
Nudelsalat | Nudelsalat mit Mayonnaise, Pasta salad | SA | 1.0 | 1 Portion | nudeln 80, mayonnaise 40, gewuerzgurke 30, mais 30, erbsen 30, schinken 30, joghurt 25
Eiersalat | Eiersalat, Egg salad | SA | 1.0 | 1 Portion | ei 120, mayonnaise 30, joghurt 30, zwiebel 10
Gurkensalat | Gurkensalat mit Dill, Cucumber salad German | SA | 1.0 | 1 Portion | gurke 200, joghurt 40, essig 10, dill 3, oel 6
Tomatensalat | Tomatensalat mit Zwiebeln | SA | 1.0 | 1 Portion | tomate 200, zwiebel 20, oel 10, essig 10
Kopfsalat | Kopfsalat mit Dressing, Green salad | SA | 1.0 | 1 Portion | salat 100, oel 10, essig 8
Gemischter Salat | Beilagensalat, Mixed salad | SA | 1.0 | 1 Portion | salat 60, tomate 50, gurke 50, karotte 30, oel 10, essig 8
Krautsalat | Weißkohlsalat, Coleslaw German | SA | 1.0 | 1 Portion | weisskohl 150, essig 15, oel 12, zucker 3
Rotkohlsalat | Rotkrautsalat | SA | 1.0 | 1 Portion | rotkohl 150, apfel 30, oel 10, essig 12
Möhrensalat | Karottensalat, Carrot salad | SA | 1.0 | 1 Portion | karotte 150, apfel 30, zitrone 10, oel 10
Selleriesalat | Sellerie-Apfel-Salat, Celery root salad | SA | 1.0 | 1 Portion | sellerie 130, apfel 40, mayonnaise 20, joghurt 30, zitrone 5
Rote-Bete-Salat | Rote Bete Salat, Beet salad | SA | 1.0 | 1 Portion | rote_bete 150, zwiebel 15, essig 15, oel 10
Bohnensalat | Grüne Bohnen Salat, Bean salad | SA | 1.0 | 1 Portion | gruene_bohnen 150, zwiebel 20, essig 12, oel 12, bohnen_trocken 20
Linsensalat | Linsensalat, Lentil salad | SA | 1.0 | 1 Portion | linsen 60, wasser 120, zwiebel 20, essig 12, oel 12, karotte 30
Spargelsalat | Spargelsalat, Asparagus salad | SA | 1.0 | 1 Portion | spargel 200, tomate 60, essig 10, oel 12
Wurst-Käse-Salat | Wurst Käse Salat | SA | 1.0 | 1 Portion | salami 40, gouda 50, gewuerzgurke 30, salat 50, oel 10, essig 8
Chefsalat | Chef salad, Salatteller | SA | 1.0 | 1 Teller | salat 80, schinken 40, gouda 40, ei 50, tomate 50, gurke 40, oel 12, essig 8
Salat mit Hähnchenbruststreifen | Salat mit Hähnchenstreifen, Salad with chicken strips | SA | 0.95 | 1 Teller | salat 100, hahn_brust 100, tomate 60, gurke 50, oel 12, essig 8
Brotzeitteller | Brotzeit, Bavarian cold platter | SN | 1.0 | 1 Teller | roggenbrot 80, salami 30, schinken 30, gouda 40, butter 10, gewuerzgurke 30, tomate 40, rettich 40
Vesperteller | Vesper, Swabian cold plate | SN | 1.0 | 1 Teller | roggenbrot 80, schinken 40, leberwurst 30, gouda 40, butter 10, gewuerzgurke 30
Obatzda | Obazda, Bavarian cheese spread | SD | 1.0 | 1 Portion | camembert 100, frischkaese 30, butter 15, zwiebel 10, paprikapulver 1, bier 10
Radi | Bayerischer Radi, Salted radish | SN | 1.0 | 1 Portion | rettich 150, salz 1
Handkäs mit Musik | Handkäse mit Musik, Cheese in vinegar and onions | SN | 1.0 | 1 Portion | quark_mager 120, zwiebel 30, essig 10, oel 8, senf 3
Käseplatte | Käseteller, Cheese board | SN | 1.0 | 1 Teller | gouda 40, emmentaler 40, camembert 40, traube 30, walnuss 10, roggenbrot 30
Käse-Schinken-Toast | Ham and cheese toast | SN | 0.95 | 1 Toast | weissbrot 50, schinken 30, gouda 30, butter 5
Toast Hawaii | Toast Hawaii, Hawaii toast | SN | 0.95 | 1 Toast | weissbrot 50, schinken 30, gouda 30, butter 5, ananas 40
Flammkuchen | Elsässer Flammkuchen, Tarte flambée | PF | 0.9 | 1 Flammkuchen | mehl 100, wasser 50, schmand 80, speck 40, zwiebel 40, oel 8
Flammkuchen vegetarisch | Flammkuchen ohne Speck | PF | 0.9 | 1 Flammkuchen | mehl 100, wasser 50, schmand 80, zwiebel 60, pilz 40, oel 8
Zwiebelkuchen | Zwiebelkuchen, Onion tart | K | 0.9 | 1 Stück | mehl 50, butter 20, zwiebel 150, speck 30, ei 40, schmand 50, milch 20
Speckkuchen | Specktorte, Bacon tart | K | 0.9 | 1 Stück | mehl 60, hefe 2, speck 60, zwiebel 40, schmand 60, ei 30
"""
