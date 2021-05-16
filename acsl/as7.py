import numpy as np

data = "5 5 2F59 2EEB 840 840 33B1"

def make_grid(r : str, c : str, *rows): # gather into 3 params
    """
    r - number of rows
    c - number of columns
    rows - data for each row, convert to decimal
    """
    r = int(r)
    c = int(c)
    # print(f"r: {r}; c: {c}; rows: {rows}")
    grid = np.zeros((int(r), int(c)), dtype=np.int)
    template = "{:0" + str(c) + "d}"
    for row in range(r):
        row_data = list(template.format(int(rows[row], 16)))
        print(row_data)
        grid[row, :] = list(map(int, row_data))
    return grid
    
def embed_grid(the_grid):
    r, c = the_grid.shape
    new_r = r + 2; new_c = c + 2
    new_grid = np.zeros((new_r, new_c), dtype=np.int)
    new_grid[1:r+1,1:c+1] = the_grid
    return new_grid

def walk_frame(the_grid):
    r, c = the_grid.shape
    print((r,c))
    # top
    print("top")
    for col in range(1, c-1):
        yield ((0,col), (the_grid[1, col], the_grid[2, col]))
    # right
    print("right")
    for row in range(1, r-1):
        yield ((row, c-1), (the_grid[row, -2], the_grid[row, -3]))
    # bottom
    print("bottom")
    for col in range(1, c-1):
        yield ((r-1, col), (the_grid[-2, col], the_grid[-3, col]))   
    # left
    print("left")
    for row in range(1, r-1):
        yield ((row-1, 0), (the_grid[row, 1], the_grid[row, 2]))

g = make_grid(*data.split())  # explode into 6 args
print(g)

ng = embed_grid(g)
print(ng)

def fix_frame(the_grid):
    for probe in walk_frame(the_grid):
        print (probe)
        if probe[1][0]==0 and probe[1][1]==1:
            continue
        if probe[1][0]==1 and probe[1][1]==1:
            continue
        if probe[1][0]==1 and probe[1][1]==0:
            the_grid[probe[0][0],probe[0][1]] = 1
        if probe[1][0]==1 and probe[1][1]==3:
            continue
        
        if probe[1][0]==2 and probe[1][1]>=1:
            the_grid[probe[0][0],probe[0][1]] = 1

        if probe[1][0]==3 and probe[1][1]>1:
            the_grid[probe[0][0],probe[0][1]] = 1

fix_frame(ng)
print(ng)

print("ANSWER:")
answer = np.sum(ng)//2
print(answer)