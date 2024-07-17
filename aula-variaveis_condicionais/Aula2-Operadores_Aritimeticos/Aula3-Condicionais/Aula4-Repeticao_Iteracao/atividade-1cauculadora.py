def soma():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Soma: ", x + y)

def subtracao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Subtração: ", x - y)

def multiplicacao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Multiplicação: ", x * y)

def divisao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Divisão: ", x / y)

opcao = 1

while opcao:
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão")

    opcao = int(input("Opção: "))

    match opcao:
        case 0:
            print("Saindo...")
        case 1:
            soma()
        case 2:
            subtracao()
        case 3:
            multiplicacao()
        case 4:
            divisao()
        case _:
            print("Opção inválida, tente novamente.")