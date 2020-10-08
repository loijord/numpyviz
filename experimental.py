#This is an issue opened at https://stackoverflow.com/questions/64235867

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D

def fix_view(ax, scalefactor=1.5):
    # preserves constant lengths of cube edges
    bbox = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
    bbox_center = np.mean(bbox, axis=1)
    bbox_dim = np.max(bbox, axis=1) - np.min(bbox, axis=1)
    scaling_factors = scalefactor * bbox_dim / np.max(bbox_dim)
    tr1, tr2, tr3 = bbox_center
    s1, s2, s3 = scaling_factors
    A = np.array([[1, 0, 0, -tr1], [0, 1, 0, -tr2], [0, 0, 1, -tr3], [0, 0, 0, 1]])
    T = np.array([[s1, 0, 0, 0], [0, s2, 0, 0], [0, 0, s3, 0], [0, 0, 0, 1]])
    B = np.array([[1, 0, 0, tr1], [0, 1, 0, tr2], [0, 0, 1, tr3], [0, 0, 0, 1]])
    ax.get_proj = lambda: np.dot(np.dot(np.dot(Axes3D.get_proj(ax), B), T), A)

def draw(spec, row, col):
    ax = fig.add_subplot(spec[row, col], projection='3d')
    ax.set_title('body of shape = (8, 1, 1)')
    ax.voxels(arr, facecolors='aqua', edgecolors='k')
    fix_view(ax, scalefactor=1.5)
    #ax.axis('off')

arr = np.ones(shape=(8,1,1), dtype=bool)
fig = plt.figure(constrained_layout=True)
spec = gridspec.GridSpec(ncols=10, nrows=3, figure=fig, wspace=0.025, hspace=0.05)

for i in range(3):
    draw(spec, i, 0)
    draw(spec, i, slice(1,10))

plt.show()

