
def countdown(n):
    """Print out a countdown using recursion.

    >>> countdown(3)
    3
    2
    1
    """
    print(n)

    if n == 1:
        return
    else:
        countdown(n-1)


# i can't think of an easier way since we're counting up.
# somehow i need to preserve the original count target to compare it
# in my base clause
def countup(n, cnt=1):
    """counting up instead

    >>> countup(3)
    1
    2
    3
    """
   
    print(cnt) 

    if n == cnt:
        return
    else:
        countup(n, cnt+1 )


def expt(base, power):
    """implements the exponent function

    >>> expt(3,2)
    9
    >>> expt(2,3)
    8
    """

    if power == 1:
        return base
    else:
        return base * expt(base, power-1)


def is_prime(n):
    """
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(17)
    True
    >>> is_prime(16)
    False
    """

    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_primes_up_to(n):
    """
    >>> sum_primes_up_to(3)
    5
    >>> sum_primes_up_to(5)
    10
    >>> sum_primes_up_to(10)
    17
    """

    # base crit.
    if n == 2:
        return 2

    # recursive breakdown
    elif is_prime(n):
        return n + sum_primes_up_to(n-1)
    else:
        return sum_primes_up_to(n-1)

def sum_filter_up_to(n, pred):
    """
    >>> sum_filter_up_to(3, is_prime)
    5
    >>> sum_filter_up_to(5, is_prime)
    10
    >>> sum_filter_up_to(10, is_prime)
    17
    """

    # base crit.
    if n == 0:
        return 0

    # recursive breakdown
    elif pred(n):
        return n + sum_filter_up_to(n-1, pred)
    else:
        return sum_filter_up_to(n-1, pred)

def count_stair_ways(n):
    """
    I want to go up a flight of stairs that has n steps. I can either take 1 or 2 steps each
    time. How many different ways can I go up this flight of stairs? Write a function
    count stair ways that solves this problem for me.

    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(3)
    3
    >>> count_stair_ways(4)
    5
    >>> count_stair_ways(5)
    8
    """

    # if one step is left, only one possibility is left
    if n == 1:
        return 1
    # having two steps left leaves two options: taking each single step or
    # taking two steps at once
    elif n == 2:
        return 2
    else:
    # break down   
        return count_stair_ways(n-1) + count_stair_ways(n-2)


def pascal(row, column):
    """
    finds the value at that position in the triangle, see pdf for more info

    >>> pascal(0,0)
    1
    >>> pascal(1,1)
    1
    >>> pascal(1,1)
    1
    >>> pascal(3,2)
    3
    >>> pascal(5,4)
    5
    """

    if column == 0:
        return 1
    elif row == 0:
        return 0
    else:
        return pascal(row-1, column) + pascal(row-1, column-1)


def sum_less_than(total, num):
#    """
#    Using any combination of numbers 1 through num, we want to figure out whether or
#    not we can sum to a given total. You can only use each number once. Challenge:
#    Try to sum to total using only the factors of num.
#
#    >>> sum_less_than(1,1)
#    True
#    >>> sum_less_than(2,1)
#    False
#    >>> sum_less_than(3,2)
#    True
#    >>> sum_less_than(6,3)
#    True
#    """
#    >>> sum_less_than(6,4)
#    True
#    >>> sum_less_than(8, 5) # 5 + 3 = 8
#    True
#    >>> sum_less_than(23, 5) # no way to make 23 by summing 1-5
#    False
#    if num == total:
#        return True
#    elif num > total:
#        return False
#    else:
#        return num + sum_less_than(total, num-1 ) 

# i didn't figure out this one. the solution was simple. instead of summing up (i didnt know how to do that)
# reduce the total by the current number. in the base case check if total is "0"
    if total == 0:
        return True
    if num == 0:
        return False
    return sum_less_than(total, num - 1) or sum_less_than(total - num, num - 1)        


def consists_of_multiple(sum, n):
    """
    >>> consists_of_multiple(4,2)
    True
    >>> consists_of_multiple(5,2)
    False
    """
    if sum % n == 0:
        return True
    return False



# counting down, zero/ below zero terminates function calls
def has_sum(sum, n1, n2 ):
    """
    >>> has_sum(4, 3, 5)
    False
    >>> has_sum(5, 3, 5) # 1(5) + 0(3) = 5
    True
    >>> has_sum(5, 5, 3) # 1(5) + 0(3) = 5
    True
    >>> has_sum(11, 3, 5) # 2(3) + 1(5) = 11
    True
    """

    if sum == 0:
        return True
    elif sum < 0:
        return False

    return has_sum( sum - n1, n1, n2 ) or has_sum( sum - n2, n1, n2 )


# counting up, preserving original sum value by using
# a helper function
def has_sum2(sum, n1, n2 ):
    """
    >>> has_sum(4, 3, 5)
    False
    >>> has_sum(5, 3, 5) # 1(5) + 0(3) = 5
    True
    >>> has_sum(5, 5, 3) # 1(5) + 0(3) = 5
    True
    >>> has_sum(11, 3, 5) # 2(3) + 1(5) = 11
    True
    """

    def _has_sum( current_sum, goal_sum, n1, n2):
        if current_sum == goal_sum:
            return True
        elif current_sum >  goal_sum:
            return False
    
        return _has_sum(current_sum + n1, goal_sum, n1, n2) or \
               _has_sum(current_sum + n2, goal_sum, n1, n2) 

    return _has_sum( sum, sum, n1, n2 )


def sum_range(lower, upper):
    """
    >>> sum_range(45, 60) # Printer A prints within this range the TAs would be satisfied with any number it prints
    True
    >>> sum_range(40, 55) # Printer A can print some number 56-60 copies, which is not within the TA acceptable range
    False
    >>> sum_range(170, 201) # Printer A + Printer B will print somewhere between 180 and 200 copies total
    True
    """

    printer_A_min = 50
    printer_A_max = 60
    printer_B_min = 130
    printer_B_max = 140

    def _sum_range( current_lower, current_upper):

        if current_upper > upper:
            return False
        if current_lower >= lower and current_upper <= upper:
            return True

        return _sum_range( current_lower + printer_A_min, current_upper + printer_A_max ) or \
               _sum_range( current_lower + printer_B_min, current_upper + printer_B_max )
    
    # start printing either with printer A or printer B ( kick off the tree recursion with two
    # different roots
    return _sum_range( printer_A_min, printer_A_max ) or \
           _sum_range( printer_B_min, printer_B_max ) 

