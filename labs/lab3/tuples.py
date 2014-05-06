# What would Python print?
# 
# Predict what Python will display when you type the following into the interpreter. Then try it to check your answers.
# Question 6
#
#>>> x = (1, 2, 3)
#>>> x[0]     # Q1
#___1__
#>>> x[3]     # Q2
#___Exception__
#
#>>> x[-1]    # Q3
#___3__
#>>> x[-3]    # Q4
#___1__
#
#
#Question 7
#
#>>> x = (1, 2, 3, 4)
#>>> x[1:3]       # Q1
#__(2,3)____
#>>> x[:2]        # Q2
#___(1,2)___
#>>> x[1:]        # Q3
#____(2,3,4)__
#>>> x[-2:3]      # Q4
#___(3)___
#>>> x[::2]       # Q5
#______
#>>> x[::-1]      # Q6
#__(4)____ was wrong, (4,3,2,1) is right > reverses list
#>>> x[-1:0:-1]   # Q7
#__double reverse, list in orignal order, why is first element missing? ____
#
#Question 8
#
#>>> y = (1,)
#>>> len(y)       # Q1
#___1___
#>>> 1 in y       # Q2
#___True___
#
#>>> y + (2, 3)   # Q3
#___???___  > prepending y to (2,3) tuple. result is (1,2,3)
#
#>>> (0,) + y     # Q4
#___(0,1)___
#>>> y * 3        # Q5
#___Error__> multiplies tuple content three times. result is (1,1,1)
#
#>>> z = ((1, 2), (3, 4, 5))
#>>> len(z)       # Q6
#___2___
#
#
#Question 9
#
#For each of the following, give the correct expression to get 7.
#
#>>> x = (1, 3, 5, 7)
#>>> x[-1]    # example
#7
#
#>>> x = (1, 3, (5, 7), 9)
#>>> x[2][1]
#7
#
#>>> x = ((7,),)
#>>> x[0][0]
#7
#
#>>> x = (1, (2, (3, (4, (5, (6, (7,)))))))
#>>> x[1][1][1][1][1][1][0]
#7


"""Starter file for tuples lab"""

##########
# TUPLES #
##########

def reverse_iter(tup):
    """Returns the reverse of the given tuple.

    >>> reverse_iter((1, 2, 3, 4))
    (4, 3, 2, 1)
    """
    "*** YOUR CODE HERE ***"
   
    rev_tup = ()

    # take last tuple element + shorten original tupel by this element
    while len(tup) > 0:
        rev_tup = rev_tup + (tup[-1],)
        tup = tup[0:-1]
    return rev_tup


def reverse_recursive(tup):
    """Returns the reverse of the given tuple.

    >>> reverse_recursive((1, 2, 3, 4))
    (4, 3, 2, 1)
    """
    "*** YOUR CODE HERE ***"
    
    # both base criteria are working, the second one (from the solution) recurses
    # one step further which gives an empyty tuple as the last argument to add
    if len(tup) == 1:
        return tup

    #if not tup:
    #    return ()

    else:
        # take last element + feed list shorten by last element into recursion
        return tup[-1:] + reverse_recursive(tup[0:-1])

def merge(tup1, tup2):
    """Merges two sorted tuples.

    >>> merge((1, 8), (5,))
    (1, 5, 8)
    >>> merge((), (2, 4, 6))
    (2, 4, 6)
    >>> merge((1, 2, 3), ())
    (1, 2, 3)
    >>> merge((1, 3, 5), (2, 4, 6))
    (1, 2, 3, 4, 5, 6)
    >>> merge((1, 5, 9), (3, 7))
    (1, 3, 5, 7, 9)
    """
    "*** YOUR CODE HERE ***"
    # base criterion
    if not tup1:
        return tup2
    elif not tup2: 
        return tup1

    # base crit. can be shrinked to following two lines as proposed by the solution
    # since one of the tuples is empty anyway:
    #
    # if not tup1 or not tup2:
    #    return tup1 + tup2

    # recursion
    elif tup1[0] < tup2[0]:
        return (tup1[0],) + merge(tup1[1:], tup2)
    else:  
        return (tup2[0],) + merge(tup1, tup2[1:])

