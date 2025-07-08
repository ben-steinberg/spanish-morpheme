import os 
from lists import direct_change_array, exceptions, cases
from lists import regular_verb_list, all_invalid, other_pos_list, not_confident_pos
from methods import find_endings, simple_add_slashes, count_words, infinitive_break, contains_word
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

modified_corpus = infinitive_break(modified_corpus, regular_verb_list, 2, all_invalid)

combined_pos_list = other_pos_list + not_confident_pos
print("COMBINED: ", combined_pos_list)

modified_corpus = infinitive_break(modified_corpus, combined_pos_list, 1, all_invalid)

modified_corpus = simple_add_slashes(modified_corpus, 'ititita', True, [], 'it/it/it/a')

modified_corpus = simple_add_slashes(modified_corpus, 'ita', True, ['bonita', 'tapititita', 'anita', 'Bonita'], 'it/a')

modified_corpus = simple_add_slashes(modified_corpus, 'ito', True, ['Bonito', 'miGelito', 'kito', 'Pedrito'], 'it/o')

modified_corpus = simple_add_slashes(modified_corpus, 'itas', True, [], 'it/a/s')

modified_corpus = simple_add_slashes(modified_corpus, 'iDa', True, [], 'iD/a')

modified_corpus = simple_add_slashes(modified_corpus, 'itos', True, ['karlitos', 'markitos', 'Bonitos'], 'it/o/s')

# a_endings = find_endings(modified_corpus, 'a') # make sure this is good
# modified_corpus = infinitive_break(modified_corpus, a_endings, 1, ['anit/a', 'lusi/a', 'mart/a', 'selin/a'])
modified_corpus = simple_add_slashes(modified_corpus, 'a', True, ['anita', 'lusia', 'marta', 'selina'])

modified_corpus = simple_add_slashes(modified_corpus, 'isimo')

o_endings = find_endings(modified_corpus, 'o')
modified_corpus = infinitive_break(modified_corpus, o_endings, 1, all_invalid)

modified_corpus = simple_add_slashes(modified_corpus, 'DaD')

# print(count_words(modified_corpus, False))

# find_endings(modified_corpus, 'os')


show_slashed(modified_corpus, path)

'''
Words with alternative meanings: 

Bes, para, Bebe, seR/amos CHECK THIS

'''
# contains_word(modified_corpus, 'Bes')

# from here, a way to make it so that you can divide the words based on the instance

see_percentage_checked(modified_corpus, True)

write_new_corpus(modified_corpus, path)


'''
New questions: 
if we are splitting up all words based by ending, how do we 
account for Bino which is venir in past third person? would it
be Bin/o?
Do we split up the indr and dir pronouns in verbs? pon/me/l/o? pon/se/l/a/s?
di/l/e/s?
'''


'''
Words to watch out for: 
st/os


in infinitive: 
can use 'te.ner', 'pon.er' because ten and pon are valid 
ten and pon/

Di/le? D/ile?

ko.mo
se.Ra.mos ???? s/e.Ra.mos or se.R/a.mos --> s/e.R/a.mos
Same with a.re.mos
para --> parar or para (for)

Would comida which comes from comer be split to com/ida?
com/id/a


Actual questions for meeting: 

Irregular imperative verbs: 
decir, normally dec/ir would become di. do we add a slash at all?
no just keep it di

s/er/a split future into this


Clarify on splitting up like bonit/o versus bonit/a

B/ending also implies that children won't be able to see the difference between
present tense ver and ir
and how are they supposed to associate f/$ with ser/ir from this?

f/ue no. dont take complete irregulars 

/it/o
cas/a
habl/ar/e

'''