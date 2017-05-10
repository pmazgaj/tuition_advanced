import matplotlib
import matplotlib.pyplot as plt  # make figures
from matplotlib import patches  # polygon shapes
import math  # square roots and other calculations
import imageio  # save images
import scipy  # rotation calculations
import random
import os  # file deletion

matplotlib.use("Agg")  # configure backend for PNGs

#####################################################################
# WARNING:
# This script will overwrite any files in the same directory called
# temp0.png, temp1.png ... temp(n).png
# It was also originally a practice script and is not optimized for many things.
#####################################################################

# MIT License
# Copyright (c) [2016] [Eleanor K. Lutz]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#####################################################################
# ------------------ Functions for All Patterns. ------------------ #
#####################################################################

# If something is breaking it is most likely add_shape().
# You must pass a very specific list "points" to this function as described below

pi = scipy.pi
dot = scipy.dot
sin = scipy.sin
cos = scipy.cos
ar = scipy.array


def rad():
    return lambda ang: ang * pi / 180


rad = lambda ang: ang * pi / 180


def rotate_2d(pts, cnt, ang=pi / 4):
    """pts = {} Rotates points(nx2) about center cnt(2) by angle ang(1) in radian"""
    return dot(pts - cnt, ar([[cos(ang), sin(ang)], [-sin(ang), cos(ang)]])) + cnt


def solve_for_leg(h, leg1):
    """pythagorean theorum to solve for leg (not hypotenuse)"""
    return math.sqrt(h * h - leg1 * leg1)


def add_shape(points, degrees=0, alphaParam=1, ec='none', l=0, jn='round'):
    """Finalize rotation and add shape to plot."""
    # "points" should consist of the list returned from any of the
    # geometry functions below (side3, side4, etc.)
    origin = points[-2]
    color = points[-1]
    new_points = list(points)
    del new_points[-1]
    del new_points[-1]

    pts = ar(new_points)
    radians = degrees * pi / 180
    ots = rotate_2d(pts, ar([origin]), radians)
    sub1.add_patch(patches.Polygon(ots, fc=color, ec=ec,
                                   alpha=alphaParam, joinstyle=jn, lw=l, rasterized=True))


#####################################################################
# ------------------------ Actual Geometry ------------------------ #
#####################################################################

def side3(w, oX, oY, c, e=0):
    """Makes a polygon with 3 sides of length w, centered around the origin"""
    base = solve_for_leg(w, w / float(2))
    p1 = [oX + w / float(2), oY - ((1 / float(3)) * base)]
    p2 = [oX, oY + (2 / float(3)) * base]
    p3 = [oX - w / float(2), oY - ((1 / float(3)) * base)]
    return [p1, p2, p3, [oX, oY], c]


def side4(w, oX, oY, c, e=0):
    """Makes a polygon with 4 sides of length w, centered around the origin."""
    p1 = [oX - w / float(2), oY - w / float(2)]
    p2 = [oX - (w - e) / float(2), oY + (w - e) / float(2)]
    p3 = [oX + w / float(2), oY + w / float(2)]
    p4 = [oX + (w - e) / float(2), oY - (w - e) / float(2)]
    return [p1, p2, p3, p4, [oX, oY], c]


def side6(w, oX, oY, c, e=0):
    """Makes a polygon with 6 sides of length w, centered around the origin."""
    d = solve_for_leg(w, w / float(2))
    de = solve_for_leg(w - e, (w - e) / float(2))
    p1 = [oX, oY + w]
    p2 = [oX + de, oY + (w - e) / float(2)]
    p3 = [oX + d, oY - w / float(2)]
    p4 = [oX, oY - (w - e)]
    p5 = [oX - d, oY - w / float(2)]
    p6 = [oX - de, oY + (w - e) / float(2)]
    return [p1, p2, p3, p4, p5, p6, [oX, oY], c]


def side8(w, oX, oY, c, e=0):
    """Makes a polygon with 8 sides of length w, centered around the origin."""
    pts = side4(math.sqrt(2) * w, oX, oY, c)
    pts2 = side4(math.sqrt(2) * w - e, oX, oY, c)
    del pts2[-1]
    del pts2[-1]
    ots = rotate_2d(pts2, ar([oX, oY]), 45 * pi / 180).tolist()
    return ([pts[0], ots[0], pts[3], ots[3], pts[2],
             ots[2], pts[1], ots[1], [oX, oY], c])


