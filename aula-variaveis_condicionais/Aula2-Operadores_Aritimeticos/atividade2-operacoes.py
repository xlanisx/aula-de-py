import math

def main():
    # Solicitar o valor do usuário
    valor = float(input("Por favor, insira um valor: "))

    # Calcular os resultados desejados
    dobro = valor * 2
    triplo = valor * 3
    quadrado = valor ** 2
    raiz_quadrada = math.sqrt(valor)
    raiz_cubica = valor ** (1/3)

    # Exibir os resultados
    print(f"Primeiro output: O dobro de {valor} é {dobro}")
    print(f"Segundo output: O triplo de {valor} é {triplo}")
    print(f"Terceiro output: {valor} ao quadrado é {quadrado}")
    print(f"Quarto output: A raiz quadrada de {valor} é {raiz_quadrada:.2f}")
    print(f"Quinto output: A raiz cúbica de {valor} é {raiz_cubica:.2f}")

# Executar a função principal
if __name__ == "__main__":
    main()