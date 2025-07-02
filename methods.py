import os 
from collections import Counter
import re
import string
from lists import exceptions

def find_endings(corpus, morpheme):
    # just prints endings for observation

    print()
    print("morpheme: ", morpheme)
    words_with_morpheme = []

    for line in corpus: 
        fit_line = line.rstrip("\n")
        split_line = fit_line.split(' ')

        for word in split_line:
            if word.endswith(morpheme) and len(word) > 1 and '/' not in word:
                words_with_morpheme.append(word)

    set_with_morpheme = set(words_with_morpheme)
    instance_number = 0

    sorted_words = sorted(set_with_morpheme, key=lambda word: (len(word), word))
    for line in sorted_words:
        instance_number += 1
        print(line)

    print(f'total instances of {morpheme}: {instance_number}')
    return instance_number

def count_words(corpus, show_slashes = True):
    words = []
    for line in corpus: 
        fit_line = line.rstrip("\n")
        splitted_line = fit_line.split(' ')
        
        for word in splitted_line:
            if '/' in word and not show_slashes:
                continue
            words.append(word)

    word_count = Counter(words)

    return word_count

def show_slashed(corpus, path):
    slashed = []
    non_slashed = []
    for line in corpus: 
        content = line.rstrip("\n")
        tokens = content.split(' ')
        for token in tokens: 
            if '/' in token:
                slashed.append(token)
            else:
                non_slashed.append(token)
    
    
            
    print()
    slashed_path = os.path.join(path, 'slashed.txt')
    with open(slashed_path, 'w') as file:
        for word in sorted(list(set(slashed))):
            print(word)
            file.write(word + '\n')

    non_path = os.path.join(path, 'non_slashed.txt')
    with open(non_path, 'w') as file:
        for word in sorted(list(set(non_slashed))):
            file.write(word + '\n')

def simple_add_slashes(corpus, morpheme, using_exceptions=True, choice_array=[], replaced_morpheme = ''):
    '''
    Use case for this is when it is a simple addition of /, or with exceptions or specific cases
    '''

    if replaced_morpheme == '':
        replaced_morpheme = morpheme

    new_corpus = []
    for line in corpus:
        
        # keep new line 
        has_new_line = line.endswith("\n")
        content = line.rstrip("\n")

        tokens = content.split(' ')
        new_tokens = []

        for token in tokens:
            
            base_word = token.rstrip(string.punctuation)
            punctuation_suffix = token[len(base_word):]

            if using_exceptions: 

                if (base_word.endswith(morpheme) and len(base_word) > len(morpheme)
                    and base_word not in choice_array): #  and '/' not in base_word
                    root = base_word[:-len(morpheme)]
                    if root.endswith('/'):
                        new_word = f"{root}{replaced_morpheme}"
                    else: 
                        new_word = f"{root}/{replaced_morpheme}"
                else:
                    new_word = base_word

            else: 
                if (base_word.endswith(morpheme) and len(base_word) > len(morpheme) and not using_exceptions
                  and base_word in choice_array): #  and '/' not in base_word
                    root = base_word[:-len(morpheme)]
                    if root.endswith('/'):
                        new_word = f"{root}{replaced_morpheme}"
                    else:
                        new_word = f"{root}/{replaced_morpheme}"

                    
                else:
                    new_word = base_word

            new_tokens.append(new_word + punctuation_suffix)

        new_line = ' '.join(new_tokens)
        
        if has_new_line:
            new_line += "\n"
        new_corpus.append(new_line)

    return new_corpus

def add_in_section(corpus, cut_morpheme, morpheme, exceptions):
    
    # Uses the larger morpheme to identify endings and then splits the word by the cut_morpheme,

    new_corpus = []
    for line in corpus:
        has_nl = line.endswith("\n")
        content = line.rstrip("\n")

        parts = content.split(' ')
        new_parts = []
        for part in parts:
            base_word = part.rstrip(string.punctuation)
            punctuation_suffix = part[len(base_word):]

            if (base_word.endswith(morpheme)
                and len(base_word) > len(morpheme)
                and base_word not in exceptions
                and '/' not in base_word):
                root = base_word[:-len(cut_morpheme)]
                new_word = f"{root}/{cut_morpheme}"
            else:
                new_word = base_word

            new_parts.append(new_word + punctuation_suffix)

        new_line = ' '.join(new_parts)
        if has_nl:
            new_line += "\n"
        new_corpus.append(new_line)

    return new_corpus

