class Car:
    def __init__(self,brand,model):
        self.model=model
        self.brand=brand
    def display(self):
        return self.brand,self.model
Car1=Car("toyota","Corola") 
print(Car1.display())
