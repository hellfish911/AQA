"""
This module counts even numbers.

Numbers are random.
"""

numbers = [68, 56, 27, 78, 1, 36, 11, 1, 33, 90, 83]  # 11 random numbers
even_sum = sum(num for num in numbers if num % 2 == 0)

print(even_sum)
