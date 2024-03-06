import numpy as np
import matplotlib.pyplot as plt
p=0.7
n=60
N=60000
success= np.random.binomial(n,p,N)
plt.hist(success,bins=30)
plt.show()