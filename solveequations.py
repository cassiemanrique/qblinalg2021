import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

A= np.array([[4, -2, 1], [-2, 4, -2], [1, -2, 4]])
B= np.array([11, -16, 17])

Solution=np.linalg.solve(A,B)

print(Solution)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y = np.linspace(-10,10,100), np.linspace(-10,10,100)
X, Y = np.meshgrid(x,y)

Z1 = 11 - 4*X + 2*Y
Z2 = (16 - 2*X + 4*Y) / 2
Z3 = (17 - X + 2*Y) / 4

ax.plot_surface(X,Y,Z1, alpha=0.5, facecolors="b", rstride=100, cstride=100)
ax.plot_surface(X,Y,Z2, alpha=0.5, facecolors="y", rstride=100, cstride=100)
ax.plot_surface(X,Y,Z3, alpha=0.5, facecolors='g', rstride=100, cstride=100)

ax.plot([1,1],[-10,10],[-13,27], lw=2, color="r")

ax.plot((1,),(-2,),(3,), lw=2, c='k', marker='o')

plt.show()