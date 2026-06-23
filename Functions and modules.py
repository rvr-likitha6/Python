# -*- coding: utf-8 -*-
"""
Functions and Modules

@author: Likitha Rapuri
"""

# --- basic function ---
# The def keyword is used to create a function
def say_hello():
    print("hello there!")

# calling the function
say_hello()
say_hello()   # can call it as many times as you want

print()

# --- function with parameters ---
# parameters are inputs you pass into the function
def greet(name):
    print(f"hello {name}, welcome!")

greet("Likitha")
greet("Suma")

print()

# --- function with multiple parameters ---
def add_numbers(num1, num2):
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

add_numbers(5, 3)
add_numbers(100, 250)

print()

# --- function with a return value ---
# return sends a value back so you can use it
def multiply(num1, num2):
    return num1 * num2

answer = multiply(6, 7)
print("6 x 7 =", answer)

# can also use it directly
print("3 x 9 =", multiply(3, 9))

print()

# --- default parameter values ---
# if you don't pass a value, it uses the default
def power(base, exponent=2):
    return base ** exponent

print("3 squared:", power(3))       # uses default exponent of 2
print("3 cubed:", power(3, 3))      # overrides the default

print()

# --- function that returns multiple values ---
def get_min_max(numbers):
    return min(numbers), max(numbers)

my_list = [4, 1, 9, 2, 7]
smallest, biggest = get_min_max(my_list)
print("list:", my_list)
print("smallest:", smallest)
print("biggest:", biggest)

print()

# --- calling functions inside functions ---
def square(n):
    return n * n

def sum_of_squares(a, b):
    # reusing the square function here
    return square(a) + square(b)

print("sum of squares of 3 and 4:", sum_of_squares(3, 4))

print()

# --- importing modules ---
# modules are files with pre-built functions you can use

import math

print("--- using the math module ---")
print("square root of 16:", math.sqrt(16))
print("pi:", math.pi)
print("ceiling of 4.2:", math.ceil(4.2))    # rounds up
print("floor of 4.9:", math.floor(4.9))     # rounds down

print()

import random

print("--- using the random module ---")
print("random number 1-10:", random.randint(1, 10))
print("random number 1-10:", random.randint(1, 10))   # diffrent each time

fruits = ["apple", "banana", "mango", "grapes"]
print("random fruit:", random.choice(fruits))

print()

# --- importing specific things from a module ---
from math import sqrt, pi

print("using sqrt without math.:", sqrt(25))
print("pi is:", pi)

print()
print("done! thats functions and modules in python")
