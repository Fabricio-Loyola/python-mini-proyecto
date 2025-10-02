numeros_divisibles_4 = 0
impar_mayor = 0
primero = 0
estado = 0
secuencia123 = 0

print("---Ingrese numeros enteros. Ingrese 0 para terminar.---")
primer_num = int(input("Ingrese un numero:"))
n = int(input("Ingrese un numero:"))
while n != 0:

    # Contador de números divisibles por 4
    if n % 4 == 0:
        numeros_divisibles_4 += 1
    
    # Encontrar el mayor número impar
    if n % 2 != 0 and n > impar_mayor:
        impar_mayor = n

    # Contar cuántas veces se ingresa el primer número
    if n == primer_num:
        primero += 1
    
    # Contar cuántas veces ocurre la secuencia 1,2,3
    if estado == 0 and n == 1:
        estado = n
    elif estado == 1 and n == 2:
        estado = n
    elif estado == 2 and n == 3:
        secuencia123 += 1
        estado = 0
    else:
        estado = 1 if n == 1 else 0
    
    n = int(input("Ingrese un numero:"))

print(f"Numeros divisibles por 4:{numeros_divisibles_4}")
print(f"Numero impar mayor de la secuencia:{impar_mayor}")
print(f"Primer numero ingresado: {primer_num} | Cantidad de veces: {primero}")
print(f"La secuencia 1,2,3 ocurrió: {secuencia123} veces")

