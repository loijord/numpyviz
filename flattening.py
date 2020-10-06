import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

import matplotlib.gridspec as gridspec
arr = np.random.randint(99, size=24).reshape((3, 4, 2))
fig = plt.figure(constrained_layout=True)
spec = gridspec.GridSpec(ncols=5, nrows=1, figure=fig)
ax = fig.add_subplot(spec[0], projection='3d')
ax.set_title(f'body of shape={arr.shape}')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(va.get_indices().T, color='lawngreen', basecolor='aqua')
va.mix_colors(va.get_indices_chequerwise((1,1,arr.shape[2])).T, 'black')
va.vizualize(fixview=True, axis_labels=('axis=0','axis=1','axis=2'))

ax = fig.add_subplot(spec[1:], projection='3d')
ax.set_title(f'body of shape={arr.flatten().shape}')
va2 = VisualArray(va.arr.flatten(), fig=fig, ax=ax)
va2.set_colors(va2.get_indices().T, color='lawngreen', basecolor='aqua')
va2.mix_colors(va2.get_indices_chequerwise((1,1,arr.shape[2])).T, 'black')
va2.vizualize(fixview=True, axis_labels=(None,None,'axis=0'))
ax.dist = 8
plt.get_current_fig_manager().window.state('zoomed')
plt.show()

