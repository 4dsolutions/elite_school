#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:38:26 2018

@author: Kirby Urner

How to use LIKE keyword in SQLite:
https://stackoverflow.com/questions/3498844/sqlite-string-contains-other-string-query

"""

import sqlite3 as sql

class DB:
    """
    I connect you to a database, use me as a 
    context manager
    """
    
    def __init__(self, target):
        # target to dial
        self.source = target
        
    def connect(self):
        """
        dial the target and connect
        """
        # we'll be needing these
        self.conn = sql.connect(self.source)
        self.curs = self.conn.cursor()
        
    def __enter__(self):
        """
        upon entering the context, I do my job 
        """
        self.connect() # delegating...
        return self    # I am valuable
    
    def __exit__(self, *oops):
        if oops:
            return False
        return True
    
def tag_filter(the_tag):
    
    with DB("bookmarks.db") as db:
        # see Stackoverflow link in module's __doc__
        db.curs.execute("SELECT * FROM "
                        "Bookmarks WHERE " # whoah, this OK?
                        "bk_tags LIKE ? ", (the_tag,))
        results = list(db.curs.fetchall())
    # database closes through __exit__, yahoo!      
    return results

if __name__ == "__main__":
    # try %comedy%  %docs% %tool% and %glossary% too
    for record in tag_filter("%comedy%"):
        print( record )

