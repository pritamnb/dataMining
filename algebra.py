import numpy as np
import matplotlib.pyplot as plt

# Define matrices A and B
A = np.array([[2, -1], [-1, 2]])
B = np.array([0, 3])

# Solve the linear equation using NumPy's linalg.solve()
X = np.linalg.solve(A, B)
print('X0',X[0])
print('X1',X[1])

# Extract column vectors from A
VA1 = A[:, 0]
VA2 = A[:, 1]
print('VA1',VA1)
print('VA2',VA2)

# Scaled column vectors
VA1_scaled = VA1 * X[0]
VA2_scaled = VA2 * X[1]

# Linear combination
linear_combination = VA1_scaled + VA2_scaled

# Plotting
origin = [0], [0]  # origin point
plt.quiver(*origin, VA1[0], VA1[1], color='r', scale=1, label='VA1')
plt.quiver(*origin, VA2[0], VA2[1], color='b', scale=1, label='VA2')
plt.quiver(*origin, VA1_scaled[0], VA1_scaled[1], color='g', scale=1, label='VA1 Scaled by X[0]')
plt.quiver(*origin, VA2_scaled[0], VA2_scaled[1], color='m', scale=1, label='VA2 Scaled by X[1]')
plt.quiver(*origin, linear_combination[0], linear_combination[1], color='k', scale=1, label='Linear Combination')

plt.xlim(-1, 3)
plt.ylim(-1, 3)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title('Linear Combination of Vectors')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
