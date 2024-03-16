import numpy as np

# Inicialize uma matriz 2x2 com valores binários aleatórios
matriz = np.random.randint(2, size=(2, 2))

for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        elemento = matriz[i, j]
        print(f'O elemento {elemento} está na posição ({i}, {j})')