def side12(w, oX, oY, c, e=0):
    """Makes a polygon with 12 sides, centered around the origin."""
    # w is not the side length for this function
    # this is because i wanted to solve this with a quick shortcut
    pts = side6(w, oX, oY, c)
    pts2 = side6(w - e, oX, oY, c)
    del pts2[-1]
    del pts2[-1]
    ots = rotate_2d(pts2, ar([oX, oY]), 30 * pi / 180).tolist()
    return ([pts[0], ots[0], pts[5], ots[5], pts[4], ots[4],
             pts[3], ots[3], pts[2], ots[2], pts[1], ots[1], [oX, oY], c])


# Functions below are for the box pattern only ##
def diamond_a(w, oX, oY, c='#000000', e=0):
    d = math.sqrt(w * w - ((w / float(2)) * (w / float(2))))
    p1 = [oX, oY]
    p2 = [oX, oY + w - e]
    p3 = [oX - d, oY + w - e + (w / float(2))]
    p4 = [oX - d, oY + (w / float(2))]
    return [p1, p2, p3, p4, [oX, oY], c]


def diamond_b(w, oX, oY, c='#000000', e=0):
    d = math.sqrt(w * w - ((w / float(2)) * (w / float(2))))
    p1 = [oX, oY]
    p2 = [oX, oY + w - e]
    p3 = [oX + d, oY + w - e + (w / float(2))]
    p4 = [oX + d, oY + (w / float(2))]
    return [p1, p2, p3, p4, [oX, oY], c]


def diamond_c(w, oX, oY, c='#000000', e=0):
    d = math.sqrt(w * w - ((w / float(2)) * (w / float(2))))
    p1 = [oX, oY + e]
    p2 = [oX, oY + w]
    p3 = [oX - d, oY + w + (w / float(2))]
    p4 = [oX - d, oY + (w / float(2)) + e]
    return [p1, p2, p3, p4, [oX, oY], c]


def diamond_d(w, oX, oY, c='#000000', e=0):
    d = math.sqrt(w * w - ((w / float(2)) * (w / float(2))))
    p1 = [oX, oY + e]
    p2 = [oX, oY + w]
    p3 = [oX + d, oY + w + (w / float(2))]
    p4 = [oX + d, oY + (w / float(2)) + e]
    return [p1, p2, p3, p4, [oX, oY], c]


#####################################################################
# ----------------- Remove temp files and finish ------------------ #
#####################################################################

def removal(max_degrees):
    for n in range(0, max_degrees):
        delete_name = str('temp' + repr(n) + '.png')
        try:
            os.remove(delete_name)
        except OSError:
            pass


# In[5]:
#####################################################################
# --------------------- Pattern 1: Star flex ---------------------- #
#####################################################################

