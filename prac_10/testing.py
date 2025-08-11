"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    if n <= 0:
        return ""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should now pass
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # assert statements to show if Car sets the fuel correctly (default and custom)
    car = Car()
    assert car.fuel == 0, "Car does not set default fuel correctly"

    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set custom fuel correctly"


run_tests()

# Run the doctests
doctest.testmod()


def format_sentence(phrase):
    """
    Format a phrase as a sentence: start with a capital and end with a single full stop.

    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("multiple   spaces here")
    'Multiple   spaces here.'
    """
    text = phrase.strip()
    if text == "":
        return "."
    first = text[0].upper()
    rest = text[1:]
    while len(rest) > 0 and rest[-1] in ".!?":
        rest = rest[:-1]
    return f"{first}{rest}."
