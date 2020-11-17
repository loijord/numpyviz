"""this example demonstrates how to image 3D numpy array
indices are colored in yellow if their sum is divisible by 3"""

import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

arr = np.arange(90).reshape((6,3,5))
va = VisualArray(arr)
coords = va.get_indices()
cells = coords[np.sum(coords, axis=1) % 3 == 0]
va.set_colors(cells.T, color='yellow', basecolor='lightblue')
va.vizualize(fixview=True)
plt.show()