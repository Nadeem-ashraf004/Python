student_detail=[]
def menu():
    print("\nManu ")
    print("A. To add an student datail:")
    print("B. To Display all student with all stored information")
    print("C. To Search by id ")
    print("D. To exit the application")
def add_student():
        ID=input("Enter your ID :")
        name=input("Enter your name:")
        address=input("Ener your address:")
        student_detail.append({"ID": ID, "Name": name,"address":address})
        print("Student added successfully!")
def display_student():
            for student in student_detail:
                    print(f"ID: {student['ID']}, Name: {student['Name']}, address: {student['address']}")
def search_by_id():
    student_id = input("Enter ID to search: ")
    for student in student_detail:
        if student['ID'] == student_id:
            print(f"ID: {student['ID']}, Name: {student['Name']}, address: {student['address']}")
            return
    print("Not Found") 
while True:
    menu()
    choice = input("Enter your choice: ").upper()    
    if choice=='A':
          add_student()
    elif choice=='B':
          display_student()
    elif choice=='C':
          search_by_id()
    elif choice=='D':
          print("Now exit the Application :")      
          break      
    else:
          print("invalid choicce :") 
##                     

                             