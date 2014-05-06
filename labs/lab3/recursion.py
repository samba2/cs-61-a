"""Starter file for recursion lab."""

def summation(n, term):
    """Return the sum of the 0th to nth terms in the sequence defined
    by term.

    >>> summation(4, lambda x: x*x) # 0 + 1 + 4 + 9 + 16
    30
    """
    "*** YOUR CODE HERE ***"
    # base case
    if n == 0:
        return term(n)
   
    return term(n) + summation(n-1, term) 

def gcd(a, b):
    """Return the greatest common divisor of a and b.

    >>> gcd(24, 18)
    6
    >>> gcd(2, 4)
    2
    """
    "*** YOUR CODE HERE ***"
    assert a > 0
    assert b > 0

    # true only once at the beginning
    # distance between a and b stays throught the algorithm
    if a < b:
        a, b = b, a

    if a % b == 0:
        return b

    else:
        return gcd(b, a %b )

# ugly cnt implementation
cnt = 0
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"

    print(n)

    global cnt   
    cnt+=1

    if n == 1:
        return cnt
    else:
        # even
        if n % 2 == 0:  
            return hailstone( n // 2 )
        else:
            return hailstone( n * 3 + 1 )

# nicer implementation of the counter
def hailstone2(n, cnt=1):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone2(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"

    print(n)

    if n == 1:
        return cnt
    else:
        # even
        if n % 2 == 0:  
            return hailstone2( n // 2, cnt+1 )
        else:
            return hailstone2( n * 3 + 1, cnt+1 )

def paths(m, n ):
    """Return count of paths of an insect in a grid where only moving right and down is allowed
    >>> paths(1, 2)
    1
    >>> paths(2, 1)
    1
    >>> paths(2, 2)
    2
    >>> paths(3, 3)
    6
    """
    "*** YOUR CODE HERE ***"

    if m == 1 and n == 1:
        return 1
    # we're at the right edge
    elif m == 1:
        return paths(m, n-1)
    # we're at the lower edge
    elif n == 1:
        return paths(m-1, n )
    # two directions possible, right ( m-1) and down ( n-1 )
    else:
        return paths(m-1, n ) + paths(m, n-1 )

# discussion of proposed solution:
#
# def paths(m, n):
#     if m == 1 or n == 1:
#         return 1
#     return paths(m - 1, n) + paths(m, n - 1)
#
# this is smarter. the idea is that as soon as we hit an edge ( right
# or bottom) the direction will not change anymore. we're just counting
# down the other value. hence, we can return "1" earlier, even though
# the final corner ( 1/1) wasn't reached.
