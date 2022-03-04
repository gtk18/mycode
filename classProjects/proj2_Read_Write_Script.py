#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:24:48 2022

@author: gtknapp18
"""
import csv

#creating output files from Data Sets

pokefile = open("pokedex.txt", "r")

print(pokefile.read())

pokefile.close()

totalDragons = 0
totalUser = 0
with open("pokedexData.txt", "r") as pokefile:#OVERALL nicly displayed output##
     for drag in pokefile:
        if "Dragon" in drag:
            totalDragons = totalDragons + 1
print("There are",totalDragons, "dragon type pokemon, wow!")
           
with open("pokedexData.txt", "r") as pokefile2:
    user = str(input("What type of pokemon would you like to see the total of? Fire or Ice or Poison?"))
    for x in pokefile2:
        # x = x.rstripe('\n')
        if user in pokefile2:
            totalUser = totalUser + 1       

print("There are",totalUser,"pokemon type that you chose! Wow! ")

outFile = open("chosenPokeStats.rc","a")

pokemonType = input("What's your favorite pokemon?")
print("saving pokemonType=" + pokemonType, file=outfile)
outFile.close()
#i can't figure out how to print what the user inputs as a selection...fail.


# user = str(input("What type of pokemon would you like to see the total of?"))
#     for x in pokefile:
#         if user in drag:
#             totalUser = totalUser + 1

# =============================================================================
# # pokefilelist = pokefile.readlines() #using readlines.()
# 
# # print(pokefilelist)
# # for dragonText in pokefile:
# #     if "Dragon" in dragonText:
# #         totaldragons += 1 
# # print(totaldragons)
# 
# # pokefile.close()
# =============================================================================


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

