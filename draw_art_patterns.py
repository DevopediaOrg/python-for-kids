from __future__ import division
import matplotlib, math, imageio, numpy, random, os
matplotlib.use("Agg")
import matplotlib.pyplot as plt 
from matplotlib import patches

'''
Functions to define all polygons used in each pattern.
If something is breaking it is most likely addShape().
You must pass a very specific list to this function as described below.
'''

ar = numpy.array

def Rotate2D(pts,cnt,ang=numpy.pi/4):
    '''pts = {} Rotates points(nx2) about center cnt(2) by angle ang(1) in radian'''
    return numpy.dot(pts-cnt,ar([[numpy.cos(ang),numpy.sin(ang)],
                                 [-numpy.sin(ang),numpy.cos(ang)]]))+cnt

def solveForLeg(h, leg1):
    '''pythagorean theorum to solve for leg (not hypotenuse)'''
    return(math.sqrt(h*h - leg1*leg1))

def addShape(points, degrees=0, alphaParam=1, ec='none', l=0, jn='round'):
    '''Finalize rotation and add shape to plot.'''
    # "points" should consist of the list returned from any of the
    # geometry functions below (side3, side4, etc.)
    origin = points[-2]
    color = points[-1]
    newPoints = list(points)
    del newPoints[-1]
    del newPoints[-1]
    
    pts = ar(newPoints)
    radians = degrees * numpy.pi / 180
    ots = Rotate2D(pts,ar([origin]),radians) 
    sub1.add_patch(patches.Polygon(ots, fc=color, ec=ec, 
        alpha=alphaParam, joinstyle=jn, lw=l, rasterized=True))

def side3(w, oX, oY, c, e=0):
    '''Makes a polygon with 3 sides of length w, centered around the origin'''
    base = solveForLeg(w, w/float(2))
    p1 = [oX+w/float(2), oY-((1/float(3))*base)]
    p2 = [oX, oY+(2/float(3))*base]
    p3 = [oX-w/float(2), oY-((1/float(3))*base)]
    return([p1, p2, p3, [oX, oY], c])

def side4(w, oX, oY, c, e=0):
    '''Makes a polygon with 4 sides of length w, centered around the origin.'''
    p1 = [oX-w/float(2), oY-w/float(2)]
    p2 = [oX-(w-e)/float(2), oY+(w-e)/float(2)]
    p3 = [oX+w/float(2), oY+w/float(2)]
    p4 = [oX+(w-e)/float(2), oY-(w-e)/float(2)]
    return([p1, p2, p3, p4, [oX, oY], c])

def side6(w, oX, oY, c, e=0):
    '''Makes a polygon with 6 sides of length w, centered around the origin.'''
    d = solveForLeg(w, w/float(2))
    de = solveForLeg(w-e, (w-e)/float(2))
    p1 = [oX, oY+w]
    p2 = [oX+de, oY+(w-e)/float(2)]
    p3 = [oX+d, oY-w/float(2)]
    p4 = [oX, oY-(w-e)]
    p5 = [oX-d, oY-w/float(2)]
    p6 = [oX-de, oY+(w-e)/float(2)]
    return([p1, p2, p3, p4, p5, p6, [oX,oY], c])

def side8(w, oX, oY, c, e=0):
    '''Makes a polygon with 8 sides of length w, centered around the origin.'''
    pts = side4(math.sqrt(2)*w, oX, oY, c)
    pts2 = side4(math.sqrt(2)*w-e, oX, oY, c)
    del pts2[-1]
    del pts2[-1]
    ots = Rotate2D(pts2,ar([oX, oY]),45 * numpy.pi / 180).tolist()
    return([pts[0], ots[0], pts[3], ots[3], pts[2], 
            ots[2], pts[1], ots[1], [oX,oY], c])

