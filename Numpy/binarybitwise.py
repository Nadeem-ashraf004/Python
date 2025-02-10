import numpy as np
######## bitwise_and
a=10
b=12
print("the first number you enter :")
print("the seconde number  you enter : ")
num_bits=np.bitwise_and(a,b)
print("the bitwise number is = ",num_bits)
############################# bitwise_or
num1_bit=np.bitwise_or(a,b)
print("if we just or bitwise function here is the result : ",num1_bit)
####################bitwise xor
num1_bit=np.bitwise_xor(a,b)
print("XOR operation is done :",num1_bit)
########################inverted funcction
num1_bit=np.invert(a,b)
print("After inverted function : ")
######################## left.right function 
