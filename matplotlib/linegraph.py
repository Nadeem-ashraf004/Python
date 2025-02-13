##################### line graph
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[1,2,3,4]
plt.plot(x,y)
plt.title("Line Graph :")
plt.legend(["line"])
plt.show()
##################
x=[3,1,3]
y=[3,2,1]
plt.plot(x,y)
plt.title("Line Graph ")
plt.legend(["Line"])
plt.show()
########################
x=[1,2,3,4,5]
y=[10,20,15,25,30]
plt.plot(x,y,marker='o',linestyle='-',color='b',label='data line')
plt.legend()
plt.title("Basic Line Graph ")
plt.show()
#########################

 