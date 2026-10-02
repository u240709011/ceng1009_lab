# width=input("Enter the width of the rectangle: ")
# height=input("Enter the height of the rectangle: ")
# areaofrectangle=float(width)*float(height)
# print("The area of the rectangle is",areaofrectangle)
import math

# drivenmiles=float(input("Enter the number of miles driven: "))
# gallons=float(input("Enter the number of gallons used: "))
# MPG=gallons/drivenmiles
# print("The MPG is: ",MPG)

# fahrenheit=float(input("Enter the degree of fahrenheit: "))
# convertedtocelcius=(fahrenheit-32)*5/9
# print(degreeofcelcius)

# firstday=int(input("enter first day"))
# length=int(input("enter length"))
# lastday=(firstday+length)%7
# print(lastday)

# radius=float(input("enter radius: "))
# circumference=2*math.pi*radius
# print(circumference)

# birth_year = int(input("Enter birth year: "))
# age=2024-birth_year
# print(age)

import turtle

t = turtle.Turtle()
a=float(input("enter the length of square "))
for _ in range(4):
    t.forward(a)
    t.right(90)

turtle.done()
