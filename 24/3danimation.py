import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

f = open("24/in.raw", "r")
LOW =200000000000000
HIGH=400000000000000

'''f = open("24/sample.raw", "r")
LOW = 7
HIGH=27
'''
X,Y,Z=0,1,2
P,V=0,1

lines = f.read().splitlines()
hailstones = []
line_eq = []
for line in lines:
    p,v=line.split(' @ ')
    p=tuple(map(int,p.split(', ')))
    v=tuple(map(int,v.split(', ')))
    hailstones.append((p,v))
    const = p[Y] - (v[Y]*p[X]/v[X])
    slope = v[Y]/v[X]
    line_eq.append((slope, const))


num_steps = 250
DIMENSION=1000000000000000
delta_t=DIMENSION/num_steps
delta_t=200000000000
def update_lines(num, lines):
    for i, line in enumerate(lines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data([hailstones[i][0][X],hailstones[i][0][X]+num*delta_t*hailstones[i][1][X]],
                      [hailstones[i][0][Y],hailstones[i][0][Y]+num*delta_t*hailstones[i][1][Y]])
        line.set_3d_properties([hailstones[i][0][Z],hailstones[i][0][Z]+num*delta_t*hailstones[i][1][Z]])
    return lines

# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Create lines initially without data
lines = [ax.plot([], [], [])[0] for _ in hailstones]

# Setting the axes properties
ax.set(xlim3d=(0, 1000000000000000), xlabel='X')
ax.set(ylim3d=(0, 1000000000000000), ylabel='Y')
ax.set(zlim3d=(0, 1000000000000000), zlabel='Z')

# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(lines), interval=100)

plt.show()