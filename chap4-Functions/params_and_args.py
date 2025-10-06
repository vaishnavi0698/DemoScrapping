"""
def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice('spam')   # argument name could be anything that yu want to assign to the variables inside a function.
-----------------------------------------
def print_twice(bruce):
    print(bruce)
    print(flow) #local variable names should match with the parameter names; gives error since "flow" is undefined.

print_twice('spam')  
-----------------------------------------
def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice('Spam '*4)
------------------------------------------
import math
def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice(math.pi)    
print_twice(math.cos(math.pi))
------------------------------------------

def computepay(hours, rate, pay = 0):
    if hours <= 40:
        pay = hours * rate
    else:
        pay = hours * rate * 1.5   
    return pay

hours = float(input("enter no.of hours:\n"))
rate = float(input("enter the rate:\n"))
print("Pay calculated is: ", computepay(hours,rate))
-------------------------------------------

try:
   def computegrade(score):
    if score > 0.9:
        grade = 'A'
    elif score > 0.8:
        grade = 'B'
    elif score > 0.7:
        grade = 'C'
    elif score > 0.6:
        grade = 'D'
    else:
        grade = 'F'    
    return grade
except:
     print("Enter numeric values for score!")

score = float(input("Enter score:\n")) 
print("Grade: ", computegrade(score))

# a try except block should nevr wrap a function definition we are chcking score data type so wrap it around it which means wrap it around the function call
-------------------------------------------
"""

def computegrade(score):
    if score > 1.0 or score < 0.0:   # reject invalid range
        return "Bad score"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"

try:
    score = float(input("Enter score:\n"))
    print("Grade:", computegrade(score))
except:
    print("Bad score")   # catches non-numeric input
