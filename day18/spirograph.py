import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Spirograph")
screen.setup(width=800, height=800)
screen.colormode(1.0)

screen.tracer(3, 0) 

t = turtle.Turtle()
t.speed(0)
t.width(1.5)
t.hideturtle()

num_circles = 72
radius = 300
angle_step = 360 / num_circles

for i in range(num_circles):
    hue = i / num_circles
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.color(r, g, b)

    t.circle(radius)

    t.right(angle_step)

    screen.update()

turtle.done()
