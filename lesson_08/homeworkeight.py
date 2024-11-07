"""This module intended to handle exceptions."""


def sum_numb(bundle_data):
    """
    Calculate the sum of numbers in a comma-separated string.

    This function takes a string `bundle_data` with numbers,
    splits it into individual numbers, and calculates their sum. If the string
    contains non-numeric characters, it returns the message "Cannot do this!".

    Parameters:
        bundle_data (str): A string containing numbers separated by commas.

    Returns:
        int or str: The sum of the numbers in the string, or an error message
                    if the string contains invalid characters.
    """
    try:
        numbers = map(int, bundle_data.split(','))
        return sum(numbers)
    except ValueError:
        return 'Cannot do this!'


bundle = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']

final_sum = [sum_numb(element) for element in bundle]
print(final_sum)
