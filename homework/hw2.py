#  Name: Maik Toepfer
#  Email:

def square(x):
    """Return x squared."""
    return x * x

# Q1.

def product(n, term):
    """Return the product of the first n terms in a sequence.

    term -- a function that takes one argument

    >>> product(4, square)
    576
    """
    "*** YOUR CODE HERE ***"
    
    i = 1
    product = 1

    while i <= n:
        product = term(i) * product
        i += 1

    return product

def factorial(n):
    """Return n factorial for n >= 0 by calling product.

    >>> factorial(4)
    24
    """
    "*** YOUR CODE HERE ***"

    assert n >= 0

    def is_x(x):
        return x

    return product(n, is_x)

# Q2.

from operator import add, mul

def accumulate(combiner, start, n, term):
#    """Return the result of combining the first n terms in a sequence."""
#    "*** YOUR CODE HERE ***"
#   
    """
    >>> accumulate(add, 1, 3, lambda x: x)
    6
    >>> accumulate(add, 1, 3, lambda x: x * 2)
    12
    >>> accumulate(mul, 1, 3, lambda x: x * 2)
    48
    """

    assert start < n
    
    i = start

    # initzialize result with first value
    result = term(i)
    i += 1

    # accumulate the following results
    while i <= n:
        result = combiner( term(i), result )
        i += 1

    return result

def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate.

    >>> summation_using_accumulate(4, square)
    30
    """
    "*** YOUR CODE HERE ***"

    return accumulate( add, 1, n, term )

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    """
    "*** YOUR CODE HERE ***"

    return accumulate( mul, 1, n, term )

# Q3.

def double(f):
    """Return a function that applies f twice.

    f -- a function that takes one argument

    >>> double(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"
    return lambda x: f(f(x))


# Q4.

def repeated(f, n):
    """Return the function that computes the nth application of f.

    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)
    625
    >>> repeated(square, 4)(5)
    152587890625
    """
    "*** YOUR CODE HERE ***"

    r = f
    n -= 1

    while n > 0:
        r = compose1(r,f)
        n -= 1

    return r

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

## Q5.

# too crazy stuff
def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))


def one(f):
    """Church numeral 1."""
    "*** YOUR CODE HERE ***"
    return successor(zero)


def two(f):
    """Church numeral 2."""
    "*** YOUR CODE HERE ***"
    return successor(one)
#
#def church_to_int(n):
#    """Convert the Church numeral n to a Python integer.
#
#    >>> church_to_int(zero)
#    0
#    >>> church_to_int(one)
#    1
#    >>> church_to_int(two)
#    2
#    """
#    "*** YOUR CODE HERE ***"
#
#def add_church(m, n):
#    """Return the Church numeral for m + n, for Church numerals m and n.
#
#    >>> three = successor(two)
#    >>> church_to_int(add_church(two, three))
#    5
#    """
#    "*** YOUR CODE HERE ***"
#
#def mul_church(m, n):
#    """Return the Church numeral for m * n, for Church numerals m and n.
#
#    >>> three = successor(two)
#    >>> four = successor(three)
#    >>> church_to_int(mul_church(two, three))
#    6
#    >>> church_to_int(mul_church(three, four))
#    12
#    """
#    "*** YOUR CODE HERE ***"

