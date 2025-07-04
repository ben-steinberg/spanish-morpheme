direct_change_array = [
    'ando', 'amos', 'emos', 'ir', 'imos', 
    '#ndo', 'ame', 'aste', 'arlo', 'erlo', 'irlo',
    'erla', 'arla', 'asela', 'aselo',
    'onselo', 'etela', 'atela', 'arle', 'erle', 
    'irle', 'amela', '$rmela', 'arlos', 'erlos', '#ron',
    'eron', 'aron', '$ron', 'iDo', 'itas', 'it+'
    ]  # all tested so far and with easy change

exceptions = { 
    'er': ['aBer', 'ker', 'per', 'ajer', 'fer'],
    'an': ['tan', 'pan', '|an'],
    'ar' : ['eDGar', 'itamar', "tamar"],
    'alos' : ['palos'],
    'aBa' : ['baBa'],
    'iste': ['triste'],
    'me': ['dexeme', 'pomme', 'ame', 'tome', 'kome'],
    'es': ['res', 'tres', 'Diles', 'diles', 'k#nes', 'koces', 
           'nenes', 'toRes','xuGetes', 'entonses', 's#Rales'],
    'ate': ['tomate', 'xitomate'],
    'arte': ['arte'],
    'ita': ['bonita', 'tapititita', 'anita', 'Bonita'],
    'ale': ['sale', 'orale', 'pres#nale', 'apacuRale', 'epale'],
    'ala': ['mala'], 
    'ito' : ['Bonito', 'miGelito', ' kito'], 
    'alo' : [], # s#Ralo
    'iDa' : ['rapi/Da'],
    'itos' : ['karlitos', 'markitos', 'Bonitos'], # ask about names
    's:' :  ['es', 'D#s', 'Dos', 'dos', 'k#s', 'lis', 'mas', 'nos', 'p$s', 'res', 's*s',
             'tres', 'aD@s', 'Demas', 'jolis', 'k#nes', 'naris', 'marcos',
             'm#ntras', 'entonses', 'karlitos', 'markitos', 'pakatelas',
             'pokatelas', 'platisamelos']
    }

cases = {
    'as' : ['Bas', 'Das', 'bas', 'stas', 'Bajas', 'estas', 
            'komas', 'peGas', 'x$gas', 'ajuDas'], # 'Bonitas'
    'a' : ['Ba', 'ba', 'da', 'sa', 'Dexa', 'dexa', 'Baja', 'mira', 'toma', 'peGa', 
           'pika', 'keDa', 'aBla', 'Gusta', 'kamara', 'B-la'],
    'en' : ['acen', 'k#ren', 'komen', 'ponen', 'traen', 'xuGen', 'rompen', 'asen'],
    '%n' : ['as%n'],
    }

regular_verb_list = [
    'Dar', 'dar', 'ecar', 'B-lar', 'armar', 'jeBar', 'jenar', 'jorar', 'BiBer', 'Diser',
    'kitar', 'aBlar', 'Blar', 'peGar', 'kumplir', 'BeBer', 'empuxar', 'Boltear', 'saBer',
    'kojar', 'p*nar', 'parar', 'pasar', 'sakar', 'tamar', 'tokar', 'akomoDar', 'reir',
    'tomar', 'Bar', 'Dexar', 'romper', 'poNgar', 'star', 'Buskar', 'apr#tar', 'pr#tar', 'pomer', 
    'xalar', 'xuGar', 'G&rDar', 'Gustar', 'sentar', 'aGaRar', 'GaRar', 'eskucar',
    'ajuDar', 'b-lar', 'B#ner', 'D$rmir', 'subir', 'suBir', 'esperar', 'oxearlo',
    'pasear', 'prestar', 'Bisitar', 'Golpear', 'dexar', 'aG&rDar', 'apacuRar',
    'ense|ar', 'haber', 'mandar', 'pokater', 'enoxer', 'kansar', 'azer',
    'aReGlar', 'estar', 'faltar', 's#Rar', 'aB#ntar', 'xirar', 'tr-er',
    'poDer', 'tapar', 'laBar', 'atoraste', 'tirar', 'pres#nar', # got rid of 'seR'
    'saluDar', 'enkontrar', 'Ber', 'ber', 'Baer', 'aser', 'keDar',
    'kaer', 'rekoxer', 'g&rDar', 'terminar', 'pakater', 'aBer',
    'meter', 'moBer', 'poner', 'Desaser', 'komponer', 'Desir', 
    'aBrir', 'peDir', 'salir', 'x$Gar', 'BriNkar', 'p$Der', 'sirBer',
    'G&rDar', 'pareser', 'Dormir', 'Besar', 'b-lar', 'biBir', 'DiBuxar', 
    'k#rer', 'akaBar', 'kerer', 'teNer', 'oler', 'reGresar', 'besar',
    't#ner', 'tener', 'poner', 's#ntar', 'mirar', 'komer', 'filmar', 'koRer',
    'salGar', 'jamar', 'traer', 'estorBar', 'storBar', 'andar', 'fixar', 'perar'
]

