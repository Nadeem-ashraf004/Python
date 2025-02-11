import os
arrival_person = []
def display_menu():
    os.system('cls')
    print("\nMenu:")
    print("A. To add an arriving person")
    print("B. To Display all arrived persons with all stored information")
    print("C. To count total arrived persons")
    print("D. To count persons of each type")
    print("E. To Display only students")
    print("F. To Display only Teachers")
    print("G. To Display only Employees")
    print("H. To Search a person by ID")
    print("I. To Search a person by Name")
    print("J. Delete the data (record) of a person who is leaving the lab")
    print("X. To exit the application")
def add_person():
    person_id = input("Enter ID: ")
    name = input("Enter Name: ")
    time = input("Enter Time of Arrival: ")
    person_type = input("Enter Type (Student/Teacher/Employee): ")
    arrival_person.append({"ID": person_id, "Name": name, "Time": time, "Type": person_type})
    print("Person added successfully!")
def display_all():
    for person in arrival_person:
        print(f"ID: {person['ID']}, Name: {person['Name']}, Time: {person['Time']}, Type: {person['Type']}")
def count_total():
    print(f"Total arrived persons: {len(arrival_person)}")
def count_by_type():
    types = {"Student": 0, "Teacher": 0, "Employee": 0}
    for person in arrival_person:
        types[person['Type']] += 1
    for key, value in types.items():
        print(f"{key}: {value}")
def display_students():
    for person in arrival_person:
        if person['Type'] == "Student":
            print(f"ID: {person['ID']}, Name: {person['Name']}, Time: {person['Time']}")
def display_teachers():
    for person in arrival_person:
        if person['Type'] == "Teacher":
            print(f"ID: {person['ID']}, Name: {person['Name']}, Time: {person['Time']}")
def display_employees():
    for person in arrival_person:
        if person['Type'] == "Employee":
            print(f"ID: {person['ID']}, Name: {person['Name']}, Time: {person['Time']}")
def search_by_id():
    person_id = input("Enter ID to search: ")
    for person in arrival_person:
        if person['ID'] == person_id:
            print(f"ID: {person['ID']}, Name: {person['Name']}, Time: {person['Time']}, Type: {person['Type']}")
            return
    print("Not Found")
def search_by_name():
    name = input("Enter Name to search: ")
    for person in arrival_person:
        if person['Name'] == name:
            print(f"ID: {person['ID']}, Name: {person['Name']}, Time: {person['Time']}, Type: {person['Type']}")
            return
    print("Not Found")
def delete_person():
    person_id = input("Enter ID to delete: ")
    for person in arrival_person:
        if person['ID'] == person_id:
            arrival_person.remove(person)
            print("Person deleted successfully!")
            return
    print("Not Found")

while True:
    display_menu()
    choice = input("Enter your choice: ").upper()

    if choice == "A":
        add_person()
    elif choice == "B":
        display_all()
    elif choice == "C":
        count_total()
    elif choice == "D":
        count_by_type()
    elif choice == "E":
        display_students()
    elif choice == "F":
        display_teachers()
    elif choice == "G":
        display_employees()
    elif choice == "H":
        search_by_id()
    elif choice == "I":
        search_by_name()
    elif choice == "J":
        delete_person()
    elif choice == "X":
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")