def side12(w, oX, oY, c, e=0):
    '''Makes a polygon with 12 sides, centered around the origin.'''
    # w is not the side length for this function
    pts = side6(w, oX, oY, c)
    pts2 = side6(w-e, oX, oY, c)
    del pts2[-1]
    del pts2[-1]
    ots = Rotate2D(pts2,ar([oX, oY]), 30 * numpy.pi / 180).tolist()
    return([pts[0], ots[0], pts[5], ots[5], pts[4], ots[4], 
            pts[3], ots[3], pts[2], ots[2], pts[1], ots[1], [oX,oY], c])

# diamond functions are for the box pattern only
def diamondA(w, oX, oY, c='#000000', e=0):
    d = math.sqrt(w*w-((w/float(2))*(w/float(2))))
    p1 = [oX, oY]
    p2 = [oX, oY+w-e]
    p3 = [oX-d, oY+w-e+(w/float(2))]
    p4 = [oX-d, oY+(w/float(2))]
    return([p1, p2, p3, p4, [oX, oY], c])

def diamondB(w, oX, oY, c='#000000', e=0):
    d = math.sqrt(w*w-((w/float(2))*(w/float(2))))
    p1 = [oX, oY]
    p2 = [oX, oY+w-e]
    p3 = [oX+d, oY+w-e+(w/float(2))]
    p4 = [oX+d, oY+(w/float(2))]
    return([p1, p2, p3, p4, [oX, oY], c])

def diamondC(w, oX, oY, c='#000000', e=0):
    d = math.sqrt(w*w-((w/float(2))*(w/float(2))))
    p1 = [oX, oY+e]
    p2 = [oX, oY+w]
    p3 = [oX-d, oY+w+(w/float(2))]
    p4 = [oX-d, oY+(w/float(2))+e]
    return([p1, p2, p3, p4, [oX, oY], c])

def diamondD(w, oX, oY, c='#000000', e=0):
    d = math.sqrt(w*w-((w/float(2))*(w/float(2))))
    p1 = [oX, oY+e]
    p2 = [oX, oY+w]
    p3 = [oX+d, oY+w+(w/float(2))]
    p4 = [oX+d, oY+(w/float(2))+e]
    return([p1, p2, p3, p4, [oX, oY], c])

def removal(maxdegrees) :
    '''Remove temp files created during pattern generation'''
    for n in range(0, maxdegrees):
        deletename = str('temp' + repr(n) + '.png')
        try:
            os.remove(deletename)
        except OSError: 
            pass

