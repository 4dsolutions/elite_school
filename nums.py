#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 09:10:18 2020

@author: Kirby Urner
"""
import itertools
from operator import mod as remainder

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

def tots(N):  # on the same line is OK
    """
    List numbers with no factors in common with N
    """
    return [n for n in range(1, N) if gcd(n, N)==1]

def totient(N):
    "Euler's Totient"
    return len(tots(N))

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
        