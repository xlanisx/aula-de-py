def main():
    # Solicitar informações do usuário
    nome = input("Por favor, insira o nome do cachorro: ")
    idade_humana = int(input("Por favor, insira a idade humana do cachorro: "))
    tipo_cachorro = input("Por favor, insira o tipo de cachorro (grande, medio, pequeno): ").lower()
    banhos = int(input("Por favor, insira o número de banhos tomados nos últimos 12 meses: "))

    # Calcular a idade do cachorro em anos de cachorro
    idade_cachorro = idade_humana * 7

    # Dicionários para valores e custos por banho
    valores_por_banho = {"grande": 75.00, "medio": 60.00, "pequeno": 50.00}
    custo_por_banho = {"grande": 20.00, "medio": 15.00, "pequeno": 5.00}

    # Calcular o lucro total em 12 meses
    lucro_total = (valores_por_banho[tipo_cachorro] - custo_por_banho[tipo_cachorro]) * banhos

    # Exibir as informações ao usuário
    print(f"Olá, {nome} tem {idade_cachorro} anos de cachorro e nos últimos 12 meses o lucro com este animal foi de R${lucro_total:.2f}")

# Executar a função principal
if __name__ == "__main__":
    main()
