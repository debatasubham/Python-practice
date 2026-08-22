import turtle
import random
import time

# ── Screen Setup ──────────────────────────────────────────────
screen = turtle.Screen()
screen.bgcolor("darkgreen")
screen.title("🐢 Turtle Race – Place Your Bet!")
screen.setup(width=900, height=600)
screen.tracer(0)

# ── Config ────────────────────────────────────────────────────
COLORS      = ["red", "orange", "yellow", "cyan", "hotpink"]
NAMES       = ["Red", "Orange", "Yellow", "Cyan", "Pink"]
NUM_TURTLES = 5
START_X     = -380
FINISH_X    = 360
Y_POSITIONS = [-160, -80, 0, 80, 160]

# ── Draw Track ────────────────────────────────────────────────
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(5)

# Track lanes
for y in Y_POSITIONS:
    pen.goto(START_X, y - 30)
    pen.pendown()
    pen.color("white")
    pen.pensize(1)
    pen.goto(FINISH_X + 20, y - 30)
    pen.penup()

# Finish line
pen.pensize(4)
pen.color("white")
pen.goto(FINISH_X, -200)
pen.pendown()
pen.goto(FINISH_X, 200)
pen.penup()

# Finish label
pen.goto(FINISH_X, 205)
pen.color("white")
pen.write("FINISH", align="center", font=("Arial", 13, "bold"))

# Start line
pen.pensize(3)
pen.color("yellow")
pen.goto(START_X, -200)
pen.pendown()
pen.goto(START_X, 200)
pen.penup()

# Title
pen.goto(0, 250)
pen.color("gold")
pen.write("🐢  TURTLE RACE  🐢", align="center", font=("Arial", 22, "bold"))

# Color labels on left
for i, (name, color, y) in enumerate(zip(NAMES, COLORS, Y_POSITIONS)):
    pen.goto(START_X - 10, y - 10)
    pen.color(color)
    pen.write(name, align="right", font=("Arial", 11, "bold"))

screen.update()

# ── Create Racing Turtles ─────────────────────────────────────
racers = []
for i, (color, y) in enumerate(zip(COLORS, Y_POSITIONS)):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color)
    t.penup()
    t.goto(START_X, y)
    t.setheading(0)
    t.shapesize(1.2, 1.2)
    racers.append(t)

screen.update()

# ── Get Bet ───────────────────────────────────────────────────
color_options = ", ".join(NAMES)
bet = screen.textinput(
    "🎲 Place Your Bet!",
    f"Which turtle will win?\nChoose: {color_options}"
)

if bet is None:
    turtle.bye()
    exit()

bet = bet.strip().capitalize()

# Validate bet
if bet not in NAMES:
    pen.goto(0, 0)
    pen.color("white")
    pen.write(f"Invalid colour '{bet}'! Valid: {color_options}", align="center",
              font=("Arial", 13, "normal"))
    screen.update()
    time.sleep(3)
    turtle.bye()
    exit()

# Confirm bet on screen
pen.goto(0, 220)
pen.color("white")
pen.write(f"Your bet: {bet}  |  Good luck! 🍀", align="center",
          font=("Arial", 13, "italic"))
screen.update()
time.sleep(1)

# ── Race! ─────────────────────────────────────────────────────
winner = None
while winner is None:
    for i, t in enumerate(racers):
        step = random.randint(1, 10)
        t.forward(step)

        if t.xcor() >= FINISH_X:
            winner = NAMES[i]
            winner_color = COLORS[i]
            break

    screen.update()

# ── Result ────────────────────────────────────────────────────
# Result banner
result_pen = turtle.Turtle()
result_pen.hideturtle()
result_pen.penup()

# Background box
result_pen.goto(-250, -50)
result_pen.color("black")
result_pen.begin_fill()
for _ in range(2):
    result_pen.forward(500)
    result_pen.left(90)
    result_pen.forward(120)
    result_pen.left(90)
result_pen.end_fill()

result_pen.goto(0, 20)

if bet == winner:
    result_pen.color("gold")
    result_pen.write(f"🏆  YOU WIN!  🏆", align="center", font=("Arial", 26, "bold"))
    result_pen.goto(0, -20)
    result_pen.color("lime")
    result_pen.write(f"{winner} turtle won — just as you predicted! 🎉",
                     align="center", font=("Arial", 14, "normal"))
else:
    result_pen.color("red")
    result_pen.write(f"😢  YOU LOSE!", align="center", font=("Arial", 26, "bold"))
    result_pen.goto(0, -20)
    result_pen.color("white")
    result_pen.write(f"{winner} turtle won, but you bet on {bet}.",
                     align="center", font=("Arial", 14, "normal"))

screen.update()
screen.mainloop()
