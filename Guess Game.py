# -*- coding: utf-8 -*-
"""
Number Guessing Game
"""

import random


def get_difficulty():
    print("\nChoose a difficulty:")
    print("  1. Easy   (1–50,  unlimited guesses)")
    print("  2. Medium (1–100, 10 guesses)")
    print("  3. Hard   (1–200, 7 guesses)")

    while True:
        choice = input("\nEnter 1, 2, or 3: ").strip()
        if choice == "1":
            return 50, None     # max_number, max_guesses
        elif choice == "2":
            return 100, 10
        elif choice == "3":
            return 200, 7
        else:
            print("Please enter 1, 2, or 3.")


def get_guess(low, high):
    while True:
        try:
            guess = int(input(f"Your guess ({low}–{high}): "))
            if low <= guess <= high:
                return guess
            else:
                print(f"Please guess a number between {low} and {high}.")
        except ValueError:
            print("Please enter a whole number.")


def play_game():
    max_number, max_guesses = get_difficulty()
    secret = random.randint(1, max_number)
    attempts = 0
    low, high = 1, max_number

    print(f"\nI've picked a number between 1 and {max_number}. Can you guess it?")
    if max_guesses:
        print(f"You have {max_guesses} guesses. Good luck!\n")
    else:
        print("You have unlimited guesses. Good luck!\n")

    while True:
        if max_guesses:
            remaining = max_guesses - attempts
            print(f"Guesses remaining: {remaining}")

        guess = get_guess(low, high)
        attempts += 1

        if guess == secret:
            print(f"\n🎉 Correct! You got it in {attempts} guess{'es' if attempts != 1 else ''}!")
            return True
        elif max_guesses and attempts >= max_guesses:
            print(f"\n💀 Out of guesses! The number was {secret}.")
            return False
        elif guess < secret:
            print("Too low! Try higher.\n")
            low = guess + 1      # narrow the range hint
        else:
            print("Too high! Try lower.\n")
            high = guess - 1     # narrow the range hint


def main():
    print("=" * 35)
    print("      Number Guessing Game")
    print("=" * 35)

    wins = 0
    rounds = 0

    while True:
        won = play_game()
        rounds += 1
        if won:
            wins += 1

        print(f"\nScore: {wins} win(s) out of {rounds} round(s)")

        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
