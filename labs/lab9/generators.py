def generator():
    i = 0
    while i < 6:
        yield i
        i += 1

def generator_verbose():
    print("Starting here")
    i = 0
    while i < 6:
        print("Before yield")
        yield i
        print("After yield")
        i += 1


# >>> g = generator()
# >>> g
# _a generator object__ # what is this thing?
# >>> g.__iter__()
# _same output as above, generator object__
# >>> g.__next__()
# ___it's iterating ;-)
# >>> g.__next__()
# ___... one more time_

class IterGen(object):
    def __init__(self):
        self.start = 5

    def __iter__(self):
        while self.start < 10:
            self.start += 1
            yield self.start


# why is this working:
# The for loop only expects the object returned by __iter__ to have a __next__ method, and the __iter__ method is a generator function in this case. Therefore, when __iter__ is called, it returns a generator object, which you can call __next__ on.
