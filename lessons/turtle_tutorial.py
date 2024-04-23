from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(-200, -70)
leo.pendown()
leo.color("blue")

leo.begin_fill()
leo.color("blue")
leo.end_fill()

i: int = 0
while (i < 3):
    leo.forward(360)
    leo.left(120)
    i = i + 1

done()