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