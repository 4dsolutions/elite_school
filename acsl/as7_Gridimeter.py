"""
translated from java
"""

import traceback
import numpy as np
from numpy.core.function_base import linspace


def main():  # throws FileNotFoundException
    try:
        inFile = open("as7_sample2.txt")
        casenum = 0
        for line in inFile:
            casenum += 1
            scan = line.split()
            rows = int(scan[0])
            cols = int(scan[1])
            grid = np.zeros((rows, cols), dtype=np.int8)
            r = 0
            template = "{:0" + str(cols) + "d}"
            for code in scan[2:]:
                row_data = list(template.format(int(code, 16)))
                grid[r, :] = list(map(int, row_data))
                r += 1
            print(f"{casenum}.")
            print(grid)
            process(grid, casenum)
            # print()
    except FileNotFoundError:
        print("No such file")
    return


def process(the_grid, the_case):
    grid = the_grid
    casenum = the_case
    rows, cols = the_grid.shape
    try:
        # print("Processing...")
        mark = np.zeros((rows, cols), dtype=np.int8)
        count = 0
        while count < rows * cols:
            for i in range(rows): 
                for j in range(cols):
                    # print(count)
                    # if top or bottom row, left or right margin
                    if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1):
                        if (grid[i][j] == 0):
                            if (i != 0):
                                if (mark[i - 1][j] == 0):
                                    count += 1
                                mark[i - 1][j] = 1
                            
                            if (i != rows - 1):
                                if mark[i + 1][j] == 0:
                                    count += 1
                                mark[i + 1][j] = 1
                            
                            if (j != 0):
                                if mark[i][j - 1] == 0:
                                    count += 1
                                mark[i][j - 1] = 1
                            
                            if (j != cols - 1):
                                if (mark[i][j + 1] == 0):
                                    count += 1
                                mark[i][j + 1] = 1
                            
                            if mark[i][j] == 0:
                                count += 1
                            mark[i][j] = 1
                            continue

                    if ((i == 0 or i == rows - 1) and 
                        (j == 0 or j == cols - 1)):
                        if (grid[i][j] == 1):
                            if (mark[i][j] == 0):
                                count += 1
                            mark[i][j] = 1
                            continue

                    u, d, l, r, c = 0, 0, 0, 0, 0
                    if (i == 0):
                        u = 1
                    else:
                        u = mark[i - 1][j]

                    if (i == rows - 1):
                        d = 1
                    else:
                        d = mark[i + 1][j]

                    if (j == 0):
                        l = 1
                    else:
                        l = mark[i][j - 1]

                    if (j == cols - 1):
                        r = 1
                    else:
                        r = mark[i][j + 1]

                    c = mark[i][j]
                    works = [None] * 32
                    workamt = 0

                    for bits in range(32):
                        test_u = bits % 2 + 1
                        test_d = (bits // 2) % 2 + 1
                        test_l = (bits // 4) % 2 + 1
                        test_r = (bits // 8) % 2 + 1
                        test_c = (bits // 16) % 2 + 1
                        
                        if (u != 0 and u != test_u):
                            continue
                        if (d != 0 and d != test_d):
                            continue
                        if (l != 0 and l != test_l):
                            continue
                        if (r != 0 and r != test_r):
                            continue
                        if (c != 0 and c != test_c):
                            continue

                        diffamt = 0
                        if (test_u != test_c):
                            diffamt += 1
                        if (test_d != test_c):
                            diffamt += 1
                        if (test_l != test_c):
                            diffamt += 1
                        if (test_r != test_c):
                            diffamt += 1

                        if grid[i][j] != diffamt:
                            continue

                        works[bits] = True
                        workamt += 1
                    
                    if (workamt == 1):
                        found = 0
                        for find in range(32):
                            if works[find]:
                                found = find

                        real_u = found % 2 + 1
                        real_d = (found // 2) % 2 + 1
                        real_l = (found // 4) % 2 + 1
                        real_r = (found // 8) % 2 + 1
                        real_c = (found // 16) % 2 + 1

                        if (i != 0):
                            if (mark[i - 1][j] == 0):
                                count += 1
                            mark[i - 1][j] = real_u
                        
                        if (i != rows - 1):
                            if (mark[i + 1][j] == 0):
                                count += 1
                            mark[i + 1][j] = real_d
                        
                        if (j != 0):
                            if (mark[i][j - 1] == 0):
                                count += 1
                            mark[i][j - 1] = real_l
                        
                        if (j != cols - 1):
                            if mark[i][j + 1] == 0:
                                count += 1
                            mark[i][j + 1] = real_r
                        

                        if (mark[i][j] == 0):
                            count += 1
                        mark[i][j] = real_c
            
                    if (workamt == 2 and grid[i][j] == 2 and mark[i][j] == 0):
                        found = 0
                        for find in range(32):
                            if (works[find]):
                                found = find

                        real_u = found % 2 + 1
                        real_d = (found // 2) % 2 + 1
                        real_l = (found // 4) % 2 + 1
                        real_r = (found // 8) % 2 + 1

                        if (i != 0):
                            if (mark[i - 1][j] == 0):
                                count += 1
                            mark[i - 1][j] = real_u
                        
                        if (i != rows - 1):
                            if (mark[i + 1][j] == 0):
                                count += 1
                            mark[i + 1][j] = real_d
                        
                        if (j != 0):
                            if (mark[i][j - 1] == 0):
                                count += 1
                            mark[i][j - 1] = real_l
                        
                        if (j != cols - 1):
                            if (mark[i][j + 1] == 0):
                                count += 1
                            mark[i][j + 1] = real_r

                    # diagnostic / window                      
                    if casenum == 100:  # set to 8 or something  
                        for lol in range(rows):
                            print(mark[lol,:], i, j, workamt, count)  
                        print()
                
        print(mark)
        total = 0
        for i in range(rows):
            for j in range(cols):
                if mark[i][j] == 2:
                    total += grid[i][j]
        
        print(f"{casenum}.", total)

    except Exception as e:
        traceback.print_exc()
        print("Oops")
        print(f"{casenum}.", 10)

def testing():
    for bits in range(32):
        test_u = bits % 2 + 1
        test_d = (bits // 2) % 2 + 1
        test_l = (bits // 4) % 2 + 1
        test_r = (bits // 8) % 2 + 1
        test_c = (bits // 16) % 2 + 1
        print(test_u, test_d, test_l, test_r, test_c)

main()
# testing()