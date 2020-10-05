"""this example demonstrates how to image 3D numpy array
indices are colored in yellow if their sum is divisible by 3"""

import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

arr = np.arange(90).reshape((6,3,5))
coords = np.broadcast(*np.indices(arr.shape)) #indices of every cell
cells = zip(*[c for c in coords if sum(c) % 3 == 0])
va = VisualArray(arr)
va.set_colors(cells, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)
plt.show()