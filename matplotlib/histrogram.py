import matplotlib.pyplot as plt
data=np.random.randn(1000)
plt.hist(data,bins=30,color='skyblue',edgecolor='black')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("histogram")
plt.show()
#############################
data1=np.random.randn(1000)
data2=2*data1+np.random.normal(1000)
plt.hexbin(data1,data2,gridsize=30,cmap='Blues')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('2D Histogram (Hexbin Plot)')
plt.colorbar()
plt.show()
################################