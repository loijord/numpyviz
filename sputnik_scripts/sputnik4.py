import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

start = np.random.randint(99, size=(5,7,3))
height, width = start.shape[:2]
v, u = np.indices((height, width))
print(u)
print(v)
print(np.around(-0.5 + u / (width-1), 2))
print(np.around((-0.5 + v / (height-1)) * height / width, 2))
va = VisualArray(start)
cells = va.get_indices()
va.set_colors(cells.T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)
va.ax.set_title('array of shape (5,7,3)')
plt.show()