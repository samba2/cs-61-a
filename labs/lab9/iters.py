class AnIterator(object):
    def __init__(self):
        self.current = 0

    def __next__(self):
        if self.current >= 5:
            raise StopIteration
        self.current += 1
        return self.current

    def __iter__(self):
        return self

class IteratorA(object):
    def __init__(self):
        self.start = 5

    def __next__(self):
        if self.start == 100:
            raise StopIteration
        self.start += 5
        return self.start

    def __iter__(self):
        return self

class IteratorB(object):
    def __init__(self):
        self.start = 5

    #*** my code ***, __next__ method was missing
    def __next__(self):
        if self.start == 100:
            raise StopIteration
        self.start += 5
        return self.start

    def __iter__(self):
        return self

class IteratorC(object):
    def __init__(self):
        self.start = 5

    def __next__(self):
        if self.start == 10:
            raise StopIteration
        self.start += 1
        return self.start

    # has to be implemented, purpuse still not clear
    # would __next__ not be enough to indicate that this is an iterator?
    def __iter__(self):
        return self

class IteratorD(object):
    def __init__(self):
        self.start = 1

    # stop exception was missing
    def __next__(self):
        if self.start == 1000:
            raise StopIteration
        self.start += 1
        return self.start

    def __iter__(self):
        return self

