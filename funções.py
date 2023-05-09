# Primeira função: Recebe linha, coluna, orientação e tamanho do navio a ser posicionado. Retorna posições ocupadas pelo navio no grid.
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

# Segunda função: Utiliza função anterior para armazenar posições dos navios em um dicionário 
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

# Terceira função: Recebe o tabuleiro atual, e a linha e a coluna do disparo do adverário, em seguida, indica com um X caso acerte um navio e com - se errar uma embarcação
def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
        return tabuleiro
    
    else:
        tabuleiro[linha][coluna] = '-'
        return tabuleiro

resultado = faz_jogada
print(resultado)


# Quarta função: Preenche os navios dentro do tabuleiro e retorna o tabuleiro com a posição dos navios.
def posiciona_frota(frota):
    grid = []
    lista = []
    
    for i in range(10):
        for j in range(10):
            lista.append(0)
        grid.append(lista)
        lista = []
    
    for navio in frota.values():
        for cord in navio:
            for k in range(len(cord)):
                x = cord[k][0]
                y = cord[k][1]
                grid[x][y] = 1
    
    return grid

# Quinta função: Recebe frota e tabuleiro atual. Retorna o número de navios que já foram totalmente afundados. 
def afundados(frota, tabuleiro):
    afund = 0
    for embarc, coord in frota.items():
        for c in coord:
            #Criação da variável que verifica se uma embarcação foi totalmente afundada
            af = True
            for coordenadas in c:
                if af == True:
                    ponto1 = coordenadas[0]
                    ponto2 = coordenadas[1]
                    if tabuleiro[ponto1][ponto2] != 'X':
                        af = False
            #Somente permite contagem se a variável for True
            if af == True:
                afund += 1
    return afund


# Sexta função: Usa a segunda função para definir se a nova posição é válida ou não
def posicao_valida(frota,lin,col,orient,tam):
    f = 0
    p = define_posicoes(lin,col,orient,tam)
    for i in p:
        if i[0] > 9 or i[1] > 9:
            f += 1
            break
        for j in frota.keys():
            for c in range(len(frota[j])):
                if i in frota[j][c]:
                    f += 1
                    break
                else:
                    continue
            c = 0
    if f > 0:
        return False
    else:
        return True
    
# Sétima função: Monta tabuleiros
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '__      __\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

