from methods import change_diphthongs

regular_verb_list = [
    'Dar', 'dar', 'ecar', 'B-lar', 'armar', 'jeBar', 'jenar', 'jorar', 'BiBer', 'Diser', 'arer',
    'kitar', 'aBlar', 'Blar', 'peGar', 'kumplir', 'BeBer', 'empuxar', 'Boltear', 'saBer', 'orar',
    'kojar', 'p*nar', 'parar', 'pasar', 'sakar', 'tamar', 'tokar', 'akomoDar', 'reir', 'martijar',
    'tomar', 'Bar', 'Dexar', 'romper', 'poNgar', 'star', 'Buskar', 'apr#tar', 'pr#tar', 'pomer', 
    'xalar', 'xuGar', 'G&rDar', 'Gustar', 'sentar', 'aGaRar', 'GaRar', 'eskucar', 'mueBer',
    'ajuDar', 'b-lar', 'B#ner', 'D$rmir', 'subir', 'suBir', 'esperar', 'oxear', 'seRar',
    'pasear', 'prestar', 'Bisitar', 'Golpear', 'dexar', 'aG&rDar', 'apacuRar', 'dormir',
    'ense|ar', 'haber', 'mandar', 'pokater', 'enoxer', 'kansar', 'azer', 'Biner', 'suenar',
    'aReGlar', 'estar', 'faltar', 's#Rar', 'aB#ntar', 'xirar', 'tr-er', 'Baxar', 'kantar',
    'poDer', 'tapar', 'laBar', 'atoraste', 'tirar', 'pres#nar', 'atorar', 'platisar', # got rid of 'seR'
    'saluDar', 'enkontrar', 'Ber', 'ber', 'Baer', 'aser', 'keDar', 'aserkar', 'pikar', 'faltar',
    'kaer', 'rekoxer', 'g&rDar', 'terminar', 'pakater', 'aBer', 'kajar', 'iser', 'saluDar',
    'meter', 'moBer', 'poner', 'Desaser', 'komponer', 'Desir', '$Gar', 'duermer',
    'aBrir', 'peDir', 'salir', 'x$Gar', 'BriNkar', 'p$Der', 'sirBer', 'Bestir', 'Pruebar',
    'G&rDar', 'pareser', 'Dormir', 'Besar', 'biBir', 'DiBuxar', 'iser', 'suenar', 'ueler',
    'k#rer', 'akaBar', 'kerer', 'teNer', 'oler', 'reGresar', 'besar', 'karGar', 'meter',     
    't#ner', 'tener', 'poner', 's#ntar', 'mirar', 'komer', 'filmar', 'koRer', 'Bientar',
    'salGar', 'jamar', 'traer', 'estorBar', 'storBar', 'andar', 'fixar', 'perar', 'Bajar'
]

other_pos_list = [ # others where you can remove the last leter used for adjectives
    'GorDo', 'una', 'ixa', 'otra', 'tuja', 'eja', 'toDa', 'g&pa', 'esa', 'rika', 'janta',
    'otra', 'ni|a', 'gorDa', 'roxa', 'Bonita', 'sola', 'Baxa', 'rapiDa', 'se|ora',
    'sposa', 'BlaNka', 'kasa', 'G&pa', 'kosa', 'seresa', 'amarija', 'amiGa', 'ermosa',
    'fea', 'lista', 'mia', 'poka', 'primera', 'B$na', 'alGa', 'b$na', 'kara', 'sapato'
]


not_confident_pos = [ # words that im not sure if i should switch or not
    'Baka', 'Dona', 'Gata', 'GloBa', 'baka', 'dona', 'gata', 'kamina', 'naranxa', 'kaReras',
    'pala', 'plata', 'saBrosa', 'sorpresa', 'tasa', 'Barka', 'Boka', 'DaDa', 'DeDa', 
    'G!ta', 'G$ra', 'Gaja', 'Gripa', 'caNga', 'fiGura', 'fruta', 'kaxa', 'kamara', 'BlaNka',
    'sanahoria', 'k$nta', 'mona', 'grandota', 'Granda', 'Grandota', 'saBrosa', 'kampana', 'kieto'
]

