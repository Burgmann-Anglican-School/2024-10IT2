from random import randint
import turtle

def drawhead(X, Y, width, length, fill):
    draw.penup()
    draw.goto(X,Y)
    draw.pendown()

    if fill != "~":
        draw.color("black", fill)
        draw.begin_fill()

    for x in range(2):
        draw.forward(width)
        draw.right(90)
        draw.forward(length)
        draw.right(90)

    if fill != "N":
        draw.end_fill()

window = turtle.Screen()
window.setup(500,750)

draw = turtle.Turtle()
draw.pensize(2)
draw.speed(10)
draw.color("black", "yellow")

#X Y width length fillcolor
#hair
drawhead(-25,375,100,250, "Green")
#head
drawhead(-100,300,200,350, "#F9C192")
#eyes
drawhead(-75,275,60,75, "White")
drawhead(10,275,60,75, "White")
drawhead(-50,250,25,50, "#Purple")
drawhead(25,250,25,50, "Purple")
drawhead(-45,225,15,25, "Black")
drawhead(30,225,15,25, "Black")
#nose
drawhead(5,185,50,100, "~")
#mouth
drawhead(-50,50,200,50, "White")
#eyebrows
drawhead(-80,275,60,15, "Brown")
drawhead(15,275,60,15, "Brown")

window.exitonclick()