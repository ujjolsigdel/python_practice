
import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Select a choice(rock, paper, scissors): ")
        print()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("A tie")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print("You lose")

    again = input("Do you want to play again?(y/n): ").lower()
    if again == "n":
        running = False
print("Thanks for playing")