def starFlex(c1, c2, c3, c4, c5, tag):
    '''Pattern 1: Star flex'''
    global fig 
    global sub1 # allow other functions to add shapes to the plot
    fig = plt.figure(figsize=(4.55, 2.6))
    plt.subplots_adjust(hspace=0, wspace=0)

    # origin locations plus rotation angle for each shape set
    ba = [[19.75,50,-90],[80.25,50,90],[35,24,90],[65,24,-90],
          [65,76,-90],[35,76,90]]
    ori = [[50,50,c5,c4],[4.5,24,c4,c5],[4.5,76,c4,c5],[95.5,76,c4,c5],
           [95.5,24,c4,c5],[50,102,c5,c4],[50,-2,c5,c4]]  
    tri = [[23, 55.65, -90],[77, 55.66, 90],[31.75, 29.65, 90], 
           [68.25, 29.65, -90],[23, 44.45, -90],[77, 44.45, 90],
           [68.25, 70.45, -90],[31.75, 70.45, 90],[13.39, 50, -90],
           [86.71, 50, 90],[41.5, 24, 90],[58.45, 24, -90],
           [58.45, 76, -90],[41.5, 76, 90]] 

    lhex = [-2, -1, 0, 2, 4, 7, 7, 7, 4, 2, 0, -1]
    lstar = [12, 11, 10, 8, 6, 3, 3, 3, 6, 8, 10, 11]
    op = [0.75, 0.7, 0.6, 0.5, 0.45, 0.4, 0.4, 0.4, 0.45, 0.5, 0.6, 0.7]

    linner = [-6, -7, -8, -6, -4, -3, -1, -3, -4, -6, -8, -7]
    linsize = [6.35, 6.6, 7, 9.5, 13.5, 18, 19.5, 18, 13.5, 9.5, 7, 6.6]
    linsize2 = [3, 3.5, 4, 5.5, 7, 9, 12, 9, 7, 5.5, 4, 3.5]
    linsize3 = [2, 2.5, 3, 4, 5, 6.5, 8, 6.5, 5, 4, 3, 2.5]
    lin2 = [-1, -2, -3, -5, -7, -9, -7, -9, -7, -5, -3, -2]
    op2 = [0.75, 0.8, 0.85, 0.95, 1, 1, 1, 1, 1, 0.95, 0.85, 0.8]

    for x in range(0, len(op)): # for every frame in the GIF
        sub1 = fig.add_subplot(1,1,1)
        sub1.xaxis.set_visible(False)
        sub1.yaxis.set_visible(False)
        sub1.set_xlim([4.5, 95.5])
        sub1.set_ylim([24, 76])
        sub1.axis('off')
        sub1.add_patch(patches.Rectangle((0, 0), 100, 100, fc=c3, alpha=1, ec='none'))

        for n in range(0, len(ba)): # Base triangles and hexes
            pts = side3(11, ba[n][0], ba[n][1], c5, 2)
            pts2 = side6(13, ba[n][0], ba[n][1], c2, lhex[x])
            pts3 = side3(22.5, ba[n][0], ba[n][1], c1)
            pts4 = side3(5.5, ba[n][0], ba[n][1], c3)
            addShape(pts2, ba[n][2]/(3))
            addShape(pts3, ba[n][2]/(3))
            addShape(pts, ba[n][2])
            addShape(pts4, ba[n][2]*-1, 1)

        for n in range(0, len(tri)): # Mini triangles around the center
            pts = side3(5.5, tri[n][0], tri[n][1], c3)
            addShape(pts, tri[n][2], op[x])

        for n in range(0, len(ori)): # Hex stars and overlapped circles
            c = plt.Circle((ori[n][0], ori[n][1]), radius=3.5, color=c3)
            pts = side12(24, ori[n][0], ori[n][1], ori[n][2], lstar[x])
            pts2 = side12(linsize[x], ori[n][0], ori[n][1], ori[n][3], linner[x])
            pts3 = side12(linsize2[x], ori[n][0], ori[n][1], c3, lin2[x])
            pts4 = side12(linsize3[x], ori[n][0], ori[n][1], ori[n][2], lin2[x]-6)
            addShape(pts)
            addShape(pts2, 0, min(1, op[x]+0.25)) # can't have a >1 opacity
            addShape(pts3, -30, 1)
            addShape(pts4, 0, op2[x])
            sub1.add_artist(c)

        savename = str('temp' + repr(x) + '.png')
        fig.savefig(savename, bbox_inches='tight', pad_inches=0, dpi=50)
        plt.clf() 

    images = [] #  Turn a list of images into a GIF using ImageIO
    for n in range(0, len(op)):
        readname = str('temp' + repr(n) + '.png')
        if readname == 'temp1.png' or readname == 'temp7.png':
            for c in range (0, 8):
                images.append(imageio.imread(readname))
        else: 
            images.append(imageio.imread(readname))
    imageio.mimsave(str(tag) + '.gif', images)
    plt.close('all')
    removal(len(op))

