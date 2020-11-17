"""this example demonstrates how to image 3D numpy array
indices are colored in yellow if their sum is divisible by 3"""

import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

def bin_to_num(arr):
    return [str(b.dot(1 << np.arange(b.size)[::-1])) \
                            for b in arr.reshape(-1, 8)]

def underbrace(num):
    return num
    #return r'\underbrace{' + r'\,' * 40 + '}_{' + num + '}'

n= 24
arr = np.random.randint(2, size=n)
va = VisualArray(arr)
coords = va.get_indices()
cells = coords[np.transpose(arr.nonzero())]
va.set_colors(cells.T, color='yellow', basecolor='lightblue')
va.permute(shape=((1, 1, -1, 1, 1, 8)))
s = r'$'+ ('\!')*90 + (('\,')*90).join(bin_to_num(arr))+ r'$'
#(r'\!'*150) +useaxistex

va.vizualize(fixview=True, axis_labels=(None, None, s), useaxistex=False)
plt.show()