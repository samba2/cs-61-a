from ucb import main, trace, interact
from scheme_tokens import tokenize_lines, DELIMITERS
from buffer import Buffer, InputReader

# Pairs and Scheme lists

class Pair(object):
    """A pair has two instance attributes: first and second.  For a Pair to be
    a well-formed list, second is either a well-formed list or nil.  Some
    methods only apply to well-formed lists.

    >>> s = Pair(1, Pair(2, nil))
    >>> s
    Pair(1, Pair(2, nil))
    >>> print(s)
    (1 2)
    >>> len(s)
    2
    >>> s[1]
    2
    >>> print(s.map(lambda x: x+4))
    (5 6)
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return "Pair({0}, {1})".format(repr(self.first), repr(self.second))

    def __str__(self):
        s = "(" + str(self.first)
        second = self.second
        while isinstance(second, Pair):
            s += " " + str(second.first)
            second = second.second
        if second is not nil:
            s += " . " + str(second)
        return s + ")"

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
        y = self
        for _ in range(k):
            if y.second is nil:
                raise IndexError("list index out of bounds")
            elif not isinstance(y.second, Pair):
                raise TypeError("ill-formed list")
            y = y.second
        return y.first

    def map(self, fn):
        """Return a Scheme list after mapping Python function FN to SELF."""
        mapped = fn(self.first)
        if self.second is nil or isinstance(self.second, Pair):
            return Pair(mapped, self.second.map(fn))
        else:
            raise TypeError("ill-formed list")

class nil(object):
    """The empty list"""

    def __repr__(self):
        return "nil"

    def __str__(self):
        return "()"

    def __len__(self):
        return 0

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        raise IndexError("list index out of bounds")

    def map(self, fn):
        return self

nil = nil() # Assignment hides the nil class; there is only one instance


def next_is_op(src):
    """Returns whether the next item is an operator
    >>> lines = ["+ 2 3"]
    >>> src = Buffer(tokenize_lines(lines))
    >>> next_is_op(src)
    True
    >>> lines = ["3"]
    >>> src = Buffer(tokenize_lines(lines))
    >>> next_is_op(src)
    False
    """
    "***YOUR CODE HERE***"

    operator = ('+', '-', '*', '/')

    if not src.more_on_line or src.current() is None:
        return False
    if src.current() in operator:
        return True
    return False

# Scheme list parser, without quotation or dotted lists.

def scheme_read(src):
    """Read the next expression from src, a Buffer of tokens.

    >>> lines = ['(+ 1 ', '(+ 23 4)) (']
    >>> src = Buffer(tokenize_lines(lines))
    >>> print(scheme_read(src))
    (+ 1 (+ 23 4))
    """
    if src.current() is None:
        raise EOFError
    val = src.pop()
    if val == 'nil':
        return nil
    elif type(val) in (float, int):
        "***YOUR CODE HERE***"
        
        if next_is_op(src):
            return read_infix(val, src)

        return val

    elif val not in DELIMITERS:  # ( ) ' .
        return val
    elif val == "(":

        # returns a Pair
        val = read_tail(src)

        #Note that this isn't the best idea of what to do.
        #We have to add this semi-hack because we're modifying the language
        #in a strange way to get infix notation.
        if val.second == nil and val.first != nil:
            val = val.first

        "***YOUR CODE HERE***"

        if next_is_op(src):
            return read_infix(val, src)

        return val
    else:
        raise SyntaxError("unexpected token: {0}".format(val))

def read_infix(first, src):
    """Returns a scheme expression which represents the equivalent scheme expression
        to the given infix expression
    >>> read_infix(3, Buffer(tokenize_lines("+ 4 5")))
    Pair('+', Pair(3, Pair(4, nil)))
    >>> read_infix(2, Buffer(tokenize_lines("+ (* 3 4) 7")))
    Pair('+', Pair(2, Pair(Pair('*', Pair(3, Pair(4, nil))), nil)))
    """
    "***YOUR CODE HERE***"
    
    # had to take the shortcut :-(
    if not src.more_on_line or src.current() is None or src.current() == ")":
        return nil
    op = src.pop()
    rest = scheme_read(src)
    return Pair(op, Pair(first, Pair(rest, nil)))

    # i kind was in the middle, however, the recursion of "the rest" via scheme_read
    # was missung. 
    # also I didn't see how simple the Pair construct pattern was. sad

    #    operant = src.pop()
    #    rest = src.pop()
    #    if not src.more_on_line:
    #        return nil
    #
    #    if src.current() == ")":
    #        return nil
    #
    #    if src.current() == "nil":
    #        return nil

def read_tail(src):
    """Return the remainder of a list in src, starting before an element or ).

    >>> read_tail(Buffer(tokenize_lines([')'])))
    nil
    >>> read_tail(Buffer(tokenize_lines(['2 3)'])))
    Pair(2, Pair(3, nil))
    >>> read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
    Pair(2, Pair(Pair(3, Pair(4, nil)), nil))
    """
    if src.current() is None:
        raise SyntaxError("unexpected end of file")
    if src.current() == ")":
        src.pop()
        return nil
    first = scheme_read(src)
    rest = read_tail(src)
    return Pair(first, rest)


# Interactive loop

def buffer_input():
    return Buffer(tokenize_lines(InputReader('> ')))

@main
def read_print_loop():
    """Run a read-print loop for Scheme expressions."""
    while True:
        try:
            src = buffer_input()
            while src.more_on_line:
                expression = scheme_read(src)
                print(repr(expression))
        except (SyntaxError, ValueError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            return

#if __name__ == "__main__":
#    import doctest
#    doctest.run_docstring_examples( next_is_op , globals(), verbose=True)
#
