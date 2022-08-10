#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 09:10:18 2020

@author: Kirby Urner

Aug 7 2022:  interpolated Mod type from ADS_highschool_math.ipynb
"""

import itertools
from operator import mod as remainder
from primes import invmod

# These two might help with the lab
from itertools import dropwhile, takewhile


def gcd(a, b):
    """
    Euclid's method    
    a, b should be integers
    returns integer
    """
    while b:
        a, b = b, a % b
    return a

def xgcd(a, b):
    """
    Extended Euclidean Alg.
    
    take positive integers a, b as input, and return 
    a triple (g, x, y), such that ax + by = g = gcd(a, b).
    """
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  a, x0, y0

def invmod(a, N):
    """
    What is the multiplicative inverse of a, inv_a,
    such that a * inv_a = 1 mod N.
    """
    return xgcd(a, N)[1] % N  # inv_a (gcd is 1, a * x0 + N * x1 = 1)

def tots(N):  # on the same line is OK
    """
    List numbers with no factors in common with N
    """
    return [n for n in range(1, N) if gcd(n, N)==1]

def totient(N):
    "Euler's Totient"
    return len(tots(N))

class Mod:
    """
    Integers operating relative to a _modulus.
    """
    _modulus = 12
    
    def __init__(self, n):
        self.p = n % self._modulus
        
    def __add__(self, other):
        return Mod(self.p + other.p)
    
    def __mul__(self, other):
        return Mod(self.p * other.p)
    
    def __pow__(self, e):
        new_p = self.p
        if e < 0:
            new_p = invmod(self.p, self._modulus)
        e = abs(e)
        return Mod(pow(new_p, e, self._modulus))
    
    def __eq__(self, other):
        return self.p == other.p
    
    def __lt__(self, other):
        return self.p < other.p
    
    def __hash__(self):
        return 0
    
    def __repr__(self):
        return "({} mod {})".format(self.p, self._modulus)
    
class Fibos:

    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        rtnval = self.a
        self.a, self.b = self.b, self.a + self.b
        return rtnval

    def __iter__(self):
        return self

    
class Primes:

    def __init__(self):
        self.candidate = 1
        self._primes_so_far = [2]  # first prime, only even prime
        self.odds = itertools.count(3, step=2)
        
    def __iter__(self):
        return self
        
    def __next__(self):
        while True:
            self.candidate = next(self.odds)    # check odds only from now on
            for prev in self._primes_so_far:
                if prev**2 > self.candidate:
                    self._primes_so_far.append(self.candidate)
                    return self._primes_so_far[-2]      # running behind
                if not remainder(self.candidate, prev): # no remainder!
                    break
    
# https://repl.it/@kurner/Compose-Functions

# take any two functions as args and return their composition
compose = lambda f, g: (lambda x: f(g(x)))
        