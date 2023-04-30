from funções import posicao_valida, preenche_frota

embarc = ['submarino', 'contratorpedeiro', 'navio-tanque', 'porta-aviões']
tam = 4
frota = {}

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
        valido = posicao_valida(frota, lin, col, orien, tam)
        if valido == True:
            frota = preenche_frota(frota, embarc[tam-1], lin, col, orien, tam)
            i -= 1
        else:
            print('Esta posição não está válida!')
    tam -= 1
print(frota)