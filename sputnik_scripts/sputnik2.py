import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

def argmin_axis2(arr):
    a3 = np.argmin(arr, axis=2)
    print(a3.__repr__())
    a1, a2 = np.indices((arr.shape[0], arr.shape[1]))
    x, y, z = zip(*np.broadcast(a1, a2, a3))
    return x, y, z

arr = np.random.randint(99, size=8*8*3).reshape((8,8,3))
va = VisualArray(arr)
va.set_colors(argmin_axis2(arr), color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)
va.ax.set_title('argmin on axis=-1')
plt.show()


