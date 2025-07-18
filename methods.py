import os 
from collections import Counter
import re
import string

def change_diphthongs(corpus):

    diphthong_dict = {'%' : 'ia',  '#' : 'ie', '@' : 'io',
                      '$' : 'ue', '&' : 'ua', '!' : 'ui',
                      '*' : 'ei', '+' : 'au','-' : 'ai',
                      '3' : 'oi'}

    modified_corpus = [] 

    for line in corpus:
        split_line = line.split(' ')
        adjusted_words_in_line = []

        for word in split_line:
            split_word = list(word)
            adjusted_split_word = [] 

            for char in split_word: 
                if char in diphthong_dict:

                    adjusted_split_word.append(diphthong_dict[char])
                else:
                    adjusted_split_word.append(char)

            adjusted_word = "".join(adjusted_split_word) 
            adjusted_words_in_line.append(adjusted_word)

        joined_line_string = " ".join(adjusted_words_in_line) 
        modified_corpus.append(joined_line_string)

    return modified_corpus 

def move_dip_letters(corpus, cases):
    diphthong_endings = ['ia', 'ie', 'io', 'ue', 'ua',
                         'ui', 'ei', 'au', 'ai', 'oi']

    all_words_set = set()
    for line in corpus:
        words_in_line = line.split(' ')
        for word in words_in_line:
            cleaned_word_for_lookup = word.strip(string.punctuation + '\n')
            if cleaned_word_for_lookup:
                all_words_set.add(cleaned_word_for_lookup)
    
    not_valid = ['ie', 'sto', 'io', 'marianai', 'otrai', 
                 'pau', 'ste', 'pojoi', 'ajai', 'Gustoi', 'stos']
    for word in not_valid:
        if word in all_words_set: 
            all_words_set.remove(word)
    print(all_words_set)


    modified_corpus = []

    for i, line in enumerate(corpus):
        split_line = line.split(' ')
        new_split_line = []
        j = 0

        while j < len(split_line):
            current_word_original = split_line[j]

            ends_with_newline = current_word_original.endswith('\n')

            word_base = current_word_original.rstrip('\n')

            found_diphthong_split = False
            if word_base:

                if word_base in cases:
                    new_split_line.append(current_word_original)
                    found_diphthong_split = True
                else:
                    for dip in diphthong_endings:
                        

                        if word_base.endswith(dip) and len(word_base) > len(dip):

                            shorter_word_base = word_base[:-1]
                            char_to_move = word_base[-1]

                            if j + 1 < len(split_line):
                                next_word_original = split_line[j+1]
                                next_word_ends_with_newline = next_word_original.endswith('\n')
                                next_word_for_mod = next_word_original.rstrip('\n')
                                modified_next_word = char_to_move + next_word_for_mod

                            # checks if both current and next word valid 
                            
                            
                            if shorter_word_base in all_words_set and modified_next_word and modified_next_word in all_words_set:
                                new_word_part1 = shorter_word_base
                                if ends_with_newline:
                                    new_word_part1 += '\n'
                                new_split_line.append(new_word_part1)


                                if j + 1 < len(split_line):

                                    if next_word_ends_with_newline:
                                        modified_next_word += '\n'

                                    split_line[j+1] = modified_next_word
                                else:
                                    new_split_line.append(char_to_move)

                                found_diphthong_split = True
                                break
                            elif (shorter_word_base in all_words_set and modified_next_word 
                                  and modified_next_word not in all_words_set 
                                  and char_to_move in all_words_set):
                                
                                # print("here in elif at line", i)
                                # print('new word p1 ', new_word_part1)
                                # print('char ', char_to_move)
                                # print('next word ', next_word_for_mod)
                                new_word_part1 = shorter_word_base
                                if ends_with_newline: 
                                    new_word_part1 != '\n'
                                new_split_line.append(new_word_part1)
                                new_split_line.append(char_to_move)
                                new_split_line.append(next_word_for_mod)

                                                

                        elif (len(word_base) == len(dip) and word_base.startswith(dip) and shorter_word_base in all_words_set 
                              and modified_next_word in all_words_set and next_word_for_mod not in all_words_set):
                            # print("shorter word Base: ", shorter_word_base)
                            # print('modified next word', modified_next_word)
                            if word_base == 'ie':
                                print("HERE")
                                print('modified next', modified_next_word)
                                print("char to move :", char_to_move)
                                print("next word for mod: ", next_word_for_mod)
                                print("line adjusted: ", i + 1)
                            new_split_line.append(shorter_word_base)
                            new_split_line.append(modified_next_word)


                           
                                
            if not found_diphthong_split:
                new_split_line.append(current_word_original)

            j += 1

        modified_corpus.append(" ".join(new_split_line))

    return modified_corpus
 


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
    print()
    return sorted_words

