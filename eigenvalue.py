import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from numpy import linalg as LA

vec=np.array([[4,3], [1,2]]) #making a vector

eigenvalues, eigenvectors =  LA.eig(vec) #compute the eigenvalues

#print the eigenvalues
print('lambda_1: {}, v_1: {}'.format(eigenvalues[0], eigenvectors[:, 0]))
print('lambda_2: {}, v_2: {}'.format(eigenvalues[1], eigenvectors[:, 1]))

#separate eigenvectors into x and y components
x_comp=eigenvectors[0, :]
y_comp=eigenvectors[1, :]

#set origin for plot
origin = np.array([[0, 0],[0, 0]])

plt.figure(figsize=(6,6))
plt.quiver(*origin, x_comp,y_comp,color=["blue", "green"],scale=1,units="xy") #plot eigenvectors
plt.grid()
plt.xlim(-1,1)
plt.ylim(-1,1)

#create legend
x=mpatches.Patch(color="blue",label="X Component") 
y=mpatches.Patch(color="green",label="Y Component")
plt.legend(handles=[x,y],loc="lower right")

plt.title("Eigenvectors") #title
plt.gca()
plt.show()
