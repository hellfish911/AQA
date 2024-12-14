"""This module contains iterators, generators, and decorators."""

import logging

logging.basicConfig(level=logging.INFO)

"""
Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
"""


def even_numbers(n_arg):
    """
    Yield even numbers from 0 up to the specified limit.

    Args:
        n_arg (int): The maximum number to generate.

    Yields:
        int: The next even number in the sequence.
    """
    num = 0
    while num <= n_arg:
        yield num
        num += 2


def fibonaci(nf_number):
    """
    Yield Fibonacci numbers up to the specified limit.

    Args:
        nf_number (int): The maximum Fibonacci number to generate.

    Yields:
        int: The next Fibonacci number in the sequence.
    """
    a_number, b_number = 0, 1
    while a_number <= nf_number:
        yield a_number
        a_number, b_number = b_number, a_number + b_number


"""
Реалізуйте ітератор для зворотного виведення елементів списку.
Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
"""


class Countdown:
    """
    Iterator that counts down from a specified starting value to zero.

    Attributes:
        start (int): The starting value of the countdown.
        current (int): The current value in the countdown sequence.
    """

    def __init__(self, start):
        """
        Initialize the Countdown iterator.

        Args:
            start (int): The starting value of the countdown.
        """
        self.start = start
        self.current = start

    def __iter__(self):
        """
        Return the iterator object.

        Returns:
            Countdown: The iterator itself.
        """
        return self

    def __next__(self):
        """
        Return the next value in the countdown sequence.

        Raises:
            StopIteration: When the countdown reaches zero.

        Returns:
            int: The next value in the countdown.
        """
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


"""
Напишіть декоратор, який логує аргументи та результати викликаної функції.
Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
"""


def log_args_and_res(func):
    """
    Log function arguments and results.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """

    def wrapper(*args, **kwargs):
        logging.info(f'Function {func.__name__} called with {args}, {kwargs}')
        try:
            func_result = func(*args, **kwargs)
            logging.info(f'Execution func_result: {func_result}')
            return func_result
        except Exception as exception:
            logging.error(f'Error in {func.__name__}: {exception}')
            raise

    return wrapper


def handle_exceptions(func):
    """
    Handle exceptions during function execution.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function with exception handling.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exception:
            logging.error(f'Exception in {func.__name__}: {exception}')
            return f'An error occurred: {exception}'

    return wrapper


if __name__ == '__main__':
    n_number = 10

    for itm in even_numbers(n_number):
        print(itm)

    for numb in fibonaci(100):
        print(numb)

    countdown = Countdown(5)
    for number in countdown:
        print(number)
