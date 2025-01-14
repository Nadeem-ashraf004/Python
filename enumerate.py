for key , value in enumerate(['the','big','bang','theory']):
    print(key,value)

for key , value in enumerate(['Artificial','is','the','future','of','our','sociaty\n']):
    print(value,end=" ")    

name=("Nadeem","Ashrdaf","Hussain")
age=(34,45,45)
for name , age in zip(name,age) :
    print("Name:",name)
    print("Age :",age)
    print()  

Question=['Name','color','shape']
Answer=['Apple','Red','a circle']
for Question ,Answer in zip(Question,Answer):
    print("What is your {0}? i am {1}.".format(Question,Answer))    