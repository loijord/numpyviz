#This is a trial version that contains a bug. Hopefully this will be resolved soon
#https://stackoverflow.com/questions/64235867/

import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

import matplotlib.gridspec as gridspec
arr = np.random.randint(99, size=(3,3,4))
fig = plt.figure(constrained_layout=True)
spec = gridspec.GridSpec(ncols=10, nrows=3, hspace=0.05, wspace=0.05, figure=fig)

ax = fig.add_subplot(spec[1,0], projection='3d')
ax.dist = 11 #zoom out a little
ax.set_title(f'arr of shape={arr.shape}')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(np.where(arr>65), color='lawngreen', basecolor='aqua')
va.vizualize(fixview=True, axis_labels=('axis=0','axis=1','axis=2'))

idx = np.indices(arr.shape)
for n in range(3):
    ax = fig.add_subplot(spec[n,2], projection='3d')
    ax.dist = 11 #zoom out a little
    ax.set_title(f'np.indices({arr.shape})[{n}]')
    va = VisualArray(idx[n], fig=fig, ax=ax)
    va.set_colors(np.where(arr>65), color='lightgreen', basecolor='lightblue')
    va.vizualize(fixview=True, axis_labels=('axis=0','axis=1','axis=2'))

for n in range(3):
    ax = fig.add_subplot(spec[n,4:], projection='3d')
    ax.dist = 5 #zoom in a little
    ax.set_title(f'np.where(arr)[{n}]')
    va = VisualArray(np.where(arr)[n], fig=fig, ax=ax)
    va.set_colors(basecolor='lightblue')
    va.vizualize(fixview=True, axis_labels=('axis=0','axis=1','axis=2'))


plt.get_current_fig_manager().window.state('zoomed')
plt.show()

