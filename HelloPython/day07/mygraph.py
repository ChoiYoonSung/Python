from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')
z = np.array([30,15,26,73,12])
x = np.array([1,1,1,1,1])
y = np.array([0,1,2,3,4])

print(z)

ax.plot3D(x, y, z, 'maroon')
ax.set_title('3D line plot')
plt.show()