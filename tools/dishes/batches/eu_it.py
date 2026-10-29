CUISINE = 'it'
TEXT = """
Pasta alla gricia | Gricia | NA | 1.0 | 1 Teller | nudeln 90, wasser 200, schwein_bauch 40, pecorino 30, pfeffer 1
Pappardelle al cinghiale | Wild boar pappardelle | NA | 1.0 | 1 Teller | nudeln 90, wasser 200, wildschwein 120, tomaten_dose 100, zwiebel 30, karotte 20, wein_rot 40, olivenoel 12
Spaghetti alla Nerano | Spaghetti Nerano, Zucchini spaghetti Nerano | NA | 1.0 | 1 Teller | nudeln 90, wasser 200, zucchini 200, parmesan 25, butter 10, olivenoel 20
Cavatelli broccoli e salsiccia | Cavatelli with sausage | NA | 1.0 | 1 Teller | nudeln 90, wasser 200, brokkoli 150, bratwurst 80, knoblauch 4, olivenoel 12, pecorino 10
Risotto al radicchio e gorgonzola | Radicchio risotto | RP | 0.95 | 1 Teller | reis 80, wasser 100, salat 80, blauschimmelkaese 40, wein_rot 40, zwiebel 20, butter 15, bruehe 250
Polenta e osei | Polenta and birds | HF | 0.9 | 1 Teller | maismehl 70, wasser 300, kalb 80, speck 25, butter 15, wein_weiss 30
Cotoletta alla milanese | Milanese veal cutlet, Costoletta milanese | HF | 0.85 | 1 Kotelett | kalb 200, paniermehl 25, ei 25, butter 35, mehl 10
Bistecca alla fiorentina | Florentine steak | HF | 0.8 | 1 Steak | rind_steak 450, olivenoel 8, salz 2
Stracotto di manzo | Stracotto | HF | 0.7 | 1 Portion | rind 250, zwiebel 50, karotte 30, wein_rot 100, tomatenmark 15, olivenoel 12
Trippa alla romana | Roman tripe | HF | 0.9 | 1 Portion | innereien 220, tomaten_dose 150, zwiebel 30, pecorino 15, olivenoel 12, minze 3
Coda alla vaccinara | Oxtail stew Roman | HF | 0.7 | 1 Portion | rind_fett 300, sellerie 60, tomaten_dose 150, zwiebel 40, wein_weiss 60, olivenoel 12, pinienkerne 8, rosinen 8
Abbacchio alla scottadito | Scottadito lamb chops | HF | 0.75 | 1 Portion | lamm_kotelett 300, olivenoel 10
Arista di maiale al latte | Pork loin in milk | HF | 0.75 | 1 Portion | schwein_nacken 250, milch 200, butter 15, knoblauch 5
Involtini alla messinese | Messina beef rolls | HF | 0.8 | 3 Stück | rind_steak 180, paniermehl 25, pecorino 20, zwiebel 20, rosinen 8, pinienkerne 8, olivenoel 15
Pollo con i peperoni | Chicken with peppers Roman | HG | 0.8 | 1 Portion | hahn_keule 250, paprika_rot 200, tomaten_dose 80, zwiebel 40, olivenoel 15, wein_weiss 30
Coniglio alla ligure | Ligurian rabbit | HF | 0.75 | 1 Portion | kaninchen 250, olive 30, pinienkerne 10, wein_weiss 60, olivenoel 15, knoblauch 5
Pesce spada alla ghiotta | Swordfish ghiotta | HFi | 0.85 | 1 Portion | schwertfisch 200, tomaten_dose 120, olive 25, zwiebel 30, sellerie 20, olivenoel 12, rosinen 8
Acqua pazza | Fish in crazy water | HFi | 0.9 | 1 Portion | fisch_mager 250, tomate 120, knoblauch 5, olivenoel 12, wasser 100
Brodetto di pesce | Adriatic fish stew | E | 0.95 | 1 Teller | fisch_mager 150, kalmar 50, garnele 50, tomate 120, zwiebel 30, wein_weiss 50, olivenoel 15, weissbrot 30
Spiedini di gamberi | Prawn skewers Italian | HFi | 0.85 | 1 Portion | garnele 200, olivenoel 12, zitrone 10, paniermehl 10
Insalata di arance e finocchi | Orange fennel salad Sicilian | SA | 1.0 | 1 Portion | orange 200, salat 40, zwiebel 20, olive 15, olivenoel 12
Acquacotta | Maremma vegetable soup | S | 0.95 | 1 Teller | zwiebel 60, sellerie 40, tomate 100, weissbrot 50, ei 50, pecorino 15, olivenoel 12, wasser 300
Stracciatella alla romana | Stracciatella soup, Italian egg drop soup | S | 1.0 | 1 Teller | ei 100, parmesan 20, griess 8, bruehe 300
Zuppa pavese | Pavese soup | S | 1.0 | 1 Teller | bruehe 300, ei 100, weissbrot 40, parmesan 15, butter 12
Cassoeula | Cassoeula milanese | E | 0.85 | 1 Portion | weisskohl 250, schwein_bauch 100, bratwurst 80, schwein_haxe 100, zwiebel 30, tomatenmark 8, wein_weiss 30
Cicoria e fagioli | Chicory and beans | HH | 0.95 | 1 Portion | bohnen_trocken 60, wasser 250, salat 150, olivenoel 18, knoblauch 4
Frittata di zucchine | Zucchini frittata | EI | 0.9 | 1 Portion | ei 150, zucchini 150, parmesan 15, olivenoel 15
Frittata di cipolle | Onion frittata | EI | 0.9 | 1 Portion | ei 150, zwiebel 150, parmesan 15, olivenoel 15
Uova in purgatorio | Eggs in purgatory | EI | 0.9 | 1 Portion | ei 120, tomaten_dose 200, zwiebel 30, chili 3, olivenoel 12, weissbrot 30
Fiori di zucca fritti | Fried zucchini flowers | V | 0.85 | 4 Stück | zucchini 80, mozzarella 40, sardelle 10, mehl 40, wasser 50, oel 30
Prosciutto e melone | Ham and melon | V | 1.0 | 1 Portion | rohschinken 60, melone 250
Bresaola con rucola e grana | Bresaola rocket parmesan | V | 1.0 | 1 Portion | rind_steak 60, rucola 30, parmesan 20, olivenoel 10, zitrone 5
Burrata con pomodorini | Burrata and tomatoes | V | 1.0 | 1 Portion | mozzarella 100, sahne 40, tomate 100, olivenoel 12
Panino con porchetta | Porchetta sandwich | SN | 1.0 | 1 Brötchen | semmel 90, schwein_bauch 100, salz 1
Panino al lampredotto | Lampredotto sandwich | SN | 0.95 | 1 Brötchen | semmel 90, innereien 120, tomate 40, petersilie 5, olivenoel 8
Pane e panelle | Panelle sandwich | SN | 0.9 | 1 Brötchen | semmel 80, kichererbsen_trocken 60, wasser 160, oel 35
Crostata di marmellata | Italian jam tart | K | 0.95 | 1 Stück | mehl 60, butter 35, zucker 25, ei 20, marmelade 50
Cassatelle di Agira | Cassatelle | G | 0.9 | 2 Stück | mehl 70, schmalz 20, zucker 20, ricotta 60, zimt 1, oel 20
Cioccolata calda italiana | Italian hot chocolate | GT | 1.0 | 1 Tasse | milch 150, schokolade 30, staerke 8, zucker 10
Tigella con salumi | Tigelle emiliane | SN | 1.0 | 3 Stück | mehl 80, milch 40, hefe 3, schmalz 10, rohschinken 40, salami 30, ricotta 20
Torta di verdure | Italian vegetable pie | BO | 0.9 | 1 Stück | mehl 60, olivenoel 20, mangold 150, ricotta 60, parmesan 15, ei 40
Stoccafisso alla ligure | Stockfish Ligurian | HFi | 0.9 | 1 Portion | stockfisch 200, kartoffel 120, olive 20, pinienkerne 10, tomate 50, olivenoel 15
Spezzatino di manzo con patate | Italian beef stew | E | 0.8 | 1 Portion | rind 200, kartoffel 180, karotte 40, zwiebel 40, tomatenmark 15, wein_rot 40, olivenoel 10
Salsiccia e patate al forno | Sausage and potatoes | HF | 0.85 | 1 Portion | bratwurst 180, kartoffel 250, olivenoel 15
Spätzle al ragù altoatesini | Spätzle Südtirol | NA | 1.0 | 1 Teller | mehl 100, ei 50, hack 100, tomaten_dose 100, zwiebel 30, wein_rot 40, olivenoel 10, wasser 30
Porceddu | Sardinian roast suckling pig | HF | 0.65 | 1 Portion | schwein_bauch 250, schwein_nacken 150, salz 2
Penne al pomodoro e basilico | Penne pomodoro basilico | NA | 1.0 | 1 Teller | nudeln 90, wasser 200, tomaten_dose 150, zwiebel 20, olivenoel 15, parmesan 10
Pasta con le sarde | Sicilian sardine pasta | NA | 1.0 | 1 Teller | nudeln 90, wasser 200, sardine 100, zwiebel 30, rosinen 10, pinienkerne 10, paniermehl 10, olivenoel 15
Pasta alla Siracusana | Siracusa pasta | NA | 1.0 | 1 Teller | nudeln 90, wasser 200, tomate 100, aubergine 80, olive 20, sardelle 10, olivenoel 15, paprika 40
Pasta ammuddicata | Pasta con la mollica | NA | 1.0 | 1 Teller | nudeln 90, wasser 200, paniermehl 30, sardelle 15, olivenoel 20, rosinen 10
Spaghetti alla Assassina | Assassin's spaghetti | NA | 1.0 | 1 Teller | nudeln 90, tomatenmark 40, wasser 400, chili 3, olivenoel 20, knoblauch 5
Paniscia novarese | Paniscia | RP | 0.95 | 1 Teller | reis 70, bohnen_trocken 30, wasser 300, speck 30, salami 30, weisskohl 50, zwiebel 30, wein_rot 40, karotte 20
Pasta e patate | Pasta and potatoes Neapolitan | E | 1.0 | 1 Teller | nudeln 60, kartoffel 200, tomate 60, zwiebel 30, speck 20, olivenoel 12, parmesan 10, wasser 250
Carabaccia | Tuscan onion soup | S | 0.95 | 1 Teller | zwiebel 250, olivenoel 15, zucker 5, essig 10, ei 30, parmesan 15, weissbrot 30, bruehe 250
Abbacchio al forno con patate | Roast lamb with potatoes Roman | HF | 0.75 | 1 Portion | lamm 280, kartoffel 250, olivenoel 20, wein_weiss 40, knoblauch 5
"""
