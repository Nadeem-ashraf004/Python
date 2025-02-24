#########################
import matplotlib.pyplot as plt
import numpy as np
days = [1, 2, 3, 4, 5]
Studying = [7, 8, 6, 11, 7]
playing = [8, 5, 7, 8, 13]

plt.stackplot(days, Studying, playing, colors =['r', 'c'])
plt.xlabel('Days')


plt.ylabel('No of Hours')

plt.title('Representation of Study and \
Playing wrt to Days')

plt.show()
