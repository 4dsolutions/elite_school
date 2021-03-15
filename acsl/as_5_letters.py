#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:21:23 2021

as_5_letters.py

@author: Kirby Urner
"""

from collections import Counter
from string import ascii_uppercase

def get_data(the_file = "as_5_letters_sample.txt"):
    sentences = [ ]
    with open(the_file, "r") as f:
        for sentence in f:
            s = ""
            for c in sentence:
                if c.upper() in ascii_uppercase + " ":
                    s += c.upper()
                else:
                    s += " "
            sentences.append(s)
    return sentences

def max_times(s):
    tally = Counter(s)
    del tally[" "]
    t = sorted(tally.items(), key=lambda it: it[1]) 
    return "{} {}".format(t[-1][0], t[-1][1])

def most_words(s):
    unique = set(s)
    word_tally = []
    for c in unique:
        how_many_words = sum([c in word for word in s.split()])
        word_tally.append((c, how_many_words))
    t = sorted(word_tally, key=lambda it: it[1]) 
    return "{} {}".format(t[-1][0], t[-1][1])

def any_word(s):
    s = s.replace(" ", "")
    unique = set(s)
    return "".join(sorted(unique, reverse=True))

def more_than_once(s):
    unique = set(s)
    word_tally = []
    for c in unique:
        how_many_words = sum([word.count(c)>1 for word in s.split()])
        if how_many_words == 0:
            continue
        word_tally.append((c, how_many_words))
    t = sorted(word_tally) 
    return "".join([c[0] for c in t])
    
def per_sentence(s):
    tally = Counter(s)
    del tally[" "]
    pairs = []
    for i in reversed(range(2, max(tally.values())+1)):
        to_add = [p for p in sorted(tally.items()) if p[1]==i]
        if len(to_add)>0:
            pairs += [p for p in sorted(tally.items()) if p[1]==i]
    return "".join([p[0] for p in pairs])

def main(input_file, output_file=None):
    """
    input_file = as_1_aball_sample.txt or as_1_aball_test.txt
    output_file = None or any string, output to console if None
    """
    sentences = get_data(input_file) # None or "as_5_letters_test.txt"

    if output_file:
        f =  open(output_file, "a")
    else:
        f = None
            
            
    for sentence in sentences:
        maxtimes = max_times(sentence)
        mostwords = most_words(sentence)
        anyword = any_word(sentence)
        morethanonece = more_than_once(sentence)
        pers = per_sentence(sentence)

        print(maxtimes, file=f)
        print(mostwords, file=f)
        print(anyword, file=f)
        print(morethanonece, file=f)
        print(pers, end=None, file=f) # losing team
        
    if f:
        f.close()
        
if __name__ == "__main__":
    main("as_5_letters_sample.txt")
    main("as_5_letters_test.txt")
        