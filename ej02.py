cl = 0
tiene_x = False
tiene_y = False
tiene_mo = False
palabras = 0
palabras_mas_de_4_letras = 0
tiene_x_or_y = 0
letras_totales = 0
tiene_mo = False
anterior = False
palabras_con_mo = 0

cadena = input("Ingrese palabra/frase:")

for car in cadena:

    if car == " " or car == ".":
        palabras += 1
        letras_totales += cl
        if cl > 4:
            palabras_mas_de_4_letras += 1
        
        if tiene_x == True or tiene_y == True:
            tiene_x_or_y += 1
        
        if tiene_mo:
            palabras_con_mo += 1
        
        cl = 0
        tiene_x = False
        tiene_y = False
        tiene_mo = False
        anterior = False
    
    else:
        cl += 1

        if car in "yY":
            tiene_y = True
        if car in "xX":
            tiene_x = True
        
        if car in "mM":
            anterior = True
        if anterior and car in "oO":
            tiene_mo = True
        

promedio = letras_totales // palabras


print("Palabras con mas de 4 letras:",palabras_mas_de_4_letras)
print("Palabras con al menos una vez la 'X' o 'Y':",tiene_x_or_y)
print("Promedio de letras por palabra del texto:",promedio)
print("Palabras con la expresión 'mo':",palabras_con_mo)

