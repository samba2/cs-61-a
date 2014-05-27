"""Starter file for Dictionaries lab."""

def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of
    successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> #table
    #{'catch': ['bad'], '.': ['We'], 'bad': ['guys'], ',': ['catch'], 'and': ['to'], 'investigate': [','], 'pie': ['.'], 'We': ['came'], 'to': ['investigate', 'eat'], 'guys': ['and'], 'eat': ['pie'], 'came': ['to']}
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev in table:
            "***YOUR CODE HERE ***"
            table[ prev ].append( word )
        else:
            "***YOUR CODE HERE ***"
            table[ prev ] = [word]
        prev = word
    return table

def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> construct_sent( 'eat', table )
    ' eat pie .'
    """
    import random
    result = ' '
    while word not in ['.', '!', '?']:
        "***YOUR CODE HERE ***"
        result = result + word + ' '
        word = random.choice(table[word])

    return result + word

def shakespeare_tokens(path = 'shakespeare.txt', url = 'http://goo.gl/SztLfX'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

def random_sent():
    import random
    # start random sentence with a first word of a sentence ( key is "." as previous 'word' )
    return construct_sent(random.choice(table['.']), table)

tokens = shakespeare_tokens()
table = build_successors_table(tokens)
print(random_sent())
