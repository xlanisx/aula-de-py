palavra = input("Digite uma palavra: ")

vogais = ['a', 'e', 'i', 'o', 'u']
contagem_vogal = 0
for letra in palavra:
    if letra in vogais:
        print(f'contém a letra {letra}')
        contagem_vogal += 1


print(f'O total de vogais é {contagem_vogal}')