#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:09:08 2021

@author: Kirby Urner
"""

from random import choice

class Die:
    
    def __init__(self, values=range(1,7)):
        self.values = values
        self.counter = 0
        
    def shake(self):
        self.counter += 1
        return choice(self.values)
    
class Cup:
    
    def __init__(self):
        self.dice = [ ]
    
    def add(self, die):
        self.dice.append(die)
        
    def shake(self):
        return sum([d.shake() for d in self.dice])
    

c = Cup()
c.add(Die())
c.add(Die())
results = []

while True:
    r = c.shake()
    results.append(r)
    if r == 12:
        break

print(results)
