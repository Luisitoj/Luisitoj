# Importar la librería numpy para trabajar con matrices
import numpy
import  numpy as np

# Definir las ciudades, los días de la semana y las semanas
ciudades = ["Quito", "Guayaquil", "Cuenca", "Tena", "Loja"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]

# Crear una matriz 3D vacía con las dimensiones adecuadas
# La forma de la matriz es (número de ciudades, número de días, número de semanas)
matriz = np.zeros((len(ciudades), len(dias), len(semanas)))

# Llenar la matriz con datos de temperaturas aleatorios entre 10 y 40 grados
# Usar un bucle anidado para recorrer cada elemento de la matriz
for i in range(len(ciudades)):
  for j in range(len(dias)):
    for k in range(len(semanas)):
      # Generar un número aleatorio entre 10 y 40
      temperatura = np.random.randint(10, 40)
      # Asignar el valor de la temperatura al elemento correspondiente de la matriz
      matriz[i, j, k] = temperatura

# Mostrar la matriz 3D
print(matriz)
