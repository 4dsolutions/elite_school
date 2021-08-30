#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 16:47:27 2021

@author: Kirby Urner
"""

from math import gcd
from random import shuffle 
from string import ascii_lowercase  # all lowercase letters
from nums import invmod


class Rat:
    
    def __init__(self, numer, denom=1):
        """Simplify to lowest terms upon creation"""
        common = gcd(numer, denom)
        self.numer = numer // common
        self.denom = denom // common
        
    def __mul__(self, other):
        if type(other) == int:
            other = Rat(other, 1)
        return Rat(self.numer * other.numer, self.denom * other.denom)
    
    __rmul__ = __mul__
    
    def __truediv__(self, other):
        """Multiply by the multiplicative inverse (reciprocal)"""
        return self * ~other
        
    def __invert__(self):
        """Flip Over, Reciprocal:  self * ~self == (1/1)"""
        return Rat(self.denom, self.numer)
    
    def __add__(self, other):
        if type(other) == int:
            other = Rat(other)
        return Rat(
                (self.numer * other.denom) + (other.numer * self.denom), 
                 self.denom * other.denom)
    
    __radd__ = __add__
    
    def __sub__(self, other):
        """Add the additive inverse"""
        return self + (-other)
    
    __rsub__ = __sub__
    
    def __neg__(self):
        "Additive inverse"
        return Rat(-self.numer, self.denom)
    
    def __pow__(self, n: int):
        if type(n) != int:
            raise TypeError
        if n == 0:
            return Rat(1, 1)
        if n == 1:
            return Rat(self.numer, self.denom)
        if n < 0:
            result = ~self
            n = abs(n)
            for _ in range(n-1):
                result = result * ~self
            return result    
        else:
            result = self
            for _ in range(n-1):
                result = result * self
            return result        
        
    def __repr__(self):
        if self.denom == 1:
            return f"({self.numer})"
        return f"({self.numer}/{self.denom})"


class Mod:
    
    _modulus = 12
    
    def __init__(self, n):
        self.value = n % self._modulus
        
    def __eq__(self, other):
        return self.value == other.value % self._modulus
    
    def __repr__(self):
        return "({} mod {})".format(self.value, self._modulus)
    
    def __add__(self, other):
        return type(self)(self.value + other.value)
    
    def __mul__(self, other):
        return type(self)(self.value * other.value)
    
    def __truediv__(self, other):
        return self * ~other
    
    def __neg__(self):
        return type(self)(-self.value)
    
    def __sub__(self, other):
        return self + -other
    
    def __invert__(self):
        return invmod(self.value, self._modulus)
        #for i in range(1, self._modulus):
        #    if self * Mod(i) == Mod(1):
        #        return Mod(i)
        
    def __pow__(self, n):
        if n < 0:
            value = (~self).value
            n = abs(n)
        else:
            value = self.value
        return type(self)(pow(value, n, self._modulus))
    
    def __hash__(self):
        return self.value
    

class P:
    """
    A Permutation
    
    self._code: a dict, is a mapping of iterable elements 
    to themselves in any order.
    """   

    def __init__(self, 
                 the_code = None,   # direct inject
                 inv_table = None,  # construct 
                 iterable = ascii_lowercase + ' '): # default domain
        """
        start out with Identity, or directly inject the mapping as
        a dict or use an inversions table to construct the permutation
        """
        if the_code:
            self._code = the_code
            
        elif inv_table:
            values = []
            for key in sorted(inv_table, reverse=True):
                if inv_table[key] >= len(values):
                    values.append(key)
                else:
                    values.insert(inv_table[key], key)
            self._code = dict(zip(sorted(inv_table), values))
            
        elif iterable:    
            try:
              # create two iterators for zipping together
              iter1 = iter(iterable)
              iter2 = iter(iterable)
            except:
                raise TypeError
                
            self._code = dict(zip(iter1, iter2))
        
    def shuffle(self):
        """
        return a random permutation of this permutation
        """
        # use shuffle
        # something like
        the_keys = list(self._code.keys()) # grab keys
        shuffle(the_keys)  # shuffles other one
        newP = P()
        newP._code = dict(zip(self._code.keys(), the_keys))
        return newP
        
    def encrypt(self, plain):
        """
        turn plaintext into cyphertext using self._code
        """
        output = ""  # empty string
        for c in plain:
            output = output + self._code.get(c, c) 
        return output
            
    def decrypt(self, cypher):
        """
        Turn cyphertext into plaintext using ~self
        """
        reverse_P = ~self  # invert me!
        output = ""
        for c in cypher:
            output = output + reverse_P._code.get(c, c)
        return output
 
    def __getitem__(self, key):
        return self._code.get(key, None)
               
    def __repr__(self):
        return "P class: " + str(tuple(self._code.items())[:3]) + "..."

    def cyclic(self):
        """
        cyclic notation, a compact view of a group
        """
        output = []
        the_dict = self._code.copy()
        while the_dict:
            start = tuple(the_dict.keys())[0]
            the_cycle = [start]
            the_next = the_dict.pop(start)
            while the_next != start:
                the_cycle.append(the_next)
                the_next = the_dict.pop(the_next)
            output.append(tuple(the_cycle))
        return tuple(output)

    def __mul__(self, other): 
        """
        look up my keys to get values that serve
        as keys to get others "target" values
        """
        new_code = {}
        for c in self._code:  # going through my keys
            target = other._code[ self._code[c] ]
            new_code[c] = target
        new_P = P(' ') 
        new_P._code = new_code
        return new_P
        
    def __truediv__(self, other):
        return self * ~other
                
    def __pow__(self, exp):
        """
        multiply self * self the right number of times
        """
        if exp == 0:
            output = P()
        else:
            output = self

        for x in range(1, abs(exp)):
            output *= self
        
        if exp < 0:
            output = ~output
            
        return output

    def __call__(self, s): 
        """
        another way to encrypt
        """
        return self.encrypt(s)  

    def __invert__(self):
        """
        create new P with reversed dict
        """
        newP = P(' ')
        newP._code = dict(zip(self._code.values(), self._code.keys()))
        return newP
        
    def __eq__(self, other):
        """
        are these permutation the same?  
        Yes if self._cod==e  other._code
        """
        return self._code == other._code
        
    def inversion_table(self):
        invs = {}
        invP = ~self
        keys = sorted(self._code)
        for key in keys:
            x = invP[key] # position of key
            cnt = 0
            for left_of_key in keys: # in order up to position
                if left_of_key == x: # none more to left
                    break
                if self._code[left_of_key] > key:
                    cnt += 1
            invs[key] = cnt
        return invs
        
def test_me():
    p = P() # identity permutation
    new_p = p.shuffle()
    inv_p = ~new_p 
    try:
        assert p == inv_p * new_p   # should be True
        print("First Test Succeeds")
    except AssertionError:
        print("First Test Fails")
    #==========    
    p = P().shuffle()
    try:
        assert p ** -1 == ~p
        assert p ** -2 == ~(p * p)
        assert p ** -2 == (~p * ~p)
        print("Second Test Succeeds")
    except AssertionError:
        print("Second Test Fails")
    #========== 
    p = P().shuffle()
    s = "able was i ere i saw elba"
    c = p(s)
    print("Plain:  ", s)
    print("Cipher: ", c)
    try:
        assert p.decrypt(c) == s
        print("Third Test Succeeds")
    except AssertionError:
        print("Third Test Fails")
    #========== 
    knuth = {1:5, 2:9, 3:1, 4:8, 5:2, 6:6, 7:4, 8:7, 9:3} # vol 3 pg. 12
    expected = {1:2, 2:3, 3:6, 4:4, 5:0, 6:2, 7:2, 8:1, 9:0} # Ibid
    k = P(the_code=knuth)
    try: 
        assert k.inversion_table() == expected
        print("Fourth Test Succeeds")
    except AssertionError:
        print("Fourth Test Fails")
    #========== 
    p = P(inv_table = expected)
    try: 
        assert p == k
        print("Fifth Test Succeeds")
    except AssertionError:
        print("Fifth Test Fails")
    #========== 
    p = P().shuffle()
    inv = p.inversion_table()
    print("Perm:", p._code)
    print("Inv table:", inv)
    new_p = P(inv_table = inv)
    try: 
        assert p == new_p
        print("Sixth Test Succeeds")
    except AssertionError:
        print("Sixth Test Fails")    

    