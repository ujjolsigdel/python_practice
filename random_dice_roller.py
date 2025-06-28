
import random


dice = []
total = 0
num_of_dice= int(input("How many dice do you want to roll? "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
print(dice)

for die in dice:
    total += die
print(f"Total: {total}")