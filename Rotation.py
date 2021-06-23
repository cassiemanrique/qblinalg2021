import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


vec=np.array([3,4])
rotate=np.array([[0,1],[-1,0]])

rotated=np.matmul(vec,rotate)

origin=np.zeros(vec.shape)

plt.figure(figsize=(6,6))
plt.quiver(*origin,*vec,color=["c"],scale=1,units="xy")
plt.quiver(*origin,*rotated,color=["m"],scale=1,units="xy")
plt.grid()
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.gca()

v1=mpatches.Patch(color="c",label="Original")
v2=mpatches.Patch(color="m",label="Rotated 90 Counterclockwise")
plt.legend(handles=[v1,v2],loc="lower right")
plt.show()