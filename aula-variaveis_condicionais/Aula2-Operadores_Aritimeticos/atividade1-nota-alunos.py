def obter_nota(mensagem):
    return float(input(mensagem))

def calcular_media(notas):
    return sum(notas) / len(notas)

def main():
    # Solicitar o nome do usuário
    nome = input("Por favor, insira seu nome: ")

    # Coletar 4 notas do usuário
    notas = [
        obter_nota("Por favor, insira a nota 1: "),
        obter_nota("Por favor, insira a nota 2: "),
        obter_nota("Por favor, insira a nota 3: "),
        obter_nota("Por favor, insira a nota 4: ")
    ]

    # Calcular a média aritmética das notas
    media = calcular_media(notas)

    # Exibir a mensagem com a média
    print(f"Olá, {nome}! Sua média é: {media:.2f} pontos")

# Executar a função principal
if __name__ == "__main__":
    main()