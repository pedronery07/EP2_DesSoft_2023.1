from funções import posicao_valida, preenche_frota, posiciona_frota, afundados, faz_jogada, monta_tabuleiros
from random import randint

resultado = faz_jogada
print(resultado)

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)

embarc = ['submarino', 'contratorpedeiro', 'navio-tanque', 'porta-aviões']
tam = 4
frota_jogador = {}

while tam >= 1:
    if embarc[tam-1] == 'porta-aviões':
        i = 1
    elif embarc[tam-1] == 'navio-tanque':
        i = 2
    elif embarc[tam-1] == 'contratorpedeiro':
        i = 3
    else:
        i = 4
    while i > 0:
        print(f'Insira as informações referentes ao navio {embarc[tam-1]} que possui tamanho {tam}')
        lin = int(input('Linha: '))
        col = int(input('Coluna: '))
        if embarc[tam-1] != "submarino":
            orien = int(input('Orientação ([1] Vertical [2] Horizontal): '))
            if orien == 1:
                orien = 'vertical'
            elif orien == 2:
                orien  = 'horizontal'
        valido = posicao_valida(frota_jogador, lin, col, orien, tam)
        if valido == True:
            frota_jogador = preenche_frota(frota_jogador, embarc[tam-1], lin, col, orien, tam)
            i -= 1
        else:
            print('Esta posição não está válida!')
    tam -= 1
tabuleiro_jogador = posiciona_frota(frota_jogador)

montagem_de_tabuleiros = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
print(montagem_de_tabuleiros)

jogando = True
posicoes_passadas = []
ataques_oponente = []
while jogando:
    validos = [0,1,2,3,4,5,6,7,8,9]
    posicao = []

    #ATAQUE DO JOGADOR
    linha_ataque = int(input('Linha que deseja atacar: '))
    while linha_ataque not in validos:
        print('Linha inválida')
        linha_ataque = int(input('Linha que deseja atacar: '))
    posicao.append(linha_ataque)
    coluna_ataque = int(input("Coluna que deseja atacar: "))
    while coluna_ataque not in validos:
        print('Coluna inválida')
        coluna_ataque = int(input('Coluna que deseja atacar: '))
    posicao.append(coluna_ataque)
    if posicao in posicoes_passadas:
        print(f"A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente!")
    else:
        posicoes_passadas.append(posicao)
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente,linha_ataque,coluna_ataque)
        
        #VERIFICA VITÓRIA DO JOGADOR
        a = afundados(frota_oponente, tabuleiro_oponente)
        if a == 10:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando = False
        else:
            #ATAQUE DO OPONENTE
            linha_oponente = randint(0,9)
            coluna_oponente = randint(0,9)
            ataque = [linha_oponente, coluna_oponente]
            while ataque in ataques_oponente:
                linha_oponente = randint(0,9)
                coluna_oponente = randint(0,9)
                ataque = [linha_oponente, coluna_oponente]
            print(f'Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}')
            ataques_oponente.append(ataque)
            tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)

            #VERIFICA VITÓRIA DO OPONENTE
            a2 = afundados(frota_jogador, tabuleiro_jogador)
            if a2 == 10:
                print('Xi! O oponente derrubou toda a sua frota =(')
                jogando = False
        
            #ATUALIZA TABULEIRO APÓS RODADA DE ATAQUES
            montagem_de_tabuleiros = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
            print(montagem_de_tabuleiros)