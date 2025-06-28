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
    'Dar', 'dar', 'ecar', 'B-lar', 'armar', 'jeBar', 'jenar', 'jorar', 'kitar', 'aBlar', 'peGar', 'kumplir',
    'kojar', 'p*nar', 'parar', 'pasar', 'sakar', 'tamar', 'tokar', 'tomar', 'Bar', 'Dexar', 'romper', 'poNgar'
    'xalar', 'xuGar', 'G&rDar', 'Gustar', 'sentar', 'aGaRar', 'ajuDar', 'b-lar', 'B#ner', 'D$rmir',
    'pasear', 'prestar', 'Bisitar', 'Golpear', 'dexar', 'aG&rDar', 'ense|ar', 'haber', 'mandar', 'pokater',
    'aReGlar', 'estar', 'faltar', 's#Rar', 'aB#ntar', 'seR', 'xirar', 'poDer', 'tapar', 'laBar', 'tirar', 
    'saluDar', 'enkontrar', 'Ber', 'ber', 'Baer', 'aser', 'kaer', 'rekoxer', 'g&rDar', 'terminar', 'pakater'
    'meter', 'moBer', 'poner', 'Desaser', 'komponer', 'Desir', 'aBrir', 'peDir', 'salir', 'x$Gar', 'BriNkar'
    'G&rDar', 'pareser', 'Dormir', 'Besar', 'b-lar', 'biBir', 'DiBuxar', 'k#rer', 'akaBar', 'kerer',  
    't#ner', 'tener', 'poner', 's#ntar', 'mirar', 'komer',  'star', 'salGar', 'jamar', 'traer'
]

other_pos_list = [ # others where you can remove the last leter used for adjectives
    'GorD-', 'un-', 'ix-', 'otr-', 'tuj-', 'ej-', 'toD-', 'g&p-', 'est-', 'es-', 'rik-', 
    'otr-', 'rox', 'ni|-', 'gorD-', 'st-', 'rox-', 'Bonit-', 'sol-'
]

all_invalid = [ 
    "B/laNka", "B/eto", "D/ona", "B/u", "ka/Be", "as/", "ka/t", "b/-la", "d/e", "d/i", "d/ile", "d/iles"
    "Ba/kit", "B/onit", "B/isi", "ka/ti", "ka/Ro", "D/e", "B/ete", "D/ile", "b/aka", "d/onde", 
    "D/on", "D/isen", "ka/", "B/erDaD", "D/ana", "B/ea", "ka/r", "tam/ar", "Ba/mosa", "x/ita",
    "b/$no", "b/aBa", "ka/R3", "D/aDos", "B-l/a", "ka/ren", "b/#n", "b/ente", "Ba/rko", "Ba/rku",
    "met/elo", "b/raBo", "D/$rmelo", "D/entro", "mir/%m", "B/ente", "B/arko", "B/arku", "tra/Gona",
    "B/arku", "D/os", "tom/", "b/en", "ka/xa", "b/u", "Ba/kas", "par/a", "ka/ju", "B/loke", "B/eBes", 
    "ka/cete", "met/", "B/or", "as/te", "D/an#la", "B/ino", "ka/Rit3", "B/isto", "pas/tel",
    "b/aler", "Ba/ka", "B/raBo", "B/es", "d/ona", "B/-la","B/ak-", "B/akit+", "f/er", "par/aDos",
    "b/eto", "B/arBariDaD", "ka/m@n", "D/", "D/iles", "B/onitos", "B/eB", "D/onde", "Ba/k", "ka/Reras",
    "D/#s", "B/iBi", "B/ern", "D/anae", "Ba/xo", "Ba/mosa", "as/ukarera", "ka/mina", "B/eti", "b/$n3",
    "b/um", "D/emas", "ka/ri", "ka/ri|itos", "B/$lta", "D/eDo", "ka/rit", "B/oka", "B/um", "B/", "D/eDos",
    "b/erDaD", "D/eDitos", "B/en", "ka/Bajo", "b/eBe", "tom/ate", "b/eso", "D/el", "ka/mara", "met/a",
    "ka/Ritu", "ka/jo", "B/#ne", "ka/e", "ka/Ru", "Ba/monos", "as/i", "B/#n", "D/exo", "Ba/kit+",
    "B/olsa", "ka/sa", "B/$no", "as/ta", "b/eBa", "D/ea", "B/eBe", "kom/o", "d/os", "b/es", "B/ak-", "B/aka",  
    "B/akas", "B/akit+", "p/onsela", "p/onselo", "kamar/a", "ka/Ros", "an/ita", "Ba/k-", "Ba/ka", "Ba/kas"
]

# remove dots from corpus
# add second slashes for it/o
# pon/me/lo 