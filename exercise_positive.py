def positive():
    numero = int(input())
    if numero > 0:
        print("El numero es positivo")
    elif numero < 0:
        print("El numero es negativo")
    elif numero == 0:
        print("El numero es cero")
        
positive()