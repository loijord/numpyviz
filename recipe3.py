"""this is an example that demonstrates how to multiply three polynomials"""

import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

arr = np.array([[[r'$x^2y$', r'$xy^2$'],[r'$xy^2$', r'$y^3$']],
                [[r'$x^3$', r'$x^2y$'],[r'$x^2y$', r'$xy^2$']]])
va = VisualArray(arr)
va.set_colors(np.where(arr=='$y^3$'), color='#6666ff')
va.set_colors(np.where(arr=='$x^3$'), color='#ff66ff')
va.set_colors(np.where(arr=='$x^2y$'), color='#66ff66')
va.set_colors(np.where(arr=='$xy^3$'), color='#66ffff')
va.vizualize(fixview=False,
             axis_labels = ['$x+y$', '$x+y$', '$x+y$'],
             scale=0.7)
va.ax.set_title('Why $(x+y)^3 = x^3+3x^2y+3xy^2+y^3$?')
plt.show()