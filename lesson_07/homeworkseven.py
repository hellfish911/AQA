"""Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.

Код майже готовий, треба знайти помилки та виправити доповнити.
"""


def multiplication_table(number):
    """Initialize the appropriate variable."""
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


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

storona_a = 99
storona_b = 45


def sum_two(storona_a, storona_b):
    """Calculate sum of sides."""
    print(storona_a + storona_b)


sum_two(storona_a, storona_b)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def average(numbers):
    return (sum(numbers) / len(numbers)) if numbers else print('List is empty')


t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)


print('Average is ', average(t1))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def st_reverse(string):
    return string[::-1]


print(st_reverse('abcde qwerty'))

# task 5
"""Написати функцію, яка приймає список слів т
а повертає найдовше слово у списку."""


def longest(words):
    """Find longest word and print it."""
    return max(words, key=len) if words else ''


list_words = ['joke', 'bubble', 'leftovers', 'profound', 'prayer']
print(longest(list_words))

# task 6
"""Написати функцію, яка приймає два рядки та
повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого
 рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    return str1.find(str2)


str1 = 'Hello, world!'
str2 = 'world'
print(find_substring(str1, str2))  # поверне 7

str1 = 'The quick brown fox jumps over the lazy dog'
str2 = 'cat'
print(find_substring(str1, str2))  # поверне -1

"""Оберіть будь-які 4 таски з попередніх домашніх робіт та\n
перетворіть їх у 4 функції, що отримують значення та повертають результат.\n
Обоязково документуйте функції та дайте зрозумілі імена змінним.\n"""

# task 7
# Порахуйте периметр фігури з task 05
# та виведіть його для користувача


def perimeter(storona_one, storona_two, storona_three, storona_four):
    """Find perimeter by given args."""
    return storona_one + storona_two + storona_three + storona_four


print(perimeter(2, 3, 4, 5))

# task 8
"""Count unique chars. If > 10 - print into console True, otherwise - False."""

string = input('TYPE HERE: ')


def unique_chars(string):
    """
    Check if a string contains more than 10 unique characters.

    This function takes a string as input, creates a set of its unique
    characters, and returns True if there are more
    than 10 unique characters,
    otherwise returns False.

    Parameters:
    string (str): The input string to be analyzed.

    Returns:
    bool: True if the string has more than
    10 unique characters, False otherwise.
    """
    unique_chars = set(string)  # unique characters
    return len(unique_chars) > 10


print(unique_chars(string))

# task 9
"""
This module processes counts unique characters.

It performs counting and displaying results as true or false.
"""


def seek():
    """Wait for input. If input has 'h' proceed, if not try again."""
    while True:
        word = input('Type word with "h" letter: ')
        if 'h' in word.lower():
            print('Thanks!')
            break
        else:
            print('Word does not have "h" letter')


seek()

# task 10
"""
This module counts even numbers.

Numbers are random.
"""


def even():
    """Calculate and print the sum of even numbers in a predefined list."""
    numbers = [68, 56, 27, 78, 1, 36, 11, 1, 33, 90, 83]  # 11 random numbers
    even_sum = sum(num for num in numbers if num % 2 == 0)
    print(even_sum)


even()
