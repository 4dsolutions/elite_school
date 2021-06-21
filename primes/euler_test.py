#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:36:26 2017

@author: Kirby Urner

This module demonstrates the RSA algorithm for public 
key cryptography.  Neither test_small nor test_big uses
industrial strength public keys.  Generating primes or
probable primes of some thousands of digits would require
some additional algorithms.

RSA works by raising plaintext m by e mod N.  Thanks
to N and e, there's a secret d such that pow(m, e * d, N)
is the same as m.  It's like going in a circle, with e taking
us part way around, and d taking us the rest of the way around.

One may generate (e, d) pairs, given N, but only (e, N) are
made public.  Deriving d from N requires knowing N's prime
factors, which is considered too hard a problem to solve where
N's two prime factors are big enough.
"""

from math import gcd
from binascii import hexlify, unhexlify

def totatives(n):
    return [x for x in range(1, n) if gcd(x, n) == 1]

def phi(n):
    return len(totatives(n))

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

def invmod(a, b):
    return xgcd(a, b)[1] % b


def test_small():
    # small number example
    print("---< SMALLER NUMBERS >---")
    p1 = 647
    p2 = 1213
    N = p1 * p2
    phiN = phi(N)  # small enough to use phi()
    e = 7
    d = invmod(e, phiN) # (e * d) % phiN == 1
    
    print("Public Stuff", (e, N))
    print("Secret Stuff", (d, p1, p2))
    
    m = b"it"  # bytes
    print("Text to encrypt: ", m)
    p_int = int(hexlify(m), 16)
    
    assert pow(p_int, e*d, N) == p_int
    
    c = pow(p_int, e, N)  # <--- encrypt
    output = pow(c, d, N) # <--- decrypt
    result = unhexlify(hex(output)[2:]) # drop "0x"
    print("Decrypted:       ", result)


def test_big():
    # bigger number example (still tiny)
    print("---< LARGER NUMBERS >---")
    
    p1 = 500001668113
    p2 = 704001677459
    N = p1 * p2
    phiN = (p1 - 1) * (p2 - 1) # too big for phi()
    e = 17
    d = invmod(e, phiN) # (e * d) % phiN == 1
    
    print("Public Stuff", (e, N))
    print("Secret Stuff", (d, p1, p2))
    
    m = b"dingaling"  # bytes
    print("Text to encrypt: ", m)
    p_int = int(hexlify(m), 16)
    
    assert pow(p_int, e*d, N) == p_int
    
    c = pow(p_int, e, N)  # <--- encrypt
    output = pow(c, d, N) # <--- decrypt
    result = unhexlify(hex(output)[2:]) # drop "0x"
    print("Decrypted:       ", result)

if __name__ == "__main__":
    test_small()
    test_big()
