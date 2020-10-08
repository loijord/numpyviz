import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

arr = np.arange(64).reshape((1,8,8))
va = VisualArray(arr)
cells = va.get_indices_chequerwise(window=(1,1,1))
va.set_colors(cells.T, color='white', basecolor='grey')
va.vizualize(fixview=True, axis_labels=(None,None,None))
va.ax.dist = 12.5 #zoom out a little
plt.show()


