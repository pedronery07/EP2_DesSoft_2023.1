from funções import posicao_valida, preenche_frota, posiciona_frota, afundados, faz_jogada, monta_tabuleiros

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

#AINDA É NECESSÁRIO IMPRIMIR OS TABULEIROS DO JOGADOR E DO OPONENTE
# FEITO
jogando = True
posicoes_passadas = []
while jogando:
    validos = [0,1,2,3,4,5,6,7,8,9]
    posicao = []
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
        montagem_de_tabuleiros = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
        print(montagem_de_tabuleiros)
        #AQUI DEVE AINDA OCORRER A VERIFICAÇÃO SE TODAS AS EMBARCAÇÕES DO OPONENTE FORAM AFUNDADAS PARA QUEBRAR OU NÃO O LOOP PRINCIPAL DO JOGO (jogando = False)
        a = afundados(frota_oponente, tabuleiro_oponente)
        if a == 10:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando = False
        else:
            continue