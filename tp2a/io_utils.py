from utils import *

def entrada():
    N, M = [int(l) for l in input().split()]
    a = np.empty(shape=(0, M))
    c = np.array([])
    b = np.array([int(i) for i in input().split()])
    for _ in range(N):
        ai = [int(i) for i in input().split()]
        a = np.append(a, [ai], axis=0)
    for j in range(M):
        if a[0, j] == -1:
            c = np.append(c, 1)
        else:
            c = np.append(c, 0)
    return a, b, c, N, M

def imprime_tableux(vero, c_A, vo_b):
    for i in range(c_A.shape[0]):
        for j in range(vero.shape[1]):
            print(f"{int(vero[i, j]):3}", end=' ')
        print("|", end=' ')
        for j in range(c_A.shape[1]):
            print(f"{int(c_A[i, j]):3}", end=' ')
        print(f"|{int(vo_b[i]):3}")

def imprime(arr):
    for i in arr:
        print(f"{int(i)}", end=' ')
    print()

def imprime_solucao(c_A, vo_b, certificado, M):
    valor_otimo = [vo_b[0]]
    solucao_otima = obter_solucao_otima(c_A, vo_b, M) 
    imprime(valor_otimo)
    imprime(solucao_otima)
    imprime(certificado)
