"""
This module processes counts unique characters.

It performs counting and displaying results as true or false.
"""
string = input('TYPE HERE: ')
unique_chars = set(string)  # unique characters
print(len(unique_chars) > 10)