def contains_word(corpus, word):
    lines = []
    for line in corpus:
        fit_line = line.rstrip("\n")
        split_line = fit_line.split(' ')

        if word in split_line:
            lines.append(split_line)


    for i, line in enumerate(lines):
        final_string = ''
        for word in line:
            final_string = final_string + ' ' + word
        print(f"Instance {i}: {final_string}")
    print()

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
            
            base_word = token
            punctuation_suffix = token[len(base_word):]

            if using_exceptions: 

                if (base_word.endswith(morpheme) and len(base_word) > len(morpheme)): #  and '/' not in base_word
                    root = base_word[:-len(morpheme)]
                    if root.endswith('/'):
                        new_word = f"{root}{replaced_morpheme}"
                    else: 
                        new_word = f"{root}/{replaced_morpheme}"
                else:
                    new_word = base_word

                if new_word in choice_array: 
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
                and '/' not in base_word):
                root = base_word[:-len(cut_morpheme)]
                new_word = f"{root}/{cut_morpheme}"
            else:
                new_word = base_word

            if new_word in exceptions: 
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
            

            base_word = token
            punctuation_suffix = token[len(base_word):]

            for stem in stem_list: 
                if (token.startswith(stem) and len(token) > len(stem)
                    and '/' not in token):

                    # slashed_base = slash_future(base_word, stem)
                    slashed_base = slash_pronouns(base_word, stem)
                    plural_tagged = check_plural(base_word)

                    if break_off_amount == 2:
                        suffix = slashed_base[len(stem):]
                        if len(suffix) > 4:
                            new_word = base_word


                    else: 
                        suffix = base_word[len(stem):]

                        if len(suffix) > 2:
                            # print("PREFIX: ", stem, "SUFFIX: ", suffix)
                            new_word = base_word
                            break

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
    # ablarl*
    for i in range(2):
        for pronoun in pronoun_list: 
            if suffix.endswith(pronoun) and not suffix.endswith('aste') and not suffix.endswith('iste'):
                if pronoun.startswith('l'): 
                    if len(pronoun) == 2: # la lo le
                        pronoun_array.append(pronoun[0] + '/' + pronoun[1])
                    elif len(pronoun) == 3: # las los les
                        pronoun_array.append(pronoun[0] + '/' + pronoun[1] + '/' + pronoun[2])
                    else: 
                        pronoun_array.append(pronoun)
                else:
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

def slash_future(word, stem):
    possible_infs = ['ar', 'er', 'ir']
    future_endings = ['e', 'as', 'a', 'emos', '*s', 'an']
    infinitive = ''
    for inf in possible_infs: 
        if word.startswith(stem + inf):
            infinitive = stem + inf
            print("infinitive: ", infinitive)
    
    if not infinitive: 
        return word
    
    for ending in future_endings: 
        if word.endswith(ending):
            return word[:-len(ending)] + '/' + ending
        
    return word
    
def slash_in_context(corpus, word, morpheme, choice_array, is_following=False):

    new_corpus = []
    for line in corpus:
        has_new_line = line.endswith("\n")
        content = line.rstrip("\n")

        tokens = content.split(' ')
        new_tokens = []
        
        for i, token in enumerate(tokens):
            modified_token = token
            
            if token == word:
                apply_slash = False
                
                context_word_found = False
                if is_following:
                    if i + 1 < len(tokens):
                        if tokens[i+1] in choice_array:
                            context_word_found = True
                else: 
                    if i - 1 >= 0:
                        if tokens[i-1] in choice_array:
                            context_word_found = True
                
                if not context_word_found:
                    apply_slash = True

                if apply_slash:
                    if token.endswith(morpheme) and len(token) > len(morpheme):
                        stem = token[:-len(morpheme)]
                        modified_token = f"{stem}/{morpheme}"
            
            new_tokens.append(modified_token)
        
        new_line = ' '.join(new_tokens)
        
        if has_new_line:
            new_line += "\n"
        new_corpus.append(new_line)

    return new_corpus

def see_percentage_checked(corpus, will_print = False):
    # returns slashed words
    total_words = []
    slashed_words = []
    for line in corpus: 
        splitted_line = line.split(' ')
        for word in splitted_line:
            if '/' in word: 
                slashed_words.append(word)

            if len(word) > 1:
                total_words.append(word)

    unique_slashed_words = set(slashed_words)
    unique_total_words = set(total_words)

    if will_print:
        print(f"slashed: {len(slashed_words)} total: {len(total_words)} percentage completed: {len(slashed_words) / len(total_words) * 100}%")
        print(f"unique slashed: {len(unique_slashed_words)} unique total: {len(unique_total_words)} percentage completed: {len(unique_slashed_words) / len(unique_total_words) * 100}%")
    
    return slashed_words

def write_new_corpus(modified_corpus, path, file_name):
    new_path = os.path.join(path, file_name)
    with open(new_path, 'w') as file:
        for line in modified_corpus:
            file.write(line)
