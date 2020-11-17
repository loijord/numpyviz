import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

arr = np.array([1,0,1])

fig = plt.figure()
ax = fig.add_subplot(2, 3, 1, projection='3d')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(va.get_indices().T, color='orange', basecolor='lightblue')
va.vizualize(fixview=True, axis_labels=(None, None, 'axis=0'), usetex=False)
va.ax.set_title('arr = array of shape (3,)')
va.ax.dist = 12.5
va.ax.azim, va.ax.elev = -135, 45

arr1 = np.array([1,0,1]).reshape(-1, 1)
ax = fig.add_subplot(2, 2, 2, projection='3d')
va = VisualArray(arr1, fig=fig, ax=ax)

va.set_colors(va.get_indices().T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True, axis_labels=(None, 'axis=0', 'axis=1'), usetex=False)
va.ax.set_title('arr1 = array of shape (3,1)')
va.ax.dist = 12.5
va.ax.azim, va.ax.elev = -135, 45

arr2 = np.round(np.linspace(-3,3,11),1)
ax = fig.add_subplot(2, 2, 3, projection='3d')
va = VisualArray(arr2, fig=fig, ax=ax)
va.set_colors(va.get_indices().T, color='lightblue', basecolor='lightblue')
va.vizualize(fixview=True, axis_labels=(None, None, 'axis=0'), scale=0.5, usetex=False)
va.ax.set_title('arr2 = array of shape (11,)')
va.ax.dist = 6.7
va.ax.azim, va.ax.elev = -135, 45

arr = arr1 * arr2
ax = fig.add_subplot(2, 2, 4, projection='3d')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(va.get_indices().T, color='lightgreen', basecolor='lightblue')
va.vizualize(fixview=True, axis_labels=(None, 'axis=0', 'axis=1'), scale=0.5, usetex=False)
va.ax.set_title('arr1 * arr2 = array of shape (3, 11)')
va.ax.dist = 7.5
va.ax.azim, va.ax.elev = -135, 45

plt.get_current_fig_manager().window.state('zoomed')
plt.show()
