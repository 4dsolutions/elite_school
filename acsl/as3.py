#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AS3

1 same letter, number + 1
2 next letter, if odd letter number + 1
3 next letter, if even letter number - 1
4 same letter, number - 1
5 prev letter, if even letter, number - 1
6 prev letter, if odd letter, number + 1
"""

from string import ascii_uppercase as letters
numlet = dict(enumerate(letters, start=1))
letnum = {v:k for k,v in numlet.items()}

def next_cell(direction, current):
    letter, number = current[0], int(current[1:])
    
    if direction == 1:
        number +=1
        
    elif direction == 2:
        if letnum[letter]%2: # odd
            number += 1
        letter = numlet[letnum[letter]+1]
        
    elif direction == 3:
        if not letnum[letter]%2: # even
            number -= 1
        letter = numlet[letnum[letter]+1]

    elif direction == 4:
        number -= 1
        
    elif direction == 5:
        if not letnum[letter]%2: # even
            number -= 1        
        letter = numlet[letnum[letter]-1]
        
    elif direction == 6:
        if letnum[letter]%2: # odd
            number += 1
        letter = numlet[letnum[letter]-1]

    if number < 1:
        raise Exception
        
    return letter+str(number)    

def move(direction, cell):
    try:
        cell = next_cell(int(direction), cell)
    except:
        # print("oops")
        pass
    return cell

def read_moves(the_file = "as3-test.txt"):
    scenarios = []
    with open(the_file) as f:
        for line in f.readlines():
            cell, path = line.split()
            scenarios.append((cell,list(path)))
    return enumerate(scenarios, start=1)

def main():
    turns = read_moves()
    for turn in turns:
        # print("turn:", turn)
        idx, (pos, path) = turn
        # print("pos, path:", pos, path)
        for d in path:
            # print(pos, d)
            pos = move(d, pos)
        print("{:2}. {}".format(idx, pos))


        
        