#!/usr/bin/env python

"""
Solves problem 3 of Project Euler

    http://projecteuler.net/index.php?section=problems&id=3

Problem statement:

    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
"""

def factors(number):
    halfway = int(number ** 0.5) + 1
    for potential in xrange(2, halfway):
        potential2, mod = divmod(number, potential)
        if mod == 0:
            yield potential
            yield potential2

number = 600851475143

print max(
    factor
        for factor
        in factors(number)
        if any(factors(factor)) == 0
    )
