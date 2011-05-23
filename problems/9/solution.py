#!/usr/bin/env python
"""
Solves problem 9 of Project Euler

    http://projecteuler.net/index.php?section=problems&id=9

Problem statement:

    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a**2 + b**2 = c**2

    For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
"""

import sys

target_sum = 1000

max_val = (target_sum / 3) + 1

for a in xrange(1, max_val):
    for b in xrange(a + 1, target_sum - a):
        c = target_sum - a - b
        if (a ** 2) + (b ** 2) == (c ** 2):
            print a * b * c
            sys.exit()
