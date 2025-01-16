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