#!/usr/bin/env python
"""
Solves problem 12 of Project Euler

    http://projecteuler.net/index.php?section=problems&id=12

    Problem statement:

    The sequence of triangle numbers is generated by adding the natural
    numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 =
    28.  The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

         1: 1
         3: 1,3
         6: 1,2,3,6
        10: 1,2,5,10
        15: 1,3,5,15
        21: 1,3,7,21
        28: 1,2,4,7,14,28

    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred divisors?
"""

import collections
import itertools
import operator

def primes_under(number):
    potential_primes = [True] * (number + 1)
    potential_primes[0:2] = [False, False]
    for i in xrange(2, int(number ** 0.5) + 1):
        if potential_primes[i]:
            potential_primes[2*i::i] = [False] * (int(number / i) - 1)

    return (i for i,v in enumerate(potential_primes) if v)

_primes = list(primes_under(15000))

def memoize(func):
    cache = {}
    def deco(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return deco

@memoize
def prime_factors(number):
    if number < 2:
        return []

    if number in _primes:
        return [number]

    for prime in _primes:
        divisor, modulo = divmod(number, prime)
        if not modulo:
            return [prime] + prime_factors(divisor)

    return []

def num_divisors(n):
    if n < 3:
        return n
    if n in _primes:
        return 2
    prime_power = collections.defaultdict(int)
    for f in prime_factors(n):
        prime_power[f] += 1

    return reduce(operator.mul, ((power+1) for power in prime_power.values()))

def triangle(n):
    return n * (n + 1) / 2

last_num_divisors = 0
for i in range(1, 100000):
    curr_num_divisors = num_divisors(i)
    if last_num_divisors * curr_num_divisors > 500:
        if num_divisors(triangle(i-1)) > 500:
            print triangle(i-1)
            break
    last_num_divisors = curr_num_divisors
