class nil(object):
    """The empty list"""
    def __len__(self):
        return 0
    
    def map(self, fn):
        return self

nil = nil() #nil now refers to a single instance of nil class


class Pair(object):
    def __init__(self, first, second=nil):
        self.first = first
        self.second = second
    
    def __len__(self):
        n, second = 1, self.second
    
        while isinstance(second, Pair):
            n += 1
            second = second.second
        
        if second is not nil:
            raise TypeError("length attempted on improper list")
        return n

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        j, y = 0, self
        while j < k:
            if y.second is nil:
                raise IndexError("list index out of bounds")
            elif not isinstance(y.second, Pair):
                raise TypeError("ill-formed list")
            j, y = j + 1, y.second
        
        return y.first

    def map(self, fn):
        """Returns a Scheme list after mapping Python function
        fn over self."""

        mapped = fn(self.first)
        
        if self.second is nil or isinstance(self.second, Pair):
            return Pair(mapped, self.second.map(fn))
        else:
            raise TypeError("ill-formed list")
        
    def to_py_list(self):
        """Returns a Python list containing the elements of this
        Scheme list."""
        
        y, result = self, [ ]
        while y is not nil:
            result += [y.first]
            if not ( isinstance(y.second, Pair) or y.second is nil ):
                raise TypeError("ill-formed list")
            y = y.second
        return result

def calc_eval(exp):
    """
    >>> calc_eval(Pair('+', Pair(3, Pair(4, nil))))
    7
    >>> calc_eval(Pair('=', Pair(3, Pair(4, nil))))
    False
    >>> calc_eval(Pair('=', Pair(3, Pair(3, nil))))
    True
    >>> calc_eval(Pair('<', Pair(3, Pair(4, nil))))
    True
    >>> calc_eval(Pair('<', Pair(3, Pair(3, nil))))
    False
    >>> calc_eval(Pair('<', Pair(3, Pair(2, nil))))
    False
    >>> calc_eval(Pair( 'and', Pair( Pair('=', Pair(3, Pair(4, nil))), Pair('<', Pair(3, Pair(3, nil))))))
    False
    """
    if not isinstance(exp, Pair): #expression is primitive
        return exp
    elif exp.first == 'and':
        return eval_and(exp.second)
    else:
        operator, operands = exp.first, exp.second
        args = operands.map(calc_eval).to_py_list()
    return calc_apply(operator, args)


# i had to lookup the solution for Q1.4.5
# "adding 'and'"
def eval_and(operands):
    cur = operands
    while cur is not nil:
    
        if not calc_eval(cur.first):
            return False
        cur = cur.second
    return True


def calc_apply(operator, args):
    if operator == '+':
        return sum(args)
    elif operator == '-':
        if len(args) == 1:
            return -args[0]
        else:
            return sum(args[0], [-args for args in args[1:]])
    elif operator == '*':
        return reduce(mul, args, 1)
    elif operator == '=':
        if len(args) != 2:
            raise TypeError("need two arguments for equal check")
        return args[0] == args[1]
    elif operator == '<':
        if len(args) != 2:
            raise TypeError("need two arguments for less then check")
        return args[0] < args[1]


