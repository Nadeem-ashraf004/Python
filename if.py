# x=input("Enter M or F :")

# if (x=="M" or x=="m"):
#     print("male")

# elif(x=="F" or x=="f"):
#     print("Female")
# else:
#     print("invalid input") 
  
n1=int(input("Enter any number :"))
n2=int(input("enter any number:"))
print(" Enter\n+ : to add\n- : to Sub\n* : to Mult\n/ : to Divid\n")
operator=input("Enter your choice :")
if (operator=="+"):
   result =n1+n2
   
elif(operator=="-") :
    result =n1-n2
   
elif(operator=="*") :
    result =n1*n2
    
elif(operator=="/") :
    result =n1/n2 
    if(n2==0):
         print("the must be greater !")
else :
   print ("invalid symbol") 
print(f"{n1} {operator} {n2} ={result}")             
      