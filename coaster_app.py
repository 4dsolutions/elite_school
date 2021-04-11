# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:05:10 2017
Modified April 3, 2020

@author: Kirby Urner
"""

from make_coasters_db import DB
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    body = '''<h1>Coasters!</h1><br />
    <img src="{}" width="320" height="320"><br />'''.format("/static/oakspark.jpg")
    return basic_html("Roller Coasters!", body)

@app.route("/coasters")
def coasters():
    return all_coasters()

@app.route("/coasters/<coaster>")
def coaster(coaster):
    print("one coaster...")
    return one_coaster(coaster)
    
def all_coasters():
    with DB() as db:
        query = ("SELECT name, park, yr_opened FROM Coasters "
                 "ORDER BY name")
        db.get_coasters(query)
        results = []
        for rec in db.cursor.fetchall():
            results.append(rec)
            
    body =  "<ul>"+ \
            "\n".join(["<li>{}, {}, {}</li>".format(*data) for data in results]) + \
            "</ul>"
    return basic_html("All Coasters", body)

def one_coaster(coaster):
    with DB() as db:
        if "'" in coaster:
            coaster = coaster.replace("'", "''")
        if coaster:
            query = ("SELECT * FROM Coasters "
                     "WHERE name = '{}'".format(coaster))  
        db.get_coasters(query)
        print(query)
        results = []
        for rec in db.cursor.fetchall():
            print(rec)
            results.append(rec)
            fields =("Name:  {} <br /> ",
           "Park:  {} <br /> ",
           "State: {} <br /> ",
           "Country: {} <br /> ",
           "Duration: {} <br /> ", 
           "Speed: {} <br />",
           "Height: {} <br />",
           "VertDrop: {} <br />", 
           "Length: {} <br />",
           "Yr_Opened: {} <br />",
           "Inversions: {} <br />")
            body = ("\n".join(fields))
            body = body.format(*results[0])
            break
        else:
            body = "404 No Such Rollercoaster Found"
            
    return basic_html(coaster, body)
    
def basic_html(title="Web Page", body="content goes here"):
    page = ("<!doctype html>\n"
            "<html>\n"
            "<head>\n"
            "<title>{}</title>\n"
            "</head>\n"
            "<body>\n"
            "{}\n"
            "</body>\n"
            "</html>").format(title, body)
    return page
        
if __name__ == "__main__":
    app.run()
    