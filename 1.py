import numpy as np
import matplotlib.pyplot as plt
import tkinter
a = np.arange(360)
x = np.sin(a)
ax = plt.plot(x,range(360),'bo')
plt.show()