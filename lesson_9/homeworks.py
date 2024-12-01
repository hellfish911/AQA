"""This module intended to be a test data for tests in test_homework09."""

# Task 1. Function returns longest word.


def longest(words):
    """
    Find and return the longest word in a list of words.

    This function takes a list of words and returns the longest.
    If the list is empty, an empty string is returned.

    Args:
        words (list of str): A list of words to evaluate.

    Returns:
        str: The longest word in the list, or an empty string.
    """
    return max(words, key=len) if words else ''


list_words = ['joke', 'bubble', 'leftovers', 'profound', 'prayer']
print(longest(list_words))


# Task 2. This function should print multiplier table.


def multiplication_table(number):
    """
    Print a multiplication table for a given number up to a result limit of 25.

    This function multiplies the given number by consecutive integers starting
    from 1, printing each result in the format "number x multiplier = result".
    The function stops printing once the result exceeds 25.

    Args:
        number (int): The base number for the multiplication table.
    """
    multiplier = 1

    while True:
        result = number * multiplier
        if result > 25:
            break
        print(f'{number}x{multiplier}={result}')

        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# Task 3. This function should sum two numbers.

side_a = 99
side_b = 45


def sum_two(dim_a, dim_b):
    """
    Calculate the sum of two dimensions.

    Args:
        dim_a (float or int): The first dimension.
        dim_b (float or int): The second dimension.

    Returns:
        float or int: The sum of the two dimensions.
    """
    return (dim_a + dim_b)


sum_two(side_a, side_b)


# Task 4. This function calculate average from numbers.


def average(numbers):
    """
    Calculate the average of a list or tuple of numbers.

    Args:
        numbers (list or tuple): A collection of numeric values.

    Returns: float: The average of the numbers in the list or tuple.

    If the input is empty, returns None and prints 'List is empty'.
    """
    return (sum(numbers) / len(numbers)) if numbers else print('List is empty')


t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)


print('Average is ', average(t1))

# Task 5. This function calculates perimeter.


def perimeter(side_one, side_two, side_three, side_four):
    """
    Calculate the perimeter of a quadrilateral.

    Args:
        side_one (float or int): The length of the first side.
        side_two (float or int): The length of the second side.
        side_three (float or int): The length of the third side.
        side_four (float or int): The length of the fourth side.

    Returns:
        float or int: The perimeter of the quadrilaterals.
    """
    return side_one + side_two + side_three + side_four


print(perimeter(2, 3, 4, 5))
