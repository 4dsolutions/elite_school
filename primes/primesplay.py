"""
Possible pedagogical use:
    A textbook algorithm suitable for learning IDE's
    debugging facilities, if any.

Command line use:

$ python -m primesplay.py -factors 100
$ python -m primesplay.py -isprime 42

See: PEP 338
https://www.python.org/dev/peps/pep-0338/

"""

# we decide to name roots: root2, root3, root4 etc.
from math import sqrt as root2, floor
import itertools
from collections import Counter
root3 = lambda x: pow(x, 1/3.) # 3rd root of x (not used)
root4 = lambda x: pow(x, 1/4.) # 4th root of x (not used)

def isprime(n):
    """
    isprime(n: int) -> bool

    Expects positive int, returns Boolean

    _cache is for internal cache of primes seen so far
    """
    isprime._cache = set((2,))
    if n in isprime._cache:     # see if on file already, screens 2
        return True
    if (0 == n%2) or (n == 1):  # if not two and yet even, or 1...
        return False            # n is not prime
    # check range of odds from 3 up
    for i in range(3, floor(root2(n)) + 1, 2):
        if n % i == 0:       # no remainder?
            return False     # ...then composite
    isprime._cache.add(n)            # add to _stash
    return True              # made it through the screening

def factors(n):
    """
    factors(n: int) -> tuple

    Expects int, prime or composite
    returns a tuple with all prime factors, also 1, and -1 if negative
    """
    if not isinstance(n, int):  # gotta be int
        raise ValueError
    if n == 0:
        return (0,)
    found = [1]   # always
    if n < 0:
        found.append(-1)
        n = abs(n)
    # chop n down by successive prime factors
    divisor = 2
    while True:
        if n == 1:
            break # we're done
        if isprime(n):
            found.append(n)
            break # we're done
        while n % divisor == 0 and isprime(divisor):
            # divides by same divisor as many times as it takes
            found.append(divisor)
            n //= divisor  # chop it down
        if divisor == 2:   # even once
            divisor = 3
        else:
            divisor = max(divisor, max(found)) + 2 # always odd

    return tuple(found) # make it immutable

def all_factors(n):
    c = Counter(factors(n))
    so_far = [1]
    for prime in list(c.keys())[1:]: # skip factor 1
        # raise prime to a power from 1 to however 
        # many occur and make a Cartesian product 
        # with all factors so far
        iterable = [prime**n for n in 
                    range(1, c[prime]+1)]
        so_far += (a*b for a,b 
                   in itertools.product(so_far, iterable))
    return sorted(so_far)

def eratosthenes(n):
    the_max = floor(root2(n))
    sieve = list(range(0, n+1))
    eliminator = 2
    while True:
        if eliminator > the_max:
            break
        print("Eliminating multiples of:", eliminator)
        for k in range(2 * eliminator, n + 1, eliminator):
            sieve[k] = 0
        while sieve[eliminator + 1] == 0:
            eliminator += 1
        else:
            eliminator = sieve[eliminator + 1]
        
    # shrink me down (compact the sieve)    
    sieve = [n for n in sieve if n != 0][1:]  # list comprehension!
    return sieve

def iterprimes():
    """
    Copied from:
    http://www.mypy-lang.org/examples.html   
     # An iterator of all numbers between 2 and
     # +infinity
    """
    numbers = itertools.count(2)

     # Generate primes forever
    while True:
        # Get the first number from the iterator
        # (always a prime)
        prime = next(numbers)
        yield prime
    
        # This code iteratively builds up a chain
        # of filters...
        numbers = filter(prime.__rmod__, numbers)

def sieve(n):
    it = iterprimes()
    return list(itertools.islice(it, n))

def test_eratosthenes():
    results = eratosthenes(10000)
    for row in range(0, len(results), 10):
        print( ", ".join(map(str, results[row:row+10])))

def test_me():
    print("Factors of 1000", factors(1000))
    print("Factors of 14883893", factors(14883893))
    print("Is 42 prime?", isprime(42))
    print("What's the prime factorization of 100?", factors(100))

def fun_fact():
    """
    Is it tru that 73939133 is prime and so is every number
    in the progression leading up to it, i.e.:
    7, 73, 739, 7393 and so on?  If so, is it the biggest 
    such number yet known? We can only answer the first 
    question here.
    """
    digits = "73939133"
    for test in range(1, len(digits)+1):
        check_me = int(digits[:test])
        if not isprime(check_me):
            print(f"{check_me} is not prime!")
        else:
            print(f"{check_me} checks out!")
    
def help_me():
    print(__doc__) # this module's docstring
    print("Upon importing, available functions are...")
    print(factors.__doc__)  # using builtin help to get docstring
    print(isprime.__doc__)  # ditto

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--isprime', nargs=1, help='is it prime?')
    parser.add_argument('--erat', nargs=1, help='primes up to what number?')
    parser.add_argument('--factors', nargs=1, help='factors of what number?')    
    parser.add_argument('--sieve', nargs=1, help='how many primes?')
    args = parser.parse_args()
    # print(args)
    if args.isprime:
        print(isprime(int(args.isprime[0])))
    if args.erat:
        print(eratosthenes(int(args.erat[0])))
    if args.factors:
        print(factors(int(args.factors[0])))
    if args.sieve:
        print(sieve(int(args.sieve[0])))