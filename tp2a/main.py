from utils import *
from io_utils import *

a, b, c, N, M = entrada()

a, N = remove_s_t(a, N)

vero, c_A, vo_b = gera_tableaux(a, b, c, N, M)
del a, b, c

vero, c_A, vo_b  = simplex(vero, c_A, vo_b)

certificado = obter_certificado(vero, N)

imprime_solucao(c_A, vo_b, certificado, M)
