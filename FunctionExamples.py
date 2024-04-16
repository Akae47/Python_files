# File: FunctionExamples.py
# Student: Akwawo Ekpu
# UT EID: ace2453
# Course Name: CS303E
# 
# Date Created: 02/17/2023
# Description of Program: This is a program to run mathematical multiple functions.

import math 
def sum3Numbers (x, y, z):
    """Return the sum of the three parameters."""
    return x + y + z 

def multiply3Numbers( x, y, z ):
    """Return the product of three numbers."""
    return x * y * z

def sumUpTo3Numbers (x, y = 0, z = 0):
    """Return the sum of up to three parameters."""
    return x + y + z
    
def multiplyUpTo3Numbers (x, y = 1, z = 1):
    """Return the product of up to three parameters."""
    return x * y * z

def printInOrder( x, y ):
    """Return two parameters in acending order."""
    if x < y:
        print(x, y)
    else:
        print(y, x)

def areaOfSquare( side ):
    """Return area of square from length input."""
    if side > 0:
        return side ** 2
    else :
        print("Negative value entered")

def perimeterOfSquare( side ):
    """Return perimeter of square from length input."""
    if side> 0 :
        return 4 * side
    else:
        print("Negative value entered")

def areaOfCircle( radius ):
    """Return area of circle from radius input."""
    if radius > 0:
        return math.pi * (radius**2)
    else:
        print("Negative value entered")

def circumferenceOfCircle( radius ):
    """Return circumference of circle from radius input."""
    if radius > 0:
        return  2 * math.pi * radius
    else:
        print("Negative value entered")

def bothFactors( x, y, z):
    """Return True or False for factors of x."""
    if (z % x == 0) and (z % y == 0):
        return True
    else :
        return False

def squareAndCircle( x ):
    """Return area and circumference of a circle, and return the area and perimeter of square."""
    if x > 0:
        print("\nCircle wth radius", x,"has:")
        print("  Area: ",end="")
        area = math.pi * (x**2)
        print(area)
        print("  Circumference: ", end= '')
        circumference = 2 * math.pi * x
        print(circumference)
        print("Square with side" , x ,"has:")
        print("  Area: ",end ="")
        areaOfSquare = x ** 2
        print(areaOfSquare)
        print("  Perimeter: ", end='')
        perimeter = 4 * x
        print(perimeter,"\n")
        
    else :
        print("Negative value entered")

def factorial( x):
    """Return the factorial of x."""
    if x > 0:
        for i in range(1,x):
            x *= i
        return x
    else:
        print("Input must be positive.")

            

