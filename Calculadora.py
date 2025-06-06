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

def porcentagem(num, perc):
    return (perc / 100) * num

def raiz_quadrada(num):
    if num < 0:
        raise ValueError("Raiz quadrada de número negativo não é permitida.")
    return math.sqrt(num)  

def media(*args):
    if len(args) == 0:
        raise ValueError("Pelo menos um número deve ser fornecido para calcular a média.")
    return sum(args) / len(args)

def exponenciacao(base, expoente):
    return base ** expoente

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
if escolha ==  "5":
    print("Você escolheu Porcentagem")
    num1 = float(input("Digite o número: "))
    perc = float(input("Digite a porcentagem: "))
    print("Resultado:", porcentagem(num1, perc))
if escolha == "6":
    print("Você escolheu Raiz Quadrada")
    num = float(input("Digite o número: "))
    if num < 0:
        print("Erro: Raiz quadrada de número negativo não é permitida.")
    else:
        print("Resultado:", math.sqrt(num))
if escolha == "7":
    print("Você escolheu Média")
    numeros = input("Digite os números separados por espaço: ")
    numeros = [float(num) for num in numeros.split()]
    try:
        print("Resultado:", media(*numeros))
    except ValueError as e:
        print("Erro:", e)
if escolha == "8":
    print("Você escolheu Exponenciação")
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    print("Resultado:", exponenciacao(base, expoente))
if escolha == "9":
    print("Saindo...")
