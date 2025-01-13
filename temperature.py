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
