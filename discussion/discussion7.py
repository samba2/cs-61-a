class Tree:
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right

    def __repr__(self):
        args = repr(self.entry)
        
        if self.left or self.right:
            args += ', {0}, {1}'.format(repr(self.left), repr(self.right))

        return 'Tree({0})'.format(args)



#t2 = Tree(4,
#         Tree(2, Tree(8, Tree(7)),
#              Tree(3, Tree(1), Tree(6))),
#         Tree(1, Tree(5),
#              Tree(3, Tree(2), Tree(9))))


def square_tree(t):
    """
    >>> t = Tree(2, Tree(3, Tree(4)))
    >>> square_tree(t)
    >>> print(t)
    Tree(4, Tree( 9, Tree(16)))
    """
    """Mutates a Tree t by squaring all its elements"""

    if t:
        t.entry *= t.entry

        square_tree(t.left)
        square_tree(t.right)

def height(t):
    """
    >>> t = Tree(2)
    >>> height(t)
    0
    >>> t = Tree(2, Tree(1))
    >>> height(t)
    1
    >>> t = Tree(2, Tree(3, Tree(4)))
    >>> height(t)
    2
    """
    if not t or not t.left and not t.right:
        return 0
    if t:        
        return max( 1 + height(t.left), 1 + height(t.right))

def tree_size(t):
    """
    >>> t = Tree(2, Tree(3, Tree(4)))
    >>> tree_size(t)
    3
    """
    left_sum = 0
    right_sum = 0

    if t:
        if t.left:
            left_sum = tree_size(t.left)
        if t.right:
            right_sum = tree_size(t.right)

        return 1 + left_sum + right_sum

    # the solution is even more elegant:
    # if not t:
    #     return 0
    # return 1 + tree_size(t.left) + tree_size(t.right)


def find_path(t, entry):
    """
    >>> t = Tree(2, Tree(15), Tree( 7, Tree(2), Tree(6, Tree(5), Tree(11))))
    >>> find_path(t, 5)
    (2, 7, 6, 5)
    >>> find_path(t, 8)
    False
    >>> find_path(t, 2)
    (2,)
    """
    
    def _record_path2(my_tree, path):
        if not my_tree:
            return False
        if my_tree.entry == entry:
            return path + (my_tree.entry, )
        else:
            return _record_path2(my_tree.left, path + (my_tree.entry, )) or  \
                   _record_path2(my_tree.right, path + (my_tree.entry, )) 
        
    return _record_path2(t, () )

def print_inorder(t):
    """
    >>> t = Tree(9, Tree( 4, Tree(2), Tree(6)), Tree(19))
    >>> print_inorder(t)
    2
    4
    6
    9
    19
    """
    
    if t:
        if t.left:
            print_inorder(t.left)

        print(t.entry)

        if t.right:
            print_inorder(t.right)

