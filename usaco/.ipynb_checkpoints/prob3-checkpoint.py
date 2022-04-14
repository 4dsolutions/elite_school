"""
Go through the alphabet as many times as needed
to find all the letters provided.
"""

def get_passes(alpha, h):
    original = alpha[:]
    total = 1
    loc = 0
    for c in h:
        found = False
        while not found:
            loc = alpha.find(c)
            if loc > -1:
                alpha = alpha[loc + 1:]
                found = True
            else:
                total += 1
                alpha = original
    return total
  