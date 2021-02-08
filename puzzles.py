#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 07:42:30 2021

@author: mac
"""
from random import choice

def indig(n):
    """
    Resursive function to find indig of n
    """
    if n <= 9:
        return n
    n = sum(map(int, list(str(n))))
    return indig(n)

def spr():
    
    items = {'s':'scissors', 
             'p':'paper', 
             'r':'rock'}
    wins = (('scissors', 'paper'),
            ('paper', 'rock'),
            ('rock', 'scissors'))
    
    looping = True
    
    while looping:
        player = input("s, p, r or q: ")
        if player == 'q':
            looping = False
            continue
        player = items.get(player, None)
        if not player:
            continue
        print(f"player picks {player}")
        computer = choice(list(items.values()))
        print(f"computer picks {computer}")
        print(player,"versus",computer)
        if (player, computer) in wins:
            print("player wins")
        elif player == computer:
            print("tie")
        elif (computer, player) in wins:
            print("computer wins")
    else:
        print("Thanks for playing")
             