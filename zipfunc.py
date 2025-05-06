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
      student.append({studentDetail})    
      fatherName.append({fatherNameDetail}) 
      print("student detail & father detial added successfully")
amnu()
print(student)
print(fatherName)

