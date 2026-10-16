# import random
#
# for i in range(10):
#     print(random.random())
#
# for i in range(10):
#     print(random.randint(25, 35))
#
# import math
# hypotenuse = math.hypot(4, 3)
# print(hypotenuse)
#
# def areaofCircle(radius):
#     return math.pi * radius * radius
# print(areaofCircle(5))
#
# import turtle
# def drawStar (t, side):
#     for i in range(5):
#         t.forward(100)
#         t.right(144)
# screen = turtle.Screen()
# tess = turtle.Turtle()
# drawStar(tess, 100)
# screen.exitonclick()

import turtle
def drawSquare(t, side):
    for i in range (4):
        t.forward(side)
        t.left(90)
# tess = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# tess.color("red")
# tess.pensize(3)
# for i in range(5):
#     drawSquare(tess, 20)
#     tess.penup()
#     tess.forward(40)
#     tess.pendown()
# screen.exitonclick()

screen = turtle.Screen()
tess = turtle.Turtle()
screen.bgcolor("lightgreen")
tess.color("red")
tess.pensize(3)

for i in range (20,120,20):
    drawSquare(tess, i)
    tess.penup()
    tess.backward(10)
    tess.right(90)
    tess.forward(10)
    tess.left(90)
    tess.pendown()
screen.exitonclick()