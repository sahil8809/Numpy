from scipy import linalg
import numpy as np

arr = np.array([[5,4],[6,3]])
eg_val, eg_vec = linalg.eig(arr)
print(80*'-')
print("Eigen value -",eg_val)
print(80*'-')
print("Eigen vector -",eg_vec)
print(80*'-')