#!/usr/bin/env python
"""
Solves problem 10 of Project Euler

    http://projecteuler.net/index.php?section=problems&id=10

Problem statement:

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
"""

import itertools

def primes_under(number):
    potential_primes = [True] * (number + 1)
    potential_primes[0:2] = [False, False]
    for i in xrange(2, int(number ** 0.5) + 1):
        if potential_primes[i]:
            potential_primes[2*i::i] = [False] * (int(number / i) - 1)

    return (i for i,v in enumerate(potential_primes) if v)

number = 2000000
print sum(primes_under(number))
