# === TURTLE EXPLORER ===
# Use the arrow keys to move your turtle around the arena!
# If you go past the edge, you wrap to the other side!
import turtle

# Border size — change this number to fit your screen!
BORDER = 280

# Step 1: Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Explorer")

# Step 2: Draw the arena border
border = turtle.Turtle()
border.color("black")
border.speed(0)
border.penup()
border.goto(-BORDER, BORDER)
border.pendown()
for i in range(4):
    border.forward(BORDER * 2)
    border.right(90)
border.hideturtle()

# Step 3: Create the player
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()

# Step 4: Movement functions
# setheading() points the turtle in a direction: 0=right, 90=up, 180=left, 270=down
def move_up():
    player.setheading(90)
    player.forward(20)
    # If the player goes past the top, wrap to the bottom
    if player.ycor() > BORDER:
        player.goto(player.xcor(), -BORDER)

def move_down():
    player.setheading(270)
    player.forward(20)
    if player.ycor() < -BORDER:
        player.goto(player.xcor(), BORDER)

def move_left():
    player.setheading(180)
    player.forward(20)
    if player.xcor() < -BORDER:
        player.goto(BORDER, player.ycor())

def move_right():
    player.setheading(0)
    player.forward(20)
    if player.xcor() > BORDER:
        player.goto(-BORDER, player.ycor())

# Step 5: Connect the arrow keys to our functions
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Step 6: Tell the screen to listen for key presses
screen.listen()

turtle.done()
