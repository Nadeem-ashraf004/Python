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
######################
# List of 7-days
days = [x for x in range(0, 7)]
 
# List of Suspected cases
Suspected = [12, 18, 35, 50, 72, 90, 100]
 
# List of Cured Cases
Cured = [4, 8, 15, 22, 41, 55, 62]
 
# List of Number of deaths
Deaths = [1, 3, 5, 7, 9, 11, 13]
 
# Plot x-labels, y-label and data
plt.plot([], [], color ='blue', 
         label ='Suspected')
plt.plot([], [], color ='orange',
         label ='Cured')
plt.plot([], [], color ='brown',
         label ='Deaths')
 
# Implementing stackplot on data
plt.stackplot(days, Suspected, Cured, 
              Deaths, baseline ='zero', 
              colors =['blue', 'orange', 
                       'brown'])
 
plt.legend()
 
plt.title('No of Cases')
plt.xlabel('Day of the week')
plt.ylabel('Overall cases')
 
plt.show()
##########################################