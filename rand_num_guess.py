#!/usr/bin/env python3

# Created by: Navin Balekomebole
# Created on: Dec 2021
# This program checks if there is over 30 students
import random


def main():
    # this function checks if there is over 30 students
    
    # set correct
    
    correct = random.randint(0, 9)

    # input
    guess_number = int(input("Enter your number: "))
    print("")

    # process & output
    if guess_number == correct:
        print("You guessed correctly!")
        
    if guess_number != correct:
        print ("you guessed incorrectly, the number was {}.". format(correct))


if __name__ == "__main__":
    main()