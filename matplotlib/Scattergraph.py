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
#################################### customize color and size
x = np.array([3, 12, 9, 20, 5, 18, 22, 11, 27, 16, 8, 24, 15])
y = np.array([95, 55, 63, 77, 89, 50, 41, 70, 58, 83, 61, 52, 68])
plt.scatter(x,y,color='#23d4e8')
x = np.array([1, 6, 14, 17, 3, 13, 10, 8, 19, 21, 2, 16, 23, 25])
y = np.array([80, 60, 72, 90, 68, 55, 74, 79, 66, 81, 58, 67, 62, 85])
plt.scatter(x,y,color='32cd68')
plt.show()
################################
