"""
This module performs actions on the list.

new list will contain data from first list.
"""

lst1 = [
    '1', '2', 3, True, 'False',
    5, '6', 7, 8, 'Python',
    9, 0, 'Lorem Ipsum',
]
lst2 = [unitto for unitto in lst1 if isinstance(unitto, str)]

print(lst2)
