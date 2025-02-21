import matplotlib.pyplot as plt
import numpy as np
cars=['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR', 'MERCEDES']
data=[23, 17, 35, 29, 12, 41]
fig=plt.figure(figsize=(10,7))
plt.pie(data,labels=cars)
plt.show()
#################################
cars = ['AUDI', 'BMW', 'FORD',
        'TESLA', 'JAGUAR', 'MERCEDES']

data = [23, 17, 35, 29, 12, 41]
explot=(0.1, 0.0, 0.2, 0.3, 0.0, 0.0)
colors = ("orange", "cyan", "brown",
          "grey", "indigo", "beige")
wp = {'linewidth': 1, 'edgecolor': "green"}          

