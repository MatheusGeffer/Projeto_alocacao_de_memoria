
"""
NOME DO PROGRAMA: Projeto_alocacao_de_memoria,

VERSÃO 2.0

SINTAXE: Educacional

DESCRIÇÃO: Esse projeto tem como objetivo simular como funciona a memoria dentro de um sistema operacional, utilizando o modelo de estratégia First Fit para
simular o funcionamento de alocação de memória.

O sistema "First Fit" funciona da seguinte forma:
1. Quando um novo processo precisa de memória, o sistema operacional procura na lista de blocos livres (espaços de memória disponíveis) na memória principal.

2. O algoritmo First Fit procura o primeiro bloco de memória livre que seja grande o suficiente para acomodar o processo.
Ou seja, ele aloca o primeiro espaço de memória livre que atende aos requisitos do processo em termos de tamanho.

3. Uma vez encontrado o bloco de memória adequado, o sistema operacional aloca o espaço de memória ao processo, dividindo-o em duas partes:
uma parte menor que é usada pelo processo, e a outra parte, se restar espaço, continua livre para uso futuro.

4. Se o bloco de memória encontrado for maior do que o necessário, a parte não utilizada pode ser mantida como um bloco livre na lista de blocos livres
para ser alocada a processos subsequentes.

LINGUAGENS BACKEND: Python

REQUISITOS: Um editor de código fonte de sua preferência, neste caso foi utilizado o Google Colab.

AUTOR: Matheus Tomas Geffer

CRIAÇÃO: 12/05/2023

ALTERAÇÕES E ATUALIZAÇÕES: 12/05/2023 - Incio do projeto
                           15/05/2023 - Alterações e ajustes
                           18/05/2023 - Projeto ja deviadamente comentado e finalização
                           29/05/2023 - Apresentação do projeto ao professor orientador
                           15/10/2023 - Últimos ajuste, teste final e atualização final no GitHub.

"""

memoria = [' '] * 50 # Lista com espaço para 50 processos

def first_fit(memoria, tamanho_processo): # Função que verifica se a espaço para alocar o processo
    for i in range(len(memoria)):
        if memoria[i] == ' ':
            verificacao = i
            while verificacao < len(memoria) and memoria[verificacao] == ' ':
                if verificacao - i + 1 == tamanho_processo:
                    return i
                verificacao += 1
    return -1

def reorganizar_memoria(): # Função para reorganizar a processo
    global memoria
    memoria = [nome_processo for nome_processo in memoria if nome_processo != ' '] + [' ' for _ in range(memoria.count(' '))]

memoria_final = memoria.copy()  # Faz uma cópia da processo original

while True:
    print('')
    opcao = int(input('Dentre as opções a seguir: \n'
                      '1. Adicionar processo \n'
                      '2. Remover processo \n'
                      '3. Reordenar a lista de memória \n'
                      '4. Sair do programa \n'
                      'Selecione uma opção: '))
    if opcao == 1: # Opção que adiciona processo
        tamanho_processo = int(input('Tamanho do processo indicado:'))
        nome_processo = input('Letra do processo informado:')
        index = first_fit(memoria, tamanho_processo)
        if index == -1: # Sinaliza um overflow
            print("Não há espaço suficiente para alocar a informação. \n"
                  "Aloque uma quantidade menor ou apague um processo existente.")
        else:
            for i in range(index, index + tamanho_processo): # Aloca o processo no primerio espaço disponivel
                memoria[i] = nome_processo
        print("Estado atual da memória:")
        print(memoria)

    elif opcao == 2: # Opção que remove o processo
        remover_processo = input('Informe o processo que deseja remover da memória: ')
        if remover_processo not in memoria: # Verifica se a processo realmente existe na lista
            print('ERRO! Esse processo não existe no bloco.')
        else: # Remove o processo
            memoria = [nome_processo if nome_processo != remover_processo else ' ' for nome_processo in memoria] # list comprehension
        print("Estado atual da memória:")
        print(memoria)

    elif opcao == 3: # Opção para reorganizar a lista de processos
        reorganizar_memoria()
        print("Estado atual da memória:")
        print(memoria)

    elif opcao == 4: # Opção para encerrar o programa
        with open("resultado_alocacao.txt", "w") as arquivo: # Cria um arquivo .txt com os processos de alocação realizados pelo usuário
          resultado = "',' " .join(memoria)
          arquivo.write(resultado)
        break

print("Estado final da memória:")
print(memoria)  # Imprime a memória final, afetada pelas operações
