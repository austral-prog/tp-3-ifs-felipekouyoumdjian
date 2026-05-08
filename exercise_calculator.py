def calculator():
    num1 = float(input())
    num2 = float(input())
    operacion = input()
    
    if operacion == "+":
        resultado = num1 + num2
        print(f"Resultado: {resultado}")
    elif operacion == "-":
        resultado = num1 - num2
        print(f"Resultado: {resultado}")
    elif operacion == "*":
        resultado = num1 * num2
        print(f"Resultado: {resultado}")
    elif operacion == "/":
        if num2 == "0":
            print("Error: division por cero")
        else:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
    else:
        print("Operacion invalida")
