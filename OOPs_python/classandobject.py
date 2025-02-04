class Dog():
    sound="bark"
dog1=Dog() ##instance object to directly acccess the class attributs
print(dog1.sound)    
##############################
class Dog():
    species="Canine"
    def __init__(self,name,age):
        self.name=name
        self.age=age
dog1=Dog("gundda",3)  
print(dog1.name)
print(dog1.species)
#################
class Dog():
    species="canine"
    def __init__(self,name,age):
           self.name=name
           self.age=age
    def __str__(self):
        return f"{self.name} is {self.age} year old !"
dog1=Dog("charr",3)
dog2=Dog("Vhar",5)
print(dog1)
print(dog2)  
dog1.name="Cola"
dog1.age=45
print("Update the name and age dog1 is :")
print(dog1)
