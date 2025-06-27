

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)

guesses = 0
is_running = True

print("----Python Number Guessing Game----")

while is_running:
    guess = input(f"Select a number between {lowest_num} and {highest_num}: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("THat is out of range")
            print(f"Select a number between {lowest_num} and {highest_num}")
        elif guess > answer:
            print("Guess lower!")
        elif guess < answer:
            print("Guess higher!")
        else:
            print(f"You are correct! The number is {answer}")
            print(f"You took {guesses} guesses")
            is_running = False
    else:
        print(f"Select a number between {lowest_num} and {highest_num}")
