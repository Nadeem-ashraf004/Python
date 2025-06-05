# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)  
# # ########################
# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     else:  
#       return fact(n-1)*n 
# print(fact(4))  
########## print sum of n natural number 
def calc_sum(n):
    if (n==0):
        return 1 
    print(n)
    return calc_sum(n-1)+n
sum=calc_sum(10)
print(sum)    