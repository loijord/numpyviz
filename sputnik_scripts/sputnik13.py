import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

num= 2
x = np.linspace(0, 99, num)
arr = np.meshgrid(x,x,x,x)[0].astype(int) #at first cube is 4 dimensional
fig = plt.figure('dimension')
ax = fig.add_subplot(2, 3, 1, projection='3d')
ax.set_title(f'meshgrid(x,x,x,x)[0]'+'\n'+f' of shape=({num},{num},{num},{num})')
va = VisualArray(arr.reshape((-1, num, num)), fig=fig, ax=ax)
va.set_colors(va.get_indices().T, color='lawngreen', basecolor='aqua')
va.permute(arr.shape)
va.vizualize(fixview=True, axis_labels=('axis=0+3','axis=1','axis=2'))


arr2 = arr.reshape(4, num ** 4 // 4)
ax = fig.add_subplot(2, 3, 2, projection='3d')
ax.set_title(f'meshgrid(x,x,x,x)[0].reshape(4, {num} ** 4 // 4)')
va = VisualArray(arr2, fig=fig, ax=ax)
va.set_colors(va.get_indices().T, color='lawngreen', basecolor='aqua')
va.vizualize(fixview=True, axis_labels=(None, 'axis=0','axis=1'))
ax.dist=11

arr3 = np.stack(np.meshgrid(x,x,x,x), axis=-1).astype(int)
ax = fig.add_subplot(2, 3, 4, projection='3d')
ax.set_title(f'st = np.stack(np.meshgrid(x,x,x,x), axis=-1)')
va = VisualArray(arr3.reshape((-1, num, num)), fig=fig, ax=ax)
va.set_colors(va.get_indices().T, color='lawngreen', basecolor='aqua')
va.permute(arr3.shape)
va.vizualize(fixview=True, axis_labels=('axis=0+3','axis=1+4','axis=2'))
ax.dist=12

arr4 = np.stack(np.meshgrid(x,x,x,x), axis=-1).reshape(-1, 4).astype(int)
ax = fig.add_subplot(2, 3, 5, projection='3d')
ax.set_title(f'st.reshape(-1, 4)')
va = VisualArray(arr4, fig=fig, ax=ax)
va.set_colors(va.get_indices().T, color='lawngreen', basecolor='aqua')
va.vizualize(fixview=True, axis_labels=(None,'axis=0','axis=1'), usetex=False, scale=0.8)
ax.dist=8

arr5 = np.stack(np.meshgrid(x,x,x,x), axis=-1).reshape(4, -1).astype(int)
ax = fig.add_subplot(2, 3, 6, projection='3d')
ax.set_title(f'st.reshape(4, -1)')
va = VisualArray(arr5, fig=fig, ax=ax)
va.set_colors(va.get_indices().T, color='lawngreen', basecolor='aqua')
va.vizualize(fixview=True, axis_labels=(None,'axis=0','axis=1'), usetex=False, scale=0.8)
ax.dist=8
plt.get_current_fig_manager().window.state('zoomed')
#ax.azim, ax.elev = -115, 24
plt.show()