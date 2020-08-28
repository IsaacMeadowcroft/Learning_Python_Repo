import doctest

def print_multiples(n,m):
    """ (int, int) -> None
    >>> print_multiples(3, 5)
    3 6 9 12 15 
    >>> print_multiples(1, 2)
    1 2 
    """
    for i in range(m):
        print(n*(i+1), end=' ')

def print_mult_table(n, m):
    """ (int, int) -> None
    >>> print_mult_table(2, 3)
    1 2 3 
    2 4 6 
    """
    for i in range(n):
        for j in range(m):
            print((i+1)*(j+1), end=' ')
        print()
    
if __name__ == "__main__":
    doctest.testmod()
