import sys

def func(farenheit):
    celsius = round((farenheit-32.0)*(5.0/9.0),2)
    print(str(farenheit)+" farenheit is equivalent to "+str(celsius)+" celsius")
    return celsius

func(float(sys.argv[0]))
#func(85)
