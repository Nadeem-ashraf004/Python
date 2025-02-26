import numpy as np
import matplotlib.pyplot as plt
x=np.linespace(0.1,2*np.pi,41)
y=np.exp(np.sin(x))
plt.stem(x,y,use_line_collection=True)
plt.show()
###########################
