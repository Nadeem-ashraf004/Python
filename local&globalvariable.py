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