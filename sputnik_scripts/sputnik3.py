"""this example demonstrates how to make a multiple
subplots of a VisualArray in multiple sides"""

import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

arr = np.array([[[1,2,13],
     [12,2,32],
     [61,2,6],
     [1,23,3],
     [1,21,3],
     [91,2,38]]])

fig = plt.figure()
ax = fig.add_subplot(1, 3, 1, projection='3d')
ax.set_title('a = array of shape (1, 6, 3)')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(np.array(list(np.ndindex(arr.shape))).T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)

arr = arr[:,:,:2]
ax = fig.add_subplot(1, 3, 2, projection='3d')
ax.set_title('a = a[:,:,:2] \n'
             'a is of shape (1, 6, 2) now')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(np.array(list(np.ndindex(arr.shape))).T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)

arr = arr.squeeze()
ax = fig.add_subplot(1, 3, 3, projection='3d')
ax.set_title('a = a.squeeze() \n'
             'a is of shape (6, 2) now')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(np.array(list(np.ndindex(va.arr.shape))).T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True, axis_labels=(None, 'axis=0', 'axis=1'))
plt.get_current_fig_manager().window.state('zoomed')
plt.show()