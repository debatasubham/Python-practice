import turtle
screen = turtle.Screen()
screen.title("Draw a Square")
screen.bgcolor("red")

t = turtle.Turtle()
t.shape("turtle")
t.color("yellow")
t.speed(3)

for _ in range(4):
    t.forward(100)   
    t.right(90)     

turtle.done()
t.exitonclick()