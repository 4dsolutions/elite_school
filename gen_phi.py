# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:08:49 2015
Modified Oct 17, 2017
Modified Feb 27, 2020

@author: Kirby Urner

Another generator example:  converging to Phi

https://oeis.org/A000045
http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/phi.html#section7

Shows eval( ) in action

"""

from decimal import Decimal, getcontext

getcontext().prec = 35

one = Decimal('1')
five = Decimal('5')
check = (one + five.sqrt())/2

def continuedint():
    
    patt = "+ 1/(1"
    the_expr = ''  # empty
    n = 1
    
    while True:
        the_expr = the_expr + patt
        the_frac = "1 " + (the_expr + ")" * n)
        
        # print(the_frac)
        yield the_frac  # or show the_frac
        
        n += 1
        
def continued():
    
    patt = "+ one/(one"
    the_expr = ''  # empty
    n = 1
    
    while True:
        the_expr = the_expr + patt
        the_frac = "1 " + (the_expr + ")" * n)
        
        # print(the_frac)
        yield eval(the_frac)  # or show the_frac
        
        n += 1
             
def test_me():
    the_gen = continued()
    last_time = 1
    while True:
        approx = next(the_gen)
        print(approx)
        if approx == check:
            break
        if abs(approx - last_time) < Decimal(1e-35): 
            break
        last_time = approx

    print("Approx:", approx)
    print("Check :", check)
    
if __name__ == "__main__":
    test_me()
