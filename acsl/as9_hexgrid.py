alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def lPrev(l):
    if l == 'A':
        return None
    return alphabet[alphabet.index(l) - 1]

def lNext(l):
    if l == 'Z':
        return None
    return alphabet[alphabet.index(l) + 1]

def lOdd(l):
    return alphabet.index(l) % 2 == 0

def adjacent(cell):
    def good(k):
        return (k[0] != None) and (k[1] > 0)
    if lOdd(cell[0]):
        result = [(lPrev(cell[0]), cell[1]), (lPrev(cell[0]), cell[1] + 1), (cell[0], cell[1] - 1), (cell[0], cell[1] + 1), (lNext(cell[0]), cell[1]), (lNext(cell[0]), cell[1] + 1)]
    else:
        result = [(lPrev(cell[0]), cell[1] - 1), (lPrev(cell[0]), cell[1]), (cell[0], cell[1] - 1), (cell[0], cell[1] + 1), (lNext(cell[0]), cell[1] - 1), (lNext(cell[0]), cell[1])]
    return [k for k in result if good(k)]

def dist(start, end):
    d = abs(alphabet.index(start[0]) - alphabet.index(end[0]))
    if lOdd(start[0]) ^ lOdd(end[0]):
        high = start[1] + d//2 + lOdd(start[0])
        low = start[1] - d//2 - (1 - lOdd(start[0]))
        #print((high, low))
    else:
        high = start[1] + d//2
        low = start[1] - d//2
    if end[1] > high:
        return d + end[1] - high
    elif end[1] < low:
        return d + low - end[1]
    return d

def paths(start, end, length, avoiding = []):
    if dist(start, end) > length:
        return 0
    if start == end:
        if length == 0:
            return 1
        return 0
    total = 0
    for c in adjacent(start):
        if c in avoiding:
            continue
        total += paths(c, end, length - 1, avoiding + [start,])
    return total

def parseCell(c):
    return (c[0].upper(), int(c[1:]))

def parseInput(s):
    s = s.split(' ')
    return paths(parseCell(s[0]), parseCell(s[1]), int(s[2]))

filename = input('Enter file name: ')
a = open(filename, 'r').read().split('\n')
c = 1
for i in a:
    try:
        if len(i) > 0:
            print(str(c) + '. ' + str(parseInput(i)))
            c += 1
    except:
        print(str(c) + '. 150')
        c += 1
