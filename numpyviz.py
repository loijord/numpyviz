#Special thanks to https://stackoverflow.com/a/37423823/3044825
#Attention: https://github.com/matplotlib/matplotlib/issues/14175
#is used as workaround and Axes3D (+CTRL+ALT+B) in Line 448.
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D
from matplotlib.patches import PathPatch
from matplotlib import artist
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
import numpy as np

@artist.allow_rasterization
def draw(self, renderer):
    # draw the background patch
    self.patch.draw(renderer)
    self._frameon = False

    # first, set the aspect
    # this is duplicated from `axes._base._AxesBase.draw`
    # but must be called before any of the artist are drawn as
    # it adjusts the view limits and the size of the bounding box
    # of the axes
    locator = self.get_axes_locator()
    if locator:
        pos = locator(self, renderer)
        self.apply_aspect(pos)
    else:
        self.apply_aspect()

    # add the projection matrix to the renderer
    self.M = self.get_proj()
    renderer.M = self.M
    renderer.vvec = self.vvec
    renderer.eye = self.eye
    renderer.get_axis_position = self.get_axis_position

    # Calculate projection of collections and patches and zorder them.
    # Make sure they are drawn above the grids.
    zorder_offset = max(axis.get_zorder()
                        for axis in self._get_axis_list()) + 1
    for i, col in enumerate(
            sorted(self.collections,
                   key=lambda col: col.do_3d_projection(renderer),
                   reverse=True)):
        #col.zorder = zorder_offset + i
        col.zorder = col.stable_zorder + i
    for i, patch in enumerate(
            sorted(self.patches,
                   key=lambda patch: patch.do_3d_projection(renderer),
                   reverse=True)):
        #patch.zorder = zorder_offset + i
        patch.zorder = patch.stable_zorder + i

    if self._axis3don:
        # Draw panes first
        for axis in self._get_axis_list():
            axis.draw_pane(renderer)
        # Then axes
        for axis in self._get_axis_list():
            axis.draw(renderer)

    # Then rest
    super(Axes3D, self).draw(renderer)

Axes3D.draw = draw

