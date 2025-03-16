lis=[1,2,2,3,3,4,4,31,4,55,68,77,8,9]
print("the list is sorted")
for i in sorted(set(lis)):
    print(i,end=" ")
###############################
lis=['rahat','zahid','ali','ali','sultan']
print("\nthe sorted list is :")
for i in sorted(set(lis)):
    print(i)
################################  
lis=['rahat','zahid','ali','ali','sultan']
print("the sorted list is :")
for i in sorted(reversed(lis)):
    print(i)      
#################################
Input=[]
input_number=int(input("How many number do you wants to enter :"))
for i in range(input_number):
    num=int(input("Enter your number:"))
    Input.append(num)
print(",".join(map(str,Input))) 
number_sum=sum(Input)
total_len=len(Input)   
Mean=number_sum/total_len
print("Mean of given number :",Mean)
def custom_median(lst):
        lst.sort()
        print(lst)
        mid=total_len/2
        if total_len % 2==0:
              return (lst[mid-1]+lst[mid])/2
        else:
              return lst(mid)
print("Medain :",custom_median(Input))


   