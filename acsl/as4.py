#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 18:02:32 2021

@author: Kirby

Think about this code by Mason:
    
code_input = "4 LBLBLBRRRAAA"
print(int(code_input.split(" ")[0]) + sum([{"R": 1, "L": -1, "A": -4, "B": 4}[move] for move in code_input.split(" ")[1]]))
"""

module_name = __name__

board = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2), 
    4: (0, 3),

    5: (1, 0),
    6: (1, 1),
    7: (1, 2), 
    8: (1, 3),

    9: (2, 0),
   10: (2, 1),
   11: (2, 2), 
   12: (2, 3),

   13: (3, 0),
   14: (3, 1),
   15: (3, 2), 
   16: (3, 3),
    }

def read_data(the_file = "as4-sample.txt"):
    puzzles = {}
    with open(the_file) as f:
        lines = f.readlines()
    for idx, line in enumerate(lines):
        startpos, moves = line[:-1].split()
        puzzles[idx] = (int(startpos), moves)
    return puzzles
        
def make_grid(n: int):
    if not 1 <= n <= 16:
        print("1 <= n <= 16")
    else:
        grid = []
        values = (list(range(1, n)) 
                  + [None] 
                  + list(range(n, 17)))
        for row in range(4):
            grid.append(values[:4])
            values = values[4:]
        return grid

def show_grid(grid):
    for r in range(4):
        data = map(str, grid[r])
        print("{:4}  {:4}  {:4}  {:4}".format(*data))
        
def get_None(grid):
    for i in range(1, 17):
        r, c = board[i]
        if grid[r][c] is None:
            return i
    
def slide(mv, plc, grid):  # would prefer this be swap
    r, c = board[plc]
    if mv == "B":
        grid[r][c], grid[r+1][c] = grid[r+1][c], grid[r][c] 
    
    elif mv == "A":
        grid[r][c], grid[r-1][c] = grid[r-1][c], grid[r][c] 
        
    elif mv == "R":
        grid[r][c], grid[r][c+1] = grid[r][c+1], grid[r][c] 
        
    elif mv == "L":
        grid[r][c], grid[r][c-1] = grid[r][c-1], grid[r][c] 
    
    return get_None(grid)

def main():
    all_puzzles = read_data()
    for i in range(10):
        puzzle = all_puzzles[i]
        the_grid = make_grid(puzzle[0])
        place = puzzle[0]
        for move in list(puzzle[1]):
            place = slide(move, place, the_grid)
        print("{}. {}".format(i+1, place))
        
if __name__ == "__main__":
    main()

