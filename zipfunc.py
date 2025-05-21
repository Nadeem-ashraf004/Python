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
for students,fatherNames in zip(student,fatherName):
        print(f"students detail    :{students}")
        print(f"fatherName deatail :{fatherNames}")
####################