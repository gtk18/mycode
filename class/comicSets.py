#!/usr/bin/env python3

import  csv

input_filename = "brett_comics.txt"
output_filename= "brett's_comicsSorted.txt"
    #ideas to do with the comic file???
    #sort by character names? groups such as X-men, X-Force, etc?


    ## reqs: Your script must READ IN a file that contains data.
## Your script must OUTPUT information from the file in a readable/useful way

with open("brett_comics.txt", "r") as comicdata:
    for x in csv.reader(comicdata):
        print(x["X-men"])


