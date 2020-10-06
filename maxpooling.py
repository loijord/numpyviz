import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

arr = np.random.randint(99, size=96).reshape((1,8,12))
w = (2, 4)

fig = plt.figure()
ax = fig.add_subplot(1, 3, 1, projection='3d')
ax.set_title('image')
va = VisualArray(arr, fig=fig, ax=ax) #indices of every cell
cells = va.get_indices_chequerwise(window=(1,)+w)
va.set_colors(cells.T, color='lawngreen', basecolor='aqua')
va.vizualize(fixview=True, axis_labels=(None,'axis=1','axis=0'))

ax = fig.add_subplot(1, 3, 2, projection='3d')
va2 = VisualArray(va.arr, va.colors, fig=fig, ax=ax) #shape: (1, 8, 12)
shape = (va2.arr.shape[1]//w[0], w[0], va2.arr.shape[2]//w[1], w[1])
ax.set_title(f'image.reshape{shape}')
va2.reshape(shape) #shape: (4, 2, 3, 4)
new_arr, new_colors = va2.arr.copy(), va2.colors.copy()
va2.permute(shape)
va2.vizualize(fixview=True, axis_labels=('axis=0','axis=1','axis=2'))

def argmin(arr):
    #bug...
    a2 = arr.argmin(axis=1)
    a4 = arr.argmin(axis=3)
    a1, a3 = np.indices((arr.shape[0], arr.shape[2]))
    x, y, z, t = zip(*np.broadcast(a1, a2, a3, a4))
    return x, y, z, t

ax = fig.add_subplot(1, 3, 3, projection='3d')
va3 = VisualArray(new_arr, new_colors, fig=fig, ax=ax) #shape: (1, 8, 12)
ax.set_title(f'image.reshape{shape}.max(axis=(1,3)) \n Not implemented yet')
ax.axis('off')
# va3.set_colors(argmin(new_arr), 'yellow')
#va3.permute(shape)
#va3.vizualize(fixview=True, axis_labels=('axis=0','axis=1','axis=2'))
plt.show()

