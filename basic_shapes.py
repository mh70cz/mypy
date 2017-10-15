#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 12:35:47 2017

@author: mh70
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 12:20:04 2017

@author: mh70
"""

import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.path import Path

#a = plt.plot([0.2, 0.2], [0.2, 0.8], [0.8, 0.8], [0.2, 0.8])


center = (0.5, 0.5)
radius = 0.3
c = plt.Circle(center, radius, color='r', fill = False)

width, heigth =  radius, radius * 1.8
angle = -30
e = patches.Ellipse(center, width, heigth, angle = -30)

a = patches.Arc(center, width * 1.5 , heigth * 1.5,  angle=60,
                theta1=45, theta2=135, color = "green")

vertices = [
    (0.3, 0.3),
    (0.4, 0.7),
    (0.7, 0.7),
    (0.6, 0.3),
    (0., 0.), # ignored
        ]
codes = [
    Path.MOVETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.CLOSEPOLY,
        ]
path = Path(vertices, codes)
patch_p = patches.PathPatch(path, facecolor="orange")


fig, ax = plt.subplots()
ax.set_aspect('equal')

ax.add_patch(e)
ax.add_artist(c)
ax.add_patch(a)
ax.add_patch(patch_p)
ax.plot([0.2, 0.2, 0.8, 0.8], [0.2, 0.8, 0.2, 0.8], "o", color = 'y')
ax.plot( [0.1, 0.9, 0.5, 0.1], [0.1, 0.1, 0.9, 0.1], "x--", color = "black")

"""
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

A Circle is a subclass of an Artist, and an axes has an add_artist method.

"""