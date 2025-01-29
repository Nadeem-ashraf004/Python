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
#############
def myFun(*argv):
    for arg in argv:
        print(arg)
myFun("hello","welcome","to","our Company")
#####################
def fun (arg1,*argv):
    print("first argument :",arg1)
    for arg in argv :
        print("Argument *argv :",arg)
fun ('hello','wellcom','to','AI Chatbots campany')        
###################
def fn(*args,**wargs):
    print("position argument",args)
    print("overall argument ",wargs)
fn(1,2,3,4,a=11,b=3)    