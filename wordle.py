#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 08:57:30 2022

@author: Kirby Urner

C = Correct position
P = Correct letter, wrong position
N = Incorrect letter
"""

from random import randint

words = None

def evaluate(answer, guess): 

    unmatched = answer
    clue = [None, None, None, None, None] 
    
    for idx, char in enumerate(guess):
        if (char in unmatched 
            and unmatched[idx] == guess[idx]):
            clue[idx] = "C"
            unmatched = unmatched.replace(char, ".", 1)

    for idx, char in enumerate(guess):
        if (clue[idx] is None 
            and char in unmatched 
            and unmatched.index(char) != idx): 
            clue[idx] = "P"
            unmatched = unmatched.replace(char, ".", 1)
            
    for idx, char in enumerate(guess):
        if (clue[idx] is None
            and char not in unmatched):
            clue[idx] = "N"
            
    return "".join(clue)

def words_play(answer = "BLING", show_answer = True, word_guess=True):
    global words
    
    if word_guess and not type(words) is set:
        with open("wordkeep.txt", "r") as fileobj:
            words = set(fileobj.read().split("\n"))
        
    while True:
        
        guess = input("What is your guess? > ")
        if guess.upper().strip() == "Q":
            print("Come again!")
            break
        
        if not guess.isalpha() or len(guess) != 5:
            print("Five letters please")
            continue
        
        if word_guess and (not guess.lower() in words):
            print("That's not a real word, sorry.")
            continue
    
        clue = evaluate(answer.lower(), guess.lower())
    
        if show_answer:
            print("answer   :", answer)
            
        print("guess    :", guess)
        print("clue     :", clue)
        
        if clue == "CCCCC":
            print("You win!")
            break
        
    print("See you soon!")
    print()
    
            
    
def digits_play(answer = "88976", show_answer=True):
    
    while True:
        
        guess = input("What is your guess? > ")
        if guess.upper().strip() == "Q":
            print("Come again!")
            break
        
        if not guess.isdigit() or len(guess) != 5:
            print("Five digits please")
            continue
    
        clue = evaluate(answer, guess)
    
        if show_answer:
            print("answer   :", answer)
        print("guess    :", guess)
        print("clue     :", clue)
        
        if clue == "CCCCC":
            print("You win!")
            break
        
def make_data(answer = "88976", n = 10):
    
    with open("mastermind.txt", "w") as out:
        for _ in range(10):
            guess = str(randint(9999,99999))
            clue = evaluate(answer, guess)
            print(answer, guess, clue, file=out)

if __name__ == "__main__":
    words_play()
    