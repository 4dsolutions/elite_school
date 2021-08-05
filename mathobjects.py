#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 16:47:27 2021

@author: Kirby Urner
"""

from math import gcd
#%%

class Rat:
    
    def __init__(self, numer, denom):
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
            other = Rat(other, 1)
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
        if n == 0:
            return Rat(1, 1)
        if n == 1:
            return self
        result = self
        for _ in range(n-1):
            result = result * self
        return result        
        
    def __repr__(self):
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
    
    def __pow__(self, n):
        return type(self)(pow(self.value, n, self._modulus))