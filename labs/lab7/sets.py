def union(s1, s2):
    """Returns the union of two sets.

    >>> r = {0, 6, 6}
    >>> s = {1, 2, 3, 4}
    >>> t = union(s, {1, 6})
    >>> t
    {1, 2, 3, 4, 6}
    >>> union(r, t)
    {0, 1, 2, 3, 4, 6}
    """
    "*** YOUR CODE HERE ***"

    result = s1.copy()

    for item in s2:
        if item not in result:
            result.add(item)
    
    return result

def intersection(s1, s2):
    """Returns the intersection of two sets.

    >>> r = {0, 1, 4, 0}
    >>> s = {1, 2, 3, 4}
    >>> t = intersection(s, {3, 4, 2})
    >>> t
    {2, 3, 4}
    >>> intersection(r, t)
    {4}
    """
    "*** YOUR CODE HERE ***"

    result = set()

    for item_s1 in s1:
        for item_s2 in s2:
            if item_s1 == item_s2:
                result.add( item_s1 )

    return result                


def extra_elem(a,b):
    """B contains every element in A, and has one additional member, find
    the additional member.

    >>> extra_elem(['dog', 'cat', 'monkey'],  ['dog',  'cat',  'monkey',  'giraffe'])
    'giraffe'
    >>> extra_elem([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6])
    6
    """
    "*** YOUR CODE HERE ***"

    set_b = set(b)
    return set_b.difference( set(a) ).pop()

    # the solution
    # return list(set(b) - set(a))[0]

def add_up(n, lst):
    """Returns True if any two non identical elements in lst add up to any n.

    >>> add_up(100, [1, 2, 3, 4, 5])
    False
    >>> add_up(7, [1, 2, 3, 4, 2])
    True
    >>> add_up(10, [5, 5])
    False
    """
    "*** YOUR CODE HERE ***"


    lst_len = len(lst) - 1  # index starts from "0"

    for i, val in enumerate( lst ):
        if i+1 <= lst_len:
            if lst[i] != lst[i+1] and lst[i] + lst[i+1] == n:
                return True

    return False

    # hm, this should have been this weired set operation:
#    check_set = set()
#    for elem in lst:
#        if n - elem != elem:
#            check_set.add(n - elem)
#            return bool(intersection(check_set, set(lst)))

def find_duplicates(lst):
    """Returns True if lst has any duplicates and False if it does not.

    >>> find_duplicates([1, 2, 3, 4, 5])
    False
    >>> find_duplicates([1, 2, 3, 4, 2])
    True
    """
    "*** YOUR CODE HERE ***"

    # YESSSS, got it
    return len(lst) != len( set(lst) )

def find_duplicates_k(k, lst):
    """Returns True if there are any duplicates in lst that are within k
    indices apart.

    >>> find_duplicates_k(3, [1, 2, 3, 4, 1])
    False
    >>> find_duplicates_k(4, [1, 2, 3, 4, 1])
    True
    """
    "*** YOUR CODE HERE ***"

    # hm, it's not the solution but should be fine I guess
    def _find_dup(lower, upper ):
        if upper > len( lst ):
            return find_duplicates( lst[ lower:len(lst)-1 ] )
        else:
            return find_duplicates( lst[ lower:upper] ) or \
                    _find_dup( upper, upper + k ) 

    return _find_dup( 0, k + 1 )


def pow(n,k):
    """Computes n^k.

    >>> pow(2, 3)
    8
    >>> pow(4, 2)
    16
    """
    "*** YOUR CODE HERE ***"

    # this is the naive implementation
    result = n

    while k > 1:
        result *= n
        k -= 1

    return result   

    # solution, don't know if the recursion is actually cheaper
#    if k == 1:
#        return n
#    if k % 2 == 0:
#        return pow(n*n,k//2)
#    else:
#        return n * pow(n*n, k//2)

def missing_no(lst):
    """lst contains all the numbers from 1 to n for some n except some
    number k. Find k.

    >>> missing_no([1, 0, 4, 5, 7, 9, 2, 6, 3])
    8
    >>> missing_no(list(filter(lambda x: x != 293, list(range(2000)))))
    293
    """
    "*** YOUR CODE HERE ***"

    s1 = set(lst)
    s2 = set(range(1, max(lst)+1))  # create full set

    return (s2 - s1).pop()

    # solution, via summation ;-)
    #  return sum(range(max(lst) + 1)) - sum(lst)

#def find_duplicates_k_l(k, l, lst):
#    """Returns True if there are any two values who in lst that are within k
#    indices apart AND if the absolute value of their difference is less than
#    or equal to l.
#
#    >>> find_duplicates_k_l(4, 0, [1, 2, 3, 4, 5])
#    False
#    >>> find_duplicates_k_l(4, 1, [1, 2, 3, 4, 5])
#    True
#    >>> find_duplicates_k_l(4, 0, [1, 2, 3, 4, 1])
#    True
#    >>> find_duplicates_k_l(2, 0, [1, 2, 3, 4, 1])
#    False
#    >>> find_duplicates_k_l(1, 100, [100, 275, 320, 988, 27])
#    True
#    >>> find_duplicates_k_l(1, 100, [100, 199, 275, 320, 988, 27])
#    True
#    >>> find_duplicates_k_l(1, 100, [100, 23, 199, 275, 320, 988, 27])
#    True
#    >>> find_duplicates_k_l(2, 100, [100, 23, 199, 275, 320, 988, 27])
#    True
#    """
#    "*** YOUR CODE HERE ***"
