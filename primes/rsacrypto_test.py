#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:07:56 2017

@author: Kirby Urner

conda install pycrypto
pip3 install pycrypto

https://www.dlitz.net/software/pycrypto/

Note that OpenSSL is the more frequently used not-Python
util, run from the OS command line.
"""

from primes import invmod

import Crypto.PublicKey.RSA as rsa

def generating(s):
    print("Generating: ", s, end="")
    
rsaobj = rsa.generate(1024, progress_func=generating, e=17)

print(rsaobj)

p = rsaobj.p  # prime1
q = rsaobj.q  # prime2
n = rsaobj.n  # public key (p * q)
e = rsaobj.e  # public encrypt exponent
d = rsaobj.d  # secret decrypt key

def test_n():
    return p*q == n

def test_inverse():
    return d == invmod(e, (p-1)*(q-1))
    
def test_euler():
    totient_of_n = (p-1)*(q-1)
    return (e*d) % totient_of_n == 1

def test_decrypt():
    plaintext = b"able was i ere i saw elba"  # famous palindrome
    ciphertext = rsaobj.encrypt(plaintext, b"K")
    return rsaobj.decrypt(ciphertext[0]) == plaintext
