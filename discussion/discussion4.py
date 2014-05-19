
# uses a tuple
def make_city(name, lat, lon):
    return (name, lat, lon)

def get_name(city):
    """
    >>> city = make_city( "Leipzig", 12, 20 )
    >>> get_name( city )
    'Leipzig'
    """
    return city[0]

def get_lat(city):
    """
    >>> city = make_city( "Leipzig", 12, 20 )
    >>> get_lat( city )
    12
    """
    return city[1]

def get_lon(city):
    """
    >>> city = make_city( "Leipzig", 12, 20 )
    >>> get_lon( city )
    20
    """
    return city[2]

from math import sqrt
def distance(city1, city2):
    lat_1, lon_1 = get_lat(city_1), get_lon(city_1)
    lat_2, lon_2 = get_lat(city_2), get_lon(city_2)
    return sqrt((lat_1 - lat_2)**2 + (lon_1 - lon_2)**2)

def closer_city(lat, lon, city1, city2):
    my_position = make_city( "my position", lat, lon )
    distance1= distance( my_position, city1 )
    distance2= distance( my_position, city2 )

    if distance1 <= distance2:
        return get_name( city1 )
    else:
        return get_name( city2 )


############################

from fractions import gcd

def make_rat(n, d):
    g = gcd(n, d)
    return n//g, d//g

def numer(r):
    return r[0]

def denom(r):
    return r[1]

def add_rat(x, y):
    """The sum of rational numbers X and Y.
    >>> x = make_rat(1,2)
    >>> y = make_rat(1,2)
    >>> add_rat(x,y)
    (1, 1)
    """
    return make_rat(numer(x) * denom(y) + numer(y) * denom(x), denom(x) * denom(y))

def mul_rat(x, y):
    """The product of rational numbers X and Y."""
    return make_rat(numer(x) * numer(y), denom(x) * denom(y))

def eq_rat( x, y ):
    """
    >>> x = make_rat(1,2)
    >>> y = make_rat(2,4)
    >>> z = make_rat(2,5)
    >>> eq_rat(x,y)
    True
    >>> eq_rat(x,z)
    False
    """
    
    a = make_rat( numer(x), denom(x) )
    b = make_rat( numer(y), denom(y) )

    if numer(a) == numer(b) and denom(a) == denom(b):
        return True

    return False


from math import pow
def rational_pow(x, e):
    """
    >>> rational_pow( make_rat(5, 3), 3 )
    (125, 27)
    """
    return make_rat( int(pow(numer(x), e)), int(pow(denom(x), e)) )

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def approx_e(iter=100):
    """
    >>> approx_e()
    2.718281828459045
    """

    e = make_rat( 1, factorial(0) )
    i = 1

    while i <= 100:
        tmp = make_rat(1, factorial(i))
        e = add_rat(e, tmp)
        i+=1

    return numer(e) / denom(e)

def inverse_rational(x):
    """Returns the inverse of the given non-zero rational number"""

    return make_rat( denom(x), numer(x) )

def div_rationals(x, y):
    """Returns x / y for given rational x and non-zero rational y
    >>> x = make_rat(1,2)
    >>> y = make_rat(3,4)
    >>> div_rationals(x,y)
    (2, 3)
    """
    return mul_rat(x, inverse_rational(y) )

###################################################

def make_unit(catchphrase, damage):
    return ( catchphrase, damage )

def get_catchphrase(unit):
    return unit[0]

def get_damage(unit):
    """
    a = make_unit( 'zerg', 12 )
    get_catchphrase(a)
    'zerg'
    get_damage(a)
    12
    """
    return unit[1]

def battle(first, second):
    """Simulates a battle between the first and second unit
    >>> zealot = make_unit('My life for Aiur!', 16)
    >>> zergling = make_unit('GRAAHHH!', 5)
    >>> winner = battle(zergling, zealot)
    GRAAHHH!
    My life for Aiur!
    >>> winner is zealot
    True
    """

    print(get_catchphrase(first))
    print(get_catchphrase(second))

    if get_damage(first) >= get_damage(second):
        return first
    else:
        return second

def make_resource_bundle_func(minerals, gas):

    def dispatch( selector ):
        if selector == 'minerals':
            return minerals
        elif selector == 'gas':
            return gas
    return dispatch

def get_minerals_func(bundle):
    return bundle('minerals')

def get_gas_func(bundle):
    """
    >>> a = make_resource_bundle(10, 20)
    >>> get_minerals(a)
    10
    >>> get_gas(a)
    20
    """
    return bundle('gas')

def make_resource_bundle(minerals, gas):
    return ( minerals, gas )

def get_minerals(bundle):
    return bundle[0]

def get_gas(bundle):
    """
    >>> a = make_resource_bundle(10, 20)
    >>> get_minerals(a)
    10
    >>> get_gas(a)
    20
    """
    return bundle[1]

def make_building(unit, bundle):
    return ( unit, bundle )

def get_unit(building):
    return building[0]

def get_bundle(building):
    """
    >>> u = make_unit(11,22)
    >>> r = make_resource_bundle(30, 40)
    >>> building = make_building( u, r)
    >>> get_gas(get_bundle(building))
    40
    """
    return building[1]

def build_unit(building, bundle):
    """Constructs a unit if given the minimum amount of resources.
    Otherwise, prints an error message
    >>> barracks = make_building(make_unit('Go go go!', 6), make_resource_bundle(50, 0)) 
    >>> marine = build_unit(barracks, make_resource_bundle(20, 20))
    We require more minerals!
    >>> marine = build_unit(barracks, make_resource_bundle(50, 0))
    >>> print(get_catchphrase(marine))
    Go go go!
    """

    if get_minerals( get_bundle(building) ) > get_minerals( bundle ):
        print('We require more minerals!')
        return

    if get_gas( get_bundle(building) ) > get_gas( bundle ):
        print('We require more gas!')
        return

    return get_unit(building)

