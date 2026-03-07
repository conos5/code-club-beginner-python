import turtle

turtle = turtle.Turtle()

# johnny.color("cyan")
turtle.shape("arrow")
turtle.color("red")
turtle.speed(5)

colors = ["deeppink", "blue", "green", "purple"]
#square
for side in range(4):
    turtle.forward(100)
    turtle.left(90)
    turtle.color(colors[side])

#triangle
turtle.left(90)
turtle.forward(100)

turtle.right(45)
turtle.forward(70)

turtle.right(90)
turtle.forward(70)

turtle.hideturtle()

