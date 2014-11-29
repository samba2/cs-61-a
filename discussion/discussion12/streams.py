class Stream:
    class empty:
        pass
    empty = empty()

    def __init__(self, first, compute_rest=lambda: Stream.empty):
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

def first_k_as_list(s, k):
        first_k = []
        while s is not Stream.empty and k > 0:
            first_k.append(s.first)
            s, k = s.rest, k-1
        return first_k

def make_integer_stream(first=1):
    """
    >>> s = make_integer_stream()
    >>> first_k_as_list(s, 4)
    [1, 2, 3, 4]
    """
    def compute_rest():
        return make_integer_stream(first+1)
    return Stream(first, compute_rest)


# cool, my solution is shorter than the propsed one.
# reason is, that i'm using the named arguemts as kind of hidden variables
# if mak_fib_stream is called without arguemtsn, the given defaults are used
def mak_fib_stream(curr=0, next=1):
    """
    >>> s = mak_fib_stream()
    >>> first_k_as_list(s, 10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    def compute_rest():
        return mak_fib_stream(next, curr+next)
    return Stream(curr, compute_rest)


# 2. random stream:
from random import random
# orignal  wrong code:
#random_stream = Stream(random(), lambda: random_stream)
#s = random_stream()

# works:
# def make_random_stream():
#     def compute_rest():
#         return make_random_stream()
#     return Stream(random(), compute_rest)
# 
# s = make_random_stream()
# print(first_k_as_list(s, 10))

def filter_stream(filter_func, s):
    """
    >>> s = make_integer_stream()
    >>> f = filter_stream(lambda x: x % 2 == 0, s)
    >>> first_k_as_list(f, 4)
    [2, 4, 6, 8]
    """
    def make_filtered_rest():
        return filter_stream(filter_func, s.rest)

    if s is Stream.empty:
        return s
    elif filter_func(s.first):
        return Stream(s.first, make_filtered_rest)
    else:
        return filter_stream(filter_func, s.rest)

# 1.3. output?
# def my_stream():
#     def compute_rest():
#         return add_streams(map_stream(double, my_stream()),
#                            my_stream())
#     return Stream(1, compute_rest)

# yepp!!
# 1, 3, 9, 27

# def my_stream():
#     def compute_rest():
#         return add_streams(stream_filter(lambda x: x%2 == 0, my_stream()), 
#                            stream_map(lambda x: x+2, my_stream()))
# 
#     return Stream(2, compute_rest)

# yepp!
# 2, 6, 14, 30, 62

def stream_map(map_func, s):
    """
    >>> s = make_integer_stream()
    >>> m = stream_map(lambda x: x*2, s)
    """
    
    def make_mapped_rest():
        stream_map(map_func, s.rest)

    if s is Stream.empty:
        return s
    else:
        return Stream(map_func(s.first), make_mapped_rest)

# review 
# 1.
def unique(iterable):
    """
    >>> list(unique([1, 3, 2, 2, 5, 3, 4, 1]))
    [1, 3, 2, 5, 4]
    """
    seen = []
    while len(iterable) != 0:
        val = iterable.pop(0)
        if val not in seen:
            yield val
        seen.append(val)

# solution was:
def unique_2(iterable):
    observed = set()
    i = iter(iterable)
    while True:
        el = next(i)
        if el not in observed:
            observed.add(el)
            yield el


# 2. + 3. skipped, no more logic stuff

def move_disk(start, end):
    print("Move 1 disk from rod", start, "to rod", end)

def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi
    game if we start with n disks on the start pole and want
    to move them all to the end pole.
    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move 1 disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move 1 disk from rod 1 to rod 2
    Move 1 disk from rod 1 to rod 3
    Move 1 disk from rod 2 to rod 3
    """

    def _move(_n, _start, _middle, _end):
        if _n > 0:
            _move(_n-1, _start, _end, _middle)
            move_disk(_start, _end)
            _move(_n-1, _middle, _start, _end) 

    return _move(n, start, 6-start-end, end) 

#Solution:
#    if n > 0:
#        tmp = 6 - start - end
#        towers_of_hanoi(n-1, start, tmp)
#        move_disk(start, end)
#        towers_of_hanoi(n-1, tmp, end)
# 
