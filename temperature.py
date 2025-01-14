celsius = 37.5
fahrenheit = (celsius * 1.8) + 32
print("%.1f degrees Celsius is equal to %.1f degrees Fahrenheit" % (celsius, fahrenheit))
#######
celcius=int(input("enter your currrent celcius : "))
fahrenheit = (celsius * 1.8) + 32
print("%.f degree of celcius is equal to %.f degree Fahrenheit" %(celcius,fahrenheit))


#### calculate the area of the triangle
x=float(input("Enter your first lenght side :"))
y=float(input("Enter your secode side:"))
z=float(input("Enter your third side :"))
s=(x+y+z)/2
area=(s*(s-x)*(s-y)*(s-z))**0.5
print("the area of the triangle is %0.2f"%area)
##########################################
import cmath
a = 12
b = 13
c = 14

d = (b**2) - (4*a*c)


sol1 = (-b - cmath.sqrt(d)) / (2*a)
sol2 = (-b + cmath.sqrt(d)) / (2*a)

print("The solutions are {0} and {1}".format(sol1, sol2))
