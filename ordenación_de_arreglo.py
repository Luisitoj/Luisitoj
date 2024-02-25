# Crear una matriz bidimensional (3x3) con valores numéricos
matrix = [
    [30, 20, 10],
    [60, 50, 40],
    [90, 80, 70]
]

# Función para ordenar una fila específica en orden ascendente
def ordenar_fila(matriz, fila):
    matriz[fila].sort()

# Ordenar la segunda fila (índice 1)
ordenar_fila(matrix,  1)

# Mostrar la matriz original y la matriz con la fila ordenada
print("Matriz original:")
for fila in matrix:
    print(fila)
