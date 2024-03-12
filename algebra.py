import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2,-1],[-1,2]])
B = np.array([0,3])

# vector X that satisfies the equation AX=B.
X = np.linalg.solve(A,B)
print("X=",X)

#solving for X the inverse of matrix A
A_in = np.linalg.inv(A)
X_by_in = np.matmul(A_in,B)
#print(X_by_in)
print("X from inverse=",X_by_in)

def linear_combination(A, X):

  va1 = A[:,0]
  va2 = A[:,1]
  VA1_scaled = va1*X[0]
  VA2_scaled = va2*X[1]

  combination = VA1_scaled + VA2_scaled
  
  plt.plot([0,va1[0]],[0,va1[1]], 'b-',label = 'VA1')
  plt.plot([0,va2[0]],[0,va2[1]], 'r-',label = 'VA2')
  plt.plot([0,VA1_scaled[0]],[0,VA1_scaled[1]], 'y',label = 'VA1 scaled by X[0]')
  plt.plot([VA1_scaled[0], VA1_scaled[0] + VA2_scaled[0]],[VA1_scaled[1], VA1_scaled[1] + VA2_scaled[1]],'g', label= 'VA2 scaled by X[1]')
  plt.plot([0, combination[0]], [0,combination[1]], 'c' , label = 'linear Combination')
  
  plt.xlabel('X-axis')
  plt.ylabel('Y-axis')
  plt.title("Linear Combination of Vectors")
  plt.legend()

  # Show plot
  plt.grid()
  plt.show()

A = np.array([[2,-1],[-1,2]])
B = np.array([0,3])
X_solver= np.linalg.solve(A,B)
print(f"x is", X_solver)
linear_combination(A,X_solver)