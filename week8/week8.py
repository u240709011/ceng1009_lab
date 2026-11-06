def gradeMark(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"
marks=[95,90,89.9,80,79.9,70,65,60,59]
for mark in marks:
    print(gradeMark(mark))

your_mark=input("Enter your mark: ")
print(gradeMark(your_mark))






import turtle


def choseColor(height):
    if height>=200:
        return "red"
    elif height>=100:
        return "yellow"
    else:
        return "green"


def drawBar(t, height,gap):
    t.penup()
    t.left(90)
    t.forward(height+gap)
    t.write(" "+str(height))
    t.backward(height+gap)
    t.right(90)
    t.pendown()
    t.fillcolor(choseColor(height))
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


def barChart(data):
    max_height = max(data)
    num_bars = len(data)
    border = 10
    gap = (max_height + border) / 25
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    right = 40 * num_bars + border
    top = max_height + 4 * border
    wn.setworldcoordinates(-border, -border, right, top)
    t = turtle.Turtle()
    t.color("blue")
    t.pensize(3)
    for height in data:
        drawBar(t, height,gap)

    wn.exitonclick()

data=[48, 117, 200, 240, 160, 260, 220]
barChart(data)





import turtle


def choseColor(height):
    if height>=200:
        return "red"
    elif height>=100:
        return "yellow"
    else:
        return "green"


def drawBar(t, height,gap):
    if(height>=0):
        labelY = height+gap
    else:
        labelY = gap
    t.penup()
    t.left(90)
    t.forward(labelY)
    t.write(" "+str(height))
    t.backward(labelY)
    t.right(90)
    t.pendown()
    t.fillcolor(choseColor(height))
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


def barChart(data):
    max_height = max(data)
    min_height = min(data)
    num_bars = len(data)
    border = 10
    gap = (max_height + border) / 25
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    right = 40 * num_bars + border
    top = max_height + 4 * border
    bottom= min(min_height ,0)-border
    wn.setworldcoordinates(-border, bottom, right, top)
    t = turtle.Turtle()
    t.color("blue")
    t.pensize(3)
    for height in data:
        drawBar(t, height,gap)

    wn.exitonclick()

data=[48, 117, -60, 240, 160, -110, 220]
barChart(data)

import math
def findHypot(side,side2):
    return math.sqrt(side**2+side2**2)
print(findHypot(5,12))