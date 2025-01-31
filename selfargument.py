class Car:
    def __init__(self,brand,model):
        self.model=model
        self.brand=brand
    def display(self):
        return self.brand,self.model
Car1=input("Enter you  car model :\n")
car2=input("Enter your brand :") 
Car3=Car(Car1,car2)
print(Car3.display())
###########################
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        a=3.14*self.r**2  
        return a
radius=float(input("Enter your area of circle :"))    
ins=Circle(radius)   
print("Area of the circle : ",ins.area()) 
####################
 