def boxSlide(c1, c2, c3, c4, c5, tag):
    '''Pattern 2: Box slide'''
    w = 25
    f = 3.25
    d = math.sqrt(w*w-((w/float(2))*(w/float(2))))
    oX = d*2
    oY = 0

    global fig 
    global sub1 # allow other functions to add shapes to the plot
    fig = plt.figure(figsize=(d*2/float(37), w*3/float(37)))
    plt.subplots_adjust(hspace=0, wspace=0)

    ish = [[oX, oY],[oX+2*d, oY],[oX-2*d, oY], [oX+d, oY+(1.5*w)], [oX-d, oY+(1.5*w)], 
           [oX-(3*d), oY+(1.5*w)],[oX+(3*d), oY+(1.5*w)],
          [oX+d, oY-(1.5*w)], [oX-d, oY-(1.5*w)],[oX-(3*d), oY-(1.5*w)],[oX+(3*d), oY-(1.5*w)]]
    e1 = [25-f, 23-f, 21-f, 18-f, 15-f, 10-f, 7-f, 4-f, 0]
    cTop = [c1, c2, c4, c5, c1]
    cR = [c4, c1, c1, c4, c4]
    cL = [c5, c5, c2, c2, c5]
    o1 = [0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 1]

    for x in range(0, 35):
        sub1 = fig.add_subplot(1,1,1)
        sub1.xaxis.set_visible(False)
        sub1.yaxis.set_visible(False)
        sub1.set_xlim([d, d*3])
        sub1.set_ylim([0, w*3])
        sub1.axis('off')
        sub1.add_patch(patches.Rectangle((0, 0), d*5, w*3, fc=c3, alpha=1, ec='none'))

        for n in range(0, len(ish)):
            if (x < len(e1) or x >= 2*len(e1) and 
                x < 3*len(e1) or x >= 4*len(e1)): # down to the right side
                if x < len(e1):
                    count = 0
                    eno = x
                elif x < 3*len(e1):
                    count = 2
                    eno = x-len(e1)*2
                elif x < 5*len(e1):
                    count = 4
                    eno = x-5*len(e1)*2
                pts2 = diamondA(w-f, ish[n][0], ish[n][1], e=0, c=cL[count])
                addShape(pts2)
                pts = diamondD(w-f, ish[n][0], ish[n][1], e=0, c=cR[count]) # background
                addShape(pts)
                pts = diamondD(w-f, ish[n][0], ish[n][1], e=e1[eno], c=cR[count+1])
                addShape(pts, alphaParam=o1[eno])
                pts3 = diamondC(w-f, ish[n][0]+d-f,ish[n][1]+w+(w/float(2))-f*1.5, 
                                e=0, c=cTop[count]) # background
                addShape(pts3, 60)
                pts3 = diamondC(w-f, ish[n][0]+d-f, ish[n][1]+w+(w/float(2))-f*1.5, 
                                e=e1[eno], c=cTop[count+1])
                addShape(pts3, 60)
            elif x < 2*len(e1) or x >= 3*len(e1) and x < 4*len(e1): # up from the left side
                if x < 2*len(e1):
                    count = 1
                    eno = x-len(e1)
                elif x < 4*len(e1):
                    count = 3
                    eno = x-len(e1)*3
                pts2 = diamondC(w-f, ish[n][0], ish[n][1], e=0, c=cL[count]) # background
                addShape(pts2)
                pts2 = diamondC(w-f, ish[n][0], ish[n][1], e=e1[eno], c=cL[count+1])
                addShape(pts2, alphaParam = o1[eno])
                pts = diamondD(w-f, ish[n][0], ish[n][1], e=0, c=cR[count]) # background
                addShape(pts)
                pts3 = diamondB(w-f, ish[n][0]+d-f, 
                    ish[n][1]+w+(w/float(2))-f*1.5, e=0, c=cTop[count]) # background
                addShape(pts3, 120)
                pts3 = diamondB(w-f, ish[n][0]+d-f, 
                    ish[n][1]+w+(w/float(2))-f*1.5, e=e1[eno], c=cTop[count+1])
                addShape(pts3, 120) 
        savename = str('temp' + repr(x) + '.png')
        fig.savefig(savename, bbox_inches='tight', pad_inches=0, dpi=50)
        plt.clf() 

    images = [] #  Turn a list of images into a GIF using ImageIO
    for n in range(0, 35):
        readname = str('temp' + repr(n) + '.png')
        if (readname == 'temp0.png' or readname == 'temp9.png' or 
            readname == 'temp18.png' or readname == 'temp27.png'):
            for c in range (0, 4):
                images.append(imageio.imread(readname))
        else: 
            images.append(imageio.imread(readname))
    imageio.mimsave(str(tag) + '.gif', images)
    plt.close('all')
    removal(35)

