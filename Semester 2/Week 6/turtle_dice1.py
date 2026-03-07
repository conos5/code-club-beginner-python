import turtle
import random
import time

#finish line
racer = turtle.Turtle()
racer.penup()
racer.goto(200, 100)
racer.pendown()
racer.right(90)
racer.forward(200)

#turtle racing
racer.color("red")
racer.penup()
racer.goto(-100, 0)
racer.pendown()
racer.left(90)
for turn in range(5):
    roll = random.randint(1,6)
    racer.forward(roll * 20)
    time.sleep(1)

# check if he won
if racer.xcor() >= 200:
    print("racer crossed the finish line")
else:
    print("racer did not cross the line")