class VisualArray:
    def __init__(self, arr, colors=None, fig=None, ax=None):
        if len(arr.shape) == 1:
            arr = arr[None,None,:]
        elif len(arr.shape) == 2:
            arr = arr[None,:,:]
        elif len(arr.shape) == 3:
            arr = arr[:,:,:]
        self.arr = arr
        if fig is None:
            self.fig = plt.figure()
        else:
            self.fig = fig
        if ax is None:
            self.ax = self.fig.gca(projection='3d')
        else:
            self.ax = ax
        self.ax.azim, self.ax.elev = -120, 30
        self.colors = colors

    def text3d(self, xyz, s, zdir="z", zorder=1, size=None, angle=0, usetex=False, **kwargs):
        d = {'-x': np.array([[-1.0, 0.0, 0], [0.0, 1.0, 0.0], [0, 0.0, -1]]),
             '-y': np.array([[0.0, 1.0, 0], [-1.0, 0.0, 0.0], [0, 0.0, 1]]),
             '-z': np.array([[1.0, 0.0, 0], [0.0, -1.0, 0.0], [0, 0.0, -1]])}

        x, y, z = xyz
        if "y" in zdir:
            x, y, z = x, z, y
        elif "x" in zdir:
            x, y, z = y, z, x
        elif "z" in zdir:
            x, y, z = x, y, z

        text_path = TextPath((-0.5, -0.5), s, size=size, usetex=usetex)
        aff = Affine2D()
        trans = aff.rotate(angle)

        # apply additional rotation of text_paths if side is dark
        if '-' in zdir:
            trans._mtx = np.dot(d[zdir], trans._mtx)
        trans = trans.translate(x, y)
        p = PathPatch(trans.transform_path(text_path), **kwargs)
        self.ax.add_patch(p)
        art3d.pathpatch_2d_to_3d(p, z=z, zdir=zdir)
        p.stable_zorder = zorder
        return p

    def on_rotation(self, event):
        vrot_idx = [self.ax.elev > 0, True].index(True)
        v_zorders = 10000 * np.array([(1, -1), (-1, 1)])[vrot_idx]
        for side, zorder in zip((self.side1, self.side4), v_zorders):
            for patch in side:
                patch.stable_zorder = zorder

        hrot_idx = [self.ax.azim < -90, self.ax.azim < 0, self.ax.azim < 90, True].index(True)
        h_zorders = 10000 * np.array([(1, 1, -1, -1), (-1, 1, 1, -1),
                              (-1, -1, 1, 1), (1, -1, -1, 1)])[hrot_idx]
        sides = (self.side3, self.side2, self.side6, self.side5)
        for side, zorder in zip(sides, h_zorders):
            for patch in side:
                patch.stable_zorder = zorder

    def voxelize(self):
        shape = self.arr.shape[::-1]
        x, y, z = np.indices(shape)
        arr = (x < shape[0]) & (y < shape[1]) & (z < shape[2])
        if self.colors is not None:
            colors = np.swapaxes(self.colors, 0, 2)[:, ::-1, ::-1].copy()
        else:
            colors = None
        self.ax.voxels(arr, facecolors=colors, edgecolor='k')
        for col in self.ax.collections:
            col.stable_zorder = col.zorder

    def labelize(self, scale=1):
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_rotation)
        s = self.arr.shape
        self.side1, self.side2, self.side3, self.side4, self.side5, self.side6 = [], [], [], [], [], []
        # labelling surfaces of side1 and side4
        surf = np.indices((s[2], s[1])).T[::-1].reshape(-1, 2) + 0.5
        surf_pos1 = np.insert(surf, 2, self.arr.shape[0], axis=1)
        surf_pos2 = np.insert(surf, 2, 0, axis=1)
        labels1 = (self.arr[0]).flatten()
        labels2 = (self.arr[-1]).flatten()
        for xyz, label in zip(surf_pos1, [f'${n}$' for n in labels1]):
            t = self.text3d(xyz, label, zdir="z", zorder=10000, size=scale, usetex=True, ec="none", fc="k")
            self.side1.append(t)
        for xyz, label in zip(surf_pos2, [f'${n}$' for n in labels2]):
            t = self.text3d(xyz, label, zdir="-z", zorder=-10000, size=scale, usetex=True, ec="none", fc="k")
            self.side4.append(t)

        # labelling surfaces of side2 and side5
        surf = np.indices((s[2], s[0])).T[::-1].reshape(-1, 2) + 0.5
        surf_pos1 = np.insert(surf, 1, 0, axis=1)
        surf = np.indices((s[0], s[2])).T[::-1].reshape(-1, 2) + 0.5
        surf_pos2 = np.insert(surf, 1, self.arr.shape[1], axis=1)
        labels1 = (self.arr[:, -1]).flatten()
        labels2 = (self.arr[::-1, 0].T[::-1]).flatten()
        for xyz, label in zip(surf_pos1, [f'${n}$' for n in labels1]):
            t = self.text3d(xyz, label, zdir="y", zorder=10000, size=scale, usetex=True, ec="none", fc="k")
            self.side2.append(t)
        for xyz, label in zip(surf_pos2, [f'${n}$' for n in labels2]):
            t = self.text3d(xyz, label, zdir="-y", zorder=-10000, size=scale, usetex=True, ec="none", fc="k")
            self.side5.append(t)

        # labelling surfaces of side3 and side6
        surf = np.indices((s[1], s[0])).T[::-1].reshape(-1, 2) + 0.5
        surf_pos1 = np.insert(surf, 0, self.arr.shape[2], axis=1)
        surf_pos2 = np.insert(surf, 0, 0, axis=1)
        labels1 = (self.arr[:, ::-1, -1]).flatten()
        labels2 = (self.arr[:, ::-1, 0]).flatten()
        for xyz, label in zip(surf_pos1, [f'${n}$' for n in labels1]):
            t = self.text3d(xyz, label, zdir="x", zorder=-10000, size=scale, usetex=True, ec="none", fc="k")
            self.side6.append(t)
        for xyz, label in zip(surf_pos2, [f'${n}$' for n in labels2]):
            t = self.text3d(xyz, label, zdir="-x", zorder=10000, size=scale, usetex=True, ec="none", fc="k")
            self.side3.append(t)

    def drawaxis(self, axis_labels=('axis=0', 'axis=1', 'axis=2')):
        # labelling axis
        s = self.arr.shape
        if axis_labels[0] is not None:
            self.text3d((-0.5, -0.25, s[0] / 2), axis_labels[0], angle=0.5 * np.pi, zdir='y', size=.5,
                        usetex=False, ec="purple", fc="purple")
        if axis_labels[1] is not None:
            self.text3d((0, s[1]/2, 0), axis_labels[1], angle=-0.5*np.pi, zdir='z', size=.5,
                        usetex=False, ec="purple", fc="purple")
        if axis_labels[2] is not None:
            self.text3d((s[2] / 2, 0, 0), axis_labels[2], zdir='z', size=.5,
                        usetex=False, ec="purple", fc="purple")

    @staticmethod
    def colorFader(c1, c2, r=0.0):
        # fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
        c1 = np.array(colors.to_rgb(c1))
        c2 = np.array(colors.to_rgb(c2))
        return colors.to_hex((1 - r) * c1 + r * c2)

    def set_colors(self, xyz=None, color='yellow', basecolor='lightblue'):
        if self.colors is None:
            self.colors = np.full(self.arr.shape, fill_value=basecolor, dtype=object)
        if xyz is not None:
            x, y, z = xyz
            self.colors[x, y, z] = color

    def mix_colors(self, xyz, color='black', r=0.4):
        if self.colors is None:
            raise ValueError('No initial color to mix with')
        else:
            x, y, z = xyz
            self.colors[x,y,z] = [self.colorFader(c, color, r=r) for c in self.colors[x,y,z]]

    def vizualize(self, fixview=False, axis_labels=('axis=0', 'axis=1', 'axis=2'), scale=1):
        self.voxelize()
        self.labelize(scale)
        self.drawaxis(axis_labels=axis_labels)
        if fixview:
            self.fix_view()
        plt.axis('off')

    def fix_view(self, scalefactor=1.5):
        # preserves constant lengths of cube edges but contains a bug
        bbox = np.array([getattr(self.ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
        bbox_center = np.mean(bbox, axis=1)
        bbox_dim = np.max(bbox, axis=1) - np.min(bbox, axis=1)
        scaling_factors = scalefactor * bbox_dim / np.max(bbox_dim)
        tr1, tr2, tr3 = bbox_center
        s1, s2, s3 = scaling_factors
        A = np.array([[1, 0, 0, -tr1], [0, 1, 0, -tr2], [0, 0, 1, -tr3], [0, 0, 0, 1]])
        T = np.array([[s1, 0, 0, 0], [0, s2, 0, 0], [0, 0, s3, 0], [0, 0, 0, 1]]) #replace s3 with 2*s3 sometimes
        B = np.array([[1, 0, 0, tr1], [0, 1, 0, tr2], [0, 0, 1, tr3], [0, 0, 0, 1]])
        self.ax.get_proj = lambda: np.dot(np.dot(np.dot(Axes3D.get_proj(self.ax), B), T), A)

    def get_indices(self):
        return np.array(list(np.broadcast(*np.indices(self.arr.shape))))

    def reshape(self, *args):
        #assigns reshaped copy to both self.arr and self.colors
        self.arr = self.arr.reshape(*args)
        self.colors = self.colors.reshape(*args)

    def get_indices_chequerwise(self, window):
        coords = self.get_indices()
        return coords[np.sum(coords // window, axis=1) % 2 == 0]

    def permute(self, shape):
        if len(shape) > 6:
            raise ValueError('Permuting > 6 dimensions is not supported')
        elif len(shape) < 4:
            raise ValueError('Permuting less than 4 dimensions is not accepted')
        shape_layer = np.ones(3).astype(int)
        shape_layer[:len(shape)-3]= shape[:-3]
        print(shape_layer)
        self.reshape(np.array(shape[-3:]) * shape_layer)  # dynamical reshape of va2.arr and va2.colors
        cells = self.get_indices_chequerwise(window=shape[-3:])
        self.mix_colors(cells.T, 'black', r=0.4)