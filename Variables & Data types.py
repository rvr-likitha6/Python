# -*- coding: utf-8 -*-
"""
Variables and Data Types

@author: Likitha Rapuri
"""

# --- integers (whole numbers) ---
my_age = 24
num_of_subjects = 5
print("age:", my_age)
print("subjects:", num_of_subjects)

print()

# --- floats (decimal numbers) ---
my_height = 5.4
price = 99.99
print("height:", my_height)
print("price:", price)

print()

# --- strings (text) ---
my_name = "likitha"
my_city = "chennai"
print("name:", my_name)
print("city:", my_city)

# joining strings together
full_intro = "my name is " + my_name + " and i live in " + my_city
print(full_intro)

# f-strings are easier for this (modern way)
print(f"my name is {my_name} and i am {my_age} years old")

print()

# --- booleans (true or false) ---
is_student = True
has_laptop = False
print("is student:", is_student)
print("has laptop:", has_laptop)

print()

# --- lists (a collection of items) ---
fruits = ["apple", "banana", "mango", "grapes"]
print("fruits:", fruits)
print("first fruit:", fruits[0])     # indexing starts at 0
print("last fruit:", fruits[-1])     # -1 gives the last item
print("number of fruits:", len(fruits))

# adding and removing from a list
fruits.append("orange")
print("after adding orange:", fruits)

fruits.remove("banana")
print("after removing banana:", fruits)

print()

# --- dictionaries (key value pairs) ---
student = {
    "name": "likitha",
    "age": 24,
    "course": "python"
}
print("student name:", student["name"])
print("student age:", student["age"])

# adding a new key
student["grade"] = "A"
print("updated student:", student)

print()

# --- checking the type of a variable ---
print(type(my_age))        # int
print(type(my_height))     # float
print(type(my_name))       # str
print(type(is_student))    # bool
print(type(fruits))        # list

print()

# --- converting between types ---
num_as_string = "25"
converted = int(num_as_string)   # string to int
print("converted:", converted + 5)   # now we can do math with it

price_as_int = int(price)   # float to int (cuts off decimals)
print("price as int:", price_as_int)

print()
print("done! those are the main data types in python")
