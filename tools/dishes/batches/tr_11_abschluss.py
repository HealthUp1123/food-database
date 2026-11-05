# Rezeptgerichte der Abschlussliste. Namen und prepared setzt tools/extension/build_abschluss.py
# nach dem Lauf von build.py. Synonyme ohne Komma.
CUISINE = 'tr'
TEXT = """
Tavuk Döner Porsiyon{tavuk-doner-porsiyon} | Hähnchendöner Teller, Chicken doner plate | KB | 0.85 | 1 Teller | hahn_keule 150, reis 50, wasser 90, tomate 50, salat 40, zwiebel 20, oel 8
Tavuk Şiş Dürüm{tavuk-sis-durum} | Hähnchenspieß-Dürüm, Chicken shish wrap | SN | 0.9 | 1 Dürüm | hahn_brust 120, lavas 80, tomate 30, sivri 20, zwiebel 15, joghurt 20, oel 6
Urfa Dürüm{urfa-durum} | Urfa-Dürüm, Urfa kebab wrap | SN | 0.88 | 1 Dürüm | lamm_hack 130, schwanzfett 12, lavas 90, zwiebel 20, tomate 30, petersilie 6, sumak_pulver 1
Döner Pide Üstü{doner-pide-ustu} | Döner auf Pide, Doner on pide | KB | 0.92 | 1 Teller | lamm 80, hack 70, ekmek 100, tomate 40, salat 30, zwiebel 15, joghurt 40, oel 6
Döner Karışık Et{doner-karisik-et} | Döner gemischt Lamm und Rind, Mixed meat doner | KB | 0.75 | 1 Portion | lamm 80, rind 70, schwanzfett 12
Kıymalı Kaşarlı Pide{kiymali-kasarli-pide} | Pide mit Hack und Käse, Pide with mince and cheese | PI | 0.9 | 1 Pide | mehl 120, wasser 55, hack 70, kasar 50, zwiebel 20, tomate 25, butter 10, oel 6
Bıçak Arası{bicak-arasi} | Bıçak Arası, Knife-cut sandwich Adana | SN | 0.92 | 1 Stück | ekmek 100, lamm_hack 90, tomate 30, sivri 20, zwiebel 15, sumak_pulver 1, oel 4
Serpme Kahvaltı{serpme-kahvalti} | Serpme-Frühstück pro Person, Turkish spread breakfast | FR | 1.0 | 1 Person | beyaz_peynir 40, olive 30, tomate 70, gurke 50, honig 12, kaymak 15, ei 50, ekmek 50, tee 80
Meze Teller{meze-teller} | Meze-Teller, Meze platter | V | 0.95 | 1 Teller | joghurt 40, walnuss 6, knoblauch 2, tomate 40, zwiebel 10, olivenoel 8, kichererbsen 35, tahin 8, aubergine 50, weinblatt 15, reis 12
Karışık Izgara{karisik-izgara} | Gemischter Grillteller, Mixed grill | KB | 0.8 | 1 Teller | lamm_hack 70, lamm 60, hack 50, tomate 40, sivri 30, lavas 40, oel 8, zwiebel 15
Kebap Garnitür{kebap-garnitur} | Kebap-Beilage, Kebab side garnish | B | 0.95 | 1 Beilage | salat 40, tomate 50, zwiebel 40, sivri 35, sumak_pulver 2, petersilie 6, olivenoel 8
Çatal{catal} | Çatal-Gebäck, Catal pastry | G | 0.88 | 1 Stück | mehl 70, wasser 38, hefe 2, zucker 8, oel 8, sesam 12, ei 12
Karışık Kıyma{karisik-kiyma} | Gemischtes Hackfleisch Rind und Lamm, Ground beef and lamb | HF | 1.0 | 100 g | hack 50, lamm_hack 50
Kahvaltılık Sos{kahvaltilik-sos} | Frühstückssoße Paprika-Tomate, Breakfast pepper sauce | SD | 0.75 | 1 Schälchen | tomate 80, sivri 40, paprika 30, oel 12, knoblauch 3, salz 1
Zeytin Ezmesi{zeytin-ezmesi} | Olivenpaste, Olive paste | SD | 1.0 | 1 Schälchen | olive 90, olivenoel 8, knoblauch 2, zitrone 5
Kelle Peynirli Börek{kelle-peynirli-borek} | Börek mit Mihaliç-Käse, Kelle cheese borek | BO | 0.92 | 1 Stück | yufka 70, kelle_peynir 55, ei 15, milch 25, butter 10, petersilie 4
Kepekli Ekmek{kepekli-ekmek} | Kleiebrot, Bran bread | BR | 0.86 | 1 Stück | mehl 80, weizenkleie 20, wasser 60, hefe 2, salz 2
Puf Böreği{puf-boregi} | Puf Böreği, Puff borek | BO | 0.9 | 1 Stück | blaetterteig 90, beyaz_peynir 45, petersilie 5, ei 12
Biber Kızartması{biber-kizartmasi} | Gebratene Spitzpaprika, Fried peppers | GZ | 0.78 | 1 Portion | sivri 180, oel 18, joghurt 50, knoblauch 3
Kabak Sinkonta{kabak-sinkonta} | Zucchini-Sinkonta, Zucchini sinkonta | V | 0.82 | 1 Portion | zucchini 180, zwiebel 40, tomate 50, ei 40, olivenoel 12
Sosis Kahvaltı{sosis-kahvalti} | Gebratene Würstchen, Fried sausages | FR | 0.85 | 1 Portion | sosis 100, oel 6
Çökelekli Biber{cokelekli-biber} | Paprika mit Çökelek, Peppers with cokelek | FR | 0.88 | 1 Portion | sivri 140, cokelek 70, oel 8, knoblauch 2
Kinoa Salatası{kinoa-salatasi} | Quinoasalat, Quinoa salad | SA | 1.0 | 1 Schüssel | quinoa_g 80, tomate 50, gurke 40, petersilie 8, olivenoel 10, zitrone 6
Tirmis{tirmis} | Tirmis, Lupin beans | SN | 1.0 | 1 Schälchen | lupine_g 100, salz 1
Isırgan Çorbası{isirgan-corbasi} | Brennnesselsuppe, Nettle soup | S | 0.9 | 1 Schüssel | brennnessel 100, bulgur 25, zwiebel 30, joghurt 50, oel 8, wasser 200
Böbrek Izgara{bobrek-izgara} | Niere gegrillt, Grilled kidney | KB | 0.78 | 1 Portion | lammniere 150, oel 8, sivri 20, lavas 40
Yürek Şiş{yurek-sis} | Herzspieß, Heart skewer | KB | 0.75 | 1 Spieß | lammherz 140, oel 6, sivri 25, lavas 40, sumak_pulver 1
Kokoreç Dürüm{kokorec-durum} | Kokoreç-Dürüm, Kokorec wrap | SN | 0.9 | 1 Dürüm | innereien 110, lavas 80, tomate 30, zwiebel 20, pul_biber 1, oel 6
"""

