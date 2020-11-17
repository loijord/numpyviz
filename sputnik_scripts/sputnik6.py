"""this example demonstrates how to make a multiple
subplots of a VisualArray in multiple sides"""

import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

x = np.random.randint(99, size=(1,1,9))
y = np.random.randint(99, size=(4,4,1))

fig = plt.figure()
ax = fig.add_subplot(1, 3, 1, projection='3d')
ax.set_title('x = array of shape (1, 1, 9)')
va = VisualArray(x, fig=fig, ax=ax)
va.set_colors(np.array(list(np.ndindex(x.shape))).T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)

ax = fig.add_subplot(1, 3, 2, projection='3d')
ax.set_title('y = array of shape (4, 4, 1)')
va = VisualArray(y, fig=fig, ax=ax)
va.set_colors(np.array(list(np.ndindex(y.shape))).T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)

arr = x - y
ax = fig.add_subplot(1, 3, 3, projection='3d')
ax.set_title('x - y = array of shape (4, 4, 9)')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(np.array(list(np.ndindex(va.arr.shape))).T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)
plt.get_current_fig_manager().window.state('zoomed')
plt.show()