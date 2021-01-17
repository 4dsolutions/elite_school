#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 09:10:18 2020

@author: Kirby Urner
"""

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


# https://repl.it/@kurner/Compose-Functions

# take any two functions as args and return their composition
compose = lambda f, g: (lambda x: f(g(x)))
        