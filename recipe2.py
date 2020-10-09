"""this is an example that demonstrates how to multiply two polynomials"""

import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

arr = np.array([[r'$\times$', r'$x^2$', r'$y^2$', r'$z^2$', r'$-xy$', r'$-yz$', r'$-xz$'],
                [r'$x$', r'$x^3$', r'$xy^2$', r'$xz^2$', r'$-x^2y$', r'$-xyz$', r'$-x^2z$'],
                [r'$y$', r'$x^2y$', r'$y^3$', r'$yz^2$', r'$-xy^2$', r'$-y^2z$', r'$-xyz$'],
                [r'$z$', r'$x^2z$', r'$y^2z$', r'$z^3$', r'$-xyz$', r'$-yz^2$', r'$-xz^2$']])
va = VisualArray(arr)
blue = [(0,i,0) for i in range(1,4)] + [(0,0,i) for i in range(1,7)]
lime = [(0,1,1), (0,2,2), (0,3,3), (0,1,-2), (0,2,-1), (0,3,-3)]
va.set_colors(zip(*blue), color='lightblue', basecolor='white')
va.set_colors(zip(*lime), color='lime')
va.set_colors(zip(*[(0,2,-2), (0,-1,2)]), color='#ffff00')
va.set_colors(zip(*[(0,1,2), (0,2,4)]), color='#dddd00')
va.set_colors(zip(*[(0,1,3), (0,-1,-1)]), color='#bbbb00')
va.set_colors(zip(*[(0,1,4), (0,2,1)]), color='#999900')
va.set_colors(zip(*[(0,1,6), (0,-1,1)]), color='#777700')
va.set_colors(zip(*[(0,2,3), (0,-1,-2)]), color='#555500')
va.vizualize(fixview=True,
             axis_labels = [None, '$x+y+z$', r'$' + r'\!'*35 + r' x^2+y^2+z^2-xy-yz-zx$'],
             scale=0.4)
va.ax.set_title('Why $(x+y+z)(x^2+y^2+z^2-xy-yz-zx) = x^3+y^3+z^3-3xyz$? \n Simplify monochromatic pairs of yellow cubes!')
va.ax.azim, va.ax.elev = -108, 54
plt.show()