from methods import change_diphthongs

regular_verb_list = [
    'Dar', 'dar', 'ecar', 'B-lar', 'armar', 'jeBar', 'jenar', 'jorar', 'BiBer', 'Diser',
    'kitar', 'aBlar', 'Blar', 'peGar', 'kumplir', 'BeBer', 'empuxar', 'Boltear', 'saBer',
    'kojar', 'p*nar', 'parar', 'pasar', 'sakar', 'tamar', 'tokar', 'akomoDar', 'reir',
    'tomar', 'Bar', 'Dexar', 'romper', 'poNgar', 'star', 'Buskar', 'apr#tar', 'pr#tar', 'pomer', 
    'xalar', 'xuGar', 'G&rDar', 'Gustar', 'sentar', 'aGaRar', 'GaRar', 'eskucar', 'mueBer'
    'ajuDar', 'b-lar', 'B#ner', 'D$rmir', 'subir', 'suBir', 'esperar', 'oxear', 'seRar',
    'pasear', 'prestar', 'Bisitar', 'Golpear', 'dexar', 'aG&rDar', 'apacuRar', 'dormir',
    'ense|ar', 'haber', 'mandar', 'pokater', 'enoxer', 'kansar', 'azer', 'Biner',
    'aReGlar', 'estar', 'faltar', 's#Rar', 'aB#ntar', 'xirar', 'tr-er', 'Baxar',
    'poDer', 'tapar', 'laBar', 'atoraste', 'tirar', 'pres#nar', 'atorar', # got rid of 'seR'
    'saluDar', 'enkontrar', 'Ber', 'ber', 'Baer', 'aser', 'keDar', 'aserkar',
    'kaer', 'rekoxer', 'g&rDar', 'terminar', 'pakater', 'aBer', 'kajar',
    'meter', 'moBer', 'poner', 'Desaser', 'komponer', 'Desir', '$Gar',
    'aBrir', 'peDir', 'salir', 'x$Gar', 'BriNkar', 'p$Der', 'sirBer', 'Bestir',
    'G&rDar', 'pareser', 'Dormir', 'Besar', 'biBir', 'DiBuxar', 
    'k#rer', 'akaBar', 'kerer', 'teNer', 'oler', 'reGresar', 'besar', 'karGar',
    't#ner', 'tener', 'poner', 's#ntar', 'mirar', 'komer', 'filmar', 'koRer',
    'salGar', 'jamar', 'traer', 'estorBar', 'storBar', 'andar', 'fixar', 'perar'
]

other_pos_list = [ # others where you can remove the last leter used for adjectives
    'GorDo', 'una', 'ixa', 'otra', 'tuja', 'eja', 'toDa', 'g&pa', 'esa', 'rika', 
    'otra', 'ni|a', 'gorDa', 'roxa', 'Bonita', 'sola', 'Baxa', 'rapiDa', 'se|ora',
    'sposa', 'BlaNka', 'kasa', 'G&pa', 'kosa', 'seresa', 'amarija', 'amiGa', 'ermosa',
    'fea', 'lista', 'mia', 'poka', 'primera', 'B$na', 'alGa', 'b$na', 'kara'
]


not_confident_pos = [ # words that im not sure if i should switch or not
    'Baka', 'Dona', 'Gata', 'GloBa', 'baka', 'dona', 'gata', 'kamina', 'naranxa', 
    'pala', 'plata', 'saBrosa', 'sorpresa', 'tasa', 'Barka', 'Boka', 'DaDa', 'DeDa', 
    'G!ta', 'G$ra', 'Gaja', 'Gripa', 'caNga', 'fiGura', 'fruta', 'kaxa', 'kamara', 
    'sanahoria', 'k$nta', 'mona', 'grandota', 'Granda', 'Grandota', 'saBrosa', 'kampana'
]

