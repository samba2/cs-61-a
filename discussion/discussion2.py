
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

def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(59)
    True
    >>> is_prime(60)
    False
    """

    assert n > 1

    cnt_down = n - 1

    while cnt_down > 1:
        if n % cnt_down == 0:
            return False

        cnt_down = cnt_down - 1

    return True



# weiter bei 2.2 iteration        
