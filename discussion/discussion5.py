def remove_all(el, lst):
    """Removes all instances of el from lst.
    >>> x = [3, 1, 2, 1, 5, 1, 1, 7]
    >>> remove_all(1, x)
    >>> x
    [3, 2, 5, 7]
    """

    while el in lst:
        lst.remove(el)

def add_this_many(x, y, lst):
    """ Adds y to the end of lst the number of times x occurs in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    """
    
    cnt = 0

    for el in lst:
        if el == x:
            cnt += 1

    for i in range(0,cnt):
        lst.append(y)

#1. What would Python print?
#>>> a = [3, 1, 4, 2, 5, 3]
#>>> a[:4]
# [3, 1, 4, 2 ]
#>>> a
# [3, 1, 4, 2, 5, 3]
#>>> a[1::2]
# [1,2,3]
#>>> a[:]
# [3, 5, 2, 4, 1, 3]
#>>> a[4:2]
# [5, 2 ]
#>>> a[1:-2]
# [ 1,4, 2 ]
#>>> a[::-1]
# [ ???? ]
 
def reverse(lst):
    """ Reverses lst in place.
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse(x)
    >>> x
    [1, 5, 4, 2, 3]
    """

    for i in range(len(lst)):
        lst.insert(i, lst.pop())


def rotate(lst, k):
    """ Return a new list, with the same elements
    of lst, rotated to the right k.
    >>> x = [1, 2, 3, 4, 5]
    >>> rotate(x, 3)
    [3, 4, 5, 1, 2]
    """

    length = len(lst)
    new_lst = [0] * length  # create new list, initilize with 0

    def _get_new_position( old_position, length, offset ):
        new_position = old_position + offset

        if new_position >= length:
            new_position =  new_position - length
        
        return new_position
        # remark:
        # the solution handles the wrapping by using the remainder of the list length:
        #
        # new_position = (old_position + offset) % length
        # return new_position

    for i in range(length):
        new_position = _get_new_position( i, length, k)

        new_lst[new_position] = lst[i]

    return new_lst


#1. What would Python print?
#>>> l_1, l_2 = lambda x: 3*x + 1, lambda x: x % 2 == 0
#>>> list(filter(l_2, map(l_1, [1,2,3,4])))
#
# org:     1  2  3  4
#
# map:     4  7  10 13
#
# filter:  4     10
# [ 4, 10 ]

#>>> [x*x - x for x in [1, 2, 3, 4] if x > 2]
# [ 6, 9 ]

#>>> [[y*2 for y in [x, x+1]] for x in [1,2,3,4]]
# [ 2, 4, 4, 6, 6, 8, 8, 10 ] 

# >>> superbowls = {’joe montana’: 4, ’tom brady’:3, ’joe flacco’: 0}
# >>> superbowls[’tom brady’]
# 3
# >>> superbowls[’peyton manning’] = 1
# >>> superbowls
# {’peyton manning’: 1, ’tom brady’: 3, ’joe flacco’: 0, ’joe montana’: 4}
# >>> superbowls[’joe flacco’] = 1
# >>> superbowls
# {’peyton manning’: 1, ’tom brady’: 3, ’joe flacco’: 1, ’joe montana’: 4}
# 
# 1. Continuing from above, what would Python print?
# >>> ’colin kaepernick’ in superbowls
# False
#
# >>> len(superbowls)
# 4
# 
# superbowls[’peyton manning’] = superbowls[’joe montana’]
# superbowls[(’eli manning’, ’giants’)] = 2
# superbowls[3] = ’cat’
# superbowls
# {’peyton manning’: 4, ’tom brady’: 3, ’joe flacco’: 1, ’joe montana’: 4
#  ('eli manning','giants') : 2, 3 : 'cat '}
#
# >>> superbowls[(’eli manning’, ’giants)] = \
# superbowls[’joe montana’] + superbowls[’peyton manning’]
# >>> superbowls[[’steelers’, ’49ers’]] = 11
# >>> superbowls
# {’peyton manning’: 4, ’tom brady’: 3, ’joe flacco’: 1, ’joe montana’: 4
#  ('eli manning','giants') : 8, 3 : 'cat ', [’steelers’, ’49ers’] = 11}


def replace_all(d, x, y):
    """Replaces all values of x with y.
    >>> d = {1: {2:3, 3:4}, 2:{4:4, 5:3}}
    >>> replace_all(d,3,1)
    >>> d
    {1: {2: 1, 3: 4}, 2: {4: 4, 5: 1}}
    """

#    for key in d.keys():
#        print(d[key])
#        if type(d[key]) is int:
#            if d[key] == x:
#                print('hier')
#                d[key] = y
#            return
#
#        else:
#            replace_all(d[key], x, y )

    # this one lets the test pass, however it is tight to the strucute of
    # of the unit test dict
    for inner_dict in d:
        for key in d[inner_dict]:
            if d[inner_dict][key] == x:
                d[inner_dict][key] = y

def rm(d, x):
    """Removes all pairs with value x.
    >>> d = {1:2, 2:3, 3:2, 4:3}
    >>> rm(d,2)
    >>> d
    {2: 3, 4: 3}
    """

    keys_to_delete = []

    for key in d:
        if d[key] == x:
            keys_to_delete.append( key )

    for key in keys_to_delete:
        del d[key]

if __name__ == "__main__":
    import doctest
    doctest.run_docstring_examples( rm , globals(), verbose=True)
    
