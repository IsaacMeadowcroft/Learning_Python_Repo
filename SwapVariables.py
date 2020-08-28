#A program that takes inputs
import doctest
#doctest.testmod()

def func():
    """ () -> noneType""" #docstring
    var1 = input("Please type in the value for var1: ")
    var2 = input("Please type in the value for var2: ")

    print("var1 =",var1,"and var2 =",var2)
    print("Doing the swap")

    temp = var1
    var1 = var2
    var2 = temp

    print("var1 =",var1,"and var2 =",var2)

func()

