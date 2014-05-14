#  Name:
#  Email:

# Q1.

#def g(n):
#    """Return the value of G(n), computed recursively.
#
#    >>> g(1)
#    1
#    >>> g(2)
#    2
#    >>> g(3)
#    3
#    >>> g(4)
#    10
#    >>> g(5)
#    22
#    """
#    "*** YOUR CODE HERE ***"
#
#    if n <= 3:
#        return n
#
#    return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)
#
#
## implementation is wrong :-(
## reason is that the return value does not contain sub results of the recursion.
## general pattern for converting recursion into iteration:
#
## http://www.refactoring.com/catalog/replaceRecursionWithIteration.html
#def g_iter(n):
#    """Return the value of G(n), computed iteratively.
#
#    >>> g_iter(1)
#    1
#    >>> g_iter(2)
#    2
#    >>> g_iter(3)
#    3
#    >>> g_iter(4)
#    10
#    >>> g_iter(5)
#    22
#    """
#    "*** YOUR CODE HERE ***"
#
#    if n <= 3:
#        return n
#
#    def get_start_value( n, steps):
#        while n > 3:
#            n = n - steps
#        return n    
#
#    def single_factor( steps ):
#        start_value = get_start_value( n, steps )
#        factor = start_value
#
#        while start_value < n:
#            factor = steps * factor
#            start_value = start_value + steps
#                      
#        return factor
#                  
#    return single_factor( 1 ) + single_factor( 2 ) + single_factor( 3 )              

## Q2.            
#                 

def get_first_number(k):
#    """return first digit of an integer
#    >>> get_first_number(5)
#    5
#    >>> get_first_number(85)
#    8
#    >>> get_first_number(353535)
#    3
#    """
#
    return int(str(k)[0])
#
def get_rest(k):
#    """returns integer without first digit
#    >>> get_rest(5)
#    >>> get_rest(85)
#    5
#    >>> get_rest(353535)
#    53535
#    """
#
    if k < 10:
        return -1
#
    return int(str(k)[1:])
#
## to access the single numbers a temp. conversion into a string
## is necessary
#def has_seven(k) :
#    """Has a has_seven
#    >>> has_seven(3)
#    False
#    >>> has_seven(7)
#    True
#    >>> has_seven(2734)
#    True
#    >>> has_seven(2634)
#    False
#    >>> has_seven(734)
#    True
#    >>> has_seven(7777)
#    True
#    """          
#    "*** YOUR CODE HERE ***"
#
#    if get_first_number(k) == 7:
#        return True
#
#    if k <= 9:
#        return False
#
#    return has_seven( get_rest(k) )
#
## Q3.
#
##"1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6"
#
#def pingpong(n):
#    """Return the nth element of the ping-pong sequence.
#
#    >>> pingpong(7)
#    7
#    >>> pingpong(8)
#    6
#    >>> pingpong(15)
#    1
#    >>> pingpong(21)
#    -1
#    >>> pingpong(22)
#    0
#    >>> pingpong(30)
#    6
#    >>> pingpong(68)
#    2
#    >>> pingpong(69)
#    1
#    >>> pingpong(70)
#    0
#    >>> pingpong(71)
#    1
#    >>> pingpong(72)
#    0
#    >>> pingpong(100)
#    2
#    """
#    "*** YOUR CODE HERE ***"
#
#    from operator import add, sub
#
#    def _pingpong( current_element, current_val, current_cnt_func, other_cnt_func ):
#
#        # base case
#        if current_element >= n:
#            return current_val
#        
#        # change count direction
#        if current_element % 7 == 0 or has_seven( current_element ):
#            return _pingpong( current_element+1, 
#                              other_cnt_func( current_val, 1 ), 
#                              other_cnt_func, 
#                              current_cnt_func )
#        # keep on counting
#        return _pingpong( current_element+1, 
#                          current_cnt_func( current_val, 1 ), 
#                          current_cnt_func, 
#                          other_cnt_func )
#        
#    return _pingpong( 1, 1, add, sub )     

# Q4.
# 
# This was hard work. I had to split it into two functions since I had to make sure
# that "the rest" is not counted multiple times.
# 
# The algorithm:
# call for each posible fraction of number the function test_ten().
# E.g. 1982 calls test_ten with 1982 and 982 ( 82 is answered by the base case)
#
# test_ten() counts how often the first digit + each other digit is 10
#
# I assume the solution is much simpler :-(
#
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.
    >>> ten_pairs(1)
    0
    >>> ten_pairs(19)
    1
    >>> ten_pairs(199)
    2
    >>> ten_pairs(198)
    1
    >>> ten_pairs(1982)
    2
    >>> ten_pairs(1782)
    1
    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """

    if n <= 99:
        return is_first_plus_second_ten(n)

    else:
        return test_ten(n) + ten_pairs( int(str(n)[1:]))


def is_first_plus_second_ten( n ):
    """Base clause"""
    assert n <= 99

    if n <= 9:
        return 0
    else:
        if int(str(n)[0]) + int(str(n)[1]) == 10:
            return 1
        else:
            return 0

def test_ten( n ):
    """Return number of ten-pairs for the first digit combined with the rest
    >>> test_ten(1)
    0
    >>> test_ten( 12 )
    0
    >>> test_ten( 19 )
    1
    >>> test_ten( 288 )  # 2 + 8 and 2 + 8
    2
    >>> test_ten( 1982 ) # 1 + 9
    1
    >>> test_ten( 1099 ) # 1 + 9 and 1 + 9
    2
    """

    if n <= 99:
        return is_first_plus_second_ten(n)

    else:
        return test_ten( int(str(n)[0] + str(n)[1])) + test_ten( int(str(n)[0] + str(n)[2:]))

# Q5.

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> #count_change(10)
    #14
    >>> #count_change(20)
    #60
    >>> #count_change(100)
    #9828
    """
    "*** YOUR CODE HERE ***"

## Q6.
#
#from operator import sub, mul
#
#def make_anonymous_factorial():
#    """Return the value of an expression that computes factorial.
#
#    >>> make_anonymous_factorial()(5)
#    120
#    """
#    return YOUR_EXPRESSION_HERE


