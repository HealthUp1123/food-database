CUISINE = 'gr'
TEXT = """
Kreatopita | Κρεατόπιτα, Greek meat pie | BO | 0.9 | 1 Stück | yufka 70, hack 120, zwiebel 30, tomatenmark 10, olivenoel 15
Hortopita | Χορτόπιτα | BO | 0.9 | 1 Stück | yufka 70, spinat 100, mangold 60, beyaz_peynir 50, ei 25, olivenoel 15
Bourekia Chania | Μπουρέκι Χανίων | BO | 0.9 | 3 Stück | yufka 60, ziegenkaese 80, honig 10, oel 15
Gemista rice | Γεμιστά με ρύζι | DO | 0.9 | 2 Stück | tomate 150, paprika 100, reis 40, zwiebel 30, petersilie 8, minze 3, olivenoel 20, wasser 60
Melitzanes imam | Μελιτζάνες ιμάμ, Greek imam baildi | GZ | 0.85 | 1 Portion | aubergine 250, zwiebel 60, tomate 100, knoblauch 5, olivenoel 35
Fasolada | Φασολάδα, Greek bean soup | S | 0.95 | 1 Teller | bohnen_trocken 70, wasser 400, karotte 30, sellerie 30, tomatenmark 15, zwiebel 30, olivenoel 20
Fakes | Φακές, Greek lentil soup | S | 0.95 | 1 Teller | linsen 70, wasser 400, zwiebel 30, tomate 40, olivenoel 15, essig 5
Avgolemono soup | Αυγολέμονο | S | 0.95 | 1 Teller | hahn_brust 60, reis 30, ei 50, zitrone 30, wasser 300
Kakavia | Κακαβιά, Greek fish soup | S | 0.95 | 1 Teller | fisch_mager 150, kartoffel 100, zwiebel 40, tomate 50, olivenoel 20, wasser 300, zitrone 15
Magiritsa | Μαγειρίτσα | S | 0.95 | 1 Teller | innereien 100, reis 30, ei 50, zitrone 20, dill 8, fruehlingszwiebel 30, wasser 300
Patsas | Πατσάς | S | 0.95 | 1 Teller | innereien 200, knoblauch 10, essig 15, zitrone 15, wasser 300
Kokkinisto | Κοκκινιστό | E | 0.75 | 1 Portion | rind 200, tomate 100, tomatenmark 15, zwiebel 40, wein_rot 40, olivenoel 12, zimt 1
Stuffed bifteki | Μπιφτέκι γεμιστό | KF | 0.85 | 1 Stück | gemischtes_hack 160, beyaz_peynir 40, zwiebel 20, semmel 15, ei 15, oregano 1, olivenoel 8
Youvarlakia | Γιουβαρλάκια | S | 0.95 | 1 Teller | gemischtes_hack 120, reis 20, ei 40, zwiebel 20, zitrone 25, mehl 8, wasser 250, petersilie 5
Lemon potatoes chicken Greek | Κοτόπουλο με πατάτες φούρνου | HG | 0.8 | 1 Portion | hahn_keule 250, kartoffel 250, zitrone 40, olivenoel 20, oregano 1
Chicken giouvetsi | Κοτόπουλο γιουβέτσι | HG | 0.9 | 1 Portion | hahn_keule 220, nudeln 70, tomaten_dose 150, zwiebel 30, olivenoel 12, wasser 100
Paidakia | Παϊδάκια, Greek lamb chops | HF | 0.75 | 1 Portion | lamm_kotelett 300, zitrone 15, olivenoel 12, oregano 1
Kokoretsi | Κοκορέτσι | HF | 0.8 | 1 Portion | innereien 200, schwanzfett 20, oregano 1
Splinantero | Σπληνάντερο | HF | 0.75 | 1 Portion | innereien 200, zitrone 15, olivenoel 10, oregano 1
Lamb with peas Greek | Αρνί με αρακά | HF | 0.8 | 1 Portion | lamm 200, erbsen 150, kartoffel 100, tomate 60, zwiebel 30, olivenoel 15, dill 5
Briam | Μπριάμ, Greek roasted vegetables | GZ | 0.85 | 1 Portion | zucchini 120, aubergine 100, kartoffel 150, tomate 100, zwiebel 40, olivenoel 30, petersilie 5
Artichokes a la polita | Αγκινάρες α λα πολίτα | GZ | 0.9 | 1 Portion | artischocke 200, kartoffel 120, karotte 50, zwiebel 30, dill 8, olivenoel 25, zitrone 15, wasser 100
Lahanorizo | Λαχανόρυζο | RP | 0.95 | 1 Portion | weisskohl 200, reis 50, tomate 60, zwiebel 30, olivenoel 20, wasser 150
Horta vrasta | Χόρτα βραστά, Boiled greens Greek | GZ | 0.9 | 1 Portion | wildkraut 250, olivenoel 20, zitrone 15
Kolokithokeftedes | Κολοκυθοκεφτέδες, Zucchini fritters Greek | SN | 0.85 | 4 Stück | zucchini 200, beyaz_peynir 40, ei 25, mehl 25, minze 3, oel 25
Domatokeftedes | Ντοματοκεφτέδες, Santorini tomato fritters | SN | 0.85 | 4 Stück | tomate 200, zwiebel 30, mehl 50, minze 3, oel 25
Fried zucchini Greek | Τηγανητά κολοκυθάκια | V | 0.8 | 1 Portion | zucchini 200, mehl 25, oel 30
Fava Santorini | Φάβα Σαντορίνης | SD | 0.95 | 1 Portion | erbsen_trocken 70, zwiebel 40, olivenoel 20, zitrone 10, wasser 250
Lahanosalata | Λαχανοσαλάτα, Greek cabbage salad | SA | 1.0 | 1 Portion | weisskohl 150, karotte 30, olivenoel 15, zitrone 15
Patatosalata | Πατατοσαλάτα, Greek potato salad | SA | 1.0 | 1 Portion | kartoffel 200, zwiebel 20, fruehlingszwiebel 15, olivenoel 18, zitrone 15, petersilie 5
Pantzarosalata | Παντζαροσαλάτα, Greek beet salad | SA | 1.0 | 1 Portion | rote_bete 150, knoblauch 3, olivenoel 12, essig 10, joghurt 30
Baked feta Greek | Φέτα ψητή στο φούρνο | V | 0.9 | 1 Portion | beyaz_peynir 120, tomate 80, paprika 40, olivenoel 12, oregano 1
Bouyiourdi | Μπουγιουρντί | V | 0.9 | 1 Portion | beyaz_peynir 100, tomate 100, chili 8, olivenoel 12
Htapodi xidato | Χταπόδι ξιδάτο, Octopus in vinegar | V | 1.0 | 1 Portion | oktopus 120, essig 20, olivenoel 12, oregano 1
Htapodi krasato | Χταπόδι κρασάτο, Octopus in wine | HFi | 0.85 | 1 Portion | oktopus 250, wein_rot 80, zwiebel 40, tomate 60, olivenoel 15
Kalamarakia | Καλαμαράκια τηγανητά, Fried calamari Greek | HFi | 0.85 | 1 Portion | kalmar 200, mehl 25, oel 35, zitrone 10
Garides saganaki | Γαρίδες σαγανάκι | HFi | 0.9 | 1 Portion | garnele 200, tomate 120, beyaz_peynir 50, zwiebel 20, olivenoel 12, spirituose 10
Midia saganaki | Μύδια σαγανάκι | HFi | 0.9 | 1 Portion | muschel 300, tomate 100, beyaz_peynir 40, olivenoel 12, wein_weiss 30, chili 3
Midia ahnista | Μύδια αχνιστά | HFi | 0.9 | 1 Portion | muschel 400, wein_weiss 60, zitrone 15, butter 8, knoblauch 3
Bakaliaros skordalia | Μπακαλιάρος σκορδαλιά | HFi | 0.85 | 1 Portion | stockfisch 150, kartoffel 150, knoblauch 12, olivenoel 25, mehl 20, oel 25
Psari plaki | Ψάρι πλακί | HFi | 0.85 | 1 Portion | fisch_mager 220, tomate 120, kartoffel 100, zwiebel 40, olivenoel 25, knoblauch 5
Gavros marinatos | Γαύρος μαρινάτος | V | 1.0 | 1 Portion | sardelle 100, essig 25, olivenoel 20, knoblauch 3
Sardeles psites | Σαρδέλες ψητές | HFi | 0.85 | 1 Portion | sardine 250, olivenoel 10, zitrone 10
Barbounia | Μπαρμπούνια τηγανητά, Fried red mullet | HFi | 0.85 | 1 Portion | fisch_mager 220, mehl 20, oel 30
Bourdeto | Μπουρδέτο | E | 0.9 | 1 Portion | fisch_mager 220, zwiebel 60, paprikapulver 3, olivenoel 20, tomatenmark 10, wasser 100
Cuttlefish with spinach | Σουπιές με σπανάκι | HFi | 0.85 | 1 Portion | kalmar 180, spinat 200, zwiebel 40, olivenoel 20, dill 5, wein_weiss 30
Tiganiá | Τηγανιά, Pork tigania | PF | 0.8 | 1 Portion | schwein_nacken 200, olivenoel 12, zitrone 15, oregano 1
Kontosouvli | Κοντοσούβλι | HF | 0.7 | 1 Portion | schwein_nacken 300, olivenoel 8, zitrone 10, oregano 1
Greek village sausage | Λουκάνικο Χωριάτικο | WU | 0.9 | 1 Portion | bratwurst 140, orange 20, fladenbrot 60
Tsouknidopita | Τσουκνιδόπιτα | BO | 0.9 | 1 Stück | yufka 70, hack 120, zwiebel 30, tomate 30, olivenoel 15
Galaktoboureko | Γαλακτομπούρεκο | SW | 0.95 | 1 Stück | yufka 40, milch 120, griess 20, zucker 60, ei 40, butter 25, wasser 30
Portokalopita | Πορτοκαλόπιτα | K | 0.95 | 1 Stück | yufka 50, joghurt 80, ei 50, zucker 70, orange 40, oel 40
Ravani | Ραβανί | K | 0.95 | 1 Stück | griess 50, mehl 25, ei 50, zucker 70, butter 35, joghurt 30, wasser 40
Samali | Σαμαλί | K | 0.95 | 1 Stück | griess 70, zucker 70, mandel 20, butter 25, wasser 80, orange 10
Diples | Διπλές | SW | 0.9 | 3 Stück | mehl 60, ei 30, honig 40, walnuss 15, oel 30
Halva Greek semolina | Χαλβάς σιμιγδαλένιος | PU | 0.95 | 1 Schälchen | griess 40, oel 30, zucker 50, rosinen 15, mandel 15, wasser 130, zimt 1
Spoon sweets | Γλυκό του κουταλιού | D | 1.0 | 1 Löffel (30 g) | zucker 20, quitte 10
Karydopita | Καρυδόπιτα | K | 0.95 | 1 Stück | walnuss 40, mehl 30, griess 15, zucker 45, ei 40, oel 25, zimt 1
Vasilopita | Βασιλόπιτα | K | 0.95 | 1 Scheibe | mehl 70, butter 35, zucker 50, ei 40, orange 15, mandel 10
Freddo cappuccino | Φρέντο καπουτσίνο | GT | 1.0 | 1 Glas | kaffee 80, milch 80, sahne 30, zucker 8
Tsipouro | Τσίπουρο | GT | 1.0 | 1 Glas (40 ml) | spirituose 38
Sfakianes pites | Σφακιανή πίτα | PI | 0.9 | 1 Stück | mehl 80, ziegenkaese 70, honig 15, oel 15
Kalitsounia | Καλιτσούνια | G | 0.95 | 3 Stück | mehl 70, ricotta 60, honig 15, ei 20, zimt 1, oel 10
Lahanodolmades | Λαχανοντολμάδες | DO | 0.85 | 4 Stück | weisskohl 180, gemischtes_hack 100, reis 25, zwiebel 20, olivenoel 12, zitrone 10, ei 20
Makaronia me kima | Μακαρόνια με κιμά | NA | 1.0 | 1 Teller | nudeln 90, wasser 200, hack 100, tomaten_dose 100, zwiebel 30, olivenoel 10, parmesan 10
Kritharoto | Κριθαρότο | RP | 0.95 | 1 Portion | nudeln 80, hahn 100, tomaten_dose 100, zwiebel 30, olivenoel 12, wasser 150
Seafood giouvetsi | Γιουβέτσι θαλασσινών | NA | 0.9 | 1 Portion | nudeln 70, garnele 80, muschel 100, kalmar 60, tomaten_dose 120, zwiebel 30, olivenoel 12, wasser 80
Baked chickpeas Greek | Ρεβύθια φούρνου | HH | 0.95 | 1 Portion | kichererbsen_trocken 70, wasser 300, zwiebel 40, zitrone 15, olivenoel 20, oregano 1
Koukia | Κουκιά λαδερά | HH | 0.9 | 1 Portion | dicke_bohnen 250, tomate 80, zwiebel 40, dill 8, olivenoel 22
Fried anchovies Greek | Γαύρος τηγανητός | HFi | 0.85 | 1 Portion | sardelle 200, mehl 25, oel 30, zitrone 10
Sole with lemon Greek | Γλώσσα με λεμόνι | HFi | 0.85 | 1 Portion | fisch_mager 250, olivenoel 15, zitrone 20, petersilie 5
Grilled red mullet | Μπαρμπούνια ψητά | HFi | 0.85 | 1 Portion | fisch_mager 250, olivenoel 12, zitrone 10
"""
