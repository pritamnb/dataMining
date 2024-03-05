import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2,-1],[-1,2]])
B = np.array([0,3])
X = np.linalg.solve(A,B)
A_in = np.linalg.inv(A)
X_by_in = np.matmul(A_in,B)
va1 = np.array([3, -2])
va2 = np.array([-1, 2])
vx1 = X[0]
vx2 = X[1]
print('va1', va1)
print('va2', va2)
print('vx1 ',vx1)
print('vx2',vx2)

plt.clf()

plt.arrow(0,0,va1[0],va2[0], color="blue")
plt.arrow(0,0,va1[1], va2[1], color="orange")
plt.arrow(0,0,vx1,vx2,color="black")
plt.arrow(0, 0, B[0], B[1], color="purple")

plt.xlim((-1, 3))
plt.ylim((-1, 3))
plt.title("2D picture")
plt.show()

# https://realpython.com/python-linear-algebra/
# https://realpython.com/python-scipy-linalg/
# https://realpython.com/python-scipy-linalg/#working-with-vectors-and-matrices-using-numpy
# https://realpython.com/python-linear-algebra/