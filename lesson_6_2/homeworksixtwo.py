"""
This module processes counts unique characters.

It performs counting and displaying results as true or false.
"""

while True:
    word = input('Type word with "h" letter: ')
    if 'h' in word.lower():
        print('Thanks!')
        break
    else:
        print('Word does not have "h" letter')
