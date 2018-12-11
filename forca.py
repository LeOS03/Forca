# coding = UTF-8
# Jogo da forca em Python (Primeiro programa)
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

listaVogais = ['a', 'á', 'ã', 'â', 'e', 'é', 'ê', 'i', 'í', 'o', 'ó', 'ô', 'u', 'ú']


def jogar(palavraEscolhida, dica):
    # Caso ambos os objetos entrem nulos/vazios
    # Gera um número aleatório entre 0 e 25

    if palavraEscolhida == "":
        index = int(random.randint(0, 25))
        palavraEscolhida = palavraAleatoria(index)
        dica = dicaAleatoria(index)

    letrasJogadas = []
    listaLetras = []
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

    for i in range(0, len(palavraEscolhida)):
        listaLetras.append(palavraEscolhida[i].lower())

    print('\nVocê tem 10 tentativas para acertar a palavra.\nDica: {}'.format(dica))
    letra = input('Informe uma letra: ')

    while not acertou or tentativas != 10:
        letrasJogadas.append(letra.upper())
        visitou = 0

        # Caso nao seja uma letra acentuada
        for j in range(0, len(listaLetras)):
            # Caso nao seja uma letra acentuada
            if letra == listaLetras[j]:
                acertou = True
                palavraDesvendada[j] = letra.upper()

            # Caso seja uma letra acentuada
            for v in range(0, len(listaVogais)):
                if listaVogais[v] in palavraEscolhida.lower() and letra in listaVogais and \
                                                        palavraDesvendada[j] != letra and letra not in letrasJogadas:
                    acertou = True
                    palavraDesvendada[palavraEscolhida.lower().index(listaVogais[v])] = listaVogais[v].upper()

        print('\nDica: {}'.format(dica))
        print('Palavra: {}'.format(palavraDesvendada))
        print('Letras jogadas: {}'.format(letrasJogadas))

        if acertou:
            print('Tentativas: {}\n'.format(tentativas))
        else:
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
            letra = input('\nInforme uma letra: ')


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