"""
    Ana Zeneli
    Lab 3: VGraph algorithm implementation
"""
from math import pow
from scipy.spatial import ConvexHull
import numpy as np
import matplotlib.pyplot as plt

# Grow the obstacles using reflection algorithm
def load_obstacles():
    with open('../data/world_obstacles.txt', 'r') as f:
        obstacles = []
        # initialize number of objects
        num_obs =  f.readline()
        print num_obs
        ob = []

        for line in f:
            if len(line.split()) == 1 :
                # reset ob so lists are proper vertex length
                ob = []

                # set number of vertices
                num_v = int(line)
            else:
                ob.append((int(line.split()[0]),  int(line.split()[1])))

            num_v -= 1
            if num_v == 0:
                obstacles.append(ob)

        # for i in  obstacles:
        #     print len(i), i
    return obstacles
#
# def find_midpoints(obstacles):
#     mids = []
#     for i in obstacles:
#         if len(i) == 3:
#             m1 = (i[0][0] + i[1][0]) /2 ,  (i[0][1] + i[1][1]) / 2
#             m2 = (2*float(i[2][0])/3 + 1*float(m1[0])/3 , 2*float(i[2][1])/3 + 1*float(m1[1])/3 )
#             mids.append(m2)
#         elif len(i) == 4:
#             x = [x[0] for x in i ]
#             y = [y[1] for y in i ]
#
#             m1 = sum(x) / float(len(x)) , sum(y)/ float(len(y))
#             mids.append(m1)
#
#     return mids

def grow_obstacles(obstacles):
    grown = []
    for i in obstacles:
        ob = []

        for j in i:
            xl = j[0] - 18
            xr = j[0] + 18
            yt = j[1] + 18
            yb = j[1] - 18
            # append all possible combos of grown obtacle
            ob.append((xl,yt))
            ob.append((xl, yb))
            ob.append((xr, yt))
            ob.append((xr, yb))

        grown.append(ob)

    return grown

def write_grown_obstacles_file(obs):
    num_obs = len(obs)
    with open('world_obstacles_grown.txt', 'w') as file:
        file.write("%d\n" % num_obs)
        for i in grown:
            points = np.array(i)
            hull = ConvexHull(points)
            hull_points = []

            hull_points = zip(points[hull.vertices,0], points[hull.vertices,1])
            file.write("%d\n" % len(hull_points))
            for i in hull_points:
                file.write("%d " % i[0])
                file.write("%d"  % i[1])
                file.write("\n")

            # print len(hull_points),hull_points

if __name__ == "__main__":
    obstacles = load_obstacles()
    grown = grow_obstacles(obstacles)
    write_grown_obstacles_file(grown)
