import matplotlib.pyplot as plt
data=np.random.randn(1000)
plt.hist(data,bins=30,color='skyblue',edgecolor='black')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("histogram")
plt.show()