def M(de, en, tr, fr, es, pt, it, zh, prepared):
    return {'names': {'de': de, 'en': en, 'tr': tr, 'fr': fr, 'es': es, 'pt': pt, 'it': it, 'zh': zh}, 'prepared': prepared}

# prepared: Lokanta/Imbiss restaurant, Hausgericht homemade.
META = {
 'tavuk-doner-porsiyon': M('Hähnchendöner, Teller', 'Chicken döner plate', 'Tavuk döner (porsiyon)', 'Assiette de döner au poulet', 'Plato de döner de pollo', 'Prato de döner de frango', 'Piatto di döner di pollo', '鸡肉旋转烤肉盘', 'restaurant'),
 'tavuk-sis-durum': M('Hähnchenspieß-Dürüm', 'Chicken shish wrap', 'Tavuk şiş dürüm', 'Dürüm de brochettes de poulet', 'Dürüm de brocheta de pollo', 'Dürüm de espetada de frango', 'Dürüm di spiedini di pollo', '鸡肉串卷饼', 'restaurant'),
 'urfa-durum': M('Urfa-Dürüm', 'Urfa kebab wrap', 'Urfa dürüm', 'Dürüm kebab d’Urfa', 'Dürüm kebab de Urfa', 'Dürüm kebab de Urfa', 'Dürüm kebab di Urfa', '乌尔法烤肉卷', 'restaurant'),
 'doner-pide-ustu': M('Döner auf Pide', 'Döner on pide', 'Döner tabağı (pide üstü)', 'Döner sur pide', 'Döner sobre pide', 'Döner sobre pide', 'Döner su pide', '皮德饼旋转烤肉', 'restaurant'),
 'doner-karisik-et': M('Döner gemischt (Lamm/Rind)', 'Mixed meat döner', 'Döner (et, karışık)', 'Döner mélange agneau et bœuf', 'Döner mixto de cordero y ternera', 'Döner misto de borrego e vaca', 'Döner misto agnello e manzo', '牛羊混合旋转烤肉', 'restaurant'),
 'kiymali-kasarli-pide': M('Pide mit Hack und Käse', 'Pide with mince and cheese', 'Kıymalı kaşarlı pide', 'Pide à la viande et au fromage', 'Pide con carne y queso', 'Pide com carne e queijo', 'Pide con carne e formaggio', '肉末奶酪皮德饼', 'restaurant'),
 'bicak-arasi': M('Bıçak Arası', 'Knife-cut sandwich (Adana)', 'Bıçak arası (Adana)', 'Sandwich Bıçak Arası', 'Sándwich Bıçak Arası', 'Sanduíche Bıçak Arası', 'Panino Bıçak Arası', '阿达纳夹肉面包', 'restaurant'),
 'serpme-kahvalti': M('Serpme-Frühstück pro Person', 'Turkish spread breakfast per person', 'Serpme kahvaltı (kişi başı)', 'Petit-déjeuner turc servi (1 personne)', 'Desayuno turco servido (1 persona)', 'Pequeno-almoço turco servido (1 pessoa)', 'Colazione turca servita (1 persona)', '土耳其拼盘早餐（一人）', 'homemade'),
 'meze-teller': M('Meze-Teller', 'Meze platter', 'Rakı sofrası meze tabağı', 'Assiette de meze', 'Plato de meze', 'Travessa de meze', 'Piatto di meze', '梅泽拼盘', 'homemade'),
 'karisik-izgara': M('Gemischter Grillteller', 'Mixed grill', 'Karışık ızgara', 'Grillade mixte', 'Parrillada mixta', 'Grelhada mista', 'Grigliata mista', '混合烤盘', 'restaurant'),
 'kebap-garnitur': M('Kebap-Beilage', 'Kebab side garnish', 'Kebap tabağı garnitür', 'Garniture de kebab', 'Guarnición de kebab', 'Acompanhamento de kebab', 'Contorno di kebab', '烤肉配菜', 'restaurant'),
 'catal': M('Çatal (Gebäck)', 'Çatal pastry', 'Çatal', 'Pâtisserie Çatal', 'Pastel Çatal', 'Doce Çatal', 'Pasticcino Çatal', '恰塔尔点心', 'homemade'),
 'karisik-kiyma': M('Gemischtes Hackfleisch Rind/Lamm', 'Ground beef and lamb', 'Karışık kıyma', 'Viande hachée bœuf et agneau', 'Carne picada de ternera y cordero', 'Carne picada de vaca e borrego', 'Carne macinata di manzo e agnello', '牛羊混合肉末', 'homemade'),
 'kahvaltilik-sos': M('Frühstückssoße (Paprika-Tomate)', 'Breakfast pepper sauce', 'Kahvaltılık sos', 'Sauce petit-déjeuner poivron-tomate', 'Salsa de desayuno de pimiento y tomate', 'Molho de pequeno-almoço de pimento e tomate', 'Salsa da colazione peperone e pomodoro', '早餐辣椒番茄酱', 'homemade'),
 'zeytin-ezmesi': M('Olivenpaste', 'Olive paste', 'Zeytin ezmesi', 'Pâte d’olives', 'Pasta de aceitunas', 'Pasta de azeitona', 'Pasta di olive', '橄榄酱', 'homemade'),
 'kelle-peynirli-borek': M('Börek mit Mihaliç-Käse', 'Kelle cheese börek', 'Kelle peynirli börek', 'Börek au fromage Mihaliç', 'Börek con queso Mihaliç', 'Börek com queijo Mihaliç', 'Börek al formaggio Mihaliç', '米哈利奇奶酪酥饼', 'homemade'),
 'kepekli-ekmek': M('Kleiebrot', 'Bran bread', 'Kepekli ekmek', 'Pain au son', 'Pan de salvado', 'Pão de farelo', 'Pane di crusca', '麸皮面包', 'homemade'),
 'puf-boregi': M('Puf Böreği', 'Puff börek', 'Puf böreği', 'Börek feuilleté', 'Börek de hojaldre', 'Börek folhado', 'Börek di pasta sfoglia', '酥皮博雷克', 'homemade'),
 'biber-kizartmasi': M('Gebratene Spitzpaprika', 'Fried peppers', 'Biber kızartması', 'Poivrons frits', 'Pimientos fritos', 'Pimentos fritos', 'Peperoni fritti', '煎尖椒', 'homemade'),
 'kabak-sinkonta': M('Zucchini-Sinkonta', 'Zucchini sinkonta', 'Kabak sinkonta', 'Sinkonta de courgette', 'Sinkonta de calabacín', 'Sinkonta de curgete', 'Sinkonta di zucchine', '西葫芦辛孔塔', 'homemade'),
 'sosis-kahvalti': M('Gebratene Würstchen', 'Fried sausages', 'Sosis (kahvaltı, kızarmış)', 'Saucisses poêlées', 'Salchichas fritas', 'Salsichas fritas', 'Salsicce fritte', '煎肠', 'restaurant'),
 'cokelekli-biber': M('Paprika mit Çökelek', 'Peppers with çökelek', 'Çökelekli biber', 'Poivrons au çökelek', 'Pimientos con çökelek', 'Pimentos com çökelek', 'Peperoni con çökelek', '乔凯莱克辣椒', 'homemade'),
 'kinoa-salatasi': M('Quinoasalat', 'Quinoa salad', 'Kinoa salatası', 'Salade de quinoa', 'Ensalada de quinoa', 'Salada de quinoa', 'Insalata di quinoa', '藜麦沙拉', 'homemade'),
 'tirmis': M('Tirmis (Lupinen, gekocht)', 'Lupin beans', 'Tirmis', 'Lupins cuits (tirmis)', 'Altramuces cocidos (tirmis)', 'Tremoços cozidos (tirmis)', 'Lupini cotti (tirmis)', '羽扇豆（煮）', 'homemade'),
 'isirgan-corbasi': M('Brennnesselsuppe', 'Nettle soup', 'Isırgan çorbası', 'Soupe d’orties', 'Sopa de ortigas', 'Sopa de urtigas', 'Zuppa di ortiche', '荨麻汤', 'homemade'),
 'bobrek-izgara': M('Niere gegrillt', 'Grilled kidney', 'Böbrek (ızgara)', 'Rognon grillé', 'Riñón a la parrilla', 'Rim grelhado', 'Rene alla griglia', '烤羊肾', 'restaurant'),
 'yurek-sis': M('Herzspieß', 'Heart skewer', 'Yürek şiş', 'Brochette de cœur', 'Brocheta de corazón', 'Espetada de coração', 'Spiedino di cuore', '烤心串', 'restaurant'),
 'kokorec-durum': M('Kokoreç-Dürüm', 'Kokoreç wrap', 'Kokoreç dürüm', 'Dürüm de kokoreç', 'Dürüm de kokoreç', 'Dürüm de kokoreç', 'Dürüm di kokoreç', '羊肠卷饼', 'restaurant'),
}
