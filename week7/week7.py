# def sumTo(n):
#      return n*(n+1)/2
#
#
# print(sumTo(10))
#
# n = int(input("Enter a number: "))
# print("sum is",sumTo(n))

# import turtle
# def drawStar(t,n,size):
#     angle = 180-180/n
#     for i in range(n):
#         turtle.forward(size)
#         turtle.right(angle)
#
# wn = turtle.Screen()
# t= turtle.Turtle()
# t.pensize(3)
# drawStar(t,11,100)
# wn.exitonclick()

# def sumTo(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total
# print(sumTo(10))
# n = int(input("Enter a number: "))
# print("Sum is",sumTo(n))


# import math
# def mySqrt(x):
#     guess=x/2
#     for i in range (20):
#         guess=(1/2) * (guess + x/guess)
#     return guess
#
# n=int(input("Enter a number: "))
# print("The result is", mySqrt(n))
# print("The result is",math.sqrt(n))


# import turtle
# def drawTip(t,size):
#     t.begin_fill()
#     t.left(90)
#     t.forward(size/2)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size/2)
#     t.right(90)
#     t.end_fill()
#
# def drawSpriteWithTips(someturtle,legs,length):
#     angle = 360/legs
#     for i in range(legs):
#         someturtle.forward(length)
#         drawTip(someturtle,10)
#         someturtle.backward(length)
#         someturtle.left(angle)
#
# def fancySquare(t,size):
#     for i in range(4):
#         drawSpriteWithTips(t,8,20)
#         t.forward(size)
#         t.left(90)
#
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
# t.color("pink")
# t.speed(6)
# t.pensize(3)
# fancySquare(t,100)
# wn.exitonclick()


def PositiveorNot(x):
    if x > 0:
        return "Positive"
    elif x == 0:
        return "Zero"
    else:
        return "Negative"

numbers=[-7,5,0]
for i in numbers:
    print(PositiveorNot(i))
x=int(input("Enter a number: "))
print(PositiveorNot(x))