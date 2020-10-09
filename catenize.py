# Warning: this might be quite slow to render visual array of shape (32, 32, 3)
import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray
from time import time

def tohex(arr):
    #shape of array: (X,Y,3)
    #this is a vectorized version of arr of rgb -> arr of hex color codes
    def tohexarr(x):
        form = list('#000000')
        c = np.base_repr(x, base=16)
        form[-len(c):] = list(c)
        return ''.join(form)
    arr = np.asarray(arr, dtype='uint32')
    hexarr = np.vectorize(tohexarr)
    return hexarr((arr[:, :, 0]<<16) + (arr[:, :, 1]<<8) + arr[:, :, 2])\

from PIL import Image
test_image = Image.open('cat.jpg')
test_image = test_image.resize((32, 32), Image.ANTIALIAS)
test_image = np.array(test_image).astype(int)

t = time()
va = VisualArray(test_image)
coords = va.get_indices()
eye = np.eye(3, dtype=int)

#input of set_colors can be another array of len(cellsT)
for i in range(3):
    color = np.expand_dims(test_image[:,:,i], axis=2) * eye[i]
    cellsT = coords[coords[:, 2] == i].T #list of coords where z = i
    va.set_colors(cellsT, color=tohex(color)[cellsT[0], cellsT[1]])
va.vizualize(fixview=True, scale=0.7, axis_labels=(None,None,None))
va.ax.azim = 40 #change to 40 to see another back side
va.ax.elev = 20
va.ax.dist = 8 #zoom in a little
print(time() - t)
plt.get_current_fig_manager().window.state('zoomed')
plt.show()


