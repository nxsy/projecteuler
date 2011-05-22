#!/usr/bin/env python

"""
Solves problem 4 of Project Euler

    http://projecteuler.net/index.php?section=problems&id=4

Problem statement:

    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 x 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

Solution approach:

    Randomly assert that the order in which to look for the largest palindrome
    of the product of any two numbers that have a maximum of x is to start
    with numbers with the highest sum towards the lowest sum.  Stop looking
    once we have found any sum of two numbers that has any palindromes, and
    pick the highest palindrome.
"""

def is_palindrome(number):
    """
    There must be an easier way to write this...
    """
    number_string = str(number)
    midpoint = int(len(number_string))
    for i in xrange(midpoint):
        if number_string[i] != number_string[len(number_string) - i - 1]:
            return False
    return True

def numbers_to_test(sum_, largest, smallest):
    """
    Find all pairs of numbers, where each member of the pair is between
    largest and smallest, that add up to a particular number.
    """
    start = sum_ - largest
    if start < smallest:
        return
    
    yield largest * start
    for a in xrange(largest, start, -1):
        yield a * (sum_ - a)

largest = 999
smallest = 100

sum_ = largest + largest

for sum_ in xrange(largest+largest, 0, -1):
    palindromes = list(
        number
            for number
            in numbers_to_test(sum_, largest, smallest)
            if is_palindrome(number)
        )
    if palindromes:
        print max(palindromes)
        break
