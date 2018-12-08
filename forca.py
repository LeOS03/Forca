# -*- coding: UTF-8 -*-
# Jogo da forcaem Python (Primeiro programa)
# O jogador tem 10 tentativas para acertar a palavra
# Número de jogadores: 1 ou mais
# Caso o número de jogadores seja 1:
# O programa gera uma palavra aleatória dentro de uma lista com 26 palavras (passível de aumentar em futuras versões)
# Caso seja 2 ou mais:
# Os jogadores têm tanto a opção de preencher manualmente a palavra e a dica,
# Ou jogar com uma palavra aleatória

import os
import random
from palavras import palavraAleatoria, dicaAleatoria

listaVogais = ['a', 'e', 'i', 'o', 'u']


def jogar(palavraEscolhida, dica):
    # Caso ambos os objetos entrem nulos/vazios
    # Gera um número aleatório entre 0 e 25

    if palavraEscolhida == "":
        index = int(random.randint(0, 25))
        palavraEscolhida = palavraAleatoria(index)
        dica = dicaAleatoria(index)

    listaLetras = []
    letrasJogadas = []
    palavraDesvendada = []
    tentativas = 0
    acertou = False
    op = 0
    resposta = ""

    # Preenche uma lista com '_' com o tamanho da palavra
    # Essa lista será preenchida com as letras descobertas à medida que o jogador for acertando
    for x in range(0, len(palavraEscolhida)):
        # Caso seja uma palavra composta, a lista deve ser separada por espaço também
        if palavraEscolhida[x] == ' ' and x != len(palavraEscolhida):
            palavraDesvendada.append(' ')

        palavraDesvendada.append('_')

    # Separa a palavra em letras e guarda em outra lista, para facilitar buscas e comparações
    for i in range(0, len(palavraEscolhida)):
        listaLetras.append(palavraEscolhida[i].lower())

    print('\nVocê tem 10 tentativas para acertar a palavra.\nDica: {}'.format(dica))
    letra = str(input('Informe uma letra: '))

    while acertou == False or tentativas != 10:
        letrasJogadas.append(letra)
        for j in range(0, len(listaLetras)):
            # Caso nao seja uma letra acentuada
            if letra == listaLetras[j]:
                acertou = True
                palavraDesvendada[j] = letra.upper()

            # Caso seja uma letra acentuada
            for v in range(0, 5):
                if letra == listaVogais[v]:
                    if 'ã' in palavraEscolhida.lower():
                        acertou = True
                        palavraDesvendada[palavraEscolhida.lower().index('ã')] = 'Ã'
                    elif 'â' in palavraEscolhida.lower():
                        acertou = True
                        palavraDesvendada[palavraEscolhida.lower().index('â')] = 'Â'
                    elif 'ê' in palavraEscolhida.lower():
                        acertou = True
                        palavraDesvendada[palavraEscolhida.lower().index('ê')] = 'Ê'
                    elif 'ô' in palavraEscolhida.lower():
                        acertou = True
                        palavraDesvendada[palavraEscolhida.lower().index('ô')] = 'Ô'
                    elif 'õ' in palavraEscolhida.lower():
                        acertou = True
                        palavraDesvendada[palavraEscolhida.lower().index('õ')] = 'Õ'
                    elif 'á' in palavraEscolhida.lower():
                        acertou = True
                        palavraDesvendada[palavraEscolhida.lower().index('á')] = 'Á'
                    elif 'é' in palavraEscolhida.lower():
                        acertou = True
                        palavraDesvendada[palavraEscolhida.lower().index('é')] = 'É'
                    elif 'í' in palavraEscolhida.lower():
                        acertou = True
                        palavraDesvendada[palavraEscolhida.lower().index('í')] = 'Í'
                    elif 'ó' in palavraEscolhida.lower():
                        acertou = True
                        palavraDesvendada[palavraEscolhida.lower().index('ó')] = 'Ó'
                    elif 'ú' in palavraEscolhida.lower():
                        acertou = True
                        palavraDesvendada[palavraEscolhida.lower().index('ú')] = 'Ú'

        print('\nDica: {}'.format(dica))
        print('Palavra: {}'.format(palavraDesvendada))
        print('Letras jogadas: {}'.format(letrasJogadas))

        if acertou == True:
            print('Tentativas: {}\n'.format(tentativas))

        tentativas = tentativas + 1
        print('Tentativas: {}\n'.format(tentativas))

        print('1 - Responder\n2 - Tentar mais uma letra')
        op = int(input('Opção: '))

        if op == 1:
            resposta = str(input('Sua resposta: '))
            if resposta.title() == palavraEscolhida.title():
                acertou = True
                os.system('clear')
                print('\n**********   Parabéns! Você acertou!   **********\nPalavra: {}'.format(palavraEscolhida))
                break

            else:
                os.system('clear')
                print('\nxxxxxxxxxx   Nah você errou :(   xxxxxxxxxx\nPalavra correta: {}'.format(palavraEscolhida))
                break

        else:
            acertou = False
            letra = str(input('\nInforme uma letra: '))


print("******  Seja bem-vindx ao jogo da forca  ******")
print("\nO que gostaria de fazer?")

op = -1
palavraEscolhida = ""
dica = ""

while op != 0:
    print("\n1 - Inserir palavra"
          "\n2 - Inserir dica"
          "\n3 - Jogar"
          "\n0 - Sair")

    op = int(input('Opção: '))

    if op == 1:
        palavraEscolhida = str(input('Informe a palavra desejada: '))
        os.system('clear')

    elif op == 2:
        dica = str(input('Informe a dica da palavra inserida: '))
        os.system('clear')

    elif op == 3:
        jogar(palavraEscolhida.strip(), dica)

    else:
        print('Obrigado por jogar! Volte sempre <3')
