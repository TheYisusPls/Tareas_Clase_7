print("Ingrese el numero que desee: ")
numero = int(input())

if numero > 0:

    for i in range(1,numero+1):
        print("")

        for j in range(1,i+1):
            print(j,end=" ")

    for i in range(numero-1,0,-1):
        print("")

        for j in range(1,i+1):
            print(j, end=" ")


else:
    print("El numero ingresado no es correcto, intentelo denuevo")