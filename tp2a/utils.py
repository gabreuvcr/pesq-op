import numpy as np

def remove_s_t(a, N):
    a = a[1:-1]
    N = N - 2
    return a, N

def transforma_fpi(a, b, c, N, M):
    aux = np.array([np.zeros(M)] * N)
    aux = np.concatenate((aux, np.eye(M)), axis=0)
    a = np.append(a, np.eye(M), axis=0)
    a = np.append(a, aux, axis=1)
    c = np.append(c, [0.] * M)
    b = np.append([0.] * N, b)
    return a, b, c

def gera_tableaux(a, b, c, N, M):
    a, b, c = transforma_fpi(a, b, c, N, M)
    vero = np.array([[0.] * (M + N)])
    vero = np.append(vero, np.eye(M + N), axis=0)
    c_A = np.append([-c], a, axis=0)
    vo_b = np.append([0.], b, axis=0)
    return vero, c_A, vo_b

def tem_c_negativo(c_A):
    for j in range(c_A.shape[1]):
        if c_A[0, j] < 0 and not np.isclose(c_A[0, j], 0):
            return True
    return False

def primeiro_c_negativo(c_A):
    for j in range(c_A.shape[1]):
        if c_A[0, j] < 0 and not np.isclose(c_A[0, j], 0):
            return j
    return -1

def menor_razao(c_A, vo_b, a_j):
    a_i = None
    for i in range(1, c_A.shape[0]):
        if c_A[i, a_j] < 0 or np.isclose(c_A[i, a_j], 0): 
            continue
        if a_i == None or vo_b[i] / c_A[i, a_j] < vo_b[a_i] / c_A[a_i, a_j]:
            a_i = i
    return a_i

def pivo_igual_a_um(vero, c_A, vo_b, a_i, a_j):
    razao = c_A[a_i, a_j]
    c_A[a_i] = c_A[a_i] / razao
    vero[a_i] = vero[a_i] / razao
    vo_b[a_i] = vo_b[a_i] / razao

def pivoteia_linhas(vero, c_A, vo_b, a_i, a_j):
    for i in range(0, c_A.shape[0]):
        if i != a_i:
            razao = - c_A[i, a_j] / c_A[a_i, a_j]
            c_A[i] = c_A[i] + c_A[a_i] * razao
            vero[i] = vero[i] + vero[a_i] * razao
            vo_b[i] = vo_b[i] + vo_b[a_i] * razao

def obter_certificado(vero, N):
    certificado = np.array([1])
    for i in range(N):
        certificado = np.append(certificado, vero[0, i])
    certificado = np.append(certificado, 0)
    return certificado

def base(c_A, j):
    return (np.isclose(c_A[0, j], 0) and np.sum(c_A[1:, j] == 1) == 1 
            and np.all(np.logical_or(c_A[1:, j] == 0, c_A[1:, j] == 1)))

def obter_solucao_otima(c_A, vo_b, M):
    solucao_otima = np.array([0.] * M)
    for j in range(M):
        if not base(c_A, j): continue

        for i in range(1, c_A.shape[0]):
            if c_A[i, j] == 1:
                x_j = vo_b[i]
        solucao_otima[j] = x_j
        
    return solucao_otima

def simplex(vero, c_A, vo_b):
    while tem_c_negativo(c_A):
        a_j = primeiro_c_negativo(c_A)
        a_i = menor_razao(c_A, vo_b, a_j)

        pivo_igual_a_um(vero, c_A, vo_b, a_i, a_j)
        
        pivoteia_linhas(vero, c_A, vo_b, a_i, a_j)

    return vero, c_A, vo_b
