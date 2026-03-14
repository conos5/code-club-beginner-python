# === TURTLE ARENA ===
# Set up a game arena and practice moving our turtle around!
import turtle

# Border size — change this number to fit your screen!
BORDER = 150

# Step 1: Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Arena")

# Step 2: Draw the arena border using a for loop
border = turtle.Turtle()
border.color("white")
border.speed(0)
border.penup()
border.goto(-BORDER, BORDER)
border.pendown()
for i in range(4):
    border.forward(BORDER * 2)
    border.right(90)
border.hideturtle()

# Step 3: Create our player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("lime")
player.penup()

# Step 4: Move the player around — xcor() and ycor() tell us where it is
player.goto(300, 100)
print(f"Player is at x: {player.xcor()}, y: {player.ycor()}")
if player.xcor() < BORDER:
    print("Within Right wall!")
else:
    print("Outside Right wall!")

player.goto(-50, -100)
print(f"Player is at x: {player.xcor()}, y: {player.ycor()}")

if player.ycor() > -1*BORDER:
    print("Within Bottom wall!")
else:
    print("Outside Bottom wall!")

# Step 6: Move to a safe spot in the center
player.goto(0, 0)
print(f"Player is safe at ({player.xcor()}, {player.ycor()})")

turtle.done()
