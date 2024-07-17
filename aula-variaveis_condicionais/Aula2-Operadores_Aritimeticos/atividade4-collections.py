# Crie uma tupla com 5 dados
tupla = (1, 2, 3, 4, 5)

# Altere a tupla para uma lista
lista = list(tupla)

# Insira 2 dados extras a essa lista
lista.append(6)
lista.append(7)

# Remova o primeiro dado da lista
del lista[0]

# Remova o último dado da lista
del lista[-1]

# Faça um print com o primeiro dado da lista
print("Primeiro dado da lista:", lista[0])

# Faça um print com a quantidade de dados da lista
print("Quantidade de dados na lista:", len(lista))

# Crie um dicionário com os seguintes dados: Nome, Idade, Profissão
dicionario = {
    "Nome": "Alanis",
    "Idade": 25,
    "Profissão": "QA"
}

# Imprima somente o valor contido na chave Nome do dicionário
print("Nome no dicionário:", dicionario["Nome"])
