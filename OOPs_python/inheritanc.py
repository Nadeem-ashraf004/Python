class person():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def name(self):
        print(self.fname,self.lname) 
x=person('Nadeem','ashraf')
x.name()      
##########################   create a child class 
class student(person):
    pass  
x=student('Ali','Ahmad')
x.name()
