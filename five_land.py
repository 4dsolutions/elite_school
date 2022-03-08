#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 15:25:48 2022

@author: Kirby Urner
"""
from random import choice

words = set()
from string import ascii_lowercase
from wordle import evaluate

def initialize():
    global words
    if not words:
        with open("wordkeep.txt", "r") as fileobj:
            words = set(fileobj.read().split("\n"))
    if "" in words:
        words.remove("")
    print(len(words))
            
def roll_alpha(the_word, show_candidate=False):
    fish = set()
    fish.add(the_word)
    stone = list(the_word)
    for i in range(len(the_word)):
        for letter in ascii_lowercase:
            listy = stone.copy()
            listy[i] = letter
            candidate = "".join(listy)
            if candidate in words:
                fish.add(candidate)
                if show_candidate:
                    print(candidate)

    fish.remove(the_word)
    return fish

def fish_pond(pond):
    """
    Find all the words one letter distant from 
    all of those in the current set
    """
    bigger_pond = set(pond)
    for fish in pond:
        kin = roll_alpha(fish)
        bigger_pond.update(kin)
    return bigger_pond

def grow_pool(p, show_stats=False):
    """
    find all the words reachable from p by means 
    of *any number* of one letter legal word hops,
    and stop when p stops growing.
    """
    new_p = fish_pond(p)
    while len(new_p) > len(p):
        p = new_p
        new_p = fish_pond(p)
        if show_stats:
            print(len(p), len(new_p))
    return p

def survey(curate_len=0):
    """
    find the biggest island starting from never_reached
    words. How big is the biggest island.
    """
    global final_set, never_reached
    biggest = 0
    curated = set()
    biggest_word = ""
    if (not "final_set" in globals() 
        or not "never_reached" in globals()
        or len(final_set)==0 
        or len(never_reached)==0):
        # regenerate on the fly
        final_set = grow_pool({"caked"})
        never_reached = words - final_set
    tally = dict()
    for w in never_reached:
        neighborhood = grow_pool({w})
        nb_size = len(neighborhood)
        if curate_len == nb_size:
            curated.add(w)
        if nb_size > biggest:
            biggest = nb_size
            biggest_word = w
        tally[len(neighborhood)] = tally.get(len(neighborhood), 0) + 1
    return tally, biggest, biggest_word, curated


def path_exists(wordA: str, wordB: str) -> bool:
    """
    yes or no, does a path exist between these two input words?
    """
    if wordA not in words or wordB not in words:
        raise ValueError("not both legal words")
    if wordA == wordB:
        return True

    # interim list prevents fragmentation into characters
    poolA = set([wordA])
    poolB = set([wordB])

    for _ in range(4):
        poolA = fish_pond(poolA)
        poolB = fish_pond(poolB)

    if len(poolA) > 24 and len(poolB) > 24:
        print("Both on big island")
        return True
    if len(poolA.intersection(poolB)) > 0:
        print("Same small island")
        return True
    return False

def elim_char(c, pool):
    return {word for word in pool if c not in word}
    
def keep_char(c, p, pool):
    keep = set()
    for word in pool:
        listy = list(word)
        for i in range(len(listy)):
            if listy[i].upper() == c.upper() and i != p:
                listy[i] = c.upper()
                keep.add("".join(listy))
                listy[i] = c # set back to what it was
    return keep 

def keep_char_pos(c, p, pool):
    keep = set()
    for word in pool:
        listy = list(word)
        listy[p] = c.upper()
        keep.add("".join(listy))
    return keep    

def eliminate(guess, answer, clue, pool):
    # print("Eliminating possibilities...")
    # print("Pool size:", len(pool))
    for idx, char in enumerate(clue):
        if char == "C":
            pool = keep_char_pos(guess[idx], idx, pool)
            # print("C:",idx, char, len(pool))
    if answer.upper() not in [word.upper() for word in pool]:
        print("After C")

    for idx, char in enumerate(clue):        
        if char == "P":
            pool = keep_char(guess[idx], idx, pool)
            # print("P:",idx, char, len(pool))
    if answer.upper() not in [word.upper() for word in pool]:
        print("After P")
        
    for idx, char in enumerate(clue):
        if char == "N":
            pool = elim_char(guess[idx], pool)
            # print("N:",idx, char, len(pool))
    if answer.upper() not in [word.upper() for word in pool]:
        print("After N")
        

    
    return pool
            
def wordle(answer=None, guess=None):
    initialize()
    # from wordle import evaluate
    if not answer:
        answer = choice(list(words))
    if not guess:
        guess = choice(list(words))
    pool = words.copy()
    while True:
        clue = evaluate(answer, guess.lower())
        print(answer, guess.lower(), clue)
        if clue == "CCCCC":
            print("That's it!")
            break

        pool = eliminate(guess, answer, clue, pool)

        # print(" New size:", len(pool))
        # print("Remaining:", len(pool))
        if len(pool) == 0:
            print("Out of options")
            break
        
        guess = choice(list(pool))
        
def word_path(start_word):
    visited = set(start_word)
    last_word = start_word
    while True:
        next_words = roll_alpha(last_word)
        while next_words:
            word = next_words.pop()
            if word not in visited:
                visited.add(word)
                last_word = word
                yield word
        else:
            break
    print("path ended")
    return

if __name__ == "__main__":
    words = ""
    initialize()