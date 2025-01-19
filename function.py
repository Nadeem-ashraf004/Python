def add(num1:int,num2:int) ->int:
    num3=num1 + num2
    return num3
num1=int(input("Enter your first number :"))
num2=int(input("Enter your second number :"))
ans=add(num1,num2)
print(f"the addition of {num1} and {num2} is equal to {ans}.")
################ multipication of two number
def mult(num1:int,num2:int)->int:
    num3=num1*num2
    return num3
num1=int(input("Enter your first number :"))
num2=int(input("Enter your seconde number :"))
ans=mult(num1,num2)
print(f"th multiplication of {num1} and {num2} is equal to {ans}")
##################################### default argumrnt
def fun (x,y=50):
    print ('x =',x)
    print('y =',y)
fun(39)
#example2
import math
def calculate_circle_area(radius):
    return math.pi * radius ** 2
radius = float(input("Enter the radius of the circle: "))

area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
############################
import math
def calculate_circle_area(radius):
    return math.pi * radius ** 2
radius = float(input("Enter the radius of the circle: "))

area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
