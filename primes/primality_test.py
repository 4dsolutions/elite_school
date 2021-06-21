#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 18:50:36 2017

@author: Kirby Urner

Primes always pass the Fermat Test:

Given b,p have no factors in common:
    b**(p-1) / p == 1 
or: pow(b, p-1, p) == 1
or: (b**p - b)

But then so do some composites. The Carmichael Numbers 
are called absolute Fermat pseudoprimes because they
pass all Fermat Tests with flying colors.
"""

from math import gcd
from primesplay import factors
from itertools import count, islice

def coprime(a, b):
    """
    Yes, True a and b are coprime or...
    No they're not."""
    # coprimes have 1 as greatest common factor
    return gcd(a, b) == 1  

def fermat_test(candidate, base):
    "primes always pass this test, composites do sometimes"
    return pow(base, candidate-1, candidate) == 1

bases = [3, 5, 7, 11, 13, 17] # primes make good bases

def fermat_trials(pp):
    for the_base in bases:
        if not coprime(the_base, pp):
            continue
        if not fermat_test(pp, the_base):
            return False
    else:
        return True  # passed all tests
        
def Ω(n):
    """
    number of prime factors of n
    """
    return len(factors(n)) - 1 

def ω(n):
    """
    number of distinct prime factors of n
    """
    return len(set(factors(n))) - 1

def μ(n): 
    """
    Möbius function
    """
    return bool((ω(n) == Ω(n)) * (-1) ** ω(n))

def q(n):
    """
    characteristic function of squarefree numbers
    """
    return abs(μ(n))

# http://oeis.org/wiki/Carmichael_numbers
carmichael_numbers = [561, 1105, 1729, 2465, 2821, 6601, 8911, 
      10585, 15841, 29341, 41041, 46657, 52633, 
      62745, 63973, 75361, 101101, 115921, 126217, 
      162401, 172081, 188461, 252601, 278545, 
      294409, 314821, 334153]

#---- These tests are designed to work with pytest ----
def test_cm_pass_fermat():
    for possible_prime in carmichael_numbers:
        assert fermat_trials(possible_prime)
        
def test_cm_nosquares():
    for cmn in carmichael_numbers:
        assert q(cmn)
    
def test_a008966():
    # http://oeis.org/A008966  	1 if n is squarefree, else 0
    c = count(1)                 # open ended...
    a008966 = (q(n) for n in c)  # generator expression
    seq = islice(a008966,100)    # could slice a lot more...      
    test_seq = [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 
     0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 
     1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 
     1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 
     1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 
     0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 
     1, 0, 1, 1, 1, 0, 1, 0, 0, 0]
    assert list(seq) == test_seq
    
def test_a005117():
    # http://oeis.org/A005117
    test_seq = [1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 
     17, 19, 21, 22, 23, 26, 29, 30, 31, 33, 
     34, 35, 37, 38, 39, 41, 42, 43, 46, 47, 
     51, 53, 55, 57, 58, 59, 61, 62, 65, 66, 67]
    squarefree = filter(lambda n: q(n), range(1, 68))
    assert list(squarefree) == test_seq