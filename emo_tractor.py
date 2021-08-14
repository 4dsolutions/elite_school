#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 15:36:57 2018

@author: kurner
"""

from tractor_1 import Field, TractorWriter
import unicodedata

skull = unicodedata.lookup("skull")
ghost = unicodedata.lookup("ghost")
tiger = unicodedata.lookup("tiger")
octopus = unicodedata.lookup("octopus")

def emofield1():
    f = Field(10,10)
    f.add_tractor(TractorWriter)
    f.add_tractor(TractorWriter)
    t1 = f.Ts[0] # get the tractor
    t2 = f.Ts[0] # get the tractor    
    t1.write(skull*100, (0,0))
    for _ in range(100):
        next(t1)
    t2.write(ghost*5, (4,4))
    for _ in range(100):
        next(t2)
    print(f)

def emofield2():
    f = Field(10,10)
    f.add_tractor(TractorWriter)
    f.add_tractor(TractorWriter)
    t1 = f.Ts[0] # get the tractor
    t2 = f.Ts[0] # get the tractor    
    t1.write(octopus*100, (0,0))
    for _ in range(100):
        next(t1)
    t2.write(tiger*5, (4,4))
    for _ in range(100):
        next(t2)
    print(f)
    
emofield1()
emofield2()
