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
############ 
class student1(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
x=student1('gulzar','gubadeem')
x.name()        
