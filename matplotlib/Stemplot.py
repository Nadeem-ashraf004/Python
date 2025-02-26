import numpy as np
import random
import matplotlib.pyplot as plt
x=np.linespace(0.1,2*np.pi,41)
y=np.exp(np.sin(x))
plt.stem(x,y,use_line_collection=True)
plt.show()
###########################
x=np.linespace(0.1,2*np.pi,41)
y=np.exp(np.sin(x))
maekerline,spaceline,stemlines=plt.stem(x,y,linefmt='grey',markerfmt='D',bottom=1.1,use_line_collection=True)
markerline.set_markerfacecolor('none')
plt.show()