lista = [4,49,67,8,9,5,3,2,64,86]
lista_par = []
lista_impar = []

for i in lista:
    if (i % 2 == 0):
        lista_par.append(i)
    else:
        lista_impar.append(i)

print("pares:", lista_par)
print("impares:", lista_impar)