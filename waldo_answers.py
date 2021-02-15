# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:23:45 2017

@author: Kirby Urner

Example of the "Where's Waldo" genre:
https://i.ytimg.com/vi/SiYrSYd7mlc/maxresdefault.jpg

Extract "Waldo" from each data structure

"""

def quiz():
    data = {"id:":["Joe", "Smith"],
            "mother": ["Judy", "Smith"],
            "father": ["Waldo", "Smith"]}
            
    waldo = data['father'][0] # output "Waldo"
    print(waldo)
    #%%
    #============================
    data = {"Waldo": {"scores":[34,56,23,98,89]}}
    
    waldo = list(data.keys())[0] # output "Waldo" hint: dict.keys()
    print(waldo)
    #============================
    data = {(1,2):{"Name":["Waldeen", "Smith"]},
            (4,5):{"Name":["Waldorf", "Smith"]},
            (9,0):{"Name":["Waldo", "Smith"]}}
    
    waldo = data[(9,0)]['Name'][0] # output "Waldo" hint: tuples may be keys
    print(waldo)
    #============================
    data = ["Joe", 3, 7, ["dog", ("cat", "Waldo")], 27, {}]
    
    waldo = data[3][1][1]
    print(waldo) # output "Waldo'
    
    #============================
    data = ([], [], ())
    data[1].append("Wendy")
    data[1].append("Waldo")
    data[1].append("Willow")
    # where's Waldo?
    waldo = data[1][1]
    print(waldo)     



if __name__ == "__main__":
    quiz()

# NOW MAKE UP SOME OF YOUR OWN!