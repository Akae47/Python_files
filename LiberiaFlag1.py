
# File: LiberiaFlag.py
# Student: Akwawo Ekpu
# UT EID: ace2453
# Course Name: CS303E
# 
# Date: 04/14/2023
# Description of Program: This is a code that uses the turtle class to draw the liberian flag.

import turtle

turtle.colormode(255)

myBlue = (0, 32, 91)
myRed = (191, 13, 62)
white = (255, 255, 255)


def drawRectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setheading(0)
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def drawStar(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setheading(0)
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
        turtle.left(72)
    turtle.end_fill()


turtle.setup(836, 440)
turtle.speed(0)
turtle.hideturtle()


turtle.pensize(3)


stripeWidth = 440 / 11
for i in range(11):
    if i % 2 == 0:
        drawRectangle(-418, 200 - i*stripeWidth, 836, stripeWidth, myRed)
    else:
        drawRectangle(-418, 200 - i*stripeWidth, 836, stripeWidth, white)



drawRectangle(-418, 40, 200,200, myBlue)


starSize = 60
starX = -300
starY = 160
drawStar(starX, starY, starSize, white)


turtle.done()
