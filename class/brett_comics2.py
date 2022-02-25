

with open("brett_comics.txt","r") as comicdata:
    for line in comicdata:
        if "X-men" in line:
            print(line)
