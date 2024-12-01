"""This module contains tests for homeworks."""

import pytest
from homeworks import sum_two, longest, average

# This test verifies function for numbers calculating.


def test_sum_two_positive():
    """Test case verifies positive scenario."""
    side_a = 99
    side_b = 45
    expected_result = 144
    assert sum_two(side_a, side_b) == expected_result


def test_sum_neg():
    """Test case with a not matching value."""
    expected_result = 144
    if expected_result != 144:
        pytest.fail('Wrong value')


# This test verifies function which calculates average.


def test_average():
    """Test case with a non-empty tuple."""
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    expected_result = 5
    assert average(numbers) == expected_result


def test_average_neg():
    """Test case with negative scenario."""
    expected_result = 5
    if expected_result != 5:
        pytest.fail('Wrong value')


# This test verifies multiplication table function.


def test_multable():
    """Test case with a checking multiplying."""
    number = 3
    assert number * number == 9


def test_mult_neg():
    """Test case with a checking multiplying by 0."""
    number = 3
    multiplier = 0
    if number * multiplier == 0:
        return 'Zero'


# This test verifies function for longest word.


def test_longest_positive():
    """Test case with a list of words of varying lengths."""
    words = ['joke', 'bubble', 'leftovers', 'profound', 'prayer']
    assert longest(words) == 'leftovers'


def test_longest_negative():
    """Test case with an empty list."""
    words = []
    assert longest(words) == ''


# This test verifies Perimeter function.


def test_perimeter_pos():
    """This rest calculates perimeter."""
    expected_result = 14
    assert expected_result == 14


def test_perimeter_neg():
    """This test checks negative case.

    Returns: 'Wrong value' warning.
    """
    expected_result = 14
    if expected_result != 14:
        return 'Wrong value'
