import doctest

def count_occurences(char,string):
    """(char) -> int
    >>> count_occurences('h',"hello")
    1
    >>> count_occurences('l',"hello")
    2
    >>> count_occurences('hello',"hello")
    Input is not a character
    """
    if(len(char)!=1):
        print("Input is not a character")
    else:
        count=0
        for c in string.lower():
            if(c==char):
                count+=1
        return count
    
if __name__ == "__main__":
    doctest.testmod()
    string=input("Please input a string: ")
    char=input("Please input a character: ")
    print("The character",char,"appears",count_occurences(char,string),"times in the string \""+string+"\".")
