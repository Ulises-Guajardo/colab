import random
# Ejercicio 1: es número primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# Ejercicio 2: Siguiente número primo
def siguiente_primo(n):
    siguiente = n + 1
    while True:
        if es_primo(siguiente):
            return siguiente
        siguiente += 1

# Ejercicio 3: Mediana de tres valores
def mediana(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros[1]

# Ejercicio 4: generar contraseña random
def generar_contraseña():
    longitud = random.randint(7, 10)
    contraseña = ""
    for _ in range(longitud):
        caracter = chr(random.randint(33, 126))
        contraseña += caracter
    return contraseña

# Ejercicio 5: calcular hipotenusa
def calcular_hipotenusa(lado1, lado2):
    hipotenusa = (lado1**2 + lado2**2)**0.5
    return hipotenusa
