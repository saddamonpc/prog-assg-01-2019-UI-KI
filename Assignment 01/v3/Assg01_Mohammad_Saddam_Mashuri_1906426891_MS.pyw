# -*- coding: utf-8 -*-
## Created on Tue Sep 17 21:49:55 2019
## Completed on Tue Sep 19 23:49:00 2019
## Edit (Sun Sep 22 19 15:29:00 2019): Simplify comments and code lines. 

## Author: Mohammad Saddam Mashuri
## File name: Assg01_Mohammad_Saddam_Mashuri_1906426891_MS.pyw
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

# Get the value of side length of the first square from User. Minimum = 20. Maximum = 60.
sideLength = int(turtle.numinput("Rotating Colorful Squares and Disks", \
                                       "Please enter the side-length of the first square [20 - 60]", \
                                       minval = 20, maxval = 60))

# Get the value of the amount of squares wanted by the User from User. Minimum = 10. Maximum = 72.
squareAmount = int(turtle.numinput("Rotating Colorful Squares and Disks", \
                                   "Please enter the amount of squares wanted to be drawn [10 - 72]", \
                                   72, minval = 10, maxval = 72))

# Get the value of the amount of circles wanted by the User from User. Minimum = 10. Maximum = 36.
circleAmount = int(turtle.numinput("Rotating Colorful Squares and Disks", \
                                   "Please enter the amount of circles wanted to be drawn [10 - 36]", \
                                   36, minval = 10, maxval = 36))

# Get the value of drawing speed from User. Minimum = 1. Maximum = 11.
drawSpeed = int(turtle.numinput("Rotating Colorful Squares and Disks", \
                                   "How fast do you want it to be drawn? [1 - 11]", \
                                   8, minval = 1, maxval = 11))
# Set turtle drawing speed from User's input
turtle.speed(drawSpeed)

# Change turtle colormode and screenmode to 255
turtle.colormode(255)

# Random color function
def getRandomColor():
    r = random.randrange(0, 257, 10)
    g = random.randrange(0, 257, 10)
    b = random.randrange(0, 257, 10)
    turtle.color(r, g, b)

# Draw a random colored square function
def drawSquare():
    turtle.begin_fill()
    for i in range(2):              # Repeat the following statements twice.
        turtle.forward(sideLength)
        turtle.right(90)
        turtle.forward(sideLength)
        turtle.right(90)
    turtle.end_fill()

# Draw a random colored circle function
def drawCircle():
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

# Draw and rotate user's amount of squares filled with random color
for squares in range(squareAmount): # Repeat the following statements according to the user's input from line 29.
    getRandomColor()                # Recall "Random color function".
    drawSquare()                    # Recall "Draw a random colored square function", from line 29.
    turtle.right(5)                 # Rotate cursor to the right by 5 degrees.
    sideLength += 2		    # Increment square side length by 2 units.

# Move the turtle to a new location at the right side
# of the turtle window and set its heading to 0
turtle.up()
turtle.goto(250, 0)
turtle.setheading(0)
turtle.down()

# Draw and rotate user's amount of circles filled with random color
for circles in range(circleAmount): # Repeat the following statements according to the user's input from line 34.
    getRandomColor()                # Recall "Random color function".
    drawCircle()                    # Recall "Draw a random colored circle function", from line 34.
    turtle.left(10)                 # Rotate cursor to the left by 10 degrees.
    sideLength -= 2		    # Decrement circle radius by 2 units.

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
