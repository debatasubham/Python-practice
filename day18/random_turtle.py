import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Random Turtle Walk")
screen.setup(width=800, height=800)

t = turtle.Turtle()
t.speed(5)
t.width(3)
t.shape("turtle")

colors = [
    "red", "orange", "yellow", "lime", "cyan",
    "deepskyblue", "violet", "hotpink", "white",
    "gold", "springgreen", "coral", "aquamarine", "magenta"
]

steps = 50

for _ in range(steps):
    t.color(random.choice(colors))

    t.forward(random.randint(10, 50))

    t.right(random.randint(-180, 180))

    x, y = t.xcor(), t.ycor()
    if x > 380:
        t.setx(-380)
    elif x < -380:
        t.setx(380)
    if y > 330:
        t.sety(-330)
    elif y < -330:
        t.sety(330)

t.hideturtle()
turtle.done()
