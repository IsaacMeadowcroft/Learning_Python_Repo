import doctest

def is_a_vowel(char):
    """(char) -> bool
    >>> is_a_vowel('o')
    True
    >>> is_a_vowel('j')
    False
    >>> is_a_vowel('string')
    Not a character
    """
    if(len(char)!=1):
        print("Not a character")
    else:
        if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='y'):
            return True
        else:
            return False

def count_vowels(string):
    count=0
    for i in range(len(string)):
        cur=is_a_vowel(string[i])
        if(cur):
            count+=1
    return count

def remove_duplicates(s):
    string=""
    for i,char in enumerate(s):
        if(char not in s[i+1:]):
            string+=char
    return string
            

if __name__ == "__main__":
    doctest.testmod()
    string = input("Please input a string: ")
    print("There are",count_vowels(string.lower()),"vowels in the input string")
