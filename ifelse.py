x=input("Enter M or F :")

if (x=="M" or x=="m"):
    print("male")

elif(x=="F" or x=="f"):
    print("Female")
else:
    print("invalid input") 
  
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
    if(n1!=0 or n2!=0):
       result =n1/n2
    else:
        print("the both number must be greater then 0 !") 
        exit()
else :
   print ("invalid symbol") 
print(f"{n1} {operator} {n2} ={result}")   
####################################

gender = input("Enter your gender (male/female): ").strip()
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
current_year = 2025
age = current_year - date_of_birth_year
print("\nUser Details:")
print(f"Gender : {gender}")
print(f"Name: {title} {firstname} {middlename} {lastname}")
print(f"Date of Birth: {date_of_birth_day} ,{date_of_birth_month}, {date_of_birth_year} Your Age Rigth Now : {age} ")
print(f"Address: {house_number}, {street}, {town}, {city}, {country}")





      