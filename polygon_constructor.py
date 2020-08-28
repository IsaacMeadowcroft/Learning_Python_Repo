import turtle

def make_polygon(side_length, my_turtle, num_sides):
    angle=360/num_sides
    for i in range(num_sides):
        my_turtle.fd(side_length)
        my_turtle.left(angle)

side_length = int(input("Please input the length og each side of the polygon: "))
num_sides = int(input("Please input the number of sides on the polygon: ") )
my_turtle = turtle.Turtle()
make_polygon(side_length,my_turtle,num_sides)
