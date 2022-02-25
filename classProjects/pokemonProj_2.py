#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:24:48 2022

@author: gtknapp18
"""

# =============================================================================
# #creating output files from Data Sets
# 
# pokefile = open("pokedex.txt", "r")
# 
# print(pokefile.read())
# 
# pokefile.close()
# =============================================================================

pokefile = open("pokedex.txt", "r")   #OVERALL nicly displayed output##

pokefilelist = pokefile.readlines() #using readlines.()
print(pokefilelist)

for x in pokefilelist:
    print(x)

pokefile.close()


# =============================================================================
# pokefile = open("pokedex.txt", "r")
# 
# pokefilelist = pokefile.read() #displays file to the screen
# 
# pokeblog = pokefilelist.splitlines()
# 
# print(pokeblog)
# 
# pokefile.close()
# #not the prettiest output...
# =============================================================================
# =============================================================================
# 
# with open("pokedex.txt", "r") as pokefile:
#     pokelist = pokefile.readlines()
#     
# print(pokelist)
# =============================================================================

