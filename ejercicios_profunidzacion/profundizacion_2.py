# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

print('este programa realiza una operación matemática entre dos números')
print('ahora debes elegir que operación matemática les realizaremos')
print('debes indicarlo mediante su simbología')
print('sumar (+), restar (-), multiplicar (*), dividir (/) o una potencia (**)')
print('si eliges no realizar nada debes escribir FIN')
while 0 == 0:
    operacion = str(input('que operación decides realizar: '))
    if operacion == 'FIN':
        print('fin de las operaciones matemáticas')
        break
    if operacion =='+' or operacion =='-' or operacion =='*' or operacion =='/' or operacion =='**':
        numero_1 = float(input('ingrese el primer número: '))
        numero_2 = float(input('ingrese el segundo número: '))
        if operacion =='+':
            resultado = numero_1 + numero_2
            opera = 'SUMA'
        if operacion =='-':
            resultado = numero_1 - numero_2
            opera = 'RESTA'
        if operacion =='*':
            resultado = numero_1 * numero_2
            opera = 'MULTIPLICACIÓN'
        if operacion =='/':
            resultado = numero_1 / numero_2
            opera = 'DIVISIÓN'
        if operacion =='**':
            resultado = numero_1 ** numero_2
            opera = 'POTENCIA'
        print('la', opera,'entre', numero_1, 'y', numero_2, 'da como resultado:', resultado)
    else:
        print('no ingresaste ninguna de las operaciones soportadas')
# fin