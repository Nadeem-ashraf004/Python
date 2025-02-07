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
def fun(n):
    x = 2
    count = 0
    while count < n:
        for d in range(2, int(x ** 0.5) + 1):  # check divisibility only up to sqrt(x)
            if x % d == 0:
                break  # if divisible, it's not prime, so break the loop
        else:
            print(x)  # prime number
            count += 1
        x += 1

# Driver Code
n = 10

fun(n)
############################
def fun(a,b):
    return a+b
fun(5,10)
#######################
def prim_num(n):
    if n in [2,3]:
        return True
    elif(n==1) or (n%2==0):
        return False
    r=3
    while r*r<n:
        if n % r == 0:
            return False
        r += 2
    return True
print(prim_num(78), prim_num(79))