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
