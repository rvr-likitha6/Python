# -*- coding: utf-8 -*-
"""
Python setup and syntax

@author: Likitha Rapuri
"""


# this is a single line comment
# python ignores anything after a #

# printing stuff to the screen
print("hello world")
print("python is pretty easy to read")

# you can print numbers too
print(100)
print(3.14)

# printing multiple things at once
print("my name is", "likitha")
print("the answer is", 42)

# blank line in output
print()

# using sep to change the separator between items
print("apple", "banana", "cherry", sep=" | ")

# using end to stop the automatic newline
print("this is on ", end="")
print("the same line")

print()

# indentation matters in Python
# if you don't indent properly, you get an error
# example (just showing the idea, not running it as a loop here)
print("indentation example:")
if True:
    print("  this is indented")
    print("  this is also indented")
print("this is back to normal")

print()

# long strings can be split using a backslash
long_sentence = "this is a really long string that " \
                "continues on the next line"
print(long_sentence)

# or use triple quotes for multi-line strings
multi_line = """this is line one
this is line two
this is line three"""
print(multi_line)

print()

# python is case sensitive
my_name = "likitha"
My_Name = "someone else"
print(my_name)   # prints likitha
print(My_Name)   # prints someone else, different variable

print()
print("done! that's the basics of Python syntax")