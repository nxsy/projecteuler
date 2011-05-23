#!/usr/bin/env python
"""
Solves problem 7 of Project Euler

    http://projecteuler.net/index.php?section=problems&id=7

Problem statement:

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10001st prime number?
"""

import itertools

def primes():
    known_primes = []
    for n in itertools.chain((2,), itertools.count(3, 2)):
        if any(k for k in known_primes if n % k == 0):
            continue
        yield n
        known_primes.append(n)

for i, prime in enumerate(primes()):
    if i + 1 == 10001:
        print prime
        break
