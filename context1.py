#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:30:04 2017
Modified April 5, 2018

@author: Kirby Urner

Typical to put your logic for connecting and gaining
a cursor (if needed) in __enter__, for use with scope
(of a context), then to close connection in __exit__
while handling / relaying any exceptions.

Used by usercrud.py
"""

import sqlite3 as sql

class DB:
    
    def __init__(self, the_db):
        self.dbname = the_db
    
    def __enter__(self):
        """
        connect and get conn, curs
        """
        self.conn = sql.connect(self.dbname)
        self.curs = self.conn.cursor()  
        return self  # this very object is db
        
    def __exit__(self, *oops):
        if self.conn:
            self.conn.close()
        if oops[0]:  # exception occurred, else None
            return False  # not handling it...
        return True       # nothing to handle


# we'll want to import DB without triggering this test:
if __name__ == "__main__":    
    with DB("./bigdata/data_warehouse/x_files.db") as db:
        # connected...
        db.curs.execute("SELECT  count(*), shape "
                        "FROM ufo_sightings GROUP BY shape")
        for row in db.curs.fetchall():
            print(row)
            
    print("Outside Context")
# disconnected       
    