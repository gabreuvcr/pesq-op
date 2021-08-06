from simplex import *
from io_utils import *

a, b, c, N, M = entrada()

np.set_printoptions(precision=7, suppress=True)

vero, c_A, vo_b = gera_tableaux(a, b, c, N)
del a, b, c

vero_aux, c_A_aux, vo_b_aux, certificado_aux, caso = auxiliar(vero, c_A, vo_b, N)

if caso == INVIAVEL:
    imprime_inviavel(certificado_aux)
else:
    vero, c_A, vo_b = reaproveita_auxiliar(vero_aux, c_A_aux, vo_b_aux, c_A[0], N, M)

    vero, c_A, vo_b, caso = primal(vero, c_A, vo_b)

    if caso == OTIMA:
        imprime_otima(vero, c_A, vo_b, M)
    elif caso == ILIMITADA:
        imprime_ilimitada(c_A, vo_b, M)
