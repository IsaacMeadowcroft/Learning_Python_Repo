import doctest

def swap_list(lst, i, j):
    """(list, int, int) -> None
    >>> l = [1,2,3]
    >>> swap_list(l, 0, 1)
    >>> l
    [2, 1, 3]
    """
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp

def shift_list(lst):
    """(list) -> None
    >>> l = [1,2,3]
    >>> shift_list(l)
    >>> l
    [3, 1, 2]
    """ 
    tmp = lst[len(lst)-1]
    lst[:]=lst[0:len(lst)-1]
    lst[0:0]=[tmp]

if __name__ == "__main__":
    print(doctest.testmod())
    
    
    
    
