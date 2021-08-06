from utils import *

def primal(vero, c_A, vo_b):
    #enquanto tiver algum c < 0
    while tem_c_negativo(c_A):
        #encontrando o primeiro c < 0
        a_j = primeiro_c_negativo(c_A)

        #encontrando a menor razao b[i] / A[i, a_j]
        a_i = menor_razao(c_A, vo_b, a_j)
        
        #se nao foi encontrado, entao todo c_A[i, a_j] é <= 0, ilimitada
        if a_i == None:
            return vero, c_A, vo_b, ILIMITADA

        #deixando o pivo c_A[a_i, a_j] = 1
        pivo_igual_a_um(vero, c_A, vo_b, a_i, a_j)

        #fazendo pivoteamento e deixando c_A[i, a_j] = 0, para todo i != a_i
        pivoteia_linhas(vero, c_A, vo_b, a_i, a_j)
    return vero, c_A, vo_b, OTIMA

def auxiliar(vero, c_A, vo_b, N):
    #copy do tableux
    vero_t = vero.copy()
    c_A_t = c_A.copy()
    vo_b_t = vo_b.copy()

    #multiplica as linhas onde b < 0
    for i in range(1, c_A_t.shape[0]):
        if vo_b_t[i] < 0:
            vero_t[i] = vero_t[i] * -1
            c_A_t[i] = c_A_t[i] * -1
            vo_b_t[i] = vo_b_t[i] * -1

    #cria um novo vetor c e adiciona identidade em A
    c_A_t = np.delete(c_A_t, 0, axis=0)
    c = np.array([[0.] * c_A_t.shape[1] + [1.] * N])
    c_A_t = np.append(c_A_t, np.eye(N), axis=1)
    c_A_t = np.append(c, c_A_t, axis=0)

    #pivoteia para zerar acima da identidade
    for i in range(1, c_A_t.shape[0]):
        vero_t[0] = vero_t[0] + vero_t[i] * -1
        c_A_t[0] = c_A_t[0] + c_A_t[i] * -1
        vo_b_t[0] = vo_b_t[0] + vo_b_t[i] * -1

    vero_t, c_A_t, vo_b_t, caso = primal(vero_t, c_A_t, vo_b_t)

    if np.isclose(vo_b_t[0], 0) or caso == ILIMITADA:
        return vero_t, c_A_t, vo_b_t, vero_t[0], VIAVEL
    return vero_t, c_A_t, vo_b_t, vero_t[0], INVIAVEL
