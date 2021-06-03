import numpy as np
import math 

# M = np.array([
# [-4.0,2.0,0.0,1.0,-36.0],
# [1.0,-2.0,1.0,0.0,0.0],
# [0.0,2.0,-3.0,1.0,0.0],
# [5.0,0.0,5.0,-12.0,0.0]])

M = np.array([



[8.05,	-4.7,	5.05,	1.25,	38.36],
[0.36,	9.05,	-4.77,	-4.78,	-20.6700],
[3.21,	7.36,	4.9500,	-6.350,31.07],
[2.02,	7.77,	-3.3600,-6.72,	0.00]

])

xInicial = np.array([0.0,0.0,0.0,0.0])
precisao = 0.0001
C0 =M[0]

x1 = (C0[4] - xInicial[1]*C0[1] - xInicial[2]*C0[2] - xInicial[3]*C0[3])/C0[0]
C1 =M[1]
x2 = (C1[4] - xInicial[0]*C1[0] - xInicial[2]*C1[2] - xInicial[3]*C1[3])/C1[1]
C2 =M[2]
x3 = (C2[4] - xInicial[0]*C2[0] - xInicial[1]*C2[1] - xInicial[3]*C2[3])/C2[2]
C3 =M[3]
x4 = (C3[4] - xInicial[0]*C3[0] - xInicial[1]*C3[1] - xInicial[2]*C3[2])/C3[3]

x1A=x1
x3A=x3
x2A=x2
x4A = x4


print()
deltaX1 = math.fabs(x1 -xInicial[0])
print(deltaX1)
deltaX2 = math.fabs(x2 -xInicial[1])
print(deltaX2)
deltaX3 = math.fabs(x3 -xInicial[2])
print(deltaX3)
deltaX4 = math.fabs(x4 -xInicial[3])
print(deltaX4)
print()

if deltaX1<deltaX2:
    maiorD = deltaX2
else: 
    maiorD = deltaX1

if maiorD < deltaX3:
    maiorD = deltaX3
else:
    maiorD = maiorD

if maiorD < deltaX4:
    maiorD = deltaX4
else:
    maiorD = maiorD

print(maiorD)
print()

if x1<x2:
    maior = x2
else: 
    maior = x1

if maior < x3:
    maior = x3
else:
    maior = maior

if maior < x4:
    maior = x4
else:
    maior = maior

print(maior)


mr = maiorD/math.fabs(maior)
while(mr > precisao):
    x1 = (C0[4] - x2A*C0[1] - x3A*C0[2] - x4A*C0[3])/C0[0]
    
    x2 = (C1[4] - x1A*C1[0] - x3A*C1[2] - x4A*C1[3])/C1[1]

    x3 = (C2[4] - x1A*C2[0] - x2A*C2[1] - x4A*C2[3])/C2[2]

    x4 = (C3[4] - x1A*C3[0] - x2A*C3[1] - x3A*C3[2])/C3[3]


    deltaX1 = math.fabs(x1 -x1A)

    deltaX2 = math.fabs(x2 -x2A)

    deltaX3 = math.fabs(x3 -x3A)

    deltaX4 = math.fabs(x4 -x4A)


    if deltaX1<deltaX2:
        maiorD = deltaX2
    else: 
        maiorD = deltaX1

    if maiorD < deltaX3:
        maiorD = deltaX3
    else:
        maiorD = maiorD

    if maiorD < deltaX4:
        maiorD = deltaX4
    else:
        maiorD = maiorD

    if x1<x2:
        maior = x2
    else: 
        maior = x1

    if maior < x3:
        maior = x3
    else:
        maior = maior

    if maior < x4:
        maior = x4
    else:
        maior = maior
    
    mr = maiorD/math.fabs(maior)

    x1A = x1
    x2A = x2
    x3A = x3
    x4A = x4


print()
print("x1:")
print(x1)
print("x2:")
print(x2)
print("x3:")
print(x3)
