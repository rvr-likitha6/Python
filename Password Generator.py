# -*- coding: utf-8 -*-
"""
PASSWORD GENERATOR - makes random passwords based on what you want

@author: Likitha Rapuri
"""

import random
import string


def get_options():
    print("\nset up your password:")

    # get the length
    while True:
        try:
            length = int(input("how long? (min 4): "))
            if length >= 4:
                break
            print("needs to be at least 4")
        except ValueError:
            print("enter a number")

    # ask what to include
    use_upper = input("include uppercase letters? (yes/no): ").strip().lower() in ("yes", "y")
    use_lower = input("include lowercase letters? (yes/no): ").strip().lower() in ("yes", "y")
    use_digits = input("include numbers? (yes/no): ").strip().lower() in ("yes", "y")
    use_symbols = input("include symbols? (yes/no): ").strip().lower() in ("yes", "y")

    # if nothing selected just use lowercase by default
    if not use_upper and not use_lower and not use_digits and not use_symbols:
        print("nothing selected, using lowercase by default")
        use_lower = True

    return length, use_upper, use_lower, use_digits, use_symbols


def build_pool(use_upper, use_lower, use_digits, use_symbols):
    # build the character pool based on options
    pool = ""
    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation
    return pool


def make_password(length, pool, use_upper, use_lower, use_digits, use_symbols):
    # make sure at least one of each selected type is in the password
    guaranteed = []
    if use_upper:
        guaranteed.append(random.choice(string.ascii_uppercase))
    if use_lower:
        guaranteed.append(random.choice(string.ascii_lowercase))
    if use_digits:
        guaranteed.append(random.choice(string.digits))
    if use_symbols:
        guaranteed.append(random.choice(string.punctuation))

    # fill the rest from the pool
    rest = [random.choice(pool) for _ in range(length - len(guaranteed))]

    all_chars = guaranteed + rest
    random.shuffle(all_chars)
    return "".join(all_chars)


def check_strength(length, use_upper, use_lower, use_digits, use_symbols):
    # simple strength check based on length and variety
    types = sum([use_upper, use_lower, use_digits, use_symbols])
    if length >= 16 and types == 4:
        return "strong"
    elif length >= 10 and types >= 3:
        return "medium"
    else:
        return "weak"


def main():
    print("=== Password Generator ===")

    while True:
        length, use_upper, use_lower, use_digits, use_symbols = get_options()
        pool = build_pool(use_upper, use_lower, use_digits, use_symbols)

        print("\nhere are 5 passwords:")
        for i in range(5):
            pwd = make_password(length, pool, use_upper, use_lower, use_digits, use_symbols)
            print(f"  {i + 1}. {pwd}")

        strength = check_strength(length, use_upper, use_lower, use_digits, use_symbols)
        print(f"\nstrength: {strength}")

        again = input("\ngenerate more? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("done!")
            break


main()
