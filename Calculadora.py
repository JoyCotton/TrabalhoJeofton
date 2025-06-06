import math


def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return num1 / num2



print("Calculadora")
print("Escolha uma operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Porcentagem")
print("6. Raiz Quadrada")
print("7. Média")
print("8. Exponenciação")
print("9. Sair")
escolha = input("Digite o número da operação desejada: ")

    
if escolha == "1":
    print("Você escolheu Soma")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("Resultado:", soma(num1, num2))
if escolha == "2":
    print("Você escolheu Subtração")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("Resultado:", subtracao(num1, num2))
if escolha == "3":
    print("Você escolheu Multiplicação")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("Resultado:", multiplicacao(num1, num2))
if escolha == "4":
    print("Você escolheu Divisão")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    try:
        print("Resultado:", divisao(num1, num2))
    except ValueError as e:
        print("Erro:", e)

if escolha == "9":
    print("Saindo...")