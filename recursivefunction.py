def factorial(n):
    if n == 1 or n==0:
        return 1
    else :
        return n*factorial(n-1)
print (factorial(5))   
######################
def febbonacci(n):
    if n==0:
        return 0
    elif n== 1:
        return 1
    else:
        return febbonacci(n-1) + febbonacci(n-2)
print(febbonacci(10))    
    
