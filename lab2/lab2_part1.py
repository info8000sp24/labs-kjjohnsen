# Kyle Johnsen
# Lab 2 Part 1

## Part A, Compute the height of the triangle

# Test case. I know that the height of this triangle is 24
a = 40
b = 30
c = 50

# This is Heron's formula broken up into 3 parts
s = (a + b + c) / 2 # half perimeter
A_squared = s*(s-a)*(s-b)*(s-c)
A = A_squared**.5 # note, also could use math library

# area = .5 * base * height.  We know the base is c, so
h = 2*A/c

print(f"The height of the triangle ({a},{b},{c}) is {h}")

## Part B Compute the 3 points of the triangle
p1 = (0,0) # assume origin
p2 = (c,0) # assume c is the base down the positive x axis
x = (a*a - h*h)**.5 # by Pythagorean theorem 
p3 = (x,h) # point at the top
p4 = (x,0) # point at the base

## Part C Visualize
import matplotlib.pyplot as plt # note, normally would do this at the top
triangle_points = [p1,p2,p3,p1]
height_points = [p3,p4]
plt.plot(*zip(*triangle_points),"b")
plt.plot(*zip(*height_points),"r--")
plt.axis('equal') # no distortion

# draw the labels about 1/2 way along each leg
a_x,a_y = p3[0]/2,p3[1]/2
b_x,b_y = (p2[0] + p3[0])/2,(p2[1] + p3[1])/2
c_x,c_y = c/2,0
h_x,h_y = p4[0],p3[1]/2

offset = 10 # this is a bit of a magic number, because it's related to the default text size
            # a slightly better way to do this would require some more math (e.g. rotate the label)
plt.annotate(f"{a}",(a_x,a_y),(-offset,0),textcoords='offset points',ha="right",va="center")
plt.annotate(f"{b}",(b_x,b_y),(offset,0),textcoords='offset points',ha="left",va="center")
plt.annotate(f"{c}",(c_x,c_y),(0,-offset),textcoords='offset points',ha="center",va="top")
plt.annotate(f"{h}",(h_x,h_y),(offset,0),textcoords='offset points',ha="left",va="center")

plt.show()