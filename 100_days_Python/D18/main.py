from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
tim.color('green4')
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(90)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(90)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(90)
# timmy_the_turtle.right(90)
# To draw a simple square using for loop.
for i in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()