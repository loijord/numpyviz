import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

arr = np.array([[11,12,13,14,15,16],
                  [21,22,23,24,25,26],
                  [31,32,33,34,35,36],
                  [41,42,43,44,45,46]])
a = arr.copy()

fig = plt.figure()
ax = fig.add_subplot(2, 3, 1, projection='3d')
va = VisualArray(arr, fig=fig, ax=ax)
coords = va.get_indices()
va.set_colors(coords.T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True, axis_labels=(None, 'axis=0', 'axis=1'))
va.ax.set_title('arr = array of shape (4,6)')
va.ax.dist = 12.5

arr = a.reshape((4,3,2))
ax = fig.add_subplot(2, 3, 2, projection='3d')
va = VisualArray(arr, fig=fig, ax=ax)
coords = va.get_indices()

va.set_colors(coords[coords[:,1]==1].T, color='lightgreen', basecolor='lightblue')
va.set_colors(coords[coords[:,1]==2].T, color='thistle', basecolor='lightblue')
va.vizualize(fixview=True)
va.ax.set_title('arr1 = array of shape (4, 3, 2)')
va.ax.dist = 12.5

arr = a.reshape((4,2,3))
ax = fig.add_subplot(2, 3, 3, projection='3d')
va = VisualArray(arr, fig=fig, ax=ax)
coords = va.get_indices()
va.set_colors(coords[coords[:,1]==1].T, color='lightgreen', basecolor='lightblue')
va.vizualize(fixview=True)
va.ax.set_title('arr2 = array of shape (4, 2, 3)')
va.ax.dist = 12.5

arr = a.reshape((4,3,2))
arr = np.vstack(arr.swapaxes(0,1))
ax = fig.add_subplot(2, 3, 5, projection='3d')
va = VisualArray(arr, fig=fig, ax=ax)
coords = va.get_indices()
va.set_colors(coords[np.isin(coords[:,1], [4,5,6,7])].T, color='lightgreen', basecolor='lightblue')
va.set_colors(coords[coords[:,1]>7].T, color='thistle', basecolor='lightblue')
va.vizualize(fixview=True, axis_labels=(None, 'axis=0', 'axis=1'))
va.ax.set_title('np.vstack(arr1.swapaxes(0,1))')
va.ax.dist = 7

arr = a.reshape((4,2,3))
arr = np.vstack(arr.swapaxes(0,1))
ax = fig.add_subplot(2, 3, 6, projection='3d')
va = VisualArray(arr, fig=fig, ax=ax)
coords = va.get_indices()
va.set_colors(coords[coords[:,1]>3].T, color='lightgreen', basecolor='lightblue')
va.vizualize(fixview=True, axis_labels=(None, 'axis=0', 'axis=1'))
va.ax.set_title('np.vstack(arr2.swapaxes(0,1))')
va.ax.dist = 7.7

plt.get_current_fig_manager().window.state('zoomed')
plt.show()
