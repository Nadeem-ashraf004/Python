import matplotlib.pyplot as plt
import numpy as np
x=np.array([12, 45, 7, 32, 89, 54, 23, 67, 14, 91])
y=np.array([99, 31, 72, 56, 19, 88, 43, 61, 35, 77])
plt.scatter(x,y)
plt.title("scatter graph")
plt.legend(["A"])
plt.show()
############################## multiple data set
x1=np.array.arange(10,1000,30)
y1=np.array.arange(10,1000,20)
x2=np.array.arange(10,1000,50)
y2=np.array.arange(10,1000,60)
plt.scatter(x1,y1,color='red',label='Group 1')
plt.scatter(x2,y2,color='red',label='Group 1')
plt.title("multiple dataset scatter ghraph")
plt.legend()
plt.show()
