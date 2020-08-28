import doctest

def cube(x):
    """ (num) -> num
    >>> cube(2)
    8
    >>> cube(3)
    27
    """
    return x*x*x

doctest.testmod()
cube(2)
