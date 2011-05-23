#!/usr/bin/env python
"""
Solves problem 6 of Project Euler

    http://projecteuler.net/index.php?section=problems&id=6

Problem statement:

    The sum of the squares of the first ten natural numbers is,
    1**2 + 2**2 + ... + 10**2 = 385

    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)**2 = 552 = 3025

    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.
"""

up_to = 100

sum_of_squares = sum(x ** 2 for x in xrange(up_to + 1))
square_of_sum = sum(x for x in xrange(up_to + 1)) ** 2

print abs(sum_of_squares - square_of_sum)
