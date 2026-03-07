import turtle
import random
import time

#finish line
finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(200, 100)
finish_line.pendown()
finish_line.right(90)
finish_line.forward(200)
finish_line.hideturtle()

# turtle creation
geoff = turtle.Turtle()
bob = turtle.Turtle()

geoff.color("red")
geoff.penup()
geoff.goto(-100, 50)
geoff.pendown()

bob.color("blue")
bob.penup()
bob.goto(-100, -50)
bob.pendown()

#turtle racing
for turn in range(10):
    geoff_roll = random.randint(1,6)
    bob_roll = random.randint(1,6)
    geoff.forward(geoff_roll * 10)
    bob.forward(bob_roll * 10)
    time.sleep(1)

    if geoff.xcor() >= 200:
        print("Geoff crossed the finish line")
        break
    if bob.xcor() >= 200:
        print("Bob crossed the finish line")
        break