def star_flex(c1, c2, c3, c4, c5, tag):
    global fig
    global sub1
    fig = plt.figure(figsize=(4.55, 2.6))
    # Yes globals are bad but add_shape() needs it and we clear the variable
    # from memory at the end of this function anyway
    plt.subplots_adjust(hspace=0, wspace=0)

    ba = [[19.75, 50, -90], [80.25, 50, 90], [35, 24, 90], [65, 24, -90],
          [65, 76, -90], [35, 76, 90]]
    ori = [[50, 50, c5, c4], [4.5, 24, c4, c5], [4.5, 76, c4, c5], [95.5, 76, c4, c5],
           [95.5, 24, c4, c5], [50, 102, c5, c4], [50, -2, c5, c4]]
    tri = [[23, 55.65, -90], [77, 55.66, 90], [31.75, 29.65, 90],
           [68.25, 29.65, -90], [23, 44.45, -90], [77, 44.45, 90],
           [68.25, 70.45, -90], [31.75, 70.45, 90], [13.39, 50, -90],
           [86.71, 50, 90], [41.5, 24, 90], [58.45, 24, -90],
           [58.45, 76, -90], [41.5, 76, 90]]

    lhex = [-2, -1, 0, 2, 4, 7, 7, 7, 4, 2, 0, -1]
    lstar = [12, 11, 10, 8, 6, 3, 3, 3, 6, 8, 10, 11]
    op = [0.75, 0.7, 0.6, 0.5, 0.45, 0.4, 0.4, 0.4, 0.45, 0.5, 0.6, 0.7]

    linner = [-6, -7, -8, -6, -4, -3, -1, -3, -4, -6, -8, -7]
    linsize = [6.35, 6.6, 7, 9.5, 13.5, 18, 19.5, 18, 13.5, 9.5, 7, 6.6]
    linsize2 = [3, 3.5, 4, 5.5, 7, 9, 12, 9, 7, 5.5, 4, 3.5]
    linsize3 = [2, 2.5, 3, 4, 5, 6.5, 8, 6.5, 5, 4, 3, 2.5]
    lin2 = [-1, -2, -3, -5, -7, -9, -7, -9, -7, -5, -3, -2]
    op2 = [0.75, 0.8, 0.85, 0.95, 1, 1, 1, 1, 1, 0.95, 0.85, 0.8]

    for frame in range(0, len(op)):  # for every frame in the GIF
        sub1 = fig.add_subplot(1, 1, 1)
        sub1.xaxis.set_visible(False)
        sub1.yaxis.set_visible(False)
        sub1.set_xlim([4.5, 95.5])
        sub1.set_ylim([24, 76])
        sub1.axis('off')
        sub1.add_patch(patches.Rectangle((0, 0), 100, 100, fc=c3, alpha=1, ec='none'))

        for n in range(0, len(ba)):  # Base triangles and hexes
            pts = side3(11, ba[n][0], ba[n][1], c5, 2)
            pts2 = side6(13, ba[n][0], ba[n][1], c2, lhex[frame])
            pts3 = side3(22.5, ba[n][0], ba[n][1], c1)
            pts4 = side3(5.5, ba[n][0], ba[n][1], c3)
            add_shape(pts2, ba[n][2] / 3)
            add_shape(pts3, ba[n][2] / 3)
            add_shape(pts, ba[n][2])
            add_shape(pts4, ba[n][2] * -1, 1)

        for n in range(0, len(tri)):  # Mini triangles around the center
            pts = side3(5.5, tri[n][0], tri[n][1], c3)
            add_shape(pts, tri[n][2], op[frame])

        for n in range(0, len(ori)):  # Hex stars and overlapped circles
            c = plt.Circle((ori[n][0], ori[n][1]), radius=3.5, color=c3)
            pts = side12(24, ori[n][0], ori[n][1], ori[n][2], lstar[frame])
            pts2 = side12(linsize[frame], ori[n][0], ori[n][1], ori[n][3], linner[frame])
            pts3 = side12(linsize2[frame], ori[n][0], ori[n][1], c3, lin2[frame])
            pts4 = side12(linsize3[frame], ori[n][0], ori[n][1], ori[n][2], lin2[frame] - 6)
            add_shape(pts)
            add_shape(pts2, 0, min(1, op[frame] + 0.25))  # can't have a >1 opacity
            add_shape(pts3, -30, 1)
            add_shape(pts4, 0, op2[frame])
            sub1.add_artist(c)

        save_name = str('temp' + repr(frame) + '.png')
        fig.savefig(save_name, bbox_inches='tight', pad_inches=0, dpi=50)
        plt.clf()

    images = []  # Turn a list of images into a GIF using ImageIO
    for n in range(0, len(op)):
        read_name = str('temp' + repr(n) + '.png')
        if read_name == 'temp1.png' or read_name == 'temp7.png':
            for c in range(0, 8):
                images.append(imageio.imread(read_name))
        else:
            images.append(imageio.imread(read_name))
    imageio.mimsave(str(tag) + '.gif', images)
    plt.close('all')

    removal(len(op))


#####################################################################
# --------------------- Pattern 2: Box slide ---------------------- #
#####################################################################

