import turtle
screen = turtle.Screen()
screen.bgcolor("yellow")
screen.setup(width=800, height=800)

t = turtle.Turtle()
t.shape("arrow")
t.color("black")
t.speed(2)

dash_length = 20
gap_length = 10
total_length = 300

x = -total_length // 2  

t.penup()
t.goto(x, 0)

drawn = 0
while drawn < total_length:
    t.pendown()
    t.forward(dash_length)
    drawn += dash_length

    t.penup()
    t.forward(gap_length)
    drawn += gap_length

turtle.done()
