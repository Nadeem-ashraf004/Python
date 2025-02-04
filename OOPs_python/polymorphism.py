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