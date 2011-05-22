#!/usr/bin/env python

"""
Solves problem 1 of Project Euler

    http://projecteuler.net/index.php?section=problems&id=1

Problem statement:

    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
"""

divisors = (3, 5)
below = 1000
start = 1

print sum(
    multiple
        for multiple
        in xrange(start, below)
        if any(divisor for divisor in divisors if multiple % divisor == 0)
    )
