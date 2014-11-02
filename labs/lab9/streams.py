class Stream(object):
    class empty(object):
        def __repr__(self):
            return 'Stream.empty'

    empty = empty()

    def __init__(self, first, compute_rest, empty= False):
        self.first = first
        self._compute_rest = compute_rest
        self.empty = empty
        self._rest = None
        self._computed = False

    @property
    def rest(self):
        assert not self.empty, 'Empty streams have no rest.'
        if not self._computed:
            self._rest = self._compute_rest()
            self._computed = True
        return self._rest

    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

def first_k_as_list(s, k):
        first_k = []
        while s is not Stream.empty and k > 0:
            first_k.append(s.first)
            s, k = s.rest, k-1
        return first_k

def make_integer_stream(first=1):
    """
    >>> s = make_integer_stream()
    >>> first_k_as_list(s, 10)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    def compute_rest():
        return make_integer_stream(first+1)
    return Stream(first, compute_rest)

def add_streams(s1, s2):
    """
    >>> a = make_integer_stream(1)
    >>> b = make_integer_stream(2)
    >>> added = add_streams(a, b)
    >>> first_k_as_list(added, 5)
    [3, 5, 7, 9, 11]
    """
    "*** YOUR CODE HERE ***"

    if s1 is Stream.empty or s2 is Stream.empty:
        return s1

    def compute_rest():
        return add_streams(s1.rest, s2.rest)
    return Stream(s1.first + s2.first, compute_rest)

def make_fib_stream():
    """
    >>> a = make_fib_stream()
    >>> first_k_as_list(a, 10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    "*** YOUR CODE HERE ***"

    # inspired by lab 5
    def _fib_helper(cur=0, next=1):
        result = cur
        cur, next = next, cur + next

        def compute_rest():
            return _fib_helper(cur, next)

        return Stream(result, compute_rest)        

    return _fib_helper()

def stream_map(func, stream):
    """
    >>> s = make_integer_stream(1)
    >>> n = stream_map(lambda x: x * 2, s)
    >>> first_k_as_list(n, 5)
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"

    if stream is Stream.empty:
        return stream
    def compute_rest():
        return stream_map(func, stream.rest)
    return Stream(func(stream.first), compute_rest)


# assumed output: 1, 3, 9, 27...
def my_stream():
    def compute_rest():
        return add_streams(map_stream(double,
                                      my_stream()),
                                      my_stream())
    return Stream(1, compute_rest)

# a clumsy implementation but it works ;-)
def interleave(stream1, stream2):
    """
    >>> a = make_integer_stream(1)
    >>> b = make_integer_stream(11)
    >>> n = interleave(a,b)
    >>> first_k_as_list(n, 8)
    [1, 11, 2, 12, 3, 13, 4, 14]
    """
    "*** YOUR CODE HERE ***"
    
    def _inter_helper(stream1, stream2, is_stream1_next):
        if stream1 is Stream.empty or stream2 is Stream.empty:
            return stream1

        def compute_rest():
            if is_stream1_next:
                return _inter_helper(stream1.rest, stream2, False)    
            else:
                return _inter_helper(stream1, stream2.rest, True)    

        if is_stream1_next:
            return Stream(stream1.first, compute_rest)
        else:
            return Stream(stream2.first, compute_rest)

    return _inter_helper(stream1, stream2, True)

# this is the solution:
# the idea: just swap the arguments and let the first stream always be the 
# current one.
def interleave(stream1, stream2):
    if stream1.empty:
        return Stream.the_empty_stream
    return Stream(stream1.first, lambda: interleave(stream2, stream1.rest))


