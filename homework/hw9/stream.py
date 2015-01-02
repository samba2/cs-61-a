class Stream:
    """A lazily computed recursive list."""

    class empty:
        def __repr__(self):
            return 'Stream.empty'
    empty = empty()

    def __init__(self, first, compute_rest=lambda: Stream.empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

    def __iter__(self):
        """Return an iterator over the elements in the stream.

        >>> list(zip(range(6), ints))
        [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
        """
        "*** YOUR CODE HERE ***"
        while True:
            yield self.first
            self = self.rest

    def __getitem__(self, k):
        """Return the k-th element of the stream.

        >>> ints[5]
        6
        >>> increment_stream(ints)[7]
        9
        """
        "*** YOUR CODE HERE ***"
        i = 0
        while i < k:
            self = self.rest
            i+=1

        return self.first

def increment_stream(s):
    """Increment all elements of a stream."""
    return Stream(s.first+1, lambda: increment_stream(s.rest))

# The stream of consecutive integers starting at 1.
ints = Stream(1, lambda: increment_stream(ints))


## Q4.
#
#def scale_stream(s, k):
#    """Return a stream of the elements of S scaled by a number K.
#
#    >>> s = scale_stream(ints, 5)
#    >>> s.first
#    5
#    >>> s.rest
#    Stream(10, <...>)
#    >>> scale_stream(s.rest, 10)[2]
#    200
#    """
#    "*** YOUR CODE HERE ***"
#
#
## Q5.
#
#def merge(s0, s1):
#    """Return a stream over the elements of increasing s0 and s1, removing
#    repeats.
#
#    >>> twos = scale_stream(ints, 2)
#    >>> threes = scale_stream(ints, 3)
#    >>> m = merge(twos, threes)
#    >>> [m[i] for i in range(10)]
#    [2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
#    """
#    if s0 is Stream.empty:
#        return s1
#    elif s1 is Stream.empty:
#        return s0
#
#    e0, e1 = s0.first, s1.first
#    "*** YOUR CODE HERE ***"
#
#def make_s():
#    """Return a stream over all positive integers with only factors 2, 3, & 5.
#
#    >>> s = make_s()
#    >>> [s[i] for i in range(20)]
#    [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36]
#    """
#    def rest():
#        "*** YOUR CODE HERE ***"
#    s = Stream(1, rest)
#    return s
