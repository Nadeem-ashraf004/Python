#multiply two number 
rows=int(input("Enter the rows for the multipication table :"))
cols=int(input("Enter the colums for the multipication table :"))
i=1
while i<=rows:
    j=1
    while j<=cols:
        print(f"{i} x {j}={i*j}")
        j+=1
        print("-"*15)
        i+= 1
###############################################  triangle pattren 
n=int(input("Enter the number of rows for the triangle :"))
i=1
while i<=n:
    j=1
    while j<=1:
        print("*",end=" ")
        j+=1
        print()
        i+=1      
####################### revese number pyrimad
n=int(input("Enter the number of rows for pyrimad :"))
i=n
while i>0:
    j=1
    while j<=i:
        print(j, end=" ")
        j+=1
       
    print()
    i-=1  
