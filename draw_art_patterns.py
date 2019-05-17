# Code here is adapted from https://github.com/eleanorlutz/AnimatedPythonPatterns

from __future__ import division
import os, glob, string, math, random
import numpy as np
import imageio
import matplotlib.pyplot as plt 
from matplotlib import patches


#=====================================================
# Initializations
#-----------------------------------------------------
# Colour names are at https://matplotlib.org/gallery/color/named_colors.html
color_palette = (
    ('#D9CB84', '#A99E46', '#737D26', '#3F522B', '#302B1D'),
    ('#C24704', '#D9CC3C', '#fff7c9', '#A0E0BA', '#00ADA7'),
    ('lightcoral', 'yellowgreen', 'lavender', 'slategrey', 'orange'),
    ('#000000', '#333333', '#777777', '#999999', '#CCCCCC')
)
width, length = 28, 14


#=====================================================
# Functions
#-----------------------------------------------------
def rotate_2d(pts,cnt,ang=np.pi/4):
    '''pts = {} Rotates points(nx2) about center cnt(2) by angle ang(1) in radian'''
    return np.dot(pts-cnt, np.array([[np.cos(ang), np.sin(ang)],
                                     [-np.sin(ang), np.cos(ang)]])) + cnt


def add_shape(sub, points, degrees=0, alphaParam=1, ec='none', l=0, jn='round'):
    '''Finalize rotation and add shape to plot.'''
    # "points" should consist of the list returned from any of the
    # geometry functions below (side4, side8)
    origin = points[-2]
    color = points[-1]
    newPoints = list(points)
    del newPoints[-1]
    del newPoints[-1]
    
    pts = np.array(newPoints)
    radians = degrees * np.pi / 180
    ots = rotate_2d(pts,np.array([origin]),radians) 
    sub.add_patch(patches.Polygon(ots, fc=color, ec=ec, 
        alpha=alphaParam, joinstyle=jn, lw=l, rasterized=True))


def side4(w, oX, oY, c, e=0):
    '''Makes a polygon with 4 sides of length w, centered around the origin.'''
    p1 = [oX-w/float(2), oY-w/float(2)]
    p2 = [oX-(w-e)/float(2), oY+(w-e)/float(2)]
    p3 = [oX+w/float(2), oY+w/float(2)]
    p4 = [oX+(w-e)/float(2), oY-(w-e)/float(2)]
    return([p1, p2, p3, p4, [oX, oY], c])


def side8(w, oX, oY, c, e=0):
    '''Makes a polygon with 8 sides of length w, centered around the origin.'''
    pts = side4(math.sqrt(2)*w, oX, oY, c)
    pts2 = side4(math.sqrt(2)*w-e, oX, oY, c)
    del pts2[-1]
    del pts2[-1]
    ots = rotate_2d(pts2, np.array([oX, oY]), 45 * np.pi / 180).tolist()
    return([pts[0], ots[0], pts[3], ots[3], pts[2], 
            ots[2], pts[1], ots[1], [oX, oY], c])


def make_gif(prefix, pause_frames):
    images = []
    for i, imgname in enumerate(glob.glob("{}.tmp.*.png".format(prefix))):
        img = imageio.imread(imgname)
        if i in pause_frames:
            for c in range(7):
                images.append(img)
        else: 
            images.append(img)
    imageio.mimsave("{}.gif".format(prefix), images)


def remove_files(prefix) :
    try:
        [os.remove(img) for img in glob.glob("{}.tmp.*.png".format(prefix))]
    except OSError: 
        pass


def octagon_flex(fig, c1, c2, c3, c4, c5): 
    shapes = [[50,50], [0,0], [100,100], [100,0], [0,100], [150,50], [200,100], 
              [200,0], [250,50], [300,0],[300,100], [350,50],[400,0],[400,100]]
    shapes2 = [[0,50], [100,50], [50,100], [50,0], [150,0], [150,100],[200,50], 
                [250,0], [250,100], [300,50], [350,100], [350,0],[400,50]]
    col = [c5, c5, c1, c1, c5, c1, c2, c2, c2, c4, c4, c4, c5, c5]
    col2 = [c2, c4, c2, c2, c4, c4, c5, c5, c5, c1, c1, c1, c2]

    e = [-2, -6, -10, -15, -19, -23, -25, -23, -19, -15, -10, -6, -2, 0]
    ls = [28, 25, 22, 20, 17, 14, 12, 14, 17, 20, 22, 25, 28, 30]
    opacity = [0, 0.25, 0.4, 0.5, 0.6, 0.75, 0.9, 1, 0.9, 0.75, 0.6, 0.5, 0.4, 0.25]

    for x, (a, b, o) in enumerate(zip(e, ls, opacity)):
        # once for every frame in this GIF
        for i in range(4):
            for j in range(2):
                sub1 = fig.add_subplot(4, 2, i*2 + j + 1)
                sub1.xaxis.set_visible(False)
                sub1.yaxis.set_visible(False)
                sub1.set_xlim([0,400])
                sub1.set_ylim([0,100])
                sub1.axis('off')
                sub1.add_patch(patches.Rectangle((400*i, 100*j), 400*(i+1), 100*(j+1), fc='white', alpha=1, ec='none'))

                for sh, co in zip(shapes, col):
                    pts = side8(b, sh[0], sh[1], co, a)
                    pts2 = side8(9, sh[0], sh[1], c3, -25-a)
                    pts3 = side8(9, sh[0], sh[1], co, -25-a)
                    add_shape(sub1, pts, 45, 1)
                    add_shape(sub1, pts2, 0, (1-o)*0.5)
                    add_shape(sub1, pts3, 45)
                    add_shape(sub1, pts2, 45, (1-o))

                for sh, co in zip(shapes2, col2):
                    pts = side8(42-b, sh[0], sh[1], co, -25-a)
                    pts2 = side8(9, sh[0], sh[1], c3, a)
                    pts3 = side8(9, sh[0], sh[1], co, a)
                    add_shape(sub1, pts, 45, 1)
                    add_shape(sub1, pts2, 0, o*0.5)
                    add_shape(sub1, pts3, 45)
                    add_shape(sub1, pts2, 45, o)

        savename = "octagon_flex.tmp.{}.png".format(string.ascii_lowercase[x])
        fig.savefig(savename, bbox_inches='tight', pad_inches=0, dpi=50)
        plt.clf()

    plt.close('all')
    make_gif("octagon_flex", (0,7))
    remove_files("octagon_flex")


if __name__ == '__main__':
    fig = plt.figure(figsize=(width, length))
    plt.subplots_adjust(hspace=0, wspace=0)
    octagon_flex(fig, *random.choice(color_palette))
