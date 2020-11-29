import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

a = np.array([[1, 2, 3], [3, 4, 5]])
b = np.array([[[1, 0, 1], [1, 1, 0], [0, 1, 1]], [[1, 1, 1], [0, 1, 0], [0, 0, 1]]])
c = np.array([1, 2, 3])

fig = plt.figure()
ax = fig.add_subplot(2, 3, 1, projection='3d')
va1 = VisualArray(a[:,None,:], fig=fig, ax=ax)
va1.ax.set_title(f'a[:,None,:] of shape=(2, 1, 3)')
va1.set_colors(va1.get_indices().T, color='lightgreen', basecolor='aqua')
va1.vizualize(fixview=True, usetex=False, scale=1.2)
va1.ax.dist = 12

ax = fig.add_subplot(2, 3, 2, projection='3d')
va2 = VisualArray(b, fig=fig, ax=ax)
va2.ax.set_title(f'b of shape=(2, 3, 3)')
va2.set_colors(va2.get_indices().T, color='lightgreen', basecolor='aqua')
va2.vizualize(fixview=True, usetex=False, scale=1.2)
va2.ax.dist = 12

ax = fig.add_subplot(2, 3, 3, projection='3d')

va3 = VisualArray(c, fig=fig, ax=ax)
va3.ax.set_title(f'c of shape=(3,)')

va3.set_colors(va3.get_indices().T, color='lightgreen', basecolor='aqua')
va3.vizualize(fixview=True, axis_labels=(None, None, 'axis=0'), usetex=False, scale=1.2)
va3.ax.dist = 12

ax = fig.add_subplot(2, 3, 4, projection='3d')
arr = a[:,None,:] * b
va4 = VisualArray(arr, fig=fig, ax=ax)
va4.ax.set_title(f'a[:,None,:] * b of shape=(2, 3, 3)')
va4.set_colors(va4.get_indices().T, color='lightgreen', basecolor='aqua')
va4.vizualize(fixview=True, usetex=False, scale=1.2)
va4.ax.dist = 12

ax = fig.add_subplot(2, 3, 5, projection='3d')
arr = np.sum((a[:,None,:] * b), axis=2)
va5 = VisualArray(arr, fig=fig, ax=ax)
va5.ax.set_title(f'np.sum((a[:,None,:] * b), axis=2) \n of shape=(2, 3)')
va5.set_colors(va5.get_indices().T, color='lightgreen', basecolor='aqua')
va5.vizualize(fixview=True, axis_labels=(None, 'axis=0', 'axis=1'), usetex=False, scale=0.8)
va5.ax.dist = 12

ax = fig.add_subplot(2, 3, 6, projection='3d')
arr = np.around(np.sum((a[:,None,:] * b), axis=2)/c,1)
va6 = VisualArray(arr, fig=fig, ax=ax)
va6.arr = np.array([[[format(n, '.10g') for n in m] for m in o] for o in va6.arr])
va6.ax.set_title(f'np.sum((a[:,None,:] * b), axis=2)/c \n of shape=(2, 3)')
va6.set_colors(va6.get_indices().T, color='lightgreen', basecolor='aqua')
va6.vizualize(fixview=True, axis_labels=(None, 'axis=0', 'axis=1'), usetex=False, scale=0.7)
va6.ax.dist = 12
plt.get_current_fig_manager().window.state('zoomed')
plt.show()



