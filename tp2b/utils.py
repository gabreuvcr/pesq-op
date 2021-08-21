import numpy as np

def entrada():
    num_elem, num_subconj = [int(l) for l in input().split()]
    custos_subconj = np.array([int(l) for l in input().split()])
    A = np.array([[int(l) for l in input().split()] for _ in range(num_elem)])
    return num_elem, num_subconj, custos_subconj, A

def imprime(arr):
    for i in arr:
        print(f"{int(i)}", end=' ')
    print()

def imprime_solucao(y, x):
    imprime(y)
    imprime(x)

def ponto_descoberto(y, A, num_elem):
    for i in range(num_elem):
        if sum(A[i] * y) == 0:
            return i
    return None

def valor_minimo(A, custos_subconj, ponto):
    valores_ponto = []
    for subconj, custo in enumerate(custos_subconj):
        if A[ponto, subconj] == 1:
            valores_ponto += [(custo, subconj)]

    valor_minimo, subconj_minimo = min(valores_ponto, key=lambda v: v[0])

    for subconj in range(len(custos_subconj)):
        if A[ponto, subconj] == 1:
            custos_subconj[subconj] -= valor_minimo

    return valor_minimo, subconj_minimo

def cobertura_por_conjuntos(num_elem, num_subconj, custos_subconj, A):
    y, x = np.zeros(num_subconj), np.zeros(num_elem)
    while True:
        ponto = ponto_descoberto(y, A, num_elem)
        if ponto is None: break
        valor, subconj = valor_minimo(A, custos_subconj, ponto)
        y[subconj] = 1
        x[ponto] = valor

    return y, x
