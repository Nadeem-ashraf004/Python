names=['Ali','sap','ka','hai']
ages=(12,12,12,12)
for name,age  in zip(names,ages):
    print(name,age)
    ##################################
student=[]
fatherName=[]
def amnu():
      studentDetail=input("Enter students name : ").lower() 
      fatherNameDetail=input("Enter father name :").lower()
      student.append({"studentsDetail":studentDetail})    
      fatherName.append({"fatherNameDetail":fatherNameDetail}) 