def circleSize(c1, c2, c3, c4, c5, tag):
    '''Pattern 3: Circle Size'''
    global fig 
    global sub1 # allow other functions to add shapes to the plot
    fig = plt.figure(figsize=(4.25, 4.25))
    plt.subplots_adjust(hspace=0, wspace=0)

    ff = [[c5, c2, c4, c2, c5, c1, c5],[c2, c4, c1, c4, c2, c5, c2],
          [c4, c1, c1, c1, c4, c2, c4],[c2, c4, c1, c4, c2, c5, c2],
          [c5, c2, c4, c2, c5, c1, c5],[c1, c5, c2, c5, c1, c1, c1],
          [c5, c2, c4, c2, c5, c1, c5]]

    f2 = [[c4, c1, c5, c1, c4, c2, c4],[c1, c5, c2, c5, c1, c4, c1],
          [c5, c2, c2, c2, c5, c1, c5],[c1, c5, c2, c5, c1, c4, c1],
          [c4, c1, c5, c1, c4, c2, c4],[c2, c4, c1, c4, c2, c2, c2],
          [c4, c1, c5, c1, c4, c2, c4]]

    aa = [[c1, c5, c2, c2, c5, c1, c1],[c5, c2, c4, c4, c2, c5, c5],
          [c2, c4, c1, c1, c4, c2, c2],[c2, c4, c1, c1, c4, c2, c2],
          [c5, c2, c4, c4, c2, c5, c5],[c1, c5, c2, c2, c5, c1, c1],
          [c1, c5, c2, c2, c5, c1, c1]]

    rr = [10, 10, 10, 10, 15, 20, 25, 30, 30, 30, 25, 20, 15]

    for x in range(0, len(rr)): 
        sub1 = fig.add_subplot(1,1,1)
        sub1.xaxis.set_visible(False)
        sub1.yaxis.set_visible(False)
        sub1.set_xlim([0, 60])
        sub1.set_ylim([0, 60])
        sub1.axis('off')
        sub1.add_patch(patches.Rectangle((0, 0), 100, 100, fc=c3, alpha=1, ec='none'))
        for i in range(0, len(ff)):
            count = 1  
            for a in range(0, len(ff[0])):
                sub1.add_patch(patches.Circle((5*count, 5+2*5*i), 
                    5, fc=ff[i][a], alpha=1, ec='none'))
                sub1.add_patch(patches.Circle((5*count, 5+2*5*i), 
                    3.5, fc=f2[i][a], alpha=random.randint(75, 100)/float(100), ec='none'))
                sub1.add_patch(patches.Circle((5*count-5, 2*5*i),1.5, 
                    fc=aa[i][a], alpha=0.75, ec='none'))
                sub1.add_patch(patches.Circle((5*count, 5+2*5*i), 
                    random.randint(10, rr[x])/float(10), fc=c3, 
                    alpha=random.randint(50, 85)/float(100), ec='none'))
                sub1.add_patch(patches.Circle((5*count, 5+2*5*i), 1, 
                    fc=c3, alpha=1, ec='none'))
                count = count + 2                
        savename = str('temp' + repr(x) + '.png')
        fig.savefig(savename, bbox_inches='tight', pad_inches=0, dpi=50)
        plt.clf()

    images = [] #  Turn a list of images into a GIF using ImageIO
    for n in range(0, len(rr)):
        readname = str('temp' + repr(n) + '.png')
        images.append(imageio.imread(readname))

    imageio.mimsave(str(tag) + '.gif', images)
    plt.close('all')
    removal(len(rr))

