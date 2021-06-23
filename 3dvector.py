import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig=plt.figure(figsize=(6,6))
ax=fig.gca(projection='3d')

vec=np.array([[7,-5],[7,2],[4,-1]])
origin=np.zeros(vec.shape)

ax.quiver(*origin,*vec,color=["c"])

plt.grid()
ax.set_zlim3d(-10,10)
ax.set_ylim3d(-10,10)
ax.set_xlim3d(-10,10)
plt.show()