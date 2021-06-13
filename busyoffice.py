#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 14:30:35 2017
Modified April 5, 2018
Modified May 24, 2018
Modified June 5, 2021

@author: Kirby Urner

alice = Secretary("Alice")  # implements Descriptor protocol

(data descriptor = full service)

The idea being, self.secretary knows the self that 
calls it, the self.worker, and so can save the 
message directly in self.worker.__dict__['inbox']

Think of other secretaries for other tasks besides
taking taking messages.
"""

import datetime, pytz

UTC = pytz.timezone('UTC')
PACIFIC = pytz.timezone('US/Pacific')
EASTERN = pytz.timezone('US/Eastern')

class Secretary:

    """
    descr.__get__(self, obj, type=None) --> value

    descr.__set__(self, obj, value) --> None

    descr.__delete__(self, obj) --> None
    
    'inbox' is hard-coded as one of the api elements of an obj
    """
    
    def __init__(self, nm):
        self.name = nm
        
    def __set__(self, obj, val):
        print(f"Secretary {self.name}: thank you.  Saving.")
        if not 'inbox' in obj.__dict__:
            obj.inbox = [ ] # initialize empty list
        # (datetime, message) appended to list
        obj.inbox.append((datetime.datetime.now(tz=UTC), val))

    def __get__(self, obj, cls):
        print(f"Worker {obj.worker} {cls.company}: Inbox:")  # obj is the worker's self, cls its class
        if ('inbox' not in obj.__dict__) or ({} == obj.__dict__):
            return 'Empty'
        else:
            return [(message[0].astimezone(tz=obj.timezone), message[1])
                       for message in obj.inbox]
        
class BusyOfficeWorker:

    my_assistant = Secretary("Frank")  # add a layer of politeness
    company = "Global Data Corporation"

    def __init__(self, worker_bee, tz=PACIFIC):
        self.worker = worker_bee
        self.timezone = tz

    def leave_message(self, message):
        self.my_assistant = message  # triggers __set__

    def pickup_message(self):
        return self.my_assistant # that'll be *my* inbox, triggers __get__

    def empty_inbox(self):
        # simplest possible
        if "inbox" in self.__dict__: # if there
            del self.__dict__["inbox"]
            
    def report(self):
        ms = self.pickup_message()
        if ms == 'Empty':
            print('Empty')
        else:
            for m in ms:
                print(f"Time: {m[0]}\n Message: {m[1]}")

def simulation():
    # incoming pipeline
    print("Taking messages...\n")
    worker1 = BusyOfficeWorker("Cindy", PACIFIC)
    worker2 = BusyOfficeWorker("Shelly", EASTERN)

    worker2.report() # testing empty inbox situation

    worker1.leave_message("Hello, this is to remind you...")
    worker2.leave_message("Your dentist appointment for...")
    worker2.leave_message("Your car is ready for pickup.")
    worker1.leave_message("Hello, this is to remind you...")
    worker1.leave_message("Spam call")

    # retrieval process
    print("\nRetrieving messages...\n")
    print("worker1:") 
    worker1.report()

    print()
    print("worker2:")
    worker2.report()
    
if __name__ == "__main__":
    simulation()