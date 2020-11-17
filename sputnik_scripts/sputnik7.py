"""this example demonstrates how to make a multiple
subplots of a VisualArray in multiple sides"""

import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

arr = np.ones(shape=(4,4,4), dtype=int)
arr[np.eye(4, dtype=bool)] = False

fig = plt.figure()
ax = fig.add_subplot(2, 2, 1, projection='3d')
ax.set_title('Step 1: array of shape (n, n, n) \n masked with np.eye(n, dtype=bool)')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(np.array(np.nonzero(arr)), color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)
va.ax.dist = 12.5

arr = arr.swapaxes(1,2)
ax = fig.add_subplot(2, 2, 2, projection='3d')
ax.set_title('Step 2: swap axis 1 and 2')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(np.array(np.nonzero(arr)), color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)
va.ax.dist = 12.5

arr[np.eye(4, dtype=bool)] = False
ax = fig.add_subplot(2, 2, 3, projection='3d')
ax.set_title('Step 3: apply a mask repeatedly')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(np.array(np.nonzero(arr)), color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)
va.ax.dist = 12.5

arr = arr.swapaxes(1,2)
ax = fig.add_subplot(2, 2, 4, projection='3d')
ax.set_title('Step 4: unswap axis 1 and 2')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(np.array(np.nonzero(arr)), color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)
va.ax.dist = 12.5

plt.get_current_fig_manager().window.state('zoomed')
plt.show()