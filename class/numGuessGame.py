#!/usr/bin/env python3
"""Number guessing game!"""

import random

def main():
    num= random.randint(1,100)

    while True:
        guess= int(input("Guess a number between 1 and 100: "))

        if guess > num:
            print("Too high!")

        elif guess < num:
            print("Too low!")

        else:
            print("Correct!")
            break

main()
