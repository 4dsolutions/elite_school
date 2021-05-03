import itertools
from typing import List

def make_panel(rows: int, cols: int, data: str) -> List:
    rows = []
    template = "{:0" + str(cols) + "b}"
    for hexcode in data.split():
        row = list(template.format((int(hexcode, 16))))
        rows.append(row)
    return rows


def make_sizes(rows, cols):
    row_sizes = [i for i in range(1, rows+1) if rows % i == 0]
    col_sizes = [i for i in range(1, cols+1) if cols % i == 0]
    g = itertools.product(row_sizes, col_sizes)
    return sorted(list(g), key=lambda t: t[0]*t[1])

def get_subpanel(p, rs, cs):
    subp = []
    for r in range(rs):
        row = p[r][:cs]
        subp.append(row)
    return subp

def mult_subpanel(sub, across, down):
    rows = []
    panel = []
    for row in sub:
        newrow = row * across
        rows.append(newrow)
    for d in range(down):
        panel += rows
    return panel 

def solve(rows, cols, data):
    p = make_panel(rows, cols, data)
    for size in make_sizes(rows, cols):
        subp = get_subpanel(p, *size)
        candidate = mult_subpanel(subp, cols//size[1], rows//size[0])
        if candidate == p:
            return size
        
