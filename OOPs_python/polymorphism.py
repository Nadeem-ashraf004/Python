class animal():
    def spark(self):
        return "place in subclass"
class Dog(animal):
    def spark(self):
        return "wooof" 
class Cat(animal):
    def spark(self):
        return "maowe"
Animals=[Dog(),Cat()]
for animal in Animals:
    print(animal.spark())           