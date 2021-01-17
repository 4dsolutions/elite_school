#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 21:07:49 2020

@author: Kirby 

Load the unicodes for food emoji.

🍔
HAMBURGER
Unicode: U+1F354 (U+D83C U+DF54), UTF-8: F0 9F 8D 94

https://unicode.org/emoji/charts/full-emoji-list.html

"""

import unicodedata as names

#food-fruit
fruits = [chr(hexcode) 
          for hexcode in range(0x1F347, 0x1F353)]

fruit_names = [names.name(c) for c in fruits]

foods = ['🍗', '🍩','🎂','🍟', '🍞']
food_names = [names.name(f) for f in foods]

faces = [chr(code) 
          for code in range(0x1F600, 0x1F64A)
          if code not in range(128577, 128581)]

face_names = [names.name(c) for c in faces]