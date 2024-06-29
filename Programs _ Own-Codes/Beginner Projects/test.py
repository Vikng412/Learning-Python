import random
import math

def Guessing_game(a,b):
    comp_guess = random.randint(a,b)
    least_guess = int(math.log(b-a+1, 2))
    g = 0
    while g <= least_guess:
        if g == 1:
            print(f"{g}st Chance")
        elif g == 2:
            print(f"{g}nd Chance")
        elif g == 3:
            print(f"{g}rd Chance")
        elif g < least_guess:
            print(f"{g}th Chance")
        if g >= least_guess:
            print(f"Sorry, you ran out of guesses, the number was {comp_guess}!")
        elif g == least_guess:
            print("This is your last chance, guess carefully: ")
        elif g <= least_guess:
            guess = int(input("Guess the number: "))
            if guess > comp_guess:
                print("Try Again! You guessed too high")
            elif guess < comp_guess:
                print("Try Again! You guessed too small")
            elif guess == comp_guess:
                print("Congratulations, You've Guessed it!")
                exit()
            else:
                print("Invalid Input!!")
                print("Keep the guesses between the set range!")
        g += 1

a = int(input("Enter the start of range: "))
b = int(input("Enter the end of the range: "))
Guessing_game(a,b)