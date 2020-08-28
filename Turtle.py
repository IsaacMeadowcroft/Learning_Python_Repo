import turtle

def make_square(side_length, my_turtle, num_sides):
    for i in range(num_sides):
        my_turtle.fd(side_length)
        my_turtle.left(360-180/num_sides)

side_length = int(input("Please input the length og each side of the polygon: "))
num_sides = int(input("Please input the number of sides on the polygon: ") 
t = turtle.Turtle()
make_square(side_length,t,num_sides)
