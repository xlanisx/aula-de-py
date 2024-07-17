# Solicita ao cliente o valor da compra
valor_compra = float(input("Informe o valor da sua compra para verificar elegibilidade para desconto: "))

# Determina a mensagem baseada no valor da compra
mensagem = (
    "PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%"
    if valor_compra > 500 else
    "PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00"
    if valor_compra >= 250 else
    "POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA."
)

# Exibe a mensagem ao cliente
print(mensagem)