def find_intersection(corpus, m1, m2):
    # this might lead to something like for instance with the suffix a and o
    # if the same words are there it could save time
    m1_array = []
    m2_array = []
    for line in corpus:
        splitted_line = line.split(' ')
        for word in splitted_line: 
            if word.endswith(m1) and '/' not in word and len(word) > len(m1):
                m1_array.append(word[:-len(m1)])
            if word.endswith(m2) and '/' not in word and len(word) > len(m2):
                m2_array.append(word[:-len(m2)])

    intersection_array = []

    for stem in set(m1_array): 
        if stem in set(m2_array): 
            intersection_array.append(stem)

    for intersection in intersection_array:
        print(intersection)

    return intersection_array

def infinitive_break(corpus, pos_list, break_off_amount, exceptions = []):
    # idea here is to use .startswith to break off the endings
    # potential problems would be words like ko.mo or verbs that have a stem change
    new_corpus = []
    stem_list = [inf[:-break_off_amount] for inf in pos_list]
    stem_list = sorted(stem_list, key = len, reverse = True)
    slashed_words = []
    for line in corpus:
        has_new_line = line.endswith("\n")
        content = line.rstrip("\n")

        tokens = content.split(' ')
        new_tokens = []

        for token in tokens:
            
            base_word = token.rstrip(string.punctuation)
            punctuation_suffix = token[len(base_word):]

            for stem in stem_list: 
                if (token.startswith(stem) and len(token) > len(stem)
                    and '/' not in token):

                    slashed_base = slash_pronouns(base_word, stem)
                    plural_tagged = check_plural(base_word)
                    if break_off_amount == 2:
                        suffix = slashed_base[len(stem):]

                    else:
                        suffix = base_word[len(stem):]
                        suffix = plural_tagged[len(stem):]
                    
                    if suffix.startswith('/'):
                        # print("HERE SUFFIX:", suffix)
                        # print("BASE WORD: ", base_word)
                        suffix = suffix[1:]

                    new_word = f"{stem}/{suffix}"

                    if new_word not in exceptions:
                    # print("NEW WORD: ", new_word)
                        slashed_words.append(new_word)        
                        break
                    else: 
                        new_word = base_word
                else: 
                    new_word = base_word

            new_tokens.append(new_word + punctuation_suffix)

        new_line = ' '.join(new_tokens)
        
        if has_new_line:
            new_line += "\n"
        new_corpus.append(new_line)

    return new_corpus

def slash_pronouns(word, stem):
    # i want this to go in the infinitive break function and check if it can remove it
    # aim is to return the suffix slashed up
    suffix = word[len(stem):]
    pronoun_array = []
    pronoun_list = ['los', 'las', 'nos', 'me', 'te', 'le', 'se', 'les', 'lo', 'la', 'l*', 'l3']
    for i in range(2):
        for pronoun in pronoun_list: 
            if suffix.endswith(pronoun) and not suffix.endswith('aste'):
                pronoun_array.append(pronoun)
                suffix = suffix[:-len(pronoun)]
                break

    pronoun_array.reverse()

    parts = [stem + suffix] + pronoun_array
    combined = "/".join(parts)

    return combined

def check_plural(word):
    if word.endswith('s'):
        prefix = word[:-1] 
        new_word = prefix + '/s'
        return new_word
    return word
    

def see_percentage_checked(corpus, will_print = False):
    # returns slashed words
    total_words = []
    slashed_words = []
    for line in corpus: 
        splitted_line = line.split(' ')
        for word in splitted_line:
            if '/' in word: 
                slashed_words.append(word)

            in_exception = False
            for key in exceptions.keys():
                if word in key:
                    in_exception = True

            if len(word) > 1 and not in_exception:
                total_words.append(word)

    unique_slashed_words = set(slashed_words)
    unique_total_words = set(total_words)

    if will_print:
        print(f"slashed: {len(slashed_words)} total: {len(total_words)} percentage completed: {len(slashed_words) / len(total_words) * 100}%")
        print(f"unique slashed: {len(unique_slashed_words)} unique total: {len(unique_total_words)} percentage completed: {len(unique_slashed_words) / len(unique_total_words) * 100}%")
    
    return slashed_words

def write_new_corpus(modified_corpus, path):
    new_path = os.path.join(path, 'modified_corpus.txt')
    with open(new_path, 'w') as file:
        for line in modified_corpus:
            file.write(line)
