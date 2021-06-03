from scipy import linalg
import numpy as np
from scipy import linalg

# A = np.array([[-4,2,0,1],[1,-2,1,0],[0,2,-3,1],[5,0,5,-12]])
# print(A)

# b = np.array([-36,0,0,72])
# print(b)

# x = linalg.solve(A,b)
# print(x)

M = np.array([[-4.0,2.0,0.0,1.0],[1.0,-2.0,1.0,0.0],[0.0,2.0,-3.0,1.0],[5.0,0.0,5.0,-12.0]])
b = np.array([-36.0,0.0,0.0,0.0])
print(M)

# zeramento da segunda linha 
m1 = M[1,0]/M[0,0]
M[1,:] = np.add(M[1,:], - m1*M[0,:], out=M[1,:], casting="unsafe")
# M[1,:] += - m1*M[0,:]
print(M)

m2 = M[2,0]/M[0,0]
M[2,:] = np.add(M[2,:], - m2*M[0,:], out=M[2,:], casting="unsafe")

print(M)

m3 = M[3,0]/M[0,0]
M[3,:] = np.add(M[3,:], - m3*M[0,:], out=M[3,:], casting="unsafe")

print(M)

# eliminação
def eliminacao(M):
    m,n = M.shape
    for i in range(m):
        for j in range(i+1,n):
            pivo = M[j,i]/M[i,i]                        
            for k in range(m):
                M[j,k] += -pivo*M[i,k]
    return M  

print(eliminacao(M))