other_pos_list = [ # others where you can remove the last leter used for adjectives
    'GorD-', 'un-', 'ix-', 'otr-', 'tuj-', 'ej-', 'toD-', 'g&p-', 'es-', 'rik-', 
    'otr-', 'ni|-', 'gorD-', 'rox-', 'Bonit-', 'sol-', 'Bax-', 'rapiD-', 'se|or-',
    'spos-', 'BlaNk-', 'kas-', 'G&p-', 'kos-', 'seres-', 'amarij-', 'amiG-', 'ermos-',
    'fe-', 'list-', 'mi-', 'pok-', 'primer-', 'B$n-', 'alG-', 'b$n-'
]

not_confident_pos = [ # words that im not sure if i should switch or not
    'Bak-', 'Don-', 'Gat-', 'GloB-', 'bak-', 'don-', 'gat-', 'kamin-', 'jo', 'naranx-', 
    'pal-', 'plat-', 'saBros-', 'sorpres-', 'tas-', 'Bark-', 'Bok-', 'DaDo', 'DeDo', 
    'G!ta', 'G$r-', 'Gaj-', 'grandot-', 'Gripa', 'caNgo', 'fiGura',  'fruta', 'kaxa', 'kamara', 
    'sanahoria', 'k$nt-', 'mon-'
]

all_invalid = [ 
    "B/laNka", "B/eto", "D/ona", "B/u", "ka/Be", "as/", "ka/t", "D/i", "Ba/ja", "Ba/jan",
    "b/-la", "d/e", "d/i", "d/ile", "d/iles", "d/#s", "b/on/it/o", "b/is/te", "peD/r/it/o",
    "Ba/kit", "B/onit", "B/isi", "ka/ti", "ka/Ro", "D/e", "B/ete", "b/en/te", "BeB/e",
    "D/ile", "b/aka", "d/onde", "tam/b#n", "tam/bor", "Ba/jas", "Ba/k/it/a", "fe/r",
    "D/on", "D/isen", "ka/", "B/erDaD", "D/ana", "ka/r", "B/ols/it/a", "Ba/rBariDaD",
    "tam/ar", "Ba/mosa", "x/ita", "peD/ro", "B/is/te", "B/la/le", "B/iBe", "tra/B#so",
    "b/$no", "b/aBa", "ka/R3", "D/aDos", "B-l/a", "ka/ren", "b/#n", "B/axo",
    "b/ente", "Ba/rko", "Ba/rku", "ro/ko", "s/*s", "s/#/te", "par/aD/it/o", 
    "met/elo", "b/raBo", "D/$rmelo", "D/entro", "mir/%m", "B/ente", 
    "B/arko", "B/arku", "tra/Gona", "B/iBeron", "par/aD/it/o", "mi/r%m",
    "B/arku", "D/os", "tom/", "b/en", "ka/xa", "b/u", "Ba/kas", 
    "par/a", "ka/ju", "B/loke", "B/eBes", "mand/arina", "d/i/les", "d/i/le",
    "ka/cete", "met/", "B/or", "as/te", "D/an#la", "B/ino", 
    "ka/Rit3", "B/isto", "pas/tel", "s/i", "Ba/s",
    "b/aler", "Ba/ka", "B/raBo", "B/es", "d/ona", "B/-la",
    "B/ak-", "B/akit+", "f/er", "par/aDos", "st/orBa",
    "b/eto", "B/arBariDaD", "ka/m@n", "D/", "D/iles", "B/onitos", 
    "B/eB", "D/onde", "Ba/k", "ka/Reras",
    "D/#s", "B/iBi", "B/ern", "D/anae", "Ba/xo", "Ba/mosa", 
    "as/ukarera", "ka/mina", "B/eti", "b/$n3",
    "b/um", "D/emas", "ka/ri", "ka/ri|itos", "B/$lta", "D/eDo", 
    "ka/rit", "B/oka", "B/um", "B/", "D/eDos",
    "b/erDaD", "D/eDitos", "B/en", "ka/Bajo", "b/eBe", "tom/ate", 
    "b/eso", "D/el", "ka/mara", "met/a", "tap/itit/it/a",
    "ka/Ritu", "ka/jo", "B/#ne", "ka/e", "ka/Ru", "Ba/monos", "as/i", 
    "B/#n", "D/exo", "Ba/kit+",
    "B/olsa", "ka/sa", "B/$no", "as/ta", "b/eBa", "D/ea", "B/eBe", 
    "kom/o", "d/os", "b/es", "B/ak-", "B/aka",  
    "B/akas", "B/akit+", "p/onsela", "p/onselo", "kamar/a", "ka/Ros", 
    "an/ita", "Ba/k-", "Ba/ka", "Ba/kas", "j/anta/s", "j/eGe", "j/i", "j/iji"
]

# grandote is this split up grand/ot/e?