all_invalid = [ 
    "B/laNka", "B/eto", "D/ona", "B/u", "ka/Be", "as/", "ka/t", "D/i", "Ba/ja", "Ba/jan", "l/i/s", "pa/m", "pa/o", "pa/s", "miu/a", "tataRatat/a",
    "b/-la", "d/e", "d/i", "d/ile", "d/iles", "d/#s", "b/on/it/o", "b/is/te", "peD/r/it/o", "s/*/s", "ar/Bol", "baB/a", "kuakuaku/a", "|i/a",
    "Ba/kita", "B/onita", "B/isi", "ka/ti", "ka/Ro", "D/e", "B/ete", "b/en/te", "BeB/e", "B/onitas", "Gu/au", "ar/on", "laralar/a", "Bl/aNka",
    "D/ile", "b/aka", "d/onde", "tam/b#n", "tam/bor", "Ba/jas", "Ba/k/it/a", "fe/r", "selin/a", "B/uelita", "braB/o", "mari/e", "suleim/a",
    "D/on", "D/isen", "ka/", "B/erDaD", "D/ana", "ka/r", "B/ols/it/a", "Ba/rBariDaD", "B/olsita", "Dan/a", "Gu/a", "lueG/o", "seli/a", "BraB/o",
    "tam/ar", "Ba/mosa", "x/ita", "peD/ro", "B/is/te", "B/la/le", "B/iBe", "tra/B#so", "miGel/it/o", "mam/a", "gu/a", "gu/au", "seli/na", "peDrit/o",
    "b/$no", "b/aBa", "ka/R3", "D/aDos", "ka/ren", "b/#n", "B/axo", "mark/it/o/s", "mart/a", "s/$", "ar/te", "guaGu/a", "mxu/a", "tap/aDera",
    "b/ente", "Ba/rko", "Ba/rku", "ro/ko", "s/*s", "s/#/te", "par/aD/it/o", "b/onito", "s/%n", "ka/laBasita", "jamani/a", "klauDi/a", "bet/o",
    "met/elo", "b/raBo", "D/$rmelo", "D/entro", "mir/%m", "B/ente", "an/it/a", "b/#nes", "s/%", "trai/Go", "ar/turo", "oc/o", "re/Ga/l/o",
    "B/arko", "B/arku", "tra/Gona", "B/iBeron", "par/aD/it/o", "mi/r%m", "b/aler%", "aj/er", "n/o", "d/uer/me/l/a", "ol/a", "ramonsit/o",
    "B/arku", "D/os", "tom/", "b/en", "ka/xa", "b/u", "Ba/kas", "an/a", "an/it/a", "s/#", "s/!", "Bet/i", "Bet/o", "paulin/a", "siNk/o",
    "par/a", "ka/ju", "B/loke", "B/eBes", "mand/arina", "d/i/les", "d/i/le", "konex/it/o", "s/@", "i/r", "ka/mita", "peDr/it/o", "aor/a",
    "ka/cete", "met/", "B/or", "as/te", "D/an#la", "B/ino", "pi/pi", "B/onito", "kom/miGo", "s/al", "ka/mita", "ka/r/it/a", "ka/r/it/a/s", 
    "ka/ria", "ka/ritai", "ka/ri|ito", "ka/s/it/a", "ka/x/it/a", "kar/en", "kar/ne", "ku/m", "ku/a", "D/i/le/s", "D/i/le", "piopiopi/o",
    "ka/Rit3", "B/isto", "pas/tel", "s/i", "Ba/s", "peDr/o", "pedr/o", "t/en", "mar/i", "s/in", "B/ak/it/a", "lueGo", "braBo", 
    "b/aler", "Ba/ka", "B/raBo", "B/es", "d/ona", "B/-la", "mi/Go", "peD/rito", "mar/ta", "j/o", "j/a", "B/akita", "tr/e/s",
    "B/ak-", "B/akit+", "f/er", "par/aDos", "st/orBa", "anit/a", "lusi/a", "par/aDito", "kuatr/o", "n/i", "pap/a", "pa/pa", "pap/i", "pa/pi",
    "b/eto", "B/arBariDaD", "ka/m@n", "D/", "D/iles", "B/onitos", "mart/a", "selin/a", "saB/rosa", "si/ek", "si/n", "GuaGu/a",
    "B/eB", "D/onde", "Ba/k", "ka/Reras", "artur/o", "teres/o", "alfons/o", "ernest/o",  "saB/roso", "si/no", "si/o", "ka/ce/te",
    "D/#s", "B/iBi", "B/ern", "D/anae", "Ba/xo", "Ba/mosa", "ka/ri|/it/o", "ka/rl/it/o/s", "ka/rne", "pa/s", "maurici/o", "mi/ua", "mi/au",
    "as/ukarera", "ka/mina", "B/eti", "b/$n3", "alexandr/o", "s/e", "s/ul*", "mar/ia", "e/n", "s/o", "s/oi", "s/on",
    "b/um", "D/emas", "ka/ri", "ka/ri|itos", "B/$lta", "D/eDo", "ka/laBas/it/a", "B/-/l/a", "pi/c", "pi/e", "pi/k", "pi/n", "pi/o",
    "ka/rit", "B/oka", "B/um", "B/", "D/eDos", "Bl/oke", "D/ar@", "mari/a", "B/$l/it/a", "miGelit/o", "Dan/ae", "jam/ania", "up/a",
    "b/erDaD", "D/eDitos", "B/en", "ka/Bajo", "b/eBe", "tom/ate", "B#n/do", "D/an#/l/a", "ka/rlitos", "Dari/o", "paul/a", "sa/le",
    "b/eso", "D/el", "ka/mara", "tap/itit/it/a", "B/in#ron", "B/#n", "B/en/te", "l/*n", "ka/mpanita", "as/ukar", "ak/i", "ak/a", "aj/a", "aj/i",
    "ka/Ritu", "ka/jo", "B/#ne", "ka/e", "ka/Ru", "Ba/monos", "as/i", "B/ols/it/a", "Ba/k/it/a", "e/s", "Don/de", "D/ientes", "n/a",
    "B/#n", "D/exo", "Ba/kit+", "d/anae", "aB/er", "B/onit-", "B/onit+", "B/on/it/a", "ramons/it/o", "ale/iD/a", "aleiD/a", "teresit/a",
    "B/olsa", "ka/sa", "B/$no", "as/ta", "b/eBa", "D/ea", "B/eBe", "B/on/it/o", "B/on/it/a/s", "e/l", "Bist/e", "don/de", "teres/it/a",
    "kom/o", "d/os", "b/es", "B/ak-", "B/aka", "Ba/n", "Ba/mos", "Ba/k/it/a", "B/aj/a", "D/eD/it/o", "son", "B/olsita", "ku/al", "ir/a",
    "B/akas", "B/akit+", "p/onsela", "p/onselo", "ka/Ros", "Ba/mo/nos", "B/e/a", "Dan#l/a", "marian/a", "pa/ra", "BiB/i", "ar/a", "ast/a",
    "an/ita", "Ba/k-", "Ba/ka", "Ba/kas", "j/anta/s", "j/eGe", "j/i", "j/iji", "Bl/aNk/a", "ka/m/it/a", "B/iste", "kati/a", "pa/u",
    "ka/mpan/it/a", "ka/mpanit-", "ka/ntas", "Grand/e", "re/zBalaDija", "ki/en", "B/oi", "i/e", "no", "pa/n", "ka/ti", "ka/tia", "mar/ie"
]

special_dip_cases = ['estoi', 'mui', 'pio', 'pie', 'miau', 'aGua', 'mio', 'oJei', 'soi', 
                     'nio', 'katia', 'maria', 'Dio', 'Guau', 'aki', 'ai', 'na']

regular_verb_list = change_diphthongs(regular_verb_list)
other_pos_list = change_diphthongs(other_pos_list)
not_confident_pos = change_diphthongs(not_confident_pos)
all_invalid = change_diphthongs(all_invalid)



# grandote is this split up grand/ot/e?
# watch for bonita and bolsita, Bes/it3, make sure it catches
# make a way for them to go simultaneously?