all_invalid = [ 
    "B/laNka", "B/eto", "D/ona", "B/u", "ka/Be", "as/", "ka/t", "D/i", "Ba/ja", "Ba/jan", "l/i/s",
    "b/-la", "d/e", "d/i", "d/ile", "d/iles", "d/#s", "b/on/it/o", "b/is/te", "peD/r/it/o", "s/*/s",
    "Ba/kita", "B/onita", "B/isi", "ka/ti", "ka/Ro", "D/e", "B/ete", "b/en/te", "BeB/e", "B/onitas",
    "D/ile", "b/aka", "d/onde", "tam/b#n", "tam/bor", "Ba/jas", "Ba/k/it/a", "fe/r", "selin/a",
    "D/on", "D/isen", "ka/", "B/erDaD", "D/ana", "ka/r", "B/ols/it/a", "Ba/rBariDaD", "B/olsita"
    "tam/ar", "Ba/mosa", "x/ita", "peD/ro", "B/is/te", "B/la/le", "B/iBe", "tra/B#so", "miGel/it/o",
    "b/$no", "b/aBa", "ka/R3", "D/aDos", "ka/ren", "b/#n", "B/axo", "mark/it/o/s", "mart/a", "s/$",
    "b/ente", "Ba/rko", "Ba/rku", "ro/ko", "s/*s", "s/#/te", "par/aD/it/o", "b/onito", "s/%n", "ka/laBasita",
    "met/elo", "b/raBo", "D/$rmelo", "D/entro", "mir/%m", "B/ente", "an/it/a", "b/#nes", "s/%",
    "B/arko", "B/arku", "tra/Gona", "B/iBeron", "par/aD/it/o", "mi/r%m", "b/aler%", "aj/er", 
    "B/arku", "D/os", "tom/", "b/en", "ka/xa", "b/u", "Ba/kas", "an/a", "an/it/a", "s/#", "s/!",
    "par/a", "ka/ju", "B/loke", "B/eBes", "mand/arina", "d/i/les", "d/i/le", "konex/it/o", "s/@",
    "ka/cete", "met/", "B/or", "as/te", "D/an#la", "B/ino", "pi/pi", "B/onito", "kom/miGo", "s/al",
    "ka/Rit3", "B/isto", "pas/tel", "s/i", "Ba/s", "peDr/o", "pedr/o", "t/en", "mar/i", "s/in",
    "b/aler", "Ba/ka", "B/raBo", "B/es", "d/ona", "B/-la", "mi/Go", "peD/rito", "mar/ta", "j/o", "j/a",
    "B/ak-", "B/akit+", "f/er", "par/aDos", "st/orBa", "anit/a", "lusi/a", "par/aDito", 
    "b/eto", "B/arBariDaD", "ka/m@n", "D/", "D/iles", "B/onitos", "mart/a", "selin/a", "saB/rosa",
    "B/eB", "D/onde", "Ba/k", "ka/Reras", "artur/o", "teres/o", "alfons/o", "ernest/o",  "saB/roso",
    "D/#s", "B/iBi", "B/ern", "D/anae", "Ba/xo", "Ba/mosa", "ka/ri|/it/o", "ka/rl/it/o/s", "ka/rne",
    "as/ukarera", "ka/mina", "B/eti", "b/$n3", "alexandr/o", "s/e", "s/ul*", "mar/ia", 
    "b/um", "D/emas", "ka/ri", "ka/ri|itos", "B/$lta", "D/eDo", "ka/laBas/it/a", "B/-/l/a",
    "ka/rit", "B/oka", "B/um", "B/", "D/eDos", "Bl/oke", "D/ar@", "mari/a", "B/$l/it/a", "miGelit/o",
    "b/erDaD", "D/eDitos", "B/en", "ka/Bajo", "b/eBe", "tom/ate", "B#n/do", "D/an#/l/a", "ka/rlitos",
    "b/eso", "D/el", "ka/mara", "met/a", "tap/itit/it/a", "B/in#ron", "B/#n", "B/en/te", "l/*n",
    "ka/Ritu", "ka/jo", "B/#ne", "ka/e", "ka/Ru", "Ba/monos", "as/i", "B/ols/it/a", "Ba/k/it/a",
    "B/#n", "D/exo", "Ba/kit+", "d/anae", "aB/er", "B/onit-", "B/onit+", "B/on/it/a", "ramons/it/o",
    "B/olsa", "ka/sa", "B/$no", "as/ta", "b/eBa", "D/ea", "B/eBe", "B/on/it/o", "B/on/it/a/s", 
    "kom/o", "d/os", "b/es", "B/ak-", "B/aka", "Ba/n", "Ba/mos", "Ba/k/it/a", "B/aj/a", "D/eD/it/o",
    "B/akas", "B/akit+", "p/onsela", "p/onselo", "kamar/a", "ka/Ros", "Ba/mo/nos", "B/e/a", "Dan#l/a",
    "an/ita", "Ba/k-", "Ba/ka", "Ba/kas", "j/anta/s", "j/eGe", "j/i", "j/iji", "Bl/aNk/a", "ka/m/it/a", 
    "ka/mpan/it/a", "ka/mpanit-", "ka/ntas", "Grand/e", "re/zBalaDija", "ki/en", "B/oi",
]

regular_verb_list = change_diphthongs(regular_verb_list)
other_pos_list = change_diphthongs(other_pos_list)
not_confident_pos = change_diphthongs(not_confident_pos)
all_invalid = change_diphthongs(all_invalid)



# grandote is this split up grand/ot/e?
# watch for bonita and bolsita, Bes/it3, make sure it catches
# make a way for them to go simultaneously?