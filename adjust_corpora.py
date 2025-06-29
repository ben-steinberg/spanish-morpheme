import os 
from lists import direct_change_array, exceptions, cases, regular_verb_list, all_invalid, other_pos_list
from methods import find_endings, simple_add_slashes, count_words, infinitive_break
from methods import find_intersection, see_percentage_checked, write_new_corpus, show_slashed

path = os.path.dirname(os.path.abspath(__file__)) 
corpus_path = os.path.join(path, 'corpus.txt')

with open(corpus_path, 'r') as file:
    corpus = file.readlines()

modified_corpus = corpus

# for morpheme in direct_change_array: 
#     find_endings(modified_corpus, morpheme)
#     modified_corpus = simple_add_slashes(modified_corpus, morpheme)

# for morpheme, choice_array in exceptions.items(): 
#     find_endings(modified_corpus, morpheme)
#     modified_corpus = simple_add_slashes(modified_corpus, morpheme, True, choice_array)

# for morpheme, choice_array in cases.items():
#     find_endings(modified_corpus, morpheme)
#     modified_corpus = simple_add_slashes(modified_corpus, morpheme, False, choice_array)


modified_corpus = infinitive_break(modified_corpus, other_pos_list, 1)

modified_corpus = infinitive_break(modified_corpus, regular_verb_list, 2, all_invalid)

# find_endings(modified_corpus, 'ita')
modified_corpus = simple_add_slashes(modified_corpus, 'ita', True, ['bonita', 'tapititita', 'anita', 'Bonita'], 'it/a')

# find_endings(modified_corpus, 'ito')
modified_corpus = simple_add_slashes(modified_corpus, 'ito', True, ['Bonito', 'miGelito', ' kito'], 'it/o')

# find_endings(modified_corpus, 'itas')
modified_corpus = simple_add_slashes(modified_corpus, 'itas', True, [], 'it/a/s')

# find_endings(modified_corpus, 'itos')
modified_corpus = simple_add_slashes(modified_corpus, 'itos', True, ['karlitos', 'markitos', 'Bonitos'], 'it/o/s')

# find_endings(modified_corpus, 'a')
# modified_corpus = simple_add_slashes(modified_corpus, 'a')

# find_endings(modified_corpus, 'o')
# modified_corpus = simple_add_slashes(modified_corpus, 'a')

# find_endings(modified_corpus, 's')
# modified_corpus = simple_add_slashes(modified_corpus, 'a')



# print(count_words(modified_corpus, False))

find_endings(modified_corpus, 's')


show_slashed(modified_corpus, path)

see_percentage_checked(modified_corpus, True)

write_new_corpus(modified_corpus, path)



'''
Words to watch out for: 
an.do - p$s jo tam.b#n an.do Bus.kan.do +  ni.|o % m# spo.sa 3.Ga no a 
Ba.er - could be va a ver but thats a stretch
per - could be short for perro but is unclear
a.Ber - a ver split up
Bajas - bajar is a verb, but usually capital B implies v
ko.mas - uses opposite ending because it's dont eat!!
pom.me ponme?
t$ res
xi.to.ma.te
would darmela be split into d/armela or dar/mela
im assuming for now d/armela
xi.ta of i.xi.ta or hijita
ta.p/i.t/i.t/i.t/a
Bla.le - most likely hablar 
o.ra.le ??
pre.s#.na.le
a.pa.cu.Ra.le
o.xi.tos - leaves possibly hojitos
s#.Ra.lo - close it maybe?
s#.ron
WATCH FOR INFINITIVE VERBS THAT CAN ALSO BE NOUNS EG PODER
a.yer


Questions: 
How do we do poner which goes directly to pon

in infinitive: 
can use 'te.ner', 'pon.er' because ten and pon are valid 
ten and pon/

Di/le? D/ile?

ko.mo
se.Ra.mos ???? s/e.Ra.mos or se.R/a.mos
Same with a.re.mos
para --> parar or para (for)
B.es and B.es meaning sees and time

Would comida which comes from comer be split to com/ida?

If we change cosa into cosita and cosita's divide is cos/ita does that mean cosas divide should also be cos/ita
'''

'''
Actual questions for meeting: 

Irregular imperative verbs: 
decir, normally dec/ir would become di. do we add a slash at all?

voy a dec/ir

s/er/a split future into this


for poner and tener, they become pon and ten. would we just add the slash at the end? it's usually pon.lo or ten.lo

Clarify on splitting up like bonit/o versus bonit/a
How does future tense work? do we split sera into s/era or ser/a or s/er/a?

For dimunitives, do we create a boundary for names? 
mar.ko --> mar.ki.tos, so does that mean mar.k/o?
Example for dimunitives for nouns: 
cos/a becomes cos/it/a but does that imply cos/a?
For nouns from adjectives such as ko.mi.da, would we separate 
that into what ko.mer is separated into? ko.m/i.d/a yes split 
Ask for definition of s#.Rar
B/ending also implies that children won't be able to see the difference between
present tense ver and ir
and how are they supposed to associate f/$ with ser/ir from this?

f/ue no. dont take complete irregulars 

/it/o
cas/a
habl/ar/e

Things to work on: 
Finding and getting rid of plurals

allowing for multiple slashes. especially for words like xijito that need multiple splits

'''