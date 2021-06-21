#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:06:40 2017

@author: Kirby Urner

This is simple trial by division meaning any new odd
number candidate that survives being divided by every 
prime on file up to sqrt(candidate), gets added to the
hall of fame, i.e. is considered prime as well.

"""
import itertools
from operator import mod as remainder

class PrimeNumbers:

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

if __name__ == "__main__":
    p = PrimeNumbers()  # class based iterator
    print([next(p) for _ in range(30)])