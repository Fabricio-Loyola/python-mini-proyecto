n1 = int(input('Numero 1:'))
n2 = int(input('Numero 2:'))
n3 = int(input('Numero 3:'))

#mayor
if n1 > n2 and n1 > n3:
    mayor = n1
    if n2 > n3:
        medio = n2
        menor = n3
    else:
        medio = n3
        menor = n2
elif n2 > n1 and n2 > n3:
    mayor = n2
    if n1 > n3:
        medio = n1
        menor = n3
    else:
        medio = n3
        menor = n1
elif n3 > n1 and n3 > n2:
    mayor = n3
    if n1 > n2:
        medio = n1
        menor = n2
    else:
        medio = n2
        menor = n1

resto = n1 % n2
if resto == n3:
    print('El tercero es el resto de la division de los dos primeros')
else:
    print('Su resto es otro')

