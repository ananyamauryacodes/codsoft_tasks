# -----------------------------------------
# Rock Paper Scissors Game
# Player vs Computer
# -----------------------------------------

import random

options = ["rock", "paper", "scissors"]

while True:

    computer_move = random.choice(options)

    player_move = input("Choose rock, paper, or scissors: ").strip().lower()

    print("Your choice:", player_move)

    if player_move not in options:
        print("Please enter a valid choice.")

    else:
        print("Computer's choice:", computer_move)

        if player_move == computer_move:
            print("Match Draw!")

        elif (
            (player_move == "rock" and computer_move == "scissors") or
            (player_move == "paper" and computer_move == "rock") or
            (player_move == "scissors" and computer_move == "paper")
        ):
            print("Congratulations! You won.")

        else:
            print("Computer wins this round.")

    choice = input("Play another round? (yes/no): ").strip().lower()

    if choice == "no":
        print("Thanks for playing. See you next time!")
        break

    elif choice != "yes":
        print("Invalid input! Exiting the game.")
        break