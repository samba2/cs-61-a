

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


def reverse_buildin(lst):
    """Reverses lst using mutation.
    >>> original_list = [5, -1, 29, 0]
    >>> reverse_buildin(original_list)
    >>> original_list
    [0, 29, -1, 5]
    """
    "*** YOUR CODE HERE ***"

    lst = lst.reverse()

def reverse_iter(lst):
    """Reverses lst using mutation.
    >>> original_list = [5, -1, 29, 0]
    >>> reverse_iter(original_list)
    >>> original_list
    [0, 29, -1, 5]
    """
    "*** YOUR CODE HERE ***"

    tmp_lst = []

    while len(lst) > 0:
        tmp_lst.append( lst.pop() )

    # attach temp list to empty org list
    lst.extend( tmp_lst )    

def reverse_recur(lst):
    """Reverses lst using mutation.
    >>> original_list = [5, -1, 29, 0]
    >>> reverse_recur(original_list)
    >>> original_list
    [0, 29, -1, 5]
    """
    "*** YOUR CODE HERE ***"

    def _reverse_recur( ):
        
        if len(lst) == 1:
            return [ lst.pop(), ]
        else:
            return [ lst.pop(), ] + _reverse_recur()

    lst.extend( _reverse_recur() )


def map_iter(fn, lst):

    """Maps fn onto lst using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> map_iter(lambda x: x * x, original_list)
    >>> original_list
    [25, 1, 4, 0]
    """
    "*** YOUR CODE HERE ***"

    for i in range(0, len(lst)):
        lst[i] = fn( lst[i] )


# logic goes:
# - as long as there are elements in lst:
#   - get last element from list, apply function and store result
#     in "tmp" on the current frame
#   - then call map_recur again, get the last element from list, apply function
#     and store value in "tmp" on a second frame
# - in the moment where the if clause is False (no more elements), the "if" branch is not executed,
#   the function returns "None"
# - !!! then, the open frames with the single "tmp" values a processed, starting from where we
#   stopped before - executing the lst.append command. 
#   This reads: append the "tmp" value of the current frame to "lst" which is in the global frame.
# - this is repeated until all open frames are done processing. 
#
# This technique uses the single frames to store temporary data.
def map_recur(fn, lst):

    """Maps fn onto lst using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> map_recur(lambda x: x * x, original_list)
    >>> original_list
    [25, 1, 4, 0]
    """
    "*** YOUR CODE HERE ***"

    if len(lst) > 0:
        tmp =  fn( lst.pop() )
        map_recur(fn, lst)

        lst.append(tmp)


def filter_iter(pred, lst):
    """Filters lst with pred using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> filter_iter(lambda x: x % 2 == 0, original_list)
    >>> original_list
    [2, 0]
    """
    "*** YOUR CODE HERE ***"

    tmp_lst = []
   
    for i in range(len(lst)):
        element = lst.pop(0)

        if pred( element ):
            tmp_lst.append( element )

    lst.extend( tmp_lst )


# same idea as above:
# - put all elements of the list in single frames
# - if list is empty execute body of filter_recur for each frame
# - if pred is True for element, insert the element in 'lst' which is now empty
def filter_recur(pred, lst):
    """Filters lst with pred using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> filter_recur(lambda x: x % 2 == 0, original_list)
    >>> original_list
    [2, 0]
    """
    "*** YOUR CODE HERE ***"

    if lst:
        element = lst.pop()

        filter_recur( pred, lst )

        if pred( element ):
            lst.append( element )

def coords(fn, seq, lower, upper):
    """
    >>> seq = (-4, -2, 0, 1, 3)
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [(-2, 4), (1, 1), (3, 9)]
    """ 
    "*** YOUR CODE HERE ***"

    return list( (x,fn(x)) for x in seq if fn(x) >= lower and fn(x) <= upper )


def add_matrices(x, y):
    """
    >>> add_matrices([[1, 3], [2, 0]], [[-3, 0], [1, 2]])
    [[-2, 3], [3, 2]]
    """
    "*** YOUR CODE HERE ***"
    return list( [ x[i][0] + y[i][0], x[i][1] + y[i][1] ] for i in range(len(x)) )

def deck():
    # had to copy solution here, didn't understand the question
    return [(suit, value) for suit in ("spades", "clubs", "diamonds", "hearts") for value in range(1, 14)]

def test_deck():
    return [('spades', 2), ('spades', 1), ('clubs', 1), ('clubs', 2), ('diamonds', 2), ('diamonds', 1)]


def stringify_card( card ):
    """
    >>> stringify_card( ('clubs', 1) )
    'clubs1'
    """
    return card[0] + str(card[1])

def sort_deck(deck):
    """
    >>>
    >>> sort_deck( test_deck )
    [('clubs', 1), ('clubs', 2), ('diamonds', 1), ('diamonds', 2), ('spades', 1), ('spades', 2)]

    """
    "*** YOUR CODE HERE ***"

    my_deck = deck()

    my_deck.sort(key=stringify_card)
    return my_deck

