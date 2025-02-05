class animal():
    def speak(self):
        return "place in subclass"
class Dog(animal):
    def speak(self):
        return "wooof" 
class Cat(animal):
    def speak(self):
        return "maowe"
Animals=[Dog(),Cat()]
for animal in Animals:
    print(animal.speak())  
####################################
class Duck():
    def Quack(self):
        return "Quack"
class person():
    def Quack(self):
        return "QUack"
def make_it_quack(thing):
    print(thing.Quack())  
make_it_quack(Duck())
make_it_quack(person())     
######################################
class Animal():
    def sound(self):
        return "Animal make sound"  
class Dog(Animal):
    def sound(self):
        return "dark"
class Cat(Animal):
    def sound(self):
        return "meaow"
Animal_sound=input("Enter the sound of animal like Dog/Cat  : ").strip().lower()
if Animal_sound=="dog":
    animal=Dog()
elif Animal_sound=="cat":
    animal=Cat()
else:
    animal=Animal()
print(f"the {Animal_sound.capitalize()}  says:{animal.sound()}")  
################################
          

             