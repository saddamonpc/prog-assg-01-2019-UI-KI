# -*- coding: utf-8 -*-
## Created on Tue Sep 17 21:49:55 2019
## Completed on

## Author: Mohammad Saddam Mashuri
## File name: Assg01_Mohammad_Saddam_Mashuri_1906426891_MS.py
## Assignment 1:
## Using turtle to draw rotating squares and disks with random colors

# Import the module turtle
import turtle

# Import the module random
import random

# Make the drawing cursor a turtle.
turtle.shape("turtle")

# Make the window title to "Rotating Colorful Squares and Disks"
turtle.title("Rotating Colorful Squares and Disks")

# Get the value of side length of the first square from User
sideLength = int(turtle.numinput("Rotating Colorful Squares and Disks", \
                                       "Please enter the side-length of the first square [20 - 60]", \
                                       minval = 20, maxval = 60))

## ASK IF THIS IS ALLOWED
# Get the value of the amount of squares wanted by the User from User
squareAmount = int(turtle.numinput("Rotating Colorful Squares and Disks", \
                                   "Please enter the amount of squares wanted to be drawn [10 - 72]", \
                                   72, minval = 10, maxval = 72))

## ASK IF THIS IS ALLOWED
# Get the value of the amount of circles wanted by the User from User
circleAmount = int(turtle.numinput("Rotating Colorful Squares and Disks", \
                                   "Please enter the amount of circles wanted to be drawn [10 - 36]", \
                                   36, minval = 10, maxval = 36))

## ASK IF THIS IS ALLOWED
# Get the value of drawing speed from User
drawSpeed = int(turtle.numinput("Rotating Colorful Squares and Disks", \
                                   "How fast do you want it to be drawn? [1 - 11]", \
                                   8, minval = 1, maxval = 11))

# Set turtle drawing speed
turtle.speed(drawSpeed)

# Change turtle colormode and screenmode to 255
turtle.colormode(255)

# Defining a random color function
def getRandomColor():
    r = random.randrange(0, 257, 10)
    g = random.randrange(0, 257, 10)
    b = random.randrange(0, 257, 10)
    turtle.color(r, g, b)

# Defining drawing a square function
def drawSquare(sideLength):
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(sideLength)
        turtle.right(90)
        turtle.forward(sideLength)
        turtle.right(90)
    turtle.end_fill()

# Defining drawing a circle function
def drawCircle(circleAmount):
    circleRadius = sideLength // 2
    turtle.begin_fill()
    turtle.circle(circleRadius)
    turtle.end_fill()

# Move the turtle to a new location at the left side
# of the turtle window and set its heading to 0
turtle.up()
turtle.goto(-250, 0)
turtle.setheading(0)
turtle.down()

# Drawing a user's amount of squares filled with random color
for squares in range(squareAmount):
    getRandomColor()
    drawSquare(sideLength)
    turtle.right(5)
    sideLength += 2

# Move the turtle to a new location at the right side
# of the turtle window and set its heading to 0
turtle.up()
turtle.goto(250, 0)
turtle.setheading(0)
turtle.down()

# Drawing a user's amount of circles filled with random color
for circles in range(circleAmount):
    getRandomColor()
    drawCircle(circleAmount)
    turtle.left(10)
    sideLength -= 2

# Make the turtle invisible
turtle.hideturtle()

# Message for user
turtle.up()
turtle.goto(0, -350)
turtle.down()
turtle.color("blue")
turtle.write("There are " + str(squareAmount) + " Squares and " \
             + str(circleAmount) + " Disks", \
             False, align = "center", font = ("Arial", 20, "normal"))

# Wait for user to click on the screen to exit
turtle.exitonclick()
# The end
