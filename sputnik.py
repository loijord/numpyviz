import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

v = np.array([[2,5,  3,5,  1,8],
              [4,6,  2,7,  5,9],
              [1,8,  2,3,  1,4],
              [2,8,  1,4,  3,5],
              [5,7,  2,3,  7,8],
              [1,2,  4,6,  3,5],
              [3,5,  2,8,  1,4]])

s = np.sort(v, axis=1)
arr1 = v[(s[:,:-1] != s[:,1:]).all(1)]
arr2 = arr1.reshape(-1, 3, 2)

fig = plt.figure()
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.set_title('Initial array')
va = VisualArray(arr1, fig=fig, ax=ax)
va.set_colors(va.get_indices().T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True, axis_labels=(None, 'axis=0', 'axis=1'))
ax.dist = 12

ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.set_title('Reshaped array')
va = VisualArray(arr2, fig=fig, ax=ax)
va.set_colors(va.get_indices().T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)
ax.dist = 12
plt.show()