def verificar_frequencia(frequencia):
    if frequencia == 21:
        return "UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ"
    else:
        return "VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO"

def frequencia_atualizada(frequencia, frequencia_consecutiva):
    if frequencia == 0:
        return 1, 1
    elif frequencia_consecutiva >= 21:
        return 1, 1
    else:
        return frequencia + 1, frequencia_consecutiva + 1

def main():
    # Frequência inicial dos alunos (pode ser carregada de um banco de dados em um sistema real)
    frequencia = 0
    frequencia_consecutiva = 0

    while True:
        # Simula a passagem do aluno pela catraca
        input("Pressione Enter para simular a passagem pela catraca...")

        # Atualiza a frequência
        frequencia, frequencia_consecutiva = frequencia_atualizada(frequencia, frequencia_consecutiva)

        # Verifica e exibe a mensagem apropriada
        mensagem = verificar_frequencia(frequencia_consecutiva)
        print(mensagem)

        # Caso o aluno falte, reseta a contagem consecutiva
        if mensagem == "UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ":
            frequencia_consecutiva = 0

        # Exemplo de simulação de ausência (em um sistema real, isso seria determinado por registros de presença)
        ausencia = input("O aluno faltou no próximo dia? (s/n): ").lower()
        if ausencia == 's':
            frequencia_consecutiva = 0
            print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")

if __name__ == "__main__":
    main()
