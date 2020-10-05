"""this an example that demonstrates how to make a multiple
subplots that explains how np.argmin() works for axis=0,1 and 2"""

import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

def argmin_axis0(arr):
    a1 = np.argmin(arr, axis=0)
    a2, a3 = np.indices((arr.shape[1], arr.shape[2]))
    x, y, z = zip(*np.broadcast(a1, a2, a3))
    return x,y,z

def argmin_axis1(arr):
    a2 = np.argmin(arr, axis=1)
    a1, a3 = np.indices((arr.shape[0], arr.shape[2]))
    x, y, z = zip(*np.broadcast(a1, a2, a3))
    return x, y, z

def argmin_axis2(arr):
    a3 = np.argmin(arr, axis=2)
    a1, a2 = np.indices((arr.shape[0], arr.shape[1]))
    x, y, z = zip(*np.broadcast(a1, a2, a3))
    return x, y, z

fig = plt.figure()
arr = np.random.randint(100, size=60).reshape((2,6,5))
titles = ['np.argmin(arr, axis=0)', 'np.argmin(arr, axis=1)', 'np.argmin(arr, axis=2)']
result_titles = ['result along axis=0', 'result along axis=1', 'result along axis=2']
cells = [argmin_axis0(arr), argmin_axis1(arr), argmin_axis2(arr)]
cell_results = [np.argmin(arr, axis=0)[None,:,:], np.argmin(arr, axis=1)[:,None,:], np.argmin(arr, axis=2)[:,:,None]]
axis_names = [(None, 'axis=0', 'axis=1'), ('axis=0', None, 'axis=1'), ('axis=0', 'axis=1', None)]

for i in range(3):
    ax = fig.add_subplot(2, 3, 1 + i, projection='3d')
    ax.set_title(titles[i])
    va = VisualArray(arr, fig=fig, ax=ax)
    va.set_colors(cells[i], color='yellow', basecolor='lightblue')
    va.vizualize(fixview=True)

for i in range(3):
    ax = fig.add_subplot(2, 3, 4 + i, projection='3d')
    ax.set_title(result_titles[i])
    va = VisualArray(cell_results[i], fig=fig, ax=ax)
    va.set_colors(basecolor='lightgreen')
    va.vizualize(fixview=True, axis_labels=axis_names[i])

plt.show()