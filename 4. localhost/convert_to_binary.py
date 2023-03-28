#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def convert_to_binary(num: int) -> str:
    """
    Purpose:        Converts a decimal number to a binary representation
    Parameters:     A decimal number, as an integer
    User Input:     No
    Prints:         Nothing
    Returns:        Result as a string of 1s and 0s
    Modifies:       Nothing
    Calls:          Basic python only
    Tests:          ./unit_tests/*
    Status:         Done!

    Usage illustrated via some simple doctests:
    >>> convert_to_binary(1)
    '1'

    >>> convert_to_binary(10)
    '1010'

    >>> import random
    >>> for _ in range(5):
    ...     num = random.randint(0, 200)
    ...     assert convert_to_binary(num) == bin(num)[2:]

    >>> for _ in range(2):
    ...     num = random.randint(0, 200)
    ...     convert_to_binary(num) == bin(num)[2:]
    True
    True

    >>> print("Unlike other frameworks, doctest does stdout easily")
    Unlike other frameworks, doctest does stdout easily
    """
    # To debug doctest test in pudb
    # Highlight the line of code below below
    # Type 't' to jump 'to' it
    # Type 's' to 'step' deeper
    # Type 'n' to 'next' over
    # Type 'f' or 'r' to finish/return a function call and go back to caller
    # YOUR CODE GOES HERE

    if num == 0:
        return "0"
    ans: str = ""
    while num > 0:
        if num % 2 == 0:
            ans += "0"
        else:
            ans += "1"
        num //= 2
    return ans[::-1]


if __name__ == "__main__":
    # Execute doctests to protect main:

    import doctest

    doctest.testmod()

    # Run main
    if len(sys.argv) == 3:
        finput = open(sys.argv[1], "r")
        foutput = open(sys.argv[2], "w")
        num = int(finput.read())
        ans: str = convert_to_binary(num) + "\n"
        foutput.write(ans)
        finput.close()
        foutput.close()
    else:
        num = int(input())
        print(convert_to_binary(num))
    # YOUR CODE GOES HERE
