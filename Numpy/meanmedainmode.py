import numpy as np
from scipy import stats

marks = []  # List to store marks

def menu():
    print("\n MENU: ")
    print("A / Enter Marks ")
    print("B / Calculate Mean ")
    print("C / Calculate Median")
    print("D / Calculate Mode ")
    print("E / Calculate variance ")
    print("F / Calculate Percentile ")
    print("G / Calculate standard derivation ")
    print("X / Exit the application")

def enter_marks():
    global marks
    try:
        marks_input = input("Enter your marks (comma-separated, e.g., 69,80,90,50): ")
        marks = list(map(int, marks_input.split(",")))  # Convert input to list of integers
        print("Marks added successfully!")
    except ValueError:
        print("Invalid input! Please enter only numbers separated by commas.")

def mean():
    if not marks:
        print("⚠️ No marks available. Please enter marks first.")
        return
    print(f"Mean: {np.mean(marks):.2f}")

def median():
    if not marks:
        print("⚠️ No marks available. Please enter marks first.")
        return
    print(f"Median: {np.median(marks)}")

def mode():
    if not marks:
        print("⚠️ No marks available. Please enter marks first.")
        return
    mode_result = stats.mode(marks, keepdims=True)
    print(f"Mode: {mode_result.mode[0]} (Appeared {mode_result.count[0]} times)")
def variance():
    if not marks:
        print("⚠️ No marks available. Please enter marks first.")
        return
    print(f"variance :{np.var(marks)}")
def percentile():
    if not marks:
        print("⚠️ No marks available. Please enter marks first.")  
    print(f"percentile :{np.percentile(marks, 75)}") 
def standard_derivation():
    if not marks:
        print("⚠️ No marks available. Please enter marks first.") 
    print(f"standard derivstion :{np.std(marks)}")            
#Main Loop
while True:
    menu()
    choice = input("Enter your choice: ").upper()

    if choice == 'A':
        enter_marks()
    elif choice == 'B':
        mean()
    elif choice == 'C':
        median()
    elif choice == 'D':
        mode()
    elif choice=='E':
        variance() 
    elif choice=='F':
        percentile() 
    elif choice=='G':
        standard_derivation()          
    elif choice == 'X':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice! Please enter A, B, C, D, or X.")
#####