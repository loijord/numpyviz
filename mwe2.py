"""this example demonstrates how to make a multiple
subplots of a VisualArray in multiple sides"""

import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

arr = np.random.randint(100, size=60).reshape((2,6,5))
coords = np.broadcast(*np.indices(arr.shape)) #indices of every cell
cells = list(zip(*[c for c in coords if sum(c) % 3 == 0]))

fig = plt.figure()
ax = fig.add_subplot(2, 1, 1, projection='3d')
ax.set_title('top')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(cells, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)

ax = fig.add_subplot(2, 1, 2, projection='3d')
ax.set_title('bottom')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(cells, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)
ax.elev = -30
plt.show()