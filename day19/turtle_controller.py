import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Controller | W=Forward  S=Backward  A=Left  D=Right  C=Clear")
screen.setup(width=800, height=700)

t = turtle.Turtle()
t.shape("turtle")
t.color("lime")
t.speed(0)
t.width(2)

move_speed = 20   # pixels per key press
turn_speed = 15   # degrees per key press

def move_forward():
    t.forward(move_speed)

def move_backward():
    t.backward(move_speed)

def turn_left():
    t.left(turn_speed)

def turn_right():
    t.right(turn_speed)

def clear_drawing():
    t.clear()
    t.home()          # return to center
    t.setheading(90)  # face up

# Bind keys
screen.listen()
screen.onkey(move_forward,  "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left,     "a")
screen.onkey(turn_right,    "d")
screen.onkey(clear_drawing, "c")

# Also bind uppercase just in case
screen.onkey(move_forward,  "W")
screen.onkey(move_backward, "S")
screen.onkey(turn_left,     "A")
screen.onkey(turn_right,    "D")
screen.onkey(clear_drawing, "C")

# Display controls on screen
label = turtle.Turtle()
label.hideturtle()
label.penup()
label.color("gray")
label.goto(0, -320)
label.write(
    "W = Forward   S = Backward   A = Counter-Clockwise   D = Clockwise   C = Clear",
    align="center",
    font=("Arial", 11, "normal")
)

screen.mainloop()
