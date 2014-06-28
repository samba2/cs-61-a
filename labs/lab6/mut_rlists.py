# Rlist definition
class Rlist:
    """A recursive list consisting of a first element and the rest.

    >>> s = Rlist(1, Rlist(2, Rlist(3)))
    >>> print(rlist_expression(s.rest))
    Rlist(2, Rlist(3))
    >>> len(s)
    3
    >>> s2 = Rlist(1)
    >>> len(s2)
    1
    >>> s[0]
    1
    >>> s[1]
    2
    """

    class EmptyList:
        def __len__(self):
            return 0

        def __getitem__(self):
            return None

    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __len__iter(self):
        "*** YOUR CODE HERE ***"
        cnt = 1
        while self.rest is not self.empty:
            self.rest = self.rest.rest
            cnt += 1
        
        return cnt

    # recursive solution(tailrecursion since len can directly be returned, 
    # no need for summing up with previous frame
    def __len__(self):
        "*** YOUR CODE HERE ***"

        def _cnt(rest, len ):
            if rest is self.empty:
                return len

            return _cnt(rest.rest, len + 1)    

        return _cnt(self.rest, 1) 


    def __getitem__iter(self, index):
        "*** YOUR CODE HERE ***"

        assert index < len(self)
        
        curr_index = 0
        mylist = self

        while curr_index != index:
            mylist = mylist.rest
            curr_index += 1

        return mylist.first


    # recursive
    def __getitem__(self, index):

        assert index < len(self)

        def _find_item( curr_list, curr_index ):
           
            if curr_index == index:
                return curr_list.first

            return _find_item( curr_list.rest, curr_index + 1 )

        return _find_item( self, 0 )


# Predict what Python will display when the following lines are typed into the interpreter:
# 
# >>> print(Rlist(1, Rlist(2)))
# _____1, Rlist(2)
# >>> Rlist()
# ____error: arguments missing_
# >>> rlist = Rlist(1, Rlist(2, Rlist(3)))
# >>> rlist.first
# __1___
# >>> rlist.rest.first
# __2___
# >>> rlist.rest.rest.rest is Rlist.empty
# __True___
# >>> rlist.first = 9001
# >>> rlist.first
# ___9001__
# >>> rlist.rest = rlist.rest.rest
# >>> rlist.rest.first
# ___3__
# >>> rlist = Rlist(1)
# >>> rlist.rest = rlist
# >>> rlist.rest.rest.rest.rest.first
# ___1__??

#################
# RList folding #
#################

from operator import add, sub, mul

def rlist_expression(s):
    """Return a string that would evaluate to s."""
    if s.rest is Rlist.empty:
        rest = ''
    else:
        rest = ', ' + rlist_expression(s.rest)
    return 'Rlist({0}{1})'.format(s.first, rest)

def foldl(rlist, fn, z):
    """ Left fold
    >>> lst = Rlist(3, Rlist(2, Rlist(1)))
    >>> foldl(lst, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl(lst, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl(lst, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    if rlist == Rlist.empty:
        return z
    return foldl( rlist.rest, fn, fn( z, rlist.first) )

def foldr(rlist, fn, z):
    """ Right fold
    >>> lst = Rlist(3, Rlist(2, Rlist(1)))
    >>> foldr(lst, sub, 0) # (3 - (2 - (1 - 0)))
    2
    >>> foldr(lst, add, 0) # (3 + (2 + (1 + 0)))
    6
    >>> foldr(lst, mul, 1) # (3 * (2 * (1 * 1)))
    6
    """
    "*** YOUR CODE HERE ***"
    if rlist == Rlist.empty:
        return z
    return fn( rlist.first, foldr( rlist.rest, fn, z))


def mapl(lst, fn):
    """ Maps FN on LST
    >>> lst = Rlist(3, Rlist(2, Rlist(1)))
    >>> mapped = mapl(lst, lambda x: x*x)
    >>> print(rlist_expression(mapped))
    Rlist(9, Rlist(4, Rlist(1)))
    """
    "*** YOUR CODE HERE ***"
    # i had to look that up
    return foldr(lst, lambda x, xs: Rlist(fn(x), xs), Rlist.empty)  

#    mapped_lst = Rlist( fn(lst.first) )
#    lst = lst.rest
#
#    for i in range(len(lst)):
#        mapped_lst = Rlist( fn(lst[i]), mapped_lst )
#
#    return mapped_lst

def filterl(lst, pred):
    """ Filters LST based on PRED
    >>> lst = Rlist(4, Rlist(3, Rlist(2, Rlist(1))))
    >>> filtered = filterl(lst, lambda x: x % 2 == 0)
    >>> print(rlist_expression(filtered))
    Rlist(4, Rlist(2))
    """
    "*** YOUR CODE HERE ***"

    def _filter(x, xs):
        if pred(x):
            return Rlist(x,xs)
        return xs

    return foldr(lst, _filter, Rlist.empty)  


def reverse(lst):
    """ Reverses LST with foldl
    >>> reversed = reverse(Rlist(3, Rlist(2, Rlist(1))))
    >>> print(rlist_expression(reversed))
    Rlist(1, Rlist(2, Rlist(3)))
    >>> reversed = reverse(Rlist(1))
    >>> print(rlist_expression(reversed))
    Rlist(1)
    >>> reversed = reverse(Rlist.empty)
    >>> reversed == Rlist.empty
    True
    """
    "*** YOUR CODE HERE ***"

    # !! YES !! Got it!!
    return foldl(lst, lambda a, b: Rlist(b, a), Rlist.empty)  


#def reverse1(lst):
#    """ Reverses LST without the Rlist constructor
#    >>> reversed = reverse2(Rlist(3, Rlist(2, Rlist(1))))
#    >>> print(rlist_expression(reversed))
#    Rlist(1, Rlist(2, Rlist(3)))
#    >>> reversed = reverse2(Rlist(1))
#    >>> print(rlist_expression(reversed))
#    Rlist(1)
#    >>> reversed = reverse(Rlist.empty)
#    >>> reversed == Rlist.empty
#    True
#    """
#    "*** YOUR CODE HERE ***"
#
#
#

#identity = lambda x: x
#
#def foldl2(rlist, fn, z):
#    """ Write foldl using foldr
#    >>> list = Rlist(3, Rlist(2, Rlist(1)))
#    >>> foldl2(list, sub, 0) # (((0 - 3) - 2) - 1)
#    -6
#    >>> foldl2(list, add, 0) # (((0 + 3) + 2) + 1)
#    6
#    >>> foldl2(list, mul, 1) # (((1 * 3) * 2) * 1)
#    6
#    """
#    def step(x, g):
#        "*** YOUR CODE HERE ***"
#    return foldr(rlist, step, identity)(z)
