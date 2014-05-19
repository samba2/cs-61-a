

# Question 1
#
# What does Python print? Think about these before typing it into an interpreter!
#
#>>> lst = [1, 2, 3, 4, 5, 6]
#>>> lst[4] = 1
#>>> lst
#____[1, 2, 3, 4, 1, 6] _____
#>>> lst[2:4] = [9, 8]
#>>> lst
#_____[1,2,9,8,1,6]____
#>>> lst[3] = ['hi', 'bye']
#>>> lst
#_____[1,2,9,['hi', 'bye'] ,1,6]____
#>>> lst[3:] = ['jom', 'magrotker']
#>>> lst
#_____[1,2,9, 'jom', 'magrotker'____
#>>> lst[1:3] = [2, 3, 4, 5, 6, 7, 8]  > insert whole list, specifies position
#>>> lst
#____[1,2,3,'jom', 'magrotker']_____  > [1, 2, 3, 4, 5, 6, 7, 8, 'jom', 'magrotker']
#>>> lst == lst[:] > copy of whole list
#____????
#>>> lst is lst[:]
#______False___
#>>> a = lst[:]
#>>> a[0] = 'oogly'
#>>> lst
#____no change of lst_____
#>>> lst = [1, 2, 3, 4]
#>>> b = ['foo', 'bar']
#>>> lst[0] = b
#>>> lst
#____[['foo', 'bar'], 2, 3, 4]_____
#>>> b[1] = 'ply'
#>>> lst
#____[['foo', 'ply'], 2, 3, 4]_____
#>>> b = ['farply', 'garply']
#>>> lst
#____[['farply', 'garply'], 2, 3, 4]____ > No, new assignment to b does not change lst
#>>> lst[0] = lst
#>>> lst
#___???______
#>>> lst[0][0][0][0][0]
#____???_____
#

"""Starter file for lists lab."""


def reverse(lst):
    """Reverses lst using mutation.
    >>> original_list = [5, -1, 29, 0]
    >>> reverse(original_list)
    >>> original_list
    [0, 29, -1, 5]
    """
    "*** YOUR CODE HERE ***"

def map(fn, lst):
    """Maps fn onto lst using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> map(lambda x: x * x, original_list)
    >>> original_list
    [25, 1, 4, 0]
    """
    "*** YOUR CODE HERE ***"

def filter(pred, lst):
    """Filters lst with pred using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> filter(lambda x: x % 2 == 0, original_list)
    >>> original_list
    [2, 0]
    """
    "*** YOUR CODE HERE ***"

def coords(fn, seq, lower, upper):
    """
    >>> seq = (-4, -2, 0, 1, 3)
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [(-2, 4), (1, 1), (3, 9)]
    """ 
    return "*** YOUR CODE HERE ***"

def add_matrices(x, y):
    """
    >>> add_matrices([[1, 3], [2, 0]], [[-3, 0], [1, 2]])
    [[-2, 3], [3, 2]]
    """
    return "*** YOUR CODE HERE ***"

def deck()
    return "*** YOUR CODE HERE ***"

def sort_deck(deck):
    "*** YOUR CODE HERE ***"
