# ocal variable 
def f():
    s=" my name is nademm ashraf"
    print(s)
f() 
#######gloabl variable 
name ="nadeem"

def fun():
    print(f"Hallo :{name}")
fun()
print(f"outside the function : {name}")  

###
counter =0
def f():
    global counter
    counter+=1
f()
f()
print(f" hello jinab :{counter}")
#################
balance=10000
def deposit(amount):
    global balance
    amount +=balance
    print(f"your cuurrent blance is : {amount}")
def withdraw(amount):
    global balance 
    if amount <= balance:
       balance-=amount
       print(f"your withdraw : {amount}")
    else:
        print("insuficeint balance :")
deposit(1000)
withdraw(300)           
