def fun(*args):
    return sum(args)
print(fun(1,2,3,4,5,6,7))
print(fun(10,19,18,171,61,15,14,13,12))
##############
def sum_even_odd(*args):
    even_sum =sum(x for x in args if x % 2==0)
    odd_sum=sum(x for x in args if x % 2!=0)
    return even_sum ,odd_sum
print(sum_even_odd(1,2,3,4,5))