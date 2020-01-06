#! /usr/bin/env python3

import random

MAX = 10

def display_title():
    print("Guess the number")
    print()
    print("Im thinking of a number between 1 to " + str(MAX))

def play_game():
    tries = 0
    number = random.randint(1, MAX)
    guess = int(input("\nYour guess: "))
    while guess != number:
        if guess < number:
            print("Too low.")
            tries += 1
        elif guess > number:
            print("Too high.")
            tries += 1
        guess = int(input("Your guess: "))
    print("You guessed it in", str(tries), "tries.")

def main():
    choice = "y"
    while choice.lower() == "y":
        display_title()
        play_game()
        choice = input("\nWould you like to play again? (y/n): ")
    print("\ncya")

if __name__=="__main__":
    main()

