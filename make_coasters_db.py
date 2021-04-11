# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:58:06 2017
Modified Oct 25, 2017

@author: Kirby Urner

Consumes csv data put into a dictionary by rollercoasters.py
Creates a SQL_Lite DB and inserts the data.
"""

import sqlite3 as sql

class DB:

    db_name = 'roller_coasters.db'

    @classmethod
    def __enter__(cls):
        print("running enter")
        cls.conn = sql.connect(cls.db_name)
        cls.cursor = cls.conn.cursor()
        return cls
        
    @classmethod
    def __exit__(cls, *oops):
        print("running exit")
        print(oops)
        cls.conn.close()

    @classmethod
    def zap_table(cls):
        # https://www.sqlite.org/lang_droptable.html
        cls.cursor.execute("""DROP TABLE IF EXISTS Coasters""")

    @classmethod
    def create_table(cls):
        cls.zap_table()
        cls.cursor.execute("""CREATE TABLE Coasters
            (Name text PRIMARY KEY, 
             Park text,
             State text, 
             Country text,
             Duration int,
             Speed int,
             Height int,
             VertDrop int,
             Length int,
             Yr_Opened int,
             Inversions int)""")
           
    @classmethod
    def save_coaster(cls, row):
        # row should be tuple / namedtuple
        query = ("INSERT INTO Coasters "
        "('Name', 'Park', 'State', 'Country', 'Duration', 'Speed'," 
        " 'Height', 'VertDrop', 'Length', 'Yr_Opened', 'Inversions')"
        " VALUES ('{}', '{}', '{}', '{}', "
        "{}, {}, {}, {}, {}, {}, {})").format
        #print(query(*row))
        cls.cursor.execute(query(*row))
        cls.conn.commit()
        
    @classmethod
    def get_coasters(cls, the_query):
        cls.cursor.execute(the_query)

if __name__ == "__main__":
    the_data = rollercoasters.read_csv()
            
    with DB() as db:
        db.zap_table()
        db.create_table()
        for rec in the_data.values():
            try:
                db.save_coaster(rec)
            except sql.OperationalError:
                print(rec)
            
    with DB() as db:
        query = ("SELECT name, park, yr_opened FROM Coasters "
                 "WHERE country = 'USA' ORDER BY Yr_Opened")
        db.get_coasters(query)
        results = []
        for rec in db.cursor.fetchall():
            results.append(rec)
    
    # fixed width allows overflow so truncate the data as well
    for row in results:
        # :a.b for string type fixes min and max width
        print("{:30.30} {:30.30} {:4}".format(*row))

    