def box_slide(c1, c2, c3, c4, c5, tag):
    w = 25
    f = 3.25
    d = math.sqrt(w * w - ((w / float(2)) * (w / float(2))))
    oX = d * 2
    oY = 0

    global fig
    global sub1
    fig = plt.figure(figsize=(d * 2 / float(37), w * 3 / float(37)))
    # Yes globals are bad but add_shape() needs it and we clear the variable
    # from memory at the end of this function anyway
    plt.subplots_adjust(hspace=0, wspace=0)

    ish = [[oX, oY], [oX + 2 * d, oY], [oX - 2 * d, oY], [oX + d, oY + (1.5 * w)], [oX - d, oY + (1.5 * w)],
           [oX - (3 * d), oY + (1.5 * w)], [oX + (3 * d), oY + (1.5 * w)],
           [oX + d, oY - (1.5 * w)], [oX - d, oY - (1.5 * w)], [oX - (3 * d), oY - (1.5 * w)],
           [oX + (3 * d), oY - (1.5 * w)]]
    e1 = [25 - f, 23 - f, 21 - f, 18 - f, 15 - f, 10 - f, 7 - f, 4 - f, 0]
    cTop = [c1, c2, c4, c5, c1]
    cR = [c4, c1, c1, c4, c4]
    cL = [c5, c5, c2, c2, c5]
    o1 = [0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 1]

    for x in range(0, 35):  # for every frame in the GIF
        sub1 = fig.add_subplot(1, 1, 1)
        sub1.xaxis.set_visible(False)
        sub1.yaxis.set_visible(False)
        sub1.set_xlim([d, d * 3])
        sub1.set_ylim([0, w * 3])
        sub1.axis('off')
        sub1.add_patch(patches.Rectangle((0, 0), d * 5, w * 3, fc=c3, alpha=1, ec='none'))

        e1_length = len(e1)
        for n in range(0, len(ish)):
            # down to the right side
            if x < e1_length or x in range(2 * e1_length, 3 * e1_length) or x >= 4 * e1_length:
                if x < e1_length:
                    count = 0
                    eno = x
                elif x < 3 * e1_length:
                    count = 2
                    eno = x - e1_length * 2
                elif x < 5 * e1_length:
                    count = 4
                    eno = x - 5 * e1_length * 2
                pts2 = diamond_a(w - f, ish[n][0], ish[n][1], e=0, c=cL[count])
                add_shape(pts2)
                pts = diamond_d(w - f, ish[n][0], ish[n][1], e=0, c=cR[count])  # background
                add_shape(pts)
                pts = diamond_d(w - f, ish[n][0], ish[n][1], e=e1[eno], c=cR[count + 1])
                add_shape(pts, alphaParam=o1[eno])
                pts3 = diamond_c(w - f, ish[n][0] + d - f, ish[n][1] + w + (w / float(2)) - f * 1.5,
                                 e=0, c=cTop[count])  # background
                add_shape(pts3, 60)
                pts3 = diamond_c(w - f, ish[n][0] + d - f, ish[n][1] + w + (w / float(2)) - f * 1.5,
                                 e=e1[eno], c=cTop[count + 1])
                add_shape(pts3, 60)
            elif x < 2 * len(e1) or x in range(3 * e1_length, 4 * e1_length):  # up from the left side
                if x < 2 * e1_length:
                    count = 1
                    eno = x - e1_length
                elif x < 4 * e1_length:
                    count = 3
                    eno = x - e1_length * 3
                pts2 = diamond_c(w - f, ish[n][0], ish[n][1], e=0, c=cL[count])  # background
                add_shape(pts2)
                pts2 = diamond_c(w - f, ish[n][0], ish[n][1], e=e1[eno], c=cL[count + 1])
                add_shape(pts2, alphaParam=o1[eno])
                pts = diamond_d(w - f, ish[n][0], ish[n][1], e=0, c=cR[count])  # background
                add_shape(pts)
                pts3 = diamond_b(w - f, ish[n][0] + d - f,
                                 ish[n][1] + w + (w / float(2)) - f * 1.5, e=0, c=cTop[count])  # background
                add_shape(pts3, 120)
                pts3 = diamond_b(w - f, ish[n][0] + d - f,
                                 ish[n][1] + w + (w / float(2)) - f * 1.5, e=e1[eno], c=cTop[count + 1])
                add_shape(pts3, 120)
        save_name = str('temp' + repr(x) + '.png')
        fig.savefig(save_name, bbox_inches='tight', pad_inches=0, dpi=50)
        plt.clf()

    images = []  # Turn a list of images into a GIF using ImageIO
    for n in range(0, 35):
        read_name = str('temp' + repr(n) + '.png')
        if (read_name == 'temp0.png' or
                    read_name == 'temp9.png' or read_name == 'temp18.png' or read_name == 'temp27.png'):
            for c in range(0, 4):
                images.append(imageio.imread(read_name))
        else:
            images.append(imageio.imread(read_name))
    imageio.mimsave(str(tag) + '.gif', images)
    plt.close('all')

    removal(35)


