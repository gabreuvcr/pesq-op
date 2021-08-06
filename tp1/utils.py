import numpy as np

OTIMA, ILIMITADA, INVIAVEL, VIAVEL = 0, 1, 2, 3

def transforma_fpi(a, b, c, N):
    a = np.append(a, np.eye(N), axis = 1)
    c = np.append(c, [0.] * N)
    return a, b, c

def gera_tableaux(a, b, c, N):
    a, b, c = transforma_fpi(a, b, c, N)
    vero = np.array([[0.] * N])
    vero = np.append(vero, np.eye(N), axis = 0)
    c_A = np.append([-c], a, axis = 0)
    vo_b = np.append([0.], b, axis = 0)
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

def reaproveita_auxiliar(vero_aux, c_A_aux, vo_b_aux, c_original, N, M):
    vero = vero_aux
    vero[0] = vero[0] * 0
    c_A = c_A_aux[:, : N + M]
    c_A[0] = c_original
    vo_b = vo_b_aux
    vo_b[0] = vo_b[0] * 0

    for j in range(c_A.shape[1]):
         if not np.isclose(c_A[0, j], 0) and np.sum(c_A[1:, j] == 1) == 1:
             for i in range(1, c_A.shape[0]):
                 if c_A[i, j] == 1:
                     pivoteia_linhas(vero, c_A, vo_b, i, j)
    return vero, c_A, vo_b

def obter_solucao_otima(c_A, vo_b, M):
    solucao_otima = np.array([0.] * M)
    for j in range(M):
        x_j = None
        if np.isclose(c_A[0, j], 0) and np.sum(c_A[1:, j] == 1) == 1:
            for i in range(1, c_A.shape[0]):
                if c_A[i, j] == 1:
                    x_j = vo_b[i]
        if x_j:
            solucao_otima[j] = x_j
    return solucao_otima

def obter_certificado_ilimitada(c_A, M):
    a_j = primeiro_c_negativo(c_A)
    certificado_ilimitada = np.array([0.] * M)
    if a_j < M:
        certificado_ilimitada[a_j] = 1
    if np.all(c_A[1:, a_j] <= 0):
        for j in range(M):
            if j == a_j: continue
            a_ij = None
            if c_A[0, j] == 0 and np.sum(c_A[1:, j] == 1) == 1:
                for i in range(1, c_A.shape[0]):
                    if c_A[i, j] == 1:
                        a_ij = -c_A[i, a_j]
            if a_ij:
                certificado_ilimitada[j] = a_ij
            else:
                certificado_ilimitada[j] = 0
    return certificado_ilimitada
