class Car:
    def __init__(self,brand,model):
        self.model=model
        self.brand=brand
    def display(self):
        return self.brand,self.model
Car1=Car("toyota","Corola") 
print(Car1.display())
###########################
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        a=3.14*self.r**2  
        return a
ins=Circle(5)   
print("Area of the circle : ",ins.area())   
