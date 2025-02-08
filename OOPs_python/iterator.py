mytuple=('nadeem','ashraf')
myit=iter(mytuple)
print(next(myit))
####################
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
  ##############
number=[1,2,9,40,4,6,8]
for i in sorted(number):
#   print(i)
  pass
print("largesr number :",i)
################
def funct(number2):
    number2.sort()
    m=number2[-1]
    return m
number1=[1,4,6,3,9]
print(funct(number1))  