import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

arr = np.array([[1,1,1,1,1,1], [1,0,0,0,0,1], [1,0,1,1,0,1]])

fig = plt.figure()
ax = fig.add_subplot(1, 3, 1, projection='3d')
va = VisualArray(arr, fig=fig, ax=ax)
coords = va.get_indices()
va.set_colors(coords.T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True, axis_labels=(None, 'axis=0', 'axis=1'))
va.ax.set_title('arr = array of shape (3,6)')
va.ax.dist = 12.5

arr = arr.reshape(3,3,2)
ax = fig.add_subplot(1, 3, 2, projection='3d')
va = VisualArray(arr, fig=fig, ax=ax)
coords = va.get_indices()
va.set_colors(coords.T, color='lightblue', basecolor='lightblue')
va.vizualize(fixview=True)
va.ax.set_title('arr = array of shape (3, 3, 2)')
va.ax.dist = 12.5

arr = arr.swapaxes(0, 1)
print(arr)
ax = fig.add_subplot(1, 3, 3, projection='3d')
va = VisualArray(arr, fig=fig, ax=ax)
coords = va.get_indices()
va.set_colors(coords.T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)
va.ax.set_title('arr.swapaxes(1, 0)')
va.ax.dist = 12.5
plt.get_current_fig_manager().window.state('zoomed')
plt.show()