def octagonFlex(c1, c2, c3, c4, c5, tag): 
    '''Pattern 4: Octagon flex'''
    global fig 
    global sub1 # allow other functions to add shapes to the plot
    fig = plt.figure(figsize=(7, 1.75))
    plt.subplots_adjust(hspace=0, wspace=0)

    shapes = [[50,50], [0,0], [100,100], [100,0], [0,100], [150,50], [200,100], 
              [200,0], [250,50], [300,0],[300,100], [350,50],[400,0],[400,100]]
    shapes2 = [[0,50], [100,50], [50,100], [50,0], [150,0], [150,100],[200,50], 
                [250,0], [250,100], [300,50], [350,100], [350,0],[400,50]]
    col = [c5, c5, c1, c1, c5, c1, c2, c2, c2, c4, c4, c4, c5, c5]
    col2 = [c2, c4, c2, c2, c4, c4, c5, c5, c5, c1, c1, c1, c2]

    e = [-2, -6, -10, -15, -19, -23, -25, -23, -19, -15, -10, -6, -2, 0]
    ls = [28, 25, 22, 20, 17, 14, 12, 14, 17, 20, 22, 25, 28, 30]
    opacity = [0, 0.25, 0.4, 0.5, 0.6, 0.75, 0.9, 1, 0.9, 0.75, 0.6, 0.5, 0.4, 0.25, 0.1, 0]

    for x in range(0, len(ls)): # for every frame in this GIF
        sub1 = fig.add_subplot(1,1,1)
        sub1.xaxis.set_visible(False)
        sub1.yaxis.set_visible(False)
        sub1.set_xlim([0,400])
        sub1.set_ylim([0,100])
        sub1.axis('off')
        sub1.add_patch(patches.Rectangle((0, 0), 400, 100, fc=c3, alpha=1, ec='none'))

        for n in range(0, len(shapes)):
            pts = side8(ls[x], shapes[n][0], shapes[n][1], col[n], e[x])
            pts2 = side8(9, shapes[n][0], shapes[n][1], c3, -25-e[x])
            pts3 = side8(9, shapes[n][0], shapes[n][1], col[n], -25-e[x])
            addShape(pts, 45, 1)
            addShape(pts2, 0, (1-opacity[x])*0.5)
            addShape(pts3, 45)
            addShape(pts2, 45, (1-opacity[x]))
        for n in range(0, len(shapes2)):
            pts = side8(42-ls[x], shapes2[n][0], shapes2[n][1], col2[n], -25-e[x])
            pts2 = side8(9, shapes2[n][0], shapes2[n][1], c3, e[x])
            pts3 = side8(9, shapes2[n][0], shapes2[n][1], col2[n], e[x])
            addShape(pts, 45, 1)
            addShape(pts2, 0, opacity[x]*0.5)
            addShape(pts3, 45)
            addShape(pts2, 45, opacity[x])

        savename = str('temp' + repr(x) + '.png')
        fig.savefig(savename, bbox_inches='tight', pad_inches=0, dpi=50)
        plt.clf()

    images = [] #  Turn a list of images into a GIF using ImageIO
    for n in range(0, len(ls)):
        readname = str('temp' + repr(n) + '.png')
        if readname == 'temp0.png' or readname == 'temp7.png':
            for c in range (0, 7):
                images.append(imageio.imread(readname)) # pause at these frames
        else: 
            images.append(imageio.imread(readname))

    imageio.mimsave(str(tag) + '.gif', images)
    plt.close('all') 
    removal(len(ls))

