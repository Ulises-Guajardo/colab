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

if __name__ == "__main__":
    num = int(input("Ingrese un número entero: "))
    if es_primo(num):
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")
    
    siguiente_primo = siguiente_primo(num)
    print(f"El primer número primo mayor que {num} es: {siguiente_primo}")


if __name__ == "__main__":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    mediana_resultado = mediana(num1, num2, num3)
    print(f"La mediana de los tres números es: {mediana_resultado}")


if __name__ == "__main__":
    contraseña_generada = generar_contraseña()
    print(f"La contraseña generada es: {contraseña_generada}")

if __name__ == "__main__":
    lado1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
    lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
    
    hipotenusa = calcular_hipotenusa(lado1, lado2)
    print(f"La longitud de la hipotenusa es: {hipotenusa}")