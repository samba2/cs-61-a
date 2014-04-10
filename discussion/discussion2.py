
def find_quartile(x):
    """
    >>> find_quartile(1)
    Q4
    >>> find_quartile(25)
    Q3
    >>> find_quartile(75)
    Q2
    >>> find_quartile(76)
    Q1
    """

    assert x >= 0
    assert x <= 100

    if x > 75:
        print("Q1")
    if x >= 50 and x <= 75:
        print("Q2")
    if x >= 25 and x < 50:
        print("Q3")
    if x < 25:
        print("Q4")

def find_quartile2(x):
    """
    >>> find_quartile2(1)
    Q4
    >>> find_quartile2(25)
    Q3
    >>> find_quartile2(75)
    Q2
    >>> find_quartile2(76)
    Q1
    """

    assert x >= 0
    assert x <= 100

    if x > 75:
        print("Q1")
    elif x >= 50 and x <= 75:
        print("Q2")
    elif x >= 25 and x < 50:
        print("Q3")
    else:    
        print("Q4")

# weiter bei 2.2 iteration        
