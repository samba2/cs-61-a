"""Starter file for recursion lab."""

def summation(n, term):
    """Return the sum of the 0th to nth terms in the sequence defined
    by term.

    >>> summation(4, lambda x: x*x) # 0 + 1 + 4 + 9 + 16
    30
    """
    "*** YOUR CODE HERE ***"
    sum = 0

    if n == 0:
        return sum
    
    return summation(n-1, term)

# TODO hier weiter

#def gcd(a, b):
#    """Return the greatest common divisor of a and b.
#
#    >>> gcd(24, 18)
#    6
#    >>> gcd(2, 4)
#    2
#    """
#    "*** YOUR CODE HERE ***"
#
#def hailstone(n):
#    """Print out the hailstone sequence starting at n, and return the
#    number of elements in the sequence.
#
#    >>> a = hailstone(10)
#    10
#    5
#    16
#    8
#    4
#    2
#    1
#    >>> a
#    7
#    """
#    "*** YOUR CODE HERE ***"
#
#def paths(m, n):
#    "*** YOUR CODE HERE ***"
#
