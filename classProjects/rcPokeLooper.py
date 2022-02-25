#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 23:40:13 2022

@author: gtknapp18
"""

import csv

with open("pokedex.txt", "r") as pokeData:
    i = 0
    for row in pokeData.reader(pokeData):
        i = i + 1
        filename = f"chosenPokeStats.rc{i}" #f strings says to fill in the value of i
        
        
        
        #will finish this another time...