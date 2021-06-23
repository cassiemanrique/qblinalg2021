import matplotlib.pyplot as plt
import numpy as np

vec=np.array([[-1,3], [2,-4]])

origin=np.zeros(vec.shape)

plt.figure(figsize=(6,6))
plt.quiver(*origin,*vec,color=["c","m","y"],scale=1,units="xy")
plt.grid()
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.gca()
plt.show()