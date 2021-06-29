import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from numpy import linalg as LA

vec=np.array([[4,3], [1,2]]) #create a matrix

eigenvalues, eigenvectors =  LA.eig(vec) #find eigenvalues and eigenvectors 

transform=np.matmul(vec,eigenvectors) #multiple matrix by eigenvectors

x_comp=eigenvectors[0, :] #x component of eigenvectors
y_comp=eigenvectors[1, :] #y component of eigenvectors

x_trans=transform[0, :] #x component of new matrix
y_trans=transform[1, :] #y componnet of new matrix 

origin = np.array([[0, 0],[0, 0]]) #set origin for plot 

plt.figure(figsize=(6,6))
plt.quiver(*origin, x_comp,y_comp,color=["blue", "green"],scale=1,units="xy") #plot eigenvectors
plt.quiver(*origin, x_trans, y_trans, color=["red", "orange"], alpha=0.5, scale=1, units="xy") #plot transformed vectors sheer
plt.grid()
plt.xlim(-5,5) #x axis limits
plt.ylim(-5,5) #y axis limits 

#legend
xeigen=mpatches.Patch(color="blue",label="X Component Eigenvector")
yeigen=mpatches.Patch(color="green",label="Y Component Eigenvector")
xtrans=mpatches.Patch(color="red", label="X Component Transformed")
ytrans=mpatches.Patch(color="orange",label="Y Component Transformed")
plt.legend(handles=[xeigen, yeigen, xtrans, ytrans],loc="lower right")

plt.title("Eigenvectors with Matrix Transformation") #title 
plt.gca()
plt.show()