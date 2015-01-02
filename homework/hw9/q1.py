class Mobile:
    """A simple binary mobile that has branches of weights or other mobiles.

    >>> Mobile(1, 2)
    Traceback (most recent call last):
        ...
    TypeError: 1 is not a Branch
    >>> Mobile(Branch(1,Weight(2)), 2)
    Traceback (most recent call last):
        ...
    TypeError: 2 is not a Branch
    >>> m = Mobile(Branch(1, Weight(2)), Branch(2, Weight(1)))
    >>> m.weight
    3
    >>> m.is_balanced()
    True
    >>> m.left.contents = Mobile(Branch(1, Weight(1)), Branch(2, Weight(1)))
    >>> type(m.left.contents)
    <class 'q1.Mobile'>
    >>> m.weight
    3
    >>> m.left.contents.is_balanced()
    False
    >>> m.is_balanced() # All submobiles must be balanced for m to be balanced
    False
    >>> m.left.contents.right.contents.weight = 0.5
    >>> m.left.contents.is_balanced()
    True
    >>> m.is_balanced()
    False
    >>> m.right.length = 1.5
    >>> m.is_balanced()
    True
    """

    def __init__(self, left, right):
        "*** YOUR CODE HERE ***"
        check_type(left, Branch)
        check_type(right, Branch)
        self.left = left
        self.right = right

    @property
    def weight(self):
        """The total weight of the mobile."""
        "*** YOUR CODE HERE ***"

        def weight_helper(branch):
            if type(branch.contents) is Weight:
                return branch.contents.weight
            elif type(branch.contents) is Mobile:
                return weight_helper(branch.contents.left) + \
                        weight_helper(branch.contents.right)
            
        return weight_helper(self.left) + weight_helper(self.right)

    def _branches_balanced(self):            
        return self.left.torque == self.right.torque

    def is_balanced(self):
        """True if and only if the mobile is balanced."""
        "*** YOUR CODE HERE ***"

# variant 1:
#
#        if type(self.left.contents) is Weight and \
#           type(self.right.contents) is Weight:
#            return self._branches_balanced()
#
#        if type(self.left.contents) is Weight:
#            return self.right.contents.is_balanced() and \
#                   self._branches_balanced()
#
#        if type(self.right.contents) is Weight:
#            return self.left.contents.is_balanced() and \
#                   self._branches_balanced()
#        else:
#            return self.left.contents.is_balanced() and \
#                   self.right.contents.is_balanced()
#      
#
# variant 2:
# both are not beautiful but work
#
        if not self._branches_balanced():
            return False
        
        if type(self.left.contents) is Mobile and \
           type(self.right.contents) is Mobile:
            return self.left.contents.is_balanced() and \
                   self.right.contents.is_balanced()

        if type(self.left.contents) is Mobile:
            return self.left.contents.is_balanced() 

        if type(self.right.contents) is Mobile:
            return self.right.contents.is_balanced() 

        return True

def check_type(object, expected_type): 
    if type(object) is not expected_type:
        raise TypeError(str(object) + ' is not a ' + expected_type.__name__)

def check_positive(x):
    """Check that x is a positive number, and raise an exception otherwise.

    >>> check_positive('hello')
    Traceback (most recent call last):
    ...
    TypeError: hello is not a number
    >>> check_positive('1')
    Traceback (most recent call last):
    ...
    TypeError: 1 is not a number
    >>> check_positive(-2)
    Traceback (most recent call last):
    ...
    ValueError: -2 <= 0
    """
    "*** YOUR CODE HERE ***"
    if not isinstance(x,int):
        raise TypeError(str(x) + ' is not a number')
    if x <= 0:
        raise ValueError(str(x) + ' <= 0')

class Branch:
    """A branch of a simple binary mobile."""

    def __init__(self, length, contents):
        if type(contents) not in (Weight, Mobile):
            raise TypeError(str(contents) + ' is not a Weight or Mobile')
        check_positive(length)
        self.length = length
        self.contents = contents

    @property
    def torque(self):
        """The torque on the branch"""
        return self.length * self.contents.weight


class Weight:
    """A weight."""
    def __init__(self, weight):
        check_positive(weight)
        self.weight = weight

    def is_balanced(self):
        return True


def interpret_mobile(s):
    """Return a Mobile described by string s by substituting one of the classes
    Branch, Weight, or Mobile for each occurrenct of the letter T.

    >>> simple = 'Mobile(T(2,T(1)), T(1,T(2)))'
    >>> a = interpret_mobile(simple)
    >>> interpret_mobile(simple).weight
    3
    >>> interpret_mobile(simple).is_balanced()
    True
    >>> s = 'T(T(4,T(T(4,T(1)),T(1,T(4)))),T(2,T(10)))'
    >>> m = interpret_mobile(s)
    >>> m.weight
    15
    >>> m.is_balanced()
    True
    """
    next_T = s.find('T')        # The index of the first 'T' in s.
    if next_T == -1:            # The string 'T' was not found in s
        try:
            return eval(s)      # Interpret s
        except TypeError as e:
            return None         # Return None if s is not a valid mobile
    for t in ('Branch', 'Weight', 'Mobile'):
        "*** YOUR CODE HERE ***"
        a = s.replace('T', t, 1)
        mobile = interpret_mobile(a)
        if type(mobile) is Mobile:
            return mobile
    return None
    
