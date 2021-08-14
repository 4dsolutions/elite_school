#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 16:57:35 2021

@author: mac
"""


def D(f, h=1e-8):
    def d(x):
        return (f(x+h)-f(x))/h
    return d

def S(f, h=1e-2):
    def s(start, x):
        domain = np.arange(start, x, h)
        return sum([f(x)*h for x in domain])
    return s

def pow2(x):
    return pow(x, 2)

int_pow2 = S(pow2)
# diff_pow2 = D(pow2)

import numpy as np
import pandas as pd

domain = np.linspace(-5, 5, 400)

table = pd.DataFrame(
           {'x'   : domain, 
            'pow2': [pow2(x) for x in domain], 
            'int': [int_pow2(-5, x) for x in domain]})

table.plot(x='x', grid=True);