#####################################################################
# -------------------- Pattern 3: Circle Size --------------------- #
#####################################################################

def circle_size(c1, c2, c3, c4, c5, tag):
    global fig
    global sub1
    fig = plt.figure(figsize=(4.25, 4.25))
    # Yes globals are bad but add_shape() needs it and we clear the variable
    # from memory at the end of this function anyway
    plt.subplots_adjust(hspace=0, wspace=0)

    ff = [[c5, c2, c4, c2, c5, c1, c5], [c2, c4, c1, c4, c2, c5, c2],
          [c4, c1, c1, c1, c4, c2, c4], [c2, c4, c1, c4, c2, c5, c2],
          [c5, c2, c4, c2, c5, c1, c5], [c1, c5, c2, c5, c1, c1, c1],
          [c5, c2, c4, c2, c5, c1, c5]]

    f2 = [[c4, c1, c5, c1, c4, c2, c4], [c1, c5, c2, c5, c1, c4, c1],
          [c5, c2, c2, c2, c5, c1, c5], [c1, c5, c2, c5, c1, c4, c1],
          [c4, c1, c5, c1, c4, c2, c4], [c2, c4, c1, c4, c2, c2, c2],
          [c4, c1, c5, c1, c4, c2, c4]]

    aa = [[c1, c5, c2, c2, c5, c1, c1], [c5, c2, c4, c4, c2, c5, c5],
          [c2, c4, c1, c1, c4, c2, c2], [c2, c4, c1, c1, c4, c2, c2],
          [c5, c2, c4, c4, c2, c5, c5], [c1, c5, c2, c2, c5, c1, c1],
          [c1, c5, c2, c2, c5, c1, c1]]

    rr = [10, 10, 10, 10, 15, 20, 25, 30, 30, 30, 25, 20, 15]

    for frame in range(0, len(rr)):  # for every frame in the GIF
        # this is necessary every time because we clear sub1 from memory
        # at the end of each for loop so that Python can garbage collect.
        # your code will start to run really slow if you don't do this.

        sub1 = fig.add_subplot(1, 1, 1)
        sub1.xaxis.set_visible(False)
        sub1.yaxis.set_visible(False)
        sub1.set_xlim([0, 60])
        sub1.set_ylim([0, 60])
        sub1.axis('off')
        sub1.add_patch(patches.Rectangle((0, 0), 100, 100, fc=c3, alpha=1, ec='none'))
        for i in range(0, len(ff)):
            count = 1
            for a in range(0, len(ff[0])):
                sub1.add_patch(patches.Circle((5 * count, 5 + 2 * 5 * i),
                                              5, fc=ff[i][a], alpha=1, ec='none'))
                sub1.add_patch(patches.Circle((5 * count, 5 + 2 * 5 * i),
                                              3.5, fc=f2[i][a], alpha=random.randint(75, 100) / float(100), ec='none'))
                sub1.add_patch(patches.Circle((5 * count - 5, 2 * 5 * i), 1.5,
                                              fc=aa[i][a], alpha=0.75, ec='none'))
                sub1.add_patch(patches.Circle((5 * count, 5 + 2 * 5 * i),
                                              random.randint(10, rr[frame]) / float(10), fc=c3,
                                              alpha=random.randint(50, 85) / float(100), ec='none'))
                sub1.add_patch(patches.Circle((5 * count, 5 + 2 * 5 * i), 1,
                                              fc=c3, alpha=1, ec='none'))
                count += 2
        save_name = str('temp' + repr(frame) + '.png')
        fig.savefig(save_name, bbox_inches='tight', pad_inches=0, dpi=50)
        plt.clf()  # fix memory leak

    images = []  # Turn a list of images into a GIF using ImageIO
    for n in range(0, len(rr)):
        read_name = str('temp' + repr(n) + '.png')
        images.append(imageio.imread(read_name))

    imageio.mimsave(str(tag) + '.gif', images)
    plt.close('all')

    removal(len(rr))


