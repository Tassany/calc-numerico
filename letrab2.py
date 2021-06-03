import math
from scipy import linalg
import numpy as np
from scipy import linalg

def gaussPivo(A,b):
    #acessas as linhas
    for i in range(len(A)):
        #verificar qual o maior pivo
        pivo = math.fabs(A[i][i])
        linhaPivo = i
        for j in range(i+1,len(A)):
            if math.fabs(A[j][i]) > pivo:
                pivo = math.fabs(A[j][i])
                linhaPivo = j
        #permutar as linhas
        if linhaPivo!=i:
            linhaAuxiliar = A[i]
            A[i] = A[linhaPivo]
            A[linhaPivo] = linhaAuxiliar

            bAuxiliar = b[i]
            b[i] = b[linhaPivo]
            b[linhaPivo] = bAuxiliar

        #eliminação gaussiana
        for m in range (i + 1, len (A)):
            multiplicador = A[m][i]/A[i][i]
            for n in range(i, len(A)):
                A[m][n] -= multiplicador*A[i][n]
            b[m] -= multiplicador*b[i]
    #Matriz a escalonada e o vetor b escalonado
    for k in range(len(A)):
        print(A[k])
    print()
    print(b)

    calculaSolucao(A,b)



def calculaSolucao(A,b):
    vetorSolucao = []
    for i in range (len(A)):
        vetorSolucao.append(0)
    linha = len(A) - 1 
    while linha>=0:
        x=b[linha]
        coluna = len(A) - 1
        while coluna > linha:
            x-=A[linha][coluna]*vetorSolucao[coluna]
            coluna -= 1 
        x/= A[linha][linha]
        linha = 1
        vetorSolucao[coluna] = x

    for j in range(len(vetorSolucao)):
        print("x" + str(j)+ "=" +vetorSolucao[j])



A = np.array([[-4.0,2.0,0.0,1.0],[1.0,-2.0,1.0,0.0],[0.0,2.0,-3.0,1.0],[5.0,0.0,5.0,-12.0]])
print(A)
print()
b = np.array([-36.0,0.0,0.0,0.0])
print(b)
print("Matrizes escalonadas:")
gaussPivo(A, b)