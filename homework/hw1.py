# Q1.

from operator import add, sub
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        op = -b
    else:
        op = b
    return op(a, b)

# Q2.

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest of a, b, c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    def my_max(a, b):
        if ( a > b ):
            return a
        
        return b

    second = 0
    big = 0

    if ( a > b and a > c ):
        big = a
        second = my_max(b,c) 
 
    elif ( b > c ): 
        big = b  
        second = my_max( a,c ) 

    else:
        big = c
        second = my_max( a,b ) 
        	
    return big * big + second * second

#print(two_of_three(1, 2, 3))
#print(two_of_three(5, 3, 1))
#print(two_of_three(10, 2, 8))
#print(two_of_three(5, 5, 5))

# Q3.

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and false_result otherwise."""
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

# TODO was muss zurueck gegeben werden
def c():
    return True

def t():
    return 1

def f():
    return 0

# Q4.
# print(with_if_statement())
# print(with_if_function())

# Q4.

def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.

    >>> a = hailstone(10)  # Seven elements are 10, 5, 16, 8, 4, 2, 1
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