#####################################################################
# -------------------- Pattern 4: Octagon flex -------------------- #
#####################################################################

def octagon_flex(c1, c2, c3, c4, c5, tag):
    global fig
    global sub1
    fig = plt.figure(figsize=(7, 1.75))
    # Yes globals are bad but add_shape() needs it and we clear the variable
    # from memory at the end of this function anyway
    plt.subplots_adjust(hspace=0, wspace=0)

    shapes = [[50, 50], [0, 0], [100, 100], [100, 0], [0, 100], [150, 50], [200, 100],
              [200, 0], [250, 50], [300, 0], [300, 100], [350, 50], [400, 0], [400, 100]]
    shapes2 = [[0, 50], [100, 50], [50, 100], [50, 0], [150, 0], [150, 100], [200, 50],
               [250, 0], [250, 100], [300, 50], [350, 100], [350, 0], [400, 50]]
    col = [c5, c5, c1, c1, c5, c1, c2, c2, c2, c4, c4, c4, c5, c5]
    col2 = [c2, c4, c2, c2, c4, c4, c5, c5, c5, c1, c1, c1, c2]

    e = [-2, -6, -10, -15, -19, -23, -25, -23, -19, -15, -10, -6, -2, 0]
    ls = [28, 25, 22, 20, 17, 14, 12, 14, 17, 20, 22, 25, 28, 30]
    opacity = [0, 0.25, 0.4, 0.5, 0.6, 0.75, 0.9, 1, 0.9, 0.75, 0.6, 0.5, 0.4, 0.25, 0.1, 0]

    for frame in range(0, len(ls)):  # for every frame in this GIF
        sub1 = fig.add_subplot(1, 1, 1)  # make a new graph
        sub1.xaxis.set_visible(False)
        sub1.yaxis.set_visible(False)
        sub1.set_xlim([0, 400])
        sub1.set_ylim([0, 100])
        sub1.axis('off')
        sub1.add_patch(patches.Rectangle((0, 0), 400, 100, fc=c3, alpha=1, ec='none'))

        for n in range(0, len(shapes)):
            pts = side8(ls[frame], shapes[n][0], shapes[n][1], col[n], e[frame])
            pts2 = side8(9, shapes[n][0], shapes[n][1], c3, -25 - e[frame])
            pts3 = side8(9, shapes[n][0], shapes[n][1], col[n], -25 - e[frame])
            add_shape(pts, 45, 1)
            add_shape(pts2, 0, (1 - opacity[frame]) * 0.5)
            add_shape(pts3, 45)
            add_shape(pts2, 45, (1 - opacity[frame]))
        for n in range(0, len(shapes2)):
            pts = side8(42 - ls[frame], shapes2[n][0], shapes2[n][1], col2[n], -25 - e[frame])
            pts2 = side8(9, shapes2[n][0], shapes2[n][1], c3, e[frame])
            pts3 = side8(9, shapes2[n][0], shapes2[n][1], col2[n], e[frame])
            add_shape(pts, 45, 1)
            add_shape(pts2, 0, int(opacity[frame] * 0.5))
            add_shape(pts3, 45)
            add_shape(pts2, 45, opacity[frame])

        save_name = str('temp' + repr(frame) + '.png')
        fig.savefig(save_name, bbox_inches='tight', pad_inches=0, dpi=50)
        plt.clf()  # plt doesn't automatically garbage collect, fix memory leak

    images = []  # Turn a list of images into a GIF using ImageIO
    for n in range(0, len(ls)):
        read_name = str('temp' + repr(n) + '.png')
        if read_name == 'temp0.png' or read_name == 'temp7.png':
            for c in range(0, 7):
                images.append(imageio.imread(read_name))  # pause at these frames
        else:
            images.append(imageio.imread(read_name))

    imageio.mimsave(str(tag) + '.gif', images)
    plt.close('all')  # plt doesn't automatically garbage collect, fix memory leak

    removal(len(ls))


#####################################################################
# -------------------- Pattern 5: Pixel slide --------------------- #
#####################################################################

