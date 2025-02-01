s1='nadeeem'
s2=lambda func:func.upper()
print(s2(s1))
#############
r1=lambda x:x**2
print(r1(12))
##############
def func(a):
    return len (a)
car=['corola','marsedies']
car.sort(func(a))
print(car)