
# Diccionario

informacion_personal = {
    'nombre':'Jose luis',
    'edad':20,
    'ciudad':'Tena',
    'provincia':'Napo',
}
print('----------------------')
print('Diccionario Original')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')

# Clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal['ciudad'] = 'Quito'
informacion_personal['provincia'] = 'Pichincha'

# Nueva clave-valor al diccionario "profesion"
informacion_personal['profesion'] = 'Estudiante'

# Verifica si la clave "telefono" existe
if 'telefono' not in informacion_personal:
    informacion_personal['telefono'] = '0953688024'

# Elimina la clave "edad" del diccionario
# del informacion_personal['edad']
informacion_personal.pop('edad')

print('----------------------')
print('Diccionario Modificado')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')

