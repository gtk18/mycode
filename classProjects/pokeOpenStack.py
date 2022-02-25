#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:59:23 2022

@author: gtknapp18
"""
outFile = open("chosenPokeStats.rc","a")

pokemonType = input("What type of Pokemon you looking for? ")
print("export pokemonType=" + pokemonType, file=outFile )

outFile.close()


