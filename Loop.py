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
#######################################
students = []  # List to store student details
current_year = 2025  # Define the current year

while True:
    print("\n--- Enter Student Details ---")
    gender = input("Enter your gender (male/female): ").strip().lower()
    firstname = input("Enter your first name: ")
    middlename = input("Enter your middle name: ")
    lastname = input("Enter your last name: ")
    date_of_birth_day = int(input("Enter your date of birth (day): "))
    date_of_birth_month = input("Enter your month of birth: ")
    date_of_birth_year = int(input("Enter your year of birth: "))
    house_number = input("Enter your house number: ")
    street = input("Enter your street: ")
    town = input("Enter your town: ")
    city = input("Enter your city: ")
    country = input("Enter your country: ")
    
    # Determine title based on gender
    if gender == "male":
        title = "Mr."
    elif gender == "female":
        title = "Ms."
    else:
        title = ""
    
    # Calculate age
    age = current_year - date_of_birth_year
    
    # Store student details in a dictionary
    student_details = {
        "gender": gender,
        "title": title,
        "name": f"{title} {firstname} {middlename} {lastname}",
        "dob": f"{date_of_birth_day} {date_of_birth_month} {date_of_birth_year}",
        "age": age,
        "address": f"{house_number}, {street}, {town}, {city}, {country}"
    }
    
    # Add the student's details to the list
    students.append(student_details)
    
    # Ask if the user wants to enter another student's details
    more_students = input("Do you want to add another student? (yes/no): ").strip().lower()
    if more_students != "yes":
        break

# Display all student details
print("\n--- All Students Details ---")
for index, student in enumerate(students, start=1):
    print(f"\nStudent {index}:")
    print(f"Gender: {student['gender']}")
    print(f"Name: {student['name']}")
    print(f"Date of Birth: {student['dob']} (Age: {student['age']})")
    print(f"Address: {student['address']}")        
######################################
students = []  
current_year = 2025  
numofstudents = int(input("How many students do you want to enter details for : "))

for i in range(numofstudents):
    print(f"\n--- Enter Details for Student {i + 1} ---")
    gender = input("Enter your gender (male/female): ").strip().lower()
    firstname = input("Enter your first name: ")
    middlename = input("Enter your middle name: ")
    lastname = input("Enter your last name: ")
    date_of_birth_day = int(input("Enter your date of birth (day): "))
    date_of_birth_month = input("Enter your month of birth: ")
    date_of_birth_year = int(input("Enter your year of birth: "))
    house_number = input("Enter your house number: ")
    street = input("Enter your street: ")
    town = input("Enter your town: ")
    city = input("Enter your city: ")
    country = input("Enter your country: ")
    
    
    if gender == "male":
        title = "Mr."
    elif gender == "female":
        title = "Ms."
    else:
        title = ""
    # Calculate age
    age = current_year - date_of_birth_year
    student_details = {
        "gender": gender,
        "title": title,
        "name": f"{title} {firstname} {middlename} {lastname}",
        "dob": f"{date_of_birth_day} {date_of_birth_month} {date_of_birth_year}",
        "age": age,
        "address": f"{house_number}, {street}, {town}, {city}, {country}"
    }
    students.append(student_details)
print("\n--- All Students Details ---")
for index, student in enumerate(students, start=1):
    print(f"\nStudent {index}:")
    print(f"Gender: {student['gender']}")
    print(f"Name: {student['name']}")
    print(f"Date of Birth: {student['dob']} (Age: {student['age']})")
    print(f"Address: {student['address']}")

###################
T=int (input("Enter Table number"))
S=int(input("Enter starting number :"))
E=int (input("Enter your ending number :"))
i=1
if S>E:
       i=-1
       E=E-1
else:
       E=E+1
              
for i in range(S,E+1,i):
       print(f"{T} x {i}={T*i}")
#####################################       