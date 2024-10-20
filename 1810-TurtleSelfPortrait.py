#https://education.launchcode.org/lchs/appendices/turtles/turtle-properties.html
#https://docs.python.org/3/library/turtle.html

from random import randint
import turtle

window = turtle.Screen() #Create a new window
window.setup(500, 500)


timmy = turtle.Turtle() #Create a new turtle called timmy
timmy.pensize(5)
timmy.color('black', 'pink')
timmy.shape("turtle")

timmy.begin_fill()
for loopCounter in range(randint(10,20)):
  timmy.forward(randint(50,100))
  timmy.right(randint(50,100))
timmy.end_fill()
window.exitonclick()