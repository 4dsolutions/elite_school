"""
Created on Thu Jan 28 21:27:07 2016

@author: kurner

A namedtuple is a subclass of tuple allowing for named
columns and therefore dot notation access, treating 
elements as named attributes.

Bookmark(place='Anaconda.org', url='http://anaconda.org', tags='tool')
"""

from collections import namedtuple
from context1 import DB

PRINT = False  # make true if you wish screen noise (echo of bookmarks)

Bmk = namedtuple('Bookmark', 'place url tags')

# tuple of tuples
tuples = (
    ("Anaconda.org", 
     "http://anaconda.org", 
     "tool"),
    ("Python.org", 
     "http://python.org", 
     "source"),
    ("Python Docs", 
     "https://docs.python.org/3/", 
     "docs"),
    ("''New Math'' by Tom Lehrer (animated)",
     "https://youtu.be/UIKGV2cTgqA", 
     "comedy"),
    ("Spaghetti Code", 
     "http://c2.com/cgi/wiki?SpaghettiCode", 
     "glossary"),
    ("Structured Programming", 
     "http://c2.com/cgi/wiki?StructuredProgramming", 
     "glossary, history"),
    ("Map of Languages", 
     "http://archive.oreilly.com/pub/a/oreilly//news/languageposter_0504.html", 
     "docs"),
    ("XKCD", "http://xkcd.com", "comedy"),
    ("Will Geeks Rule? CBS News (world domination meme)",
     "http://www.cbsnews.com/news/will-geeks-rule-the-world/", 
     "glossary, comedy"),
    ("Django","https://docs.djangoproject.com/", "source"),
    ("PythonAnywhere","https://www.pythonanywhere.com/", "tool"),
    ("CodeAcademy: Python",
     "https://www.codecademy.com/learn/python", 
     "docs"),
    ("Unicode on Youtube", 
     "https://www.youtube.com/watch?v=Z_sl99D2a18", 
     "docs, glossary"),
    ("In Defense of Ada", 
     "http://www.grunch.net/synergetics/adaessay.html", "comedy, history"),
    ("Grace Hopper on Letterman", 
     "https://www.youtube.com/watch?v=1-vcErOPofQ", "source"),
    ("The Mind of a Genius: John von Neumann", 
     "https://www.youtube.com/watch?v=XZ9tt72feL8", "docs"),
    ("World Domination meme", 
     "https://www.google.com/search?q=linux+world+domination&safe=off&source=lnms&tbm=isch", 
     "glossary, comedy, culture"),
    ("Warriors of the Net", 
     "https://www.youtube.com/watch?v=PBWhzz_Gn10", 
     "docs, glossary, comedy"),
    ("LAMP stack", 
     "https://www.google.com/search?q=lamp+stack&safe=off&biw=787&bih=535&source=lnms&tbm=isch", 
     "glossary"),
    ("LAMP stack (Wikipedia)",
     "https://en.wikipedia.org/wiki/LAMP_(software_bundle)", 
     "glossary"),
    ("Find string in string in SQLite", 
     "https://stackoverflow.com/questions/3498844/sqlite-string-contains-other-string-query", 
     "docs"),
    ("What Python IDE is best?", "https://www.quora.com/What-is-your-favorite-IDE-for-Python-programming-and-why",
     "tool"),
    ("More Help with Python", "https://medium.com/@kirbyurner/more-help-with-python-9afe2d0affe8",
     "docs")
)

# lets make these namedtuples instead OK?
# *tup explodes each tuple into two positionals, what Bmk expects

def bumpy():
    """
    if you expect problems in the input
    """
    the_list = []
    for tup in tuples:
        try:
            the_list.append(Bmk(*tup))
        except TypeError:
            print("Ill-formed tuple:", tup)
    return the_list

def smooth():
    """
    if you expect smooth sailing i.e. no problems with tuples
    """
    the_list = [Bmk(*tup) for tup in tuples] # list comprehension! 
    return the_list
        
def printall():    
    for bmk in bookmarks:
        # Bookmark(place='Anaconda.org', url='http://anaconda.org')
        print(bmk)   # notice format of output: __repr__
        print("-")

if __name__ == "__main__":

    bookmarks = bumpy()
    # bookmarks = smooth()

    if PRINT:
        printall()
        
    # login
    with DB("bookmarks.db") as db:

        # https://www.sqlite.org/lang_droptable.html
        # DB API ???
        db.curs.execute("""DROP TABLE IF EXISTS Bookmarks""")
        db.curs.execute("""CREATE TABLE Bookmarks
            (bk_place text PRIMARY KEY,
             bk_url text,
             bk_tags text)""")
        
        for bmk in sorted(bookmarks):
            query = ("INSERT INTO Bookmarks " 
            "(bk_place, bk_url, bk_tags) "
            "VALUES ('{}', '{}', '{}')".format(bmk.place, bmk.url, bmk.tags))
            # print(query)
            db.curs.execute(query)
            db.conn.commit()
