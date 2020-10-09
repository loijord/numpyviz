# Warning: this might be quite slow to render visual array of shape (32, 32, 3)
import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

def tohex(arr):
    def tohexarr(x):
        form = list('#000000')
        c = np.base_repr(x, base=16)
        form[-len(c):] = list(c)
        return ''.join(form)
    arr = np.asarray(arr, dtype='uint32')
    hexarr = np.vectorize(tohexarr)
    return hexarr((arr[:, :, 0]<<16) + (arr[:, :, 1]<<8) + arr[:, :, 2])

def tolabels(arr):
    def tolabelarr(x):
        return r'\begin{array}{l}\,\,\sharp ' + x[1:4] + r'\\ \,\,\,\, ' + x[4:7] + r'\\ ' + r'\\ ' + r'\\ ' + r'\end{array}'
    labelarr = np.vectorize(tolabelarr)
    return labelarr(arr)

from PIL import Image
test_image = Image.open('cat.jpg')
test_image = test_image.resize((32, 32), Image.ANTIALIAS)
test_image = np.array(test_image).astype(int)
arr = tohex(test_image)

va = VisualArray(arr)
cells = va.get_indices()
x,y,z = cells.T
va.set_colors(cells.T, color=va.arr[x,y,z])
va.arr = tolabels(va.arr)
va.vizualize(fixview=True, scale=0.35, axis_labels=(None,None,None))
va.ax.dist = 11.5 #zoom out a little; change to 3.5 for higher zoom
plt.get_current_fig_manager().window.state('zoomed')
plt.show()


