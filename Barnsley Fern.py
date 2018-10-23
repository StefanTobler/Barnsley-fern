import turtle
import random

turtle.screensize(800, 800)
turtle.setworldcoordinates(-2.1820,0,2.6558,9.9983)

fred = turtle.Turtle()
fred.penup()
fred.goto(0,0)
fred.hideturtle()
fred.speed(0)

x = 0.0
y = 0.0
def newCords(x,y):
    rand = random.random()
    if rand <= .01:
        nextX = 0
        nextY = .16 * y
    elif rand <= .86:
        nextX = .85 * x + .04 * y
        nextY = -.04 * x + .85 * y + 1.6
    elif rand <= .93:
        nextX = .2 * x - .26 * y
        nextY = .23 * x + .22 * y + 1.6
    else:
        nextX = -.15 * x + .28 * y
        nextY = .26 * x + .24 * y + .44

    return nextX, nextY



while True:

    fred.goto(x,y)
    fred.pendown()
    fred.dot(2, (0,0,0))
    fred.penup()
    x, y = newCords(x,y)
