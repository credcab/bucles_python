# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))

cantidad_numeros_positivos = 0  # Inicializo el contador en 0

# for ... in range(....)
total_numeros = 0
for numero in range(inicio, fin):
    print('número: ', numero)
    if numero >= 0:
        cantidad_numeros_positivos += 1
    total_numeros += 1
if fin >= 0:
    cantidad_numeros_positivos += 1
total_numeros += 1
negativos = total_numeros - cantidad_numeros_positivos

# Imprimir el valor de la cantidad de números positivos y negativos
print('número: ', fin)
print('la cantidad total de números NEGATIVOS es ', negativos)
print('la cantidad total de números POSITIVOS es ', cantidad_numeros_positivos)

print("terminamos!")
