#!/usr/bin/env python3

import csv

with open("pokedex.txt", "r") as pd:
    pokedex= csv.DictReader(pd)

    for x in pokedex:
        print(f'{x["Name"]} belongs to this generation {x["Generation"]}')
