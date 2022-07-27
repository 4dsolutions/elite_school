# -*- coding: utf-8 -*-
"""
July 15 
coding it together
"""

from random import randint

def play(guesses=5, minimum=0, maximum=10):
    secret_number = randint(minimum, maximum)
    print(f"Welcome to Guess My Number Between {minimum} and {maximum}!")
    answer = ''
    while answer != 'q':
        if 0 == guesses:
            print("Out of guesses, sorry")
            break
        print("You have {} guesses".format(guesses))        
        print("Can you guess my secret number?")
        answer = input("(q to quit) > ")
        if answer.isdigit():
            guess = int(answer)
            if secret_number == guess:
                print("You win!")
                answer = 'q'
                continue
            if secret_number < guess:
                print("Too high!")
            if secret_number > guess:
                print("Too low!")            
            guesses = guesses - 1 
        else:
            answer = answer.lower()
    print("Come back soon")