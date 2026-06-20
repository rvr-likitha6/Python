# -*- coding: utf-8 -*-
"""
Basic Operators

@author: Likhitha Rapuri
"""

# --- arithmetic operators ---
print("--- arithmetic ---")

a = 10
b = 3

print("a =", a, "| b =", b)
print()

print("addition       a + b =", a + b)       # 13
print("subtraction    a - b =", a - b)       # 7
print("multiplication a * b =", a * b)       # 30
print("division       a / b =", a / b)       # 3.333... (always gives float)
print("floor division a // b =", a // b)     # 3 (rounds down, no decimals)
print("modulus        a % b =", a % b)       # 1 (remainder after dividing)
print("exponent       a ** b =", a ** b)     # 1000 (10 to the power of 3)

print()

# modulus is useful for checking if a number is even or odd
num = 7
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

print()

# --- comparison operators ---
# these return True or False
print("--- comparison ---")

x = 5
y = 8

print("x =", x, "| y =", y)
print()

print("x == y  (equal to)         :", x == y)
print("x != y  (not equal to)     :", x != y)
print("x > y   (greater than)     :", x > y)
print("x < y   (less than)        :", x < y)
print("x >= y  (greater or equal) :", x >= y)
print("x <= y  (less or equal)    :", x <= y)

print()

# --- logical operators ---
# used to combine multiple conditions
print("--- logical ---")

is_raining = True
has_umbrella = False

print("is raining:", is_raining)
print("has umbrella:", has_umbrella)
print()

# and = both conditions must be true
print("is raining AND has umbrella:", is_raining and has_umbrella)

# or = at least one condition must be true
print("is raining OR has umbrella:", is_raining or has_umbrella)

# not = flips the value
print("NOT is raining:", not is_raining)

print()

# --- assignment operators ---
# shortcuts for updating a variable
print("--- assignment shortcuts ---")

score = 10
print("score starts at:", score)

score += 5     # same as score = score + 5
print("after += 5 :", score)

score -= 3     # same as score = score - 3
print("after -= 3 :", score)

score *= 2     # same as score = score * 2
print("after *= 2 :", score)

score //= 3    # same as score = score // 3
print("after //= 3 :", score)

print()
print("done! those are the main operators in python")