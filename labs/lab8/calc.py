"""An interpreter for the Scheme-Syntax Calculator Language

An interpreter for a calculator language that uses prefix-order call syntax.
Operator expressions must be operator symbols.  Operand expressions are
separated by spaces.

Examples:
    > (* 1 2 3)
    6
    > (+)
    0
    > (+ 2 (/ 4 8))
    2.5
    > (+ 2 2) (* 3 3)
    4
    9
    > (+ 1
         (- 23)
         (* 4 2.5))
    -12
    > )
    SyntaxError: unexpected token: )
    > 2.3.4
    ValueError: invalid numeral: 2.3.4
    > +
    TypeError: + is not a number or call expression
    > (/ 5)
    TypeError: / requires exactly 2 arguments
    > (/ 1 0)
    ZeroDivisionError: division by zero
"""

from ucb import trace, main, interact
from operator import add, sub, mul
from scheme_reader import Pair, nil, scheme_read, buffer_input


# Eval & Apply

env = {} #The global environment

def calc_eval(exp):
    """Evaluate a Calculator expression.

    >>> calc_eval(as_scheme_list('+', 2, as_scheme_list('*', 4, 6)))
    26
    >>> calc_eval(as_scheme_list('+', 2, as_scheme_list('/', 40, 5)))
    10
    >>> calc_eval(as_scheme_list('define', 'x', 3))
    x
    >>> calc_eval(as_scheme_list('+', 'x', 2))
    5
    >>> calc_eval(as_scheme_list('*', 'x', as_scheme_list('+', 2, 'x')))
    15
    """
    if type(exp) in (int, float):
        return simplify(exp)
    if type(exp) is str and is_identifier(exp): #do lookup here
        "*** YOUR CODE HERE ***"
        return nil
    elif isinstance(exp, Pair):
        if exp.first == "define":
            return do_define_form(exp.second)
        arguments = exp.second.map(calc_eval)
        return simplify(calc_apply(exp.first, arguments))
    else:
        raise TypeError(exp + ' is not a primitive or call expression')

def is_identifier(exp):
    "*** YOUR CODE HERE ***"
    return False

def do_define_form(args):
    "*** YOUR CODE HERE ***"
    return nil

def calc_apply(operator, args):
    """Apply the named operator to a list of args.

    >>> calc_apply('+', as_scheme_list(1, 2, 3))
    6
    >>> calc_apply('-', as_scheme_list(10, 1, 2, 3))
    4
    >>> calc_apply('*', nil)
    1
    >>> calc_apply('*', as_scheme_list(1, 2, 3, 4, 5))
    120
    >>> calc_apply('/', as_scheme_list(40, 5))
    8.0
    """
    if not isinstance(operator, str):
        raise TypeError(str(operator) + ' is not a symbol')
    if operator == '+':
        return reduce(add, args, 0)
    elif operator == '-':
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        elif len(args) == 1:
            return -args[0]
        else:
            return reduce(sub, args.second, args.first)
    elif operator == '*':
        return reduce(mul, args, 1)
    elif operator == '/':
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer/denom
    else:
        raise TypeError(operator + ' is an unknown operator')

def simplify(value):
    """Return an int if value is an integer, or value otherwise.

    >>> simplify(8.0)
    8
    >>> simplify(2.3)
    2.3
    >>> simplify('+')
    '+'
    """
    if isinstance(value, float) and int(value) == value:
        return int(value)
    return value

def reduce(fn, scheme_list, start):
    """Reduce a recursive list of Pairs using fn and a start value.

    >>> reduce(add, as_scheme_list(1, 2, 3), 0)
    6
    """
    if scheme_list is nil:
        return start
    return reduce(fn, scheme_list.second, fn(start, scheme_list.first))

def as_scheme_list(*args):
    """Return a recursive list of Pairs that contains the elements of args.

    >>> as_scheme_list(1, 2, 3)
    Pair(1, Pair(2, Pair(3, nil)))
    """
    if len(args) == 0:
        return nil
    return Pair(args[0], as_scheme_list(*args[1:]))

@main
def read_eval_print_loop():
    """Run a read-eval-print loop for Calculator."""

    while True:
        try:
            src = buffer_input()
            import pdb; pdb.set_trace()
            while src.more_on_line:
                expression = scheme_read(src)
                print(calc_eval(expression))
        except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            print('Calculation completed.')
            return