def pixelSlide(c1, c2, c3, c4, c5, tag):
    '''Pattern 5: Pixel slide'''
    global fig 
    global sub1 # allow other functions to add shapes to the plot
    fig = plt.figure(figsize=(28/float(6), 20/float(6)))
    plt.subplots_adjust(hspace=0, wspace=0)
    c0 = 'none'

    # A huge list of what every pixelcolor should be
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

    # Jitter amount gradually changes to create a smooth effect
    adjust = [[0]*11,
              [random.randint(0,2) for x in range(11)],
              [random.randint(0,4) for x in range(11)],
              [random.randint(0,6) for x in range(11)],
              [random.randint(0,10) for x in range(11)],
              [random.randint(0,12) for x in range(11)],
              [random.randint(0,16) for x in range(11)],
              [random.randint(0,12) for x in range(11)],
              [random.randint(0,10) for x in range(11)],
              [random.randint(0,6) for x in range(11)],
              [random.randint(0,4) for x in range(11)],
              [random.randint(0,2) for x in range(11)]
    ]

    for x in range(0, len(adjust)): # for every frame in the GIF
        sub1 = fig.add_subplot(1,1,1)
        sub1.xaxis.set_visible(False)
        sub1.yaxis.set_visible(False)
        sub1.set_xlim([0, 280])
        sub1.set_ylim([0, 200])
        sub1.axis('off')
        sub1.add_patch(patches.Rectangle((0, 0), 280, 200, fc=c3, alpha=1, ec='none'))

        for n in range(0, 1):
            for y in range(0, len(row)):
                for n in range(0, len(row[0])):   
                    pts = side4(10, 5+10*n, 5+10*y, row[y][n])
                    addShape(pts)
                    seed = random.randint(0, 1)
                    if seed == 1:
                        pts = side4(10, 5+10*n+adjust[x][y], 5+10*y, row[y][n])
                        addShape(pts, alphaParam=random.randint(25, 50)/float(100))
                        pts = side4(10, 5+10*n+adjust[x][y]-280, 5+10*y, row[y][n])
                        addShape(pts, alphaParam=random.randint(25, 50)/float(100))
                    else:
                        pts = side4(10, 5+10*n-adjust[x][y], 5+10*y, row[y][n])
                        addShape(pts, alphaParam=random.randint(25, 50)/float(100))
                        pts = side4(10, 5+10*n-adjust[x][y]+280, 5+10*y, row[y][n])
                        addShape(pts, alphaParam=random.randint(25, 50)/float(100))
            for y in range(0, len(row)):
                for n in range(0, len(row[0])):
                    pts = side4(10, 5+10*n, 210-(5+10*y), row[y][n])
                    addShape(pts)
                    seed = random.randint(0, 1)
                    if seed == 1:
                        pts = side4(10, 5+10*n-adjust[x][y], 210-(5+10*y), row[y][n])
                        addShape(pts, alphaParam=0.25)
                        pts = side4(10, 5+10*n-adjust[x][y]+280, 210-(5+10*y), row[y][n])
                        addShape(pts, alphaParam=0.25)
                    else: 
                        pts = side4(10, 5+10*n+adjust[x][y], 210-(5+10*y), row[y][n])
                        addShape(pts, alphaParam=0.25)
                        pts = side4(10, 5+10*n+adjust[x][y]-280, 210-(5+10*y), row[y][n])
                        addShape(pts, alphaParam=0.25)

        savename = str('temp' + repr(x) + '.png')
        fig.savefig(savename, bbox_inches='tight', pad_inches=0, dpi=50)
        plt.clf() 

    images = [] #  Turn a list of images into a GIF using ImageIO
    for n in range(0, len(adjust)):
        readname = str('temp' + repr(n) + '.png')
        if readname == 'temp1.png':
            for c in range (0, 3):
                images.append(imageio.imread(readname))
        else: 
            images.append(imageio.imread(readname))

    imageio.mimsave(str(tag) + '.gif', images)
    plt.close('all')
    removal(len(adjust))

'''Combine all patterns into one randomizer'''

colorList = [['TestGIF1', ['#C24704', '#D9CC3C', '#fff7c9', '#A0E0BA', '#00ADA7']],
             ['TestGIF2', ['#D9CB84', '#A99E46', '#737D26', '#3F522B', '#302B1D']]]

for x in range(0, len(colorList)):
    tag = colorList[x][0]
    c1 = colorList[x][1][0] 
    c2 = colorList[x][1][1]
    c3 = colorList[x][1][2]
    c4 = colorList[x][1][3]
    c5 = colorList[x][1][4]
    
    # determine frequency of each pattern
    randomList = [20, 40, 60, 80, 100]
    randomSeed = random.randint(1, 100)
    
    if randomSeed <= randomList[0]:
        starFlex(c1, c2, c3, c4, c5, tag)  
    elif randomSeed <= randomList[1]:
        boxSlide(c1, c2, c3, c4, c5, tag)
    elif randomSeed <= randomList[2]:
        circleSize(c1, c2, c3, c4, c5, tag) 
    elif randomSeed <= randomList[3]:
        octagonFlex(c1, c2, c3, c4, c5, tag)
    elif randomSeed <= randomList[4]:
        pixelSlide(c1, c2, c3, c4, c5, tag)
