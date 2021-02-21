# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 04:58:14 2016

@author: kurner

From the docs:

sys.exc_info()

This function returns a tuple of three values that give information 
about the exception that is currently being handled. The information 
returned is specific both to the current thread and to the current 
stack frame. If the current stack frame is not handling an exception, 
the information is taken from the calling stack frame, or its caller, 
and so on until a stack frame is found that is handling an exception. 
Here, “handling an exception” is defined as “executing an except clause.” 
For any stack frame, only information about the exception being 
currently handled is accessible.

If no exception is being handled anywhere on the stack, a tuple 
containing three None values is returned. Otherwise, the values 
returned are (type, value, traceback). Their meaning is: type 
gets the type of the exception being handled (a subclass of 
BaseException); value gets the exception instance (an instance 
of the exception type); traceback gets a traceback object (see 
the Reference Manual) which encapsulates the call stack at the 
point where the exception originally occurred.

"""

from keyword import kwlist
from random import choice
import sys

class EscapeVictorious(Exception):
    pass

class KickFromCastle(Exception):
    pass

class Castle:
    
    def __init__(self, secret):
        self.__xyjk = secret
        self.guesses = 0
        self.hints = 0
        
    def __enter__(self):
        """get the ball rolling"""
        print("Welcome to Spooky Castle. To Escape, guess the secret keyword")
        return self  # <-- make instance available within scope via 'as'

    def __exit__(self, *exception_data):
        """raise a ruckus"""
        if exception_data[0] == EscapeVictorious:
            print("Congratulations!")
            print("Here is your", exception_data[1])
            return True
        if exception_data[0] == KickFromCastle:
            print("Better Luck Next Time")
            print("The keyword was", self.__xyjk)
            return False

    def hint(self):
        if self.hints == 0:
            print("The keyword begins with", self.__xyjk[0])
        elif self.hints == 1:
            print("The keyword is", len(self.__xyjk), "letters long.")
        else:
            print("You've had your two hints, sorry")
        self.hints += 1
        
    def query(self):
        """gradations"""
        print("So what is the secret keyword then?  Guess so far:", self.guesses)
        ans = input("You may answer (or type 'hint'): ")
        if ans == self.__xyjk:
            print("Excellent, we're done here")
            print("You have won the Copper Key") # <-- RealPlayer One (novel)
            raise EscapeVictorious("Copper Key")
        elif self.guesses == 5:
            print("Uh oh, you're out of guesses, sigh")
            raise KickFromCastle("We're done!")
        elif ans == "hint":
            self.hint()
            return
        else:
            self.guesses += 1
            print("No, that's not it.")
            

if __name__ == "__main__":
    the_secret = choice(kwlist)
    try:
        with Castle(the_secret) as spooky:
            while True:
                spooky.query()
    except:
        print("Handling: ", sys.exc_info()[0].__name__)
        print(sys.exc_info()[1])  # <--- triggers __str__
        print(type(sys.exc_info()[1]))
    finally:
        print("Always always run this...")
