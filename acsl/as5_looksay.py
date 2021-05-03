def substr(s, start, more):
    return s[start-1:start+more]

def looksay(s: str) -> str:
    if not type(s) is str:
        raise TypeError
    if not s.isdigit():
        raise ValueError
    next_term = ""
    last_c = ""
    counter = 0
    for c in s:
        if (c == last_c) or last_c == "":
            counter += 1
            last_c = c
        else:
            next_term = next_term + str(counter) + last_c
            last_c = c
            counter = 1
    else:
        next_term = next_term + str(counter) + last_c
    return next_term