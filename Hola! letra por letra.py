palabra = input("Dime una palabra: ")

espacio = ''

contador = len(palabra)

for i in range (contador):
    espacio += palabra[i]
    print(espacio)
