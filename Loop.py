a=["nadeem", "ashraf","hussain"]
for i in a:
    print(i)

b="nadeem"
for i in b:
    print(i)
for i in range(0,12,1):
   print(i) 
for i in range(1,4):
   for j in range(1,4):
       print(i,j)   
for x in range(1,3):
    for y in range(1,3):
        print(f"uperloop:{x},innerloop:{y}")         
for i in range (1,3):
    for l in range(1,3):
        print(f"{i} x {j}={i*j}") 
#################################################################

n=int(input("Enter the number of rows in triangle :"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()  
#####################################################################
k= int(input("Enter the number of row in pyramid: "))
for i in range(1,k+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()  
###################################################################### 
start=int(input("enter the starting number :"))
end=int(input("Enter the ending number :"))
for i in range(start,end+1):
    for j in range(i,end+1):
        print(f"{i} x {j}={i*j}")
         
        print("-"*15)
