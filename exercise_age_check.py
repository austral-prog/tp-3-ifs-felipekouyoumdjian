def age_check():
    edad = int(input())
    limite = int(input())
    if edad >= limite:
        print("Eres mayor de edad")
    elif edad < limite:
        print("Eres menor de edad")
    else:
        print("Entrada invalida")
age_check()