x=5,
y=5,
print(x,y)
# variable to find the type
x=4 ,
y="nadeem",
print(type(x))
# asign multiple values
a,x,y="apple","orange","mango",
print(a)
print(x)
print(y)
# one value to multiple variable
x=y=z="orange"
print(x)
print(y)
print(z)
#unpack a  collection
fruite= ["apple","banana","cherrry"]
x,y,z=fruite
print(x)
print(y)
print(z)
#
x=5,
y=9,
print(x+y)
#global scope variable
global_var="i try to learn python with in three month"

def global_access_var():
    local_access_var="i put my best to learn this with in two month"
    print(global_var)
    print(local_access_var)

global_access_var()