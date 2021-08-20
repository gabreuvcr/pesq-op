from utils import *

num_elem, num_subconj, custos_subconj, A = entrada()

y, x = cobertura_por_conjuntos(num_elem, num_subconj, custos_subconj, A)
imprime_solucao(y, x)
