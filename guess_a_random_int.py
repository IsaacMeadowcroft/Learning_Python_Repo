import random

def guess_a_random_int(begin,end):
    print("The random integer is between",begin,"and",end,".")
    random_number = random.randrange(begin,end,1)
    guess=int(input("Guess what the random number is: "))
    while(guess!=random_number):
        if(guess>random_number):
            print("Guess was too high!")
        else:
            print("Guess was too low!")
        guess=int(input("Wrong!Guess again: "))
    print("Congratulations, you guessed the right number!")

guess_a_random_int(0,100)
        
