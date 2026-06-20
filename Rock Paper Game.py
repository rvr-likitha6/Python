# -*- coding: utf-8 -*-
"""
Rock, paper, scissors game
"""
import random

choices = ["rock", "paper", "scissors"]

# what beats what
beats = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}


def get_player_choice():
    while True:
        my_choice = input("rock, paper or scissors? ").strip().lower()
        if my_choice in choices:
            return my_choice
        print("type rock, paper or scissors")


def check_winner(player, computer):
    if player == computer:
        return "tie"
    elif beats[player] == computer:
        return "player"
    else:
        return "computer"


def main():
    print("=== Rock Paper Scissors ===")

    player_wins = 0
    computer_wins = 0
    ties = 0

    while True:
        print()
        my_choice = get_player_choice()
        comp_choice = random.choice(choices)

        print(f"you: {my_choice}")
        print(f"computer: {comp_choice}")

        result = check_winner(my_choice, comp_choice)

        if result == "tie":
            print("its a tie!")
            ties += 1
        elif result == "player":
            print("you win!")
            player_wins += 1
        else:
            print("computer wins!")
            computer_wins += 1

        print(f"\nscore - you: {player_wins} | computer: {computer_wins} | ties: {ties}")

        again = input("\nplay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("ok bye!")
            break


main()
