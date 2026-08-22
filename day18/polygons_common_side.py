import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Polygons with One Common Side")
screen.setup(width=800, height=800)

t = turtle.Turtle()
t.speed(5)
t.width(2)

side_length = 100

shapes = [
    (3,  "Triangle",  "red"),
    (4,  "Square",    "orange"),
    (5,  "Pentagon",  "yellow"),
    (6,  "Hexagon",   "lime"),
    (7,  "Heptagon",  "cyan"),
    (8,  "Octagon",   "deepskyblue"),
    (9,  "Nonagon",   "violet"),
    (10, "Decagon",   "hotpink"),
]

start_x = -side_length / 2
start_y = -150

for sides, name, color in shapes:
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(0)        
    t.color(color)
    t.pendown()

    for _ in range(sides):
        t.forward(side_length)
        t.left(360 / sides) 

t.penup()
t.goto(start_x, start_y)
t.setheading(0)
t.color("white")
t.width(4)
t.pendown()
t.forward(side_length)

t.penup()
t.goto(start_x + side_length / 2, start_y - 25)
t.color("white")
t.write("Common Side", align="center", font=("Arial", 12, "bold"))

t.hideturtle()
turtle.done()
