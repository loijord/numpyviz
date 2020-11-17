"""this example demonstrates how to image 3D numpy array
indices are colored in yellow if their sum is divisible by 3"""

import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

A = np.array([[[0, 0, 0],
               [0, 0, 0]],
              [[0, 0, 0],
               [0, 0, 0]],
              [[0, 0, 0],
               [0, 0, 0]],
              [[0, 0, 0],
               [0, 0, 0]]])

B = np.array([[[2, 3, 0],
              [3, 1, 2]]])

fig = plt.figure()
ax = fig.add_subplot(1, 3, 1, projection='3d')
va = VisualArray(A, fig=fig, ax=ax)
coords = va.get_indices()
va.set_colors(coords.T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)
va.ax.set_title('A = array of shape (4,2,3)')
va.ax.dist = 12.5

ax = fig.add_subplot(1, 3, 2, projection='3d')
va = VisualArray(B, fig=fig, ax=ax)
coords = va.get_indices()
va.set_colors(coords.T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)
va.ax.set_title('B = array of shape (1,2,3)')
va.ax.dist = 12.5

np.put_along_axis(A, B, 1, 0)
ax = fig.add_subplot(1, 3, 3, projection='3d')
va = VisualArray(A, fig=fig, ax=ax)
coords = va.get_indices()
x,y,z = coords.T
cells = coords[A[x,y,z]==1]
va.set_colors(cells.T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)
va.ax.set_title('new value of A after \n np.put_along_axis(A, B, 1, 0)')
va.ax.dist = 12.5
plt.get_current_fig_manager().window.state('zoomed')
plt.show()