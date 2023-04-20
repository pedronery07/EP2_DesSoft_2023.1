#Primeira função: Recebe linha, coluna, orientação e tamanho do navio a ser posicionado. Devolve posições ocupadas pelo navio no grid.

def define_posicoes(lin, col, orient, tam):
    saida = [[lin, col]]
    while len(saida) != tam:
        if orient == 'vertical':
            lin += 1
            saida.append([lin, col])
        else:
            col += 1
            saida.append([lin, col])
    return saida

#Segunda função: Utiliza função anterior para armazenar posições dos navios em um dicionário 

def preenche_frota(frota, nome, lin, col, orient, tam):
    posicao = define_posicoes(lin, col, orient, tam)
    if frota != {}:
        if nome not in frota.keys():
            frota[nome] = [posicao]
        else:
            frota[nome].append(posicao)
    else:
        frota[nome] = [posicao]
    return frota