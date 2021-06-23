import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


vec=np.array([[-1,3],[2,-4]])

res=vec[0]+vec[1]

origin=np.zeros(vec.shape)

plt.figure(figsize=(6,6))
plt.quiver(*origin,*vec,color=["c","m"],scale=1,units="xy")
plt.quiver(*origin,*res,color=["y"],scale=1,units="xy")
plt.grid()
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.gca()

v1=mpatches.Patch(color="c",label="Vector 1")
v2=mpatches.Patch(color="m",label="Vector 2")
v12=mpatches.Patch(color="y",label="Vector 1+2")
plt.legend(handles=[v1,v2,v12])
plt.show()