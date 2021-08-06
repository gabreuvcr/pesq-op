from utils import *

def entrada():
    N, M = [int(l) for l in input().split()]
    a = np.empty(shape=(0, M))
    b = np.array([])
    c = np.array([float(i) for i in input().split()])
    for _ in range(N):
        Ab = [float(i) for i in input().split()]
        b = np.append(b, Ab[-1])
        Ab.pop()
        a = np.append(a, [Ab], axis=0)
    return a, b, c, N, M

def imprime_tableux(vero, c_A, vo_b):
    for i in range(c_A.shape[0]):
        for j in range(vero.shape[1]):
            print(f"{vero[i, j]:7.2f}", end=' ')
        print("|", end=' ')
        for j in range(c_A.shape[1]):
            print(f"{c_A[i, j]:7.2f}", end=' ')
        print(f"|{vo_b[i]:7.2f}")

def imprime(arr):
    for i in arr:
        print(f"{i:.7f}", end=' ')
    print()

def imprime_inviavel(certificado_auxiliar):
    print("inviavel")
    imprime(certificado_auxiliar)

def imprime_otima(vero, c_A, vo_b, M):
    print("otima")
    imprime([vo_b[0]])
    imprime(obter_solucao_otima(c_A, vo_b, M))
    imprime(vero[0])

def imprime_ilimitada(c_A, vo_b, M):
    print("ilimitada")
    imprime(obter_solucao_otima(c_A, vo_b, M))
    imprime(obter_certificado_ilimitada(c_A, M))
