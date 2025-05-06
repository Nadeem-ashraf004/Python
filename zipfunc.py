names=['Ali','sap','ka','hai']
ages=(12,12,12,12)
for name,age  in zip(names,ages):
    print(name,age)
    ##################################
student=[]
fatherName=[]
def amnu():
      studentDetail=input("Enter students name : ").upper() 
      fatherNameDetail=input("Enter father name :").upper()
      student.append(studentDetail)    
      fatherName.append(fatherNameDetail) 
      print("student detail & father detial added successfully")
amnu()
print(f"students detail : ={student}")
print(f"fatherName deatail : ={fatherName}")