def pixelSlide(c1, c2, c3, c4, c5, tag):
    global fig
    global sub1
    fig = plt.figure(figsize=(28 / float(6), 20 / float(6)))
    # Yes globals are bad but add_shape() needs it and we clear the variable
    # from memory at the end of this function anyway
    plt.subplots_adjust(hspace=0, wspace=0)
    c0 = 'none'

    # Basically a huge list of what every pixel color should be
    row = [[c5, c5, c4, c4, c4, c4, c0, c0, c0, c2, c2, c2, c2, c1,
            c1, c1, c2, c2, c2, c2, c0, c0, c0, c4, c4, c4, c4, c5],
           [c5, c4, c4, c0, c4, c0, c0, c1, c0, c0, c2, c0, c2, c2,
            c1, c2, c2, c0, c2, c0, c0, c5, c0, c0, c4, c0, c4, c4],
           [c4, c4, c0, c0, c0, c0, c1, c1, c1, c0, c0, c0, c0, c2,
            c2, c2, c0, c0, c0, c0, c5, c5, c5, c0, c0, c0, c0, c4],
           [c5, c4, c4, c0, c5, c0, c0, c1, c0, c0, c1, c0, c2, c2,
            c1, c2, c2, c0, c1, c0, c0, c5, c0, c0, c5, c0, c4, c4],
           [c4, c4, c0, c0, c0, c0, c1, c1, c1, c0, c0, c0, c0, c2,
            c2, c2, c0, c0, c0, c0, c5, c5, c5, c0, c0, c0, c0, c4],
           [c4, c0, c0, c1, c0, c1, c1, c2, c1, c1, c0, c1, c0, c0,
            c2, c0, c0, c5, c0, c5, c5, c4, c5, c5, c0, c5, c0, c0],
           [c0, c0, c1, c1, c1, c1, c2, c2, c2, c1, c1, c1, c1, c0,
            c0, c0, c5, c5, c5, c5, c4, c4, c4, c5, c5, c5, c5, c0],
           [c4, c0, c0, c1, c0, c1, c1, c2, c1, c1, c0, c1, c0, c0,
            c2, c0, c0, c5, c0, c5, c5, c4, c5, c5, c0, c5, c0, c0],
           [c0, c0, c1, c1, c1, c1, c2, c2, c2, c1, c1, c1, c1, c0,
            c0, c0, c5, c5, c5, c5, c4, c4, c4, c5, c5, c5, c5, c0],
           [c0, c1, c1, c2, c1, c2, c2, c4, c2, c2, c1, c2, c1, c1,
            c0, c5, c5, c4, c5, c4, c4, c2, c4, c4, c5, c4, c5, c5],
           [c0, c1, c2, c2, c2, c2, c4, c4, c4, c2, c2, c2, c2, c1,
            c0, c5, c4, c4, c4, c4, c2, c2, c2, c4, c4, c4, c4, c5]
           ]

    adjust = [[0] * 11,
              [random.randint(0, 2) for x in range(11)],
              [random.randint(0, 4) for x in range(11)],
              [random.randint(0, 6) for x in range(11)],
              [random.randint(0, 10) for x in range(11)],
              [random.randint(0, 12) for x in range(11)],
              [random.randint(0, 16) for x in range(11)],
              [random.randint(0, 12) for x in range(11)],
              [random.randint(0, 10) for x in range(11)],
              [random.randint(0, 6) for x in range(11)],
              [random.randint(0, 4) for x in range(11)],
              [random.randint(0, 2) for x in range(11)]
              ]

    for frame in range(0, len(adjust)):  # for every frame in the GIF
        sub1 = fig.add_subplot(1, 1, 1)
        sub1.xaxis.set_visible(False)
        sub1.yaxis.set_visible(False)
        sub1.set_xlim([0, 280])
        sub1.set_ylim([0, 200])
        sub1.axis('off')
        sub1.add_patch(patches.Rectangle((0, 0), 280, 200, fc=c3, alpha=1, ec='none'))

        for n in range(0, 1):
            for y in range(0, len(row)):
                for n in range(0, len(row[0])):
                    pts = side4(10, 5 + 10 * n, 5 + 10 * y, row[y][n])
                    add_shape(pts)
                    seed = random.randint(0, 1)
                    if seed == 1:
                        pts = side4(10, 5 + 10 * n + adjust[frame][y], 5 + 10 * y, row[y][n])
                        add_shape(pts, alphaParam=random.randint(25, 50) / float(100))
                        pts = side4(10, 5 + 10 * n + adjust[frame][y] - 280, 5 + 10 * y, row[y][n])
                        add_shape(pts, alphaParam=random.randint(25, 50) / float(100))
                    else:
                        pts = side4(10, 5 + 10 * n - adjust[frame][y], 5 + 10 * y, row[y][n])
                        add_shape(pts, alphaParam=random.randint(25, 50) / float(100))
                        pts = side4(10, 5 + 10 * n - adjust[frame][y] + 280, 5 + 10 * y, row[y][n])
                        add_shape(pts, alphaParam=random.randint(25, 50) / float(100))
            for y in range(0, len(row)):
                for n in range(0, len(row[0])):
                    pts = side4(10, 5 + 10 * n, 210 - (5 + 10 * y), row[y][n])
                    add_shape(pts)
                    seed = random.randint(0, 1)
                    if seed == 1:
                        pts = side4(10, 5 + 10 * n - adjust[frame][y], 210 - (5 + 10 * y), row[y][n])
                        add_shape(pts, alphaParam=0.25)
                        pts = side4(10, 5 + 10 * n - adjust[frame][y] + 280, 210 - (5 + 10 * y), row[y][n])
                        add_shape(pts, alphaParam=0.25)
                    else:
                        pts = side4(10, 5 + 10 * n + adjust[frame][y], 210 - (5 + 10 * y), row[y][n])
                        add_shape(pts, alphaParam=0.25)
                        pts = side4(10, 5 + 10 * n + adjust[frame][y] - 280, 210 - (5 + 10 * y), row[y][n])
                        add_shape(pts, alphaParam=0.25)

        save_name = str('temp' + repr(frame) + '.png')
        fig.savefig(save_name, bbox_inches='tight', pad_inches=0, dpi=50)
        plt.clf()

    images = []  # Turn a list of images into a GIF using ImageIO
    for n in range(0, len(adjust)):
        read_name = str('temp' + repr(n) + '.png')
        if read_name == 'temp1.png':
            for c in range(0, 3):
                images.append(imageio.imread(read_name))
        else:
            images.append(imageio.imread(read_name))

    imageio.mimsave(str(tag) + '.gif', images)
    plt.close('all')

    removal(len(adjust))


