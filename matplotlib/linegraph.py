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
x1=np.array([1,2,3,4,5])
y1=x1*2
plt.plot(x,y)
x2=[2,4,6,8,9]
y2=[1,3,5,7,9]
plt.plot(x2,y2,'-.')
plt.title("multiple line graph")
plt.legned(['Line'])
plt.xlabel("X-axis")
plt.ylabel('Y-axis')
plt.fill_between(x1,y1,y2,color='green',alpha=0.5)
plt.show()
################################# 