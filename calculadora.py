def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b !=0:
        return a / b
    else:
        return "Não é possivel dividir por zero."

print("=== Calculadora Avançada ===")                       
print("Digite 'q' a qualquer momento para sair.")

while True: 
     op = input("\nOperação (+ - * /): ")
     if op == "q":
      print("Saindo da calculadora. Até logo!")
      break
     
     try:
        num1 = input("Primeiro número: ")
        if num1 == "q":
            break
        num1 = float(num1)
        
        num2 = input("Segundo número: ")
        if num2 == "q":
            break
        num2 = float(num2)

        if op == "+":
            resultado = somar(num1, num2)
        elif op == "-":
            resultado = subtrair(num1, num2) 
        elif op == "*":
            resultado = multiplicar(num1, num2)
        elif op == "/":
            resultado = dividir(num1, num2)
        else:
            resultado = "Operação inválida."
        print(f"resultado: {resultado}")
        
     except ValueError:
        print("Erro: Insira apenas números válidos.")                   