######################################################################
# ------------ Combine all patterns into one randomizer ------------ #
######################################################################

# List of color palettes: ["saveName", [colors 1 ~ 5]]
# NOTE: If you have two palettes with the same saveName,
# then this code will re-write all earlier versions and only keep the last one.
# Put exactly 5 colors in the color list, otherwise this will not work.

colorList = [['TestGIF1', ['#C24704', '#D9CC3C', '#fff7c9', '#A0E0BA', '#00ADA7']],
             ['TestGIF2', ['#D9CB84', '#A99E46', '#737D26', '#3F522B', '#302B1D']]]

for x in range(0, len(colorList)):
    tag = colorList[x][0]  # save name for GIF file
    c1 = colorList[x][1][0]
    c2 = colorList[x][1][1]
    c3 = colorList[x][1][2]
    c4 = colorList[x][1][3]
    c5 = colorList[x][1][4]

    randomList = [20, 40, 60, 80, 100]  # determine frequency of each pattern
    randomSeed = random.randint(1, 100)  # Pick a random pattern to apply colors to
    assert randomList[-1] == 100, 'The random list of probabilities should cover 0-100'

    if randomSeed <= randomList[0]:
        star_flex(c1, c2, c3, c4, c5, tag)  # Pattern 1
    elif randomSeed <= randomList[1]:
        box_slide(c1, c2, c3, c4, c5, tag)  # Pattern 2
    elif randomSeed <= randomList[2]:
        circle_size(c1, c2, c3, c4, c5, tag)  # Pattern 3
    elif randomSeed <= randomList[3]:
        octagon_flex(c1, c2, c3, c4, c5, tag)  # Pattern 4
    elif randomSeed <= randomList[4]:
        pixelSlide(c1, c2, c3, c4, c5, tag)  # Pattern 5

print('Finished!')
