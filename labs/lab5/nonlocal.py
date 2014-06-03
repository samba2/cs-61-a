#Question 1
#
#Predict what Python will display when the following lines are typed into the interpreter:
#
#>>> def make_funny_adder(n):
#...     def adder(x):
#...         if x == 'new':
#...             nonlocal n
#...             n = n + 1
#...         else:
#...             return x + n
#...     return adder
#>>> h = make_funny_adder(3)
#>>> h(5)
#__8____
#>>> j = make_funny_adder(7)
#>>> j(5)
#___12___
#>>> h('new')
#>>> h(5)
#___9___


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    """
    "*** YOUR CODE HERE ***"

    cnt = 0

    def _return_fib():
        nonlocal cnt

        print(str(_calc_fib_recur( cnt )))

        cnt += 1

    def _calc_fib_recur( cnt ):
        """calculates the nth fibonocci number using recursion""" 

        if cnt <= 0:
            return 0
        elif cnt == 1:
            return 1
        else:
            return _calc_fib_recur(cnt-1) + _calc_fib_recur(cnt-2)

    return _return_fib 

# thats the solution, I guess it has been too easy:
# def make_fib():
#    cur, next = 0, 1
#    def fib():
#        nonlocal cur, next
#        result = cur
#        cur, next = next, cur + next
#        return result
#    return fib


def make_test_dice(seq):
    """Makes deterministic dice.

    >>> dice = make_test_dice([2, 6, 1])
    >>> dice()
    2
    >>> dice()
    6
    >>> dice()
    1
    >>> dice()
    2
    >>> other = make_test_dice([1])
    >>> other()
    1
    >>> dice()
    6
    """
    "*** YOUR CODE HERE ***"
    
    idx = 0

    def _test_dice():
        nonlocal idx
        result = seq[idx]
        idx = (idx + 1) % len(seq)
        return result

    return _test_dice
