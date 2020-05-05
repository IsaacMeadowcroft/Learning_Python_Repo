import doctest

def is_prime(num):
    """(num) -> bool
    >>> is_prime(17)
    True
    >>> is_prime(20)
    False
    """
    if(num<2):
        return False
    for i in range(2,int(num/2)+1):
        if(num%i==0):
            return False
    return True

def first_n_primes(n):
    """(num) -> None
    >>> first_n_primes(5)
    2 3 5 7 11 
    """
    count=0
    i=2
    while(count<n):
        if(is_prime(i)):
            print(i,end=" ")
            count+=1
        i+=1

if __name__ == "__main__":
    doctest.testmod()
    print("This program takes as input n and calculates the first n primes.")
    n=int(input("Please input an integer number n: "))
    first_n_primes(n)
    
    
