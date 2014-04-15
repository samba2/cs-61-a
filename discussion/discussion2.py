from math import sqrt

def find_quartile(x):
    """
    >>> find_quartile(1)
    Q4
    >>> find_quartile(25)
    Q3
    >>> find_quartile(75)
    Q2
    >>> find_quartile(76)
    Q1
    """

    assert x >= 0
    assert x <= 100

    if x > 75:
        print("Q1")
    if x >= 50 and x <= 75:
        print("Q2")
    if x >= 25 and x < 50:
        print("Q3")
    if x < 25:
        print("Q4")

def find_quartile2(x):
    """
    >>> find_quartile2(1)
    Q4
    >>> find_quartile2(25)
    Q3
    >>> find_quartile2(75)
    Q2
    >>> find_quartile2(76)
    Q1
    """

    assert x >= 0
    assert x <= 100

    if x > 75:
        print("Q1")
    elif x >= 50 and x <= 75:
        print("Q2")
    elif x >= 25 and x < 50:
        print("Q3")
    else:    
        print("Q4")

def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(59)
    True
    >>> is_prime(60)
    False
    """

    assert n > 1

    cnt_down = n - 1

    while cnt_down > 1:
        if n % cnt_down == 0:
            return False

        cnt_down = cnt_down - 1

    return True


# higher order functions

# without:
def square_every_number(n):
    assert n > 0

    cnt = 1

    while cnt <= n:
        print( sqrt(cnt) )
        cnt = cnt + 1


def double_every_number(n):
    """
    >>> double_every_number(3)
    2
    4
    6
    """
    assert n > 0

    cnt = 1

    while cnt <= n:
        print( cnt * 2 )
        cnt = cnt + 1

# with HOF:

def every(func, n):
    
    assert n > 0

    cnt = 1

    while cnt <= n:
        print( func(cnt) )
        cnt = cnt + 1

# as learned in lecture this is the prefered style:
# the function to be handed in is first defined with a name
def double_every_number2(n):
    """
    >>> double_every_number2(3)
    2
    4
    6
    """

    def double(x):
        return x * 2

    every( double, n)

# ommitting nested function definition by passing in a
# lambda expression ( anonymous function )
def double_every_number3(n):
    """
    >>> double_every_number3(3)
    2
    4
    6
    """
    every( lambda x: x * 2, n)

def square_every_number2(n):
    every( sqrt, n )


def keep(cond, n):
    """
    >>> keep( lambda x: x > 1, 2)
    1
    2
    >>> keep( lambda x: x < 1, 2)
    """
    if cond(n):
        every( lambda x: x * 1, n )

