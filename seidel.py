import numpy as np
import math 

# M = np.array([
# [-4.0,2.0,0.0,1.0,-36.0],
# [1.0,-2.0,1.0,0.0,0.0],
# [0.0,2.0,-3.0,1.0,0.0],
# [5.0,0.0,5.0,-12.0,0.0]])

M = np.array([
[12.0000,	12.0000,	18.0000,	1080.0000],
[10.0000,	12.0000,15.0000,	960.0000],
[6.0000,	8.0000,	12.0000,	660.0000]
])

xInicial = np.array([0.0,0.0,0.0])
precisao = 0.0001
C0 =M[0]

x1 = (C0[3] - xInicial[1]*C0[1] - xInicial[2]*C0[2])/C0[0]

print(x1)

C1 =M[1]
x2 = (C1[3] - x1*C1[0] - xInicial[2]*C1[2])/C1[1]

print(x2)

C2 =M[2]
x3 = (C2[3] - x1*C2[0] - x2*C2[1] )/C2[2]

print(x3)

x1A=x1
x3A=x3
x2A=x2

print()
deltaX1 = math.fabs(x1 -xInicial[0])
print(deltaX1)
deltaX2 = math.fabs(x2 -xInicial[1])
print(deltaX2)
deltaX3 = math.fabs(x3 -xInicial[2])
print(deltaX3)


if deltaX1<deltaX2:
    maiorD = deltaX2
else: 
    maiorD = deltaX1

if maiorD < deltaX3:
    maiorD = deltaX3
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

print(maior)


mr = maiorD/math.fabs(maior)
i=0
while(mr > precisao):
    i = i + 1
    x1 = (C0[3] - x2*C0[1] - x3*C0[2])/C0[0]

    x2 = (C1[3] - x1*C1[0] - x3*C1[2] )/C1[1]

    x3 = (C2[3] - x1*C2[0] - x2*C2[1] )/C2[2]

 


    deltaX1 = math.fabs(x1 -x1A)

    deltaX2 = math.fabs(x2 -x2A)

    deltaX3 = math.fabs(x3 -x3A)




    if deltaX1<deltaX2:
        maiorD = deltaX2
    else: 
        maiorD = deltaX1

    if maiorD < deltaX3:
        maiorD = deltaX3
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


    
    mr = maiorD/math.fabs(maior)
    x1A=x1
    x3A=x3
    x2A=x2
    


print("iterações executadas:") 
print( i ) 

print()
print("x1:")
print(x1)
print("x2:")
print(x2)
print("x3:")
print(x3)
