set1={1,2,8,9,3,4,5,3,5}
print(set1)
try:
    print(set1[0])
except  TypeError as e :
    print(e)    

list1=(input("Enter your first list :".split(',')))
list2=(input("Enter your second list: ".split(',')))  
set1=set(map(int,list1))
set2=set(map(int,list2))
comman=set1 & set2
unique= set1 | set2
symetric_diff=set1 ^ set2
only_set_one = set1 - set2  

only_set_two = set2 - set1

result= {
   "comman :":comman ,
   "unique :":unique,
   "symetric difference :":symetric_diff,
   "only_set_one :":set1-set2,
   "only set two :":set2-set1,
}
print(result)