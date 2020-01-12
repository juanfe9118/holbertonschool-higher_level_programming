#!/usr/bin/python3
"""Add integer module."""

def add_integer(a, b=98):
    """
    Add integer function.

    @a: integer or float to be added.
    @b: integer or float to be added (default set to 98).
    Returns the result of the sum.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
