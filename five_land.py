#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 15:25:48 2022

@author: Kirby Urner
"""

from string import ascii_lowercase
def initialize():
    global words
    if not words:
        with open("wordkeep.txt", "r") as fileobj:
            words = set(fileobj.read().split("\n"))
            
def roll_alpha(the_word):
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

    fish.remove(the_word)
    return fish

def fish_pond(pond):
    bigger_pond = set()
    for fish in pond:
        kin = roll_alpha(fish)
        bigger_pond.update(kin)
    return bigger_pond

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