import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

arr = np.array([[1., 1., 1., 0., 0., 0., 0., 1., 2., 0., 0., 0.],
       [1., 1., 1., 0., 0., 0., 3., 4., 5., 0., 0., 0.],
       [1., 1., 1., 0., 0., 0., 6., 7., 8., 0., 0., 0.],
       [0., 0., 0., 2., 2., 2., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 2., 2., 2., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 2., 2., 2., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 3., 3., 3., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 3., 3., 3., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 3., 3., 3., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 4., 4., 4.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 4., 4., 4.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 4., 4., 4.]]).reshape((1, 12, 12)).astype(int)

arr2 = np.array([[1., 0., 0., 0., 1., 0., 1., 0., 1., 0., 2., 0.],
       [0., 2., 0., 0., 0., 2., 0., 0., 0., 2., 0., 0.],
       [0., 0., 3., 0., 0., 0., 3., 0., 0., 0., 3., 0.],
       [0., 0., 0., 4., 0., 0., 0., 4., 0., 0., 0., 4.],
       [1., 0., 3., 0., 1., 0., 4., 0., 1., 0., 5., 0.],
       [0., 2., 0., 0., 0., 2., 0., 0., 0., 2., 0., 0.],
       [0., 0., 3., 0., 0., 0., 3., 0., 0., 0., 3., 0.],
       [0., 0., 0., 4., 0., 0., 0., 4., 0., 0., 0., 4.],
       [1., 0., 6., 0., 1., 0., 7., 0., 1., 0., 8., 0.],
       [0., 2., 0., 0., 0., 2., 0., 0., 0., 2., 0., 0.],
       [0., 0., 3., 0., 0., 0., 3., 0., 0., 0., 3., 0.],
       [0., 0., 0., 4., 0., 0., 0., 4., 0., 0., 0., 4.]]).reshape((1, 12, 12)).astype(int)

fig = plt.figure()
ax = fig.add_subplot(2, 3, 1, projection='3d')
va1 = VisualArray(arr, fig=fig, ax=ax)
va1.ax.set_title(f'input')
va1.set_colors(va1.get_indices().T, color='lightgreen', basecolor='aqua')
va1.vizualize(fixview=True, axis_labels=(None, 'axis=0','axis=1'), usetex=False, scale=1.2)
va1.ax.dist = 12
va1.azim, va1.elev= -90, 45

ax = fig.add_subplot(2, 3, 2, projection='3d')
va2 = VisualArray(arr, fig=fig, ax=ax)
va2.ax.set_title(f'input <-> input.reshape((4, 3, 4, 3))')
w = (3, 3)
shape = (arr.shape[1]//w[0], w[0], arr.shape[2]//w[1], w[1])
print(shape)
va2.set_colors(va2.get_indices().T, color='lightgreen', basecolor='aqua')
va2.permute(shape)
va2.vizualize(fixview=True, axis_labels=('axis=0+3', 'axis=1', 'axis=2'), usetex=False, scale=1.2)
va2.ax.dist = 8

ax = fig.add_subplot(2, 3, 3, projection='3d')
old_shape = arr.shape
arr = arr.reshape(shape)
arr = arr.swapaxes(1, 0)
arr_final = arr.swapaxes(0, 2)
arr_final_shape = arr_final.shape
shape = arr.shape
arr = arr.reshape(old_shape)

va2a = VisualArray(arr, fig=fig, ax=ax)
va2a.ax.set_title(f'input -> input.swapaxes(0, 1)')

va2a.set_colors(va2a.get_indices().T, color='lightgreen', basecolor='aqua')
va2a.permute(shape)
va2a.vizualize(fixview=True, axis_labels=('axis=0+3', 'axis=1', 'axis=2'), usetex=False, scale=1.2)
va2a.ax.dist = 8


ax = fig.add_subplot(2, 3, 6, projection='3d')
val = VisualArray(va2a.arr.swapaxes(1,2), fig=fig, ax=ax)
val.ax.set_title(f'input -> input.swapaxes(2, 3)')

val.set_colors(val.get_indices_chequerwise(window=(4,3,4)).T, color='darkgreen', basecolor='lightgreen')
#val.permute((arr2.shape[1]//w[0], arr2.shape[2]//w[1], w[0], w[1]))
val.vizualize(fixview=True, axis_labels=('axis=0+3', 'axis=1', 'axis=2'), usetex=False, scale=1.2)
val.ax.dist = 8

ax = fig.add_subplot(2, 3, 4, projection='3d')
va3 = VisualArray(arr2, fig=fig, ax=ax)
va3.ax.set_title(f'output')
va3.set_colors(va3.get_indices().T, color='lightgreen', basecolor='aqua')
va3.ax.dist = 12
va3.azim, va3.elev= -90, 45
va3.vizualize(fixview=True, axis_labels=(None, 'axis=0','axis=1'), usetex=False, scale=1.2)


ax = fig.add_subplot(2, 3, 5, projection='3d')
va4 = VisualArray(arr2, fig=fig, ax=ax)
va4.ax.set_title(f'output <-> output.reshape((4, 3, 4, 3))')
w = (4, 4)
shape = (arr2.shape[1]//w[0], w[0], arr2.shape[2]//w[1], w[1])
va4.set_colors(va4.get_indices().T, color='lightgreen', basecolor='aqua')
va4.permute(shape)
print(shape)
va4.vizualize(fixview=True, axis_labels=('axis=0+3', 'axis=1', 'axis=2'), usetex=False, scale=1.2)
va4.ax.dist = 8
plt.get_current_fig_manager().window.state('zoomed')
plt.show()
