# === MEET THE TURTLE ===
# Let's meet our turtle and see what it can do!
import turtle

# Step 1: Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Step 2: Create your turtle!
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")       # Makes it look like a turtle!
my_turtle.color("green")        # Try: "red", "blue", "purple", "orange"
my_turtle.shapesize(3)          # Try changing this number!

# Step 3: Give it a list of colors to walk through
colors = ["red", "blue", "green", "purple", "orange"]

# Step 4: Walk forward and change color each time
for i in range(5):
    my_turtle.color(colors[i])
    my_turtle.stamp()            # Leaves a mark where it stands
    my_turtle.forward(80)        # Try changing this number!

turtle.done()
