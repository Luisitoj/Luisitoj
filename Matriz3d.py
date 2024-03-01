import numpy as np

# Definir ciudades, días de la semana y semanas
ciudades = ['CiudadA', 'CiudadB', 'CiudadC']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = ['Semana1', 'Semana2', 'Semana3']

# Crear una matriz 3D de temperaturas aleatorias
temperaturas = np.random.randint(20, 35, size=(len(ciudades), len(dias_semana), len(semanas)))

# Calcular el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(ciudades):
    for j, semana in enumerate(semanas):
        promedio_temp = np.mean(temperaturas[i, :, j])
        print(f'Promedio de temperaturas en {ciudad} para {semana}: {promedio_temp:.2f}°C')
