#!/usr/bin/env python

"""
Solves problem 5 of Project Euler

    http://projecteuler.net/index.php?section=problems&id=5

Problem statement:

    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?

Solution approach:

    For each prime factor under 20, determine its highest power that is under
    20.  Multiply.

References:

http://en.wiktionary.org/wiki/evenly_divisible
"""

import itertools
import operator

def primes():
    known_primes = []
    for n in itertools.chain((2,), itertools.count(3, 2)):
        if any(k for k in known_primes if n % k == 0):
            continue
	yield n
	known_primes.append(n)

def powers(n):
    last_power = 1
    while True:
        last_power = last_power * n
        yield last_power

below = 20

print reduce(operator.mul,
    (max(itertools.takewhile(lambda x: x < 20, powers(n)))
        for n
        in itertools.takewhile(lambda x: x < 20, primes())
    )
)
