number=[1,2,3,4,5,6]
square_number=list(map(lambda x:x**2 ,number))
print(square_number)
#########################
names=["nadeem","ashraf","hussain"]
uper=map(str.upper,names)
print(list(uper))
###################
y=[2,3,4,5,6]
squar=list(map(lambda x:x**2,y))
print(squar)
######################## take list input from user
number=list(map(int,input("Enter your list :")))
n=list(map(lambda x:x**2,number))
print(n)
####################
n=["nadeem","ashraf","hussain"]
res=tuple(map(str,n))
print(res)
#################


