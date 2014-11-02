class IteratorRestart(object):
    """
    >>> i = IteratorRestart(2, 7)
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        "*** YOUR CODE HERE ***"
        self.start = start-1
        self.end = end
        self.current = self.start

    def __next__(self):
        "*** YOUR CODE HERE ***"
        if self.current >= self.end:
            self.current = self.start
            raise StopIteration
        self.current += 1
        return self.current

    def __iter__(self):
        "*** YOUR CODE HERE ***"
        return self

def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    i = n

    while i >= 0:
        yield i
        i -= 1


class Countdown(object):
    """
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        while self.start >= 0:
            yield self.start
            self.start -= 1

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    yield int(n)

    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1

        yield int(n)

