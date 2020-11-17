"""this example demonstrates how to make a multiple
subplots of a VisualArray in multiple sides"""

import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

x = np.random.randint(50,99, size=(3,3,5))
y = np.random.randint(50, size=(3,3,1))

fig = plt.figure()
ax = fig.add_subplot(1, 3, 1, projection='3d')
ax.set_title('x = array of shape (3, 3, 5)')
va = VisualArray(x, fig=fig, ax=ax)
va.set_colors(np.array(list(np.ndindex(x.shape))).T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)

ax = fig.add_subplot(1, 3, 2, projection='3d')
ax.set_title('y = array of shape (3, 3)')
va = VisualArray(y, fig=fig, ax=ax)
#va.set_colors(np.array(list(np.ndindex(va.arr.shape))).T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)

arr = x - y
ax = fig.add_subplot(1, 3, 3, projection='3d')
ax.set_title('x - y = array of shape (3, 3, 5)')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(np.array(list(np.ndindex(va.arr.shape))).T, color='orange', basecolor='lightblue')
va.vizualize(fixview=True)
plt.get_current_fig_manager().window.state('zoomed')
plt.show()