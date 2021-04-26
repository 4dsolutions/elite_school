#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AS1
"""

def get_puzzles(the_file):
    puzzles = {}
    i = 0
    with open(the_file, 'r') as data:
        rows = data.readlines()[1:]

    for row in rows:
        rs, cs, *data = row.split()
        grid = []
        # print(rs, cs, data)
        for bits in data:
            grid.append(list(bits))
        
        puzzles[i] = grid
        i += 1
    
    return puzzles

def get_grid(the_file):
    with open(the_file, 'r') as data:
        row = data.readline().strip()
    grid = []
    for code in row.split():
        bits = bin(int(code, 16))[2:].zfill(8)
        grid.append(list(bits))
    return grid

def get_subgrid(r, c, rs, cs, the_grid):
    """
    starting from row r, col c, 
    return a rectangle of rs rows and cs columns
    from the target grid
    
    or return an empty list if the rectangle 
    goes out of bounds
    """
    subgrid = []
    if r + rs <= len(the_grid):
        for i in range(r, r + rs):
            row = the_grid[i]
            if c+cs > len(row):
                break
            subgrid.append(row[c:c+cs])
    return subgrid
            
def get_all_subgrid(rs, cs, the_grid):
    bag_subgrids = []
    for r in range(len(the_grid)):
        row = the_grid[r]
        for c in range(len(row)):
            bag_subgrids.append(get_subgrid(r, c, rs, cs, the_grid))
    return bag_subgrids

def check_bag(target, all_subgrids):
    counter = 0
    for subgrid in all_subgrids:
        if target == subgrid:
            counter += 1
    return counter
            
def main(the_file):
    grid = get_grid(the_file)
    p = get_puzzles(the_file)
    for i in range(10):
        t = p[i]
        # size of target
        rs = len(t)
        cs = len(t[0])
        # all possible subgrids of that size
        bag = get_all_subgrid(rs, cs, grid)
        # print(bag)
        # count number of matches
        cnt = check_bag(t, bag)
        print("{:2}. {:2}".format(i+1, cnt))
        