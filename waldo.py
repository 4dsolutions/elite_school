# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:23:45 2017

@author: Kirby Urner

Example of the "Where's Waldo" genre:
https://i.ytimg.com/vi/SiYrSYd7mlc/maxresdefault.jpg

Extract "Waldo" from each data structure

"""

data = {"id:":["Joe", "Smith"],
        "mother": ["Judy", "Smith"],
        "father": ["Waldo", "Smith"]}
        
waldo = None # output "Waldo"
print(waldo)
#%%
#============================
data = {"Waldo": {"scores":[34,56,23,98,89]}}

waldo = None # output "Waldo" hint: dict.keys()
print(waldo)
#%%
#============================
data = {(1,2):{"Name":["Waldeen", "Smith"]},
        (4,5):{"Name":["Waldorf", "Smith"]},
        (9,0):{"Name":["Waldo", "Smith"]}}

waldo = None
print(waldo)
#%%
#============================
data = ["Joe", 3, 7, ["dog", ("cat", "Waldo")], 27, {}]

waldo = None
print(waldo) # output "Waldo'

#============================
#%%
data = ([], [], ())
data[1].append("Wendy")
data[1].append("Waldo")
data[1].append("Willow")
# where's Waldo?
print(data)
waldo = None
print(waldo)     

# NOW MAKE UP SOME OF YOUR OWN!