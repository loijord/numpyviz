import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

arr = np.random.randint(99, size=1260).reshape((10,9,14))
shape = (7,2,3,2,5,3)

fig = plt.figure('dimension')
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.set_title(f'body of shape={arr.shape}')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(va.get_indices().T, color='lawngreen', basecolor='aqua')
va.vizualize(fixview=False, axis_labels=('axis=0','axis=1','axis=2'))

ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.set_title(f'body of shape={shape}')
va2 = VisualArray(va.arr, va.colors, fig=fig, ax=ax)
va2.permute(shape)
va2.vizualize(fixview=True, axis_labels=('axis=0','axis=1','axis=2'))
plt.get_current_fig_manager().window.state('zoomed')
plt.show()

