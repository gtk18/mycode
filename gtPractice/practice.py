#!/usr/bin/env python3

for i in range(4):
    print (i)

for x in range(10):
    print(x, end=" ")

print('\n')
#for x in range(10):
#    print(x, end = for z in range(10):
#        print(z))

fruitbowl = ['apple','pear','grapes']
for x in fruitbowl:
    print(x)

print('\n')

for fruit in fruitbowl:
    print("Look at all these goodies:",fruit)
print("")
foo = open("myfruitfile.txt","w")
for fruit in fruitbowl:
    print(fruit, file=foo)
foo.close()
