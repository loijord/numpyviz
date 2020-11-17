"""this is an example that demonstrates how to multiply five polynomials"""
import numpy as np
import matplotlib.pyplot as plt
from numpyviz import VisualArray

fig = plt.figure()
arr = np.array([[[r'$x^3y^2$', r'$x^2y^3$'],[r'$x^2y^3$', r'$xy^4$']],
                [[r'$x^2y^3$', r'$xy^4$'],[r'$xy^4$', r'$y^5$']],
                [[r'$x^4y$', r'$x^3y^2$'],[r'$x^3y^2$', r'$x^2y^3$']],
                [[r'$x^3y^2$', r'$x^2y^3$'],[r'$x^2y^3$', r'$xy^4$']],
                [[r'$x^4y$', r'$x^3y^2$'], [r'$x^3y^2$', r'$x^2y^3$']],
                [[r'$x^3y^2$', r'$x^2y^3$'], [r'$x^2y^3$', r'$xy^4$']],
                [[r'$x^5$', r'$x^4y$'], [r'$x^4y$', r'$x^3y^2$']],
                [[r'$x^4y$', r'$x^3y^2$'], [r'$x^3y^2$', r'$x^2y^3$']]])

ax = fig.add_subplot(1, 2, 1, projection='3d')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(np.where(arr=='$x^5$'), color='#6666ff')
va.set_colors(np.where(arr=='$x^4y$'), color='#66ff66')
va.set_colors(np.where(arr=='$x^3y^2$'), color='#ff6666')
va.set_colors(np.where(arr=='$x^2y^3$'), color='#ffff66')
va.set_colors(np.where(arr=='$xy^4$'), color='#ff66ff')
va.set_colors(np.where(arr=='$y^5$'), color='#66ffff')
va.permute(shape=(2,2,2,2,2))
va.vizualize(fixview=True,
             axis_labels = [r'$\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!'+'x(x+y)\!\!+\!\!y(x+y)$',
                            r'$\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!'+'x(x+y)\!\!+\!\!y(x+y)$',
                            r'$\!\!x+y$'],
             scale=0.6)
va.ax.set_title(r'Why $(x+y)^5 = x^5+5x^4y+10x^3y^2+10x^2y^3+5xy^4+y^5$?' +'\n' +
                r'Multiply each $2\times 2 \times 2$ subcube by $x^2$, $xy$, $xy$, $y^2$' +
                '\n' + r'Then reduce monochromatic terms')
va.ax.dist = 11.5

ax = fig.add_subplot(1, 2, 2, projection='3d')
va = VisualArray(arr, fig=fig, ax=ax)
va.set_colors(np.where(arr=='$x^5$'), color='#6666ff')
va.set_colors(np.where(arr=='$x^4y$'), color='#66ff66')
va.set_colors(np.where(arr=='$x^3y^2$'), color='#ff6666')
va.set_colors(np.where(arr=='$x^2y^3$'), color='#ffff66')
va.set_colors(np.where(arr=='$xy^4$'), color='#ff66ff')
va.set_colors(np.where(arr=='$y^5$'), color='#66ffff')
va.permute(shape=(2,2,2,2,2))
va.vizualize(fixview=True,
             axis_labels = [r'$\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!'+'x(x+y)\!\!+\!\!y(x+y)$',
                            r'$\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!'+'x(x+y)\!\!+\!\!y(x+y)$',
                            r'$\!\!x+y$'],
             scale=0.6)
va.ax.set_title(r'BACKSIDE CAMERA')

va.ax.azim, va.ax.elev, va.ax.dist = -55, 35, 11.5
plt.get_current_fig_manager().window.state('zoomed')
plt.show()