# Crear una matriz bidimensional (3x3) con valores numéricos
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]


# Valor específico a buscar
target_value = 50

# Función para buscar el valor en la matriz
def buscar_valor(matriz, valor):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == valor:
                return fila, columna
    return None

# Realizar la búsqueda
posicion = buscar_valor(matrix, target_value)

# Mostrar el resultado
if posicion:
    print(f"El valor {target_value} se encontró en la posición (fila, columna): {posicion}")
else:
    print(f"El valor {target_value} no se encontró en la matriz.")


