import random
import copy

passos = {
  "P": [(-1,0),(-1,-1),(-1,1)],
  "B": [(1,1),(-1,-1),(-1,1),(1,-1)],
  "T": [(-1,0),(1,0),(0,1),(0,-1)],
  "C": [(2,1),(2,-1),(-2,-1),(-2,1),(1,2),(1,-2),(-1,-2),(-1,2)],
  "R": [(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1),(0,-2),(0,2)],
  "D": [(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
}

valor = {
  "P": 1,
  "B": 3,
  "C": 3,
  "T": 5,
  "D": 9,
  "R": 100
}


mapa = {
    "P":
    [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [5, 5, 5, 5, 5, 5, 5, 5],
    [1, 1, 2, 3, 3, 2, 1, 1],
    [0.5, 0.5, 1, 2.5, 2.5, 1, 0.5, 0.55],
    [0,  0,  0, 2, 2,  0,  0,  0],
    [0.5, -0.5,-1, 0, 0, -1, -0.5, 0.5],
    [0.5, 1, 1,-2,-2, 1, 1, 0.5],
    [0, 0, 0, 0, 0, 0, 0, 0]
    ],
    
    'C':
    [
    [-3,-2,-1,-1,-1,-1,-2,-3],
    [-2,-2,  0,  0.5,  0.5,  0,-2,-2],
    [-1,  0.5, 1, 1.5, 1.5, 0.1,  0.5,-1],
    [-1,  0, 1.5, 2, 2, 1.5,  0,-1],
    [-1,  0.5, 1.5, 2, 2, 1.5,  0.5,-1],
    [-1,  0, 1, 1.5, 1.5, 1,  0,-1],
    [-2,-2,  0,  0,  0,  0,-2,-2],
    [-3,-2,-1,-1,-1,-1,-2,-3]
    ],
    
    "B":
    [
    [-2,-1, -1,-1,-1, -1, -1, -2],
    [-1, 0,  0, 0, 0,  0,  0, -1],
    [-1, 0, 0.5,1, 1, 0.5, 0, -1],
    [-1,0.5,0.5,1, 1, 0.5,0.5,-1],
    [-1, 0,  1, 1 ,1,  1,  0, -1],
    [-1, 1,  1, 1, 1,  1,  1 ,-1],
    [-1,0.5, 0, 0, 0,  0, 0.5,-1],
    [-2,-1, -1,-1,-1, -1, -1, -2]
    ],
    
    "T":
    [
    [0,  0,  0,  0,  0,  0,  0,  0],
    [0.5,  1, 1, 1, 1, 1, 1, 0.5],
    [-0.5,  0,  0,  0,  0,  0,  0, -0.5],
    [-0.5,  0,  0,  0,  0,  0,  0, -0.5],
    [-0.5,  0,  0,  0,  0,  0,  0, -0.5],
    [-0.5,  0,  0,  0,  0,  0,  0, -0.5],
    [-0.5,  0,  0,  0,  0,  0,  0, -0.5],
    [0,  0,  0.5,  1, 1, 0.5,  0,  0]
    ],
    
   "D":
    [
    [-2,-1,-1, -0.5, -0.5,-1,-1,-2],
    [-1,  0,  0,  0,  0,  0,  0,-1],
    [-1,  0,  0.5,  0.5,  0.5,  0.5,  0,-1],
    [-0.5,  0,  0.5,  0.5,  0.5,  0.5,  0, -0.5],
    [0,  0,  0.5,  0.5,  0.5,  0.5,  0, -0.5],
    [-1,  0.5,  0.5,  0.5,  0.5,  0.5,  0,-1],
    [-1,  0,  0.5,  0,  0,  0,  0,-1],
    [-2,-1,-1, -0.5, -0.5,-1,-1,-2]
    ],
    
    "R":
    [
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-2, -3, -3, -4, -4, -3, -3, -2],
    [-1, -2, -2, -2, -2, -2, -2, -1],
    [2,  2,  0,   0,   0,   0,   2,  2],
    [2,  3,  1,  0,   0,   1,  3,  2]
    ]
}


fileirasPraLinhas = {
    "8": 0,
    "7": 1,
    "6": 2,
    "5": 3,
    "4": 4,
    "3": 5,
    "2": 6,
    "1": 7
}
linhasPraFileiras = {v: k for k, v in fileirasPraLinhas.items()}



fileirasPraColunas = {
    "h": 7,
    "g": 6,
    "f": 5,
    "e": 4,
    "d": 3,
    "c": 2,
    "b": 1,
    "a": 0
}
colunasPraFileiras = {v: k for k, v in fileirasPraColunas.items()}

class Jogador:
    def __init__(self,cor,engine):
        self.cor = cor
        self.engine = engine

class Estado:
    def __init__(self):
        self.tabuleiro = [
        [("T",1), ("C",1), ("B",1), ("D",1), ("R",1), ("B",1), ("C",1), ("T",1)],
        [("P",1), ("P",1), ("P",1), ("P",1), ("P",1), ("P",1), ("P",1), ("P",1)],
        [("S",10),("S",10),("S",10),("S",10),("S",10),("S",10),("S",10),("S",10)],
        [("S",10),("S",10),("S",10),("S",10),("S",10),("S",10),("S",10),("S",10)],
        [("S",10),("S",10),("S",10),("S",10),("S",10),("S",10),("S",10),("S",10)],
        [("S",10),("S",10),("S",10),("S",10),("S",10),("S",10),("S",10),("S",10)],
        [("P",0), ("P",0), ("P",0), ("P",0), ("P",0), ("P",0), ("P",0), ("P",0)],
        [("T",0), ("C",0), ("B",0), ("D",0), ("R",0), ("B",0), ("C",0), ("T",0)]
        ]

        # self.tabuleiro = [
        # [('T', 1), ('C', 1), ('B', 1), ('D', 1), ('S', 10), ('B', 1), ('C', 1), ('T', 1)],
        # [('P', 1), ('P', 1), ('P', 1), ('P', 1), ('P', 1), ('R',1), ('S', 10), ('S', 10)],
        # [('S', 10), ('S', 10), ('S', 10), ('S', 10), ('S', 10), ('S', 10), ('S', 10), ('S', 10)],
        # [('S', 10), ('S', 10), ('S', 10), ('P', 0), ('S', 10), ('S', 10), ('B', 0), ('P', 1)],
        # [('S', 10), ('S', 10), ('C', 0), ('P', 0), ('S', 10), ('S', 10), ('S', 10), ('S', 10)],
        # [('S', 10), ('S', 10), ('C', 0), ('S', 10), ('S', 10), ('S', 10), ('S', 10), ('S', 10)],
        # [('P', 0), ('P', 0), ('P', 0), ('S', 10), ('S', 10), ('P', 0), ('P', 0), ('P', 0)],
        # [('T', 0), ('S', 10), ('S', 10), ('D', 0), ('R', 0), ('B', 0), ('S', 10), ('T', 0)]
        # ]
        self.pecasBrancas = [self.tabuleiro[i][j] for i in range(len(self.tabuleiro)) for j in range(len(self.tabuleiro[i])) if self.tabuleiro[i][j][1] == 0]
        self.pecasPretas = [self.tabuleiro[i][j] for i in range(len(self.tabuleiro)) for j in range(len(self.tabuleiro[i])) if self.tabuleiro[i][j][1] == 1]
        self.fim_de_jogo = False
        self.turno = 0
        self.logComposto = list()
        self.log = list()
        self.enPassant = None
        self.cinquentaLances = 0

    def incrementarLance(self):
        self.cinquentaLances += 1



def traducaoUCI(casaOrigem,casaDestino,promocao):
    pt_to_en = {
        "B": 'b',
        "C": 'n',
        "T": 'r',
        "D": 'q',
    }
    
    jogadaTraduzida = colunasPraFileiras(casaOrigem[1]) + linhasPraFileiras(casaOrigem[0]) + colunasPraFileiras(casaDestino[1]) + linhasPraFileiras(casaDestino[0])
    
    if promocao != False:
        jogadaTraduzida += pt_to_en(promocao)
    
    return jogadaTraduzida

def enPassant(tabuleiro,casaOrigem,casaDestino):
    x = casaDestino[0] - casaOrigem[0]
    y = casaDestino[1] - casaOrigem[1] 
    
    peca,_ = tabuleiro[casaDestino[0]][casaDestino[1]]
    movimento = (x,y)
    if (peca == 'P') and (movimento == (-2,0) or movimento == (2,0)):
        return casaDestino
    else:
        return None

def notacaoXadrez(tabuleiro,casaOrigem,casaDestino,pecaCasaDestino):
    jogada = ''
    pecaMovida = tabuleiro[casaDestino[0]][casaDestino[1]]
    cor = pecaMovida[1]
    corOposta = (cor + 1)%2
    
    if pecaMovida[0] == 'R':
        if casaOrigem[1] - casaDestino[1] == -2:
            return 'O-O'
        elif casaOrigem[1] - casaDestino[1] == 2:
            return 'O-O-O'

    if pecaMovida[0] != 'P':
        jogada += pecaMovida[0]
    pecasProximas = pecasAtacando(tabuleiro,casaDestino,True)
    
    passagem = False
    if pecasProximas[0].count(pecaMovida) > 0:
        if (pecaMovida[0] == 'P') and (casaOrigem[1] - casaDestino[1] == 1 or casaOrigem[1] - casaDestino[1] == -1):
            jogada += colunasPraFileiras[casaOrigem[1]]
            passagem = True
        elif pecaMovida[0] != 'P':
            jogada += colunasPraFileiras[casaOrigem[1]]
            
    if pecaCasaDestino != "S" or passagem:
        jogada += 'x'
    jogada += colunasPraFileiras[casaDestino[1]]
    jogada += linhasPraFileiras[casaDestino[0]]
    
    rei = ('R',corOposta)
    cRei = coordenadaPeca(tabuleiro,rei)
    if len(cRei) == 0:
        print("="*50)
        print(pecaCasaDestino)
        print("="*50)
        print(pecaMovida[0])
        print("="*50)
        print(jogada)
        print("="*50)
        printarTabuleiro(tabuleiro)
        print("="*50)
    xeque = pecasAtacando(tabuleiro,cRei[0])
        
    if len(xeque[0])>0:
        jogada += '+'
    
        
    return jogada

def valorPecaPreta(peca):
    mapaPecasPretas = copy.deepcopy(mapa[peca])
    for i in range(4):
        val = i+1
        mapaPecasPretas[i], mapaPecasPretas[len(mapaPecasPretas)-val] = mapaPecasPretas[len(mapaPecasPretas)-val], mapaPecasPretas[i]
        
    return mapaPecasPretas

def avaliacao(jogo):
    tabuleiro = jogo.tabuleiro

    situacaoBrancas = acabarOJogo(jogo,0)
    situacaoPretas = acabarOJogo(jogo,1)
    if situacaoBrancas:
        return -100000
    elif situacaoPretas == None or situacaoBrancas == None:
        return 0
    elif situacaoPretas:
        return 100000
    
    total = 0
    
    for i in range (len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            peca,cor = tabuleiro[i][j]
            if cor == 0:
                casasPecaBranca = mapa[peca]
                valorCasaPecaBranca = casasPecaBranca[i][j]  
                total += valor[peca]
                total += valorCasaPecaBranca
            elif cor == 1:
                casasPecaPreta = valorPecaPreta(peca)
                valorCasaPecaPreta = casasPecaPreta[i][j]
                total -= valorCasaPecaPreta
                total -= valor[peca]
                
    return total

def minmaxReverso(jogo,cor,corJogador,profundidade):

    if jogo.fim_de_jogo == True or jogo.fim_de_jogo == None or profundidade == 0:
        return avaliacao(jogo),None
    
    if cor == 0:
        piorPontuacao = -1000000
        if corJogador == 0:
            piorPontuacao = 1000000
            
        coordenadas,casas = jogadasTotal(jogo,0)
        piorJogada = [coordenadas[0],casas[0]]
        for i in range(len(coordenadas)):
            jogoCopia = copy.deepcopy(jogo)
            
            jogada = moverPeca(jogoCopia.tabuleiro,coordenadas[i],casas[i][0],casas[i][1])
            jogoCopia.enPassant = enPassant(jogoCopia.tabuleiro,coordenadas[i],casas[i][0])
            jogoCopia.log.append(jogada)
            jogoCopia.fim_de_jogo = acabarOJogo(jogoCopia,1)
            val,jogada = minmax(jogoCopia,1,profundidade-1)
            
            if corJogador == 1:
                if val > piorPontuacao:
                    piorPontuacao = val
                    piorJogada = [coordenadas[i],casas[i]]
            else:
                if val < piorPontuacao:
                    piorPontuacao = val
                    piorJogada = [coordenadas[i],casas[i]]
    else:
        piorPontuacao = 1000000
        if corJogador == 1:
            piorPontuacao = -1000000
        
        coordenadas,casas = jogadasTotal(jogo,1)
        piorJogada = [coordenadas[0],casas[0]]
        for i in range(len(coordenadas)):
            jogoCopia = copy.deepcopy(jogo)
            
            jogada = moverPeca(jogoCopia.tabuleiro,coordenadas[i],casas[i][0],casas[i][1])
            jogoCopia.enPassant = enPassant(jogoCopia.tabuleiro,coordenadas[i],casas[i][0])
            jogoCopia.log.append(jogada)
            jogoCopia.fim_de_jogo = acabarOJogo(jogoCopia,0)
            
            val,jogada = minmax(jogoCopia,0,profundidade-1)
            
            if corJogador == 0:
                if val < piorPontuacao:
                    piorPontuacao = val
                    piorJogada = [coordenadas[i],casas[i]]
            else:
                if val > piorPontuacao:
                    piorPontuacao = val
                    piorJogada = [coordenadas[i],casas[i]]
        
    return piorPontuacao,piorJogada

def minmax(jogo,cor,profundidade):
    
    if jogo.fim_de_jogo == True or jogo.fim_de_jogo == None or profundidade == 0:
        jogo.fim_de_jogo = False
        return avaliacao(jogo),None
    
    if cor == 0:
        melhorPontuacao = -1000000
        coordenadas,casas = jogadasTotal(jogo,0)
        melhorJogada = [coordenadas[0],casas[0]]
        for i in range(len(coordenadas)):
            jogoCopia = copy.deepcopy(jogo)
            
            jogada = moverPeca(jogoCopia.tabuleiro,coordenadas[i],casas[i][0],casas[i][1])
            jogoCopia.enPassant = enPassant(jogoCopia.tabuleiro,coordenadas[i],casas[i][0])
            jogoCopia.log.append(jogada)
            jogoCopia.fim_de_jogo = acabarOJogo(jogoCopia,1)
            val,_ = minmax(jogoCopia,1,profundidade-1)
            
            if val > melhorPontuacao:
                melhorPontuacao = val
                melhorJogada = [coordenadas[i],casas[i]]
    else:
        melhorPontuacao = 1000000
        coordenadas,casas = jogadasTotal(jogo,1)
        melhorJogada = [coordenadas[0],casas[0]]
        
        for i in range(len(coordenadas)):
            jogoCopia = copy.deepcopy(jogo)
            
            jogada = moverPeca(jogoCopia.tabuleiro,coordenadas[i],casas[i][0],casas[i][1])
            jogoCopia.enPassant = enPassant(jogoCopia.tabuleiro,coordenadas[i],casas[i][0])
            jogoCopia.log.append(jogada)
            jogoCopia.fim_de_jogo = acabarOJogo(jogoCopia,0)
            val,_ = minmax(jogoCopia,0,profundidade-1)
            
            if val < melhorPontuacao:
                melhorPontuacao = val
                melhorJogada = [coordenadas[i],casas[i]]
    
    return melhorPontuacao,melhorJogada

def pecasAtacando(tabuleiro,casa,coresIguais = False):
    pecas = list()
    coordenadas = list()
    lado = list()
    peca = tabuleiro[casa[0]][casa[1]]
    
    analisarXeque = passos["R"][:-2] + passos["C"]
    for movimento in analisarXeque:
        if movimento in passos["C"]:
            proximaPeca = primeiraPecaEncontrada(tabuleiro,casa,movimento,True,True)
            coordProxPeca = primeiraPecaEncontrada(tabuleiro,casa,movimento,False,True)
        else:
            proximaPeca = primeiraPecaEncontrada(tabuleiro,casa,movimento,True,False)
            coordProxPeca = primeiraPecaEncontrada(tabuleiro,casa,movimento,False,False)
        if proximaPeca != "--":
            if (peca[1] != proximaPeca[1] and not coresIguais) or (peca[1] == proximaPeca[1] and coresIguais):
                x,y = coordProxPeca
                x -= movimento[0]
                y -= movimento[1]
                casaAnalise = (x,y)
                movimentoCorrigido = (movimento[0]*-1,movimento[1]*-1)
                if proximaPeca[0] == 'R':
                    if casa == casaAnalise:                                              
                        pecas.append(proximaPeca)
                        coordenadas.append(coordProxPeca)
                        lado.append(movimento)
                                
                elif movimento[0] == 0 or movimento[1] == 0:
                    if (proximaPeca[0] == "T" or proximaPeca[0] == "D"):
                        pecas.append(proximaPeca)
                        coordenadas.append(coordProxPeca)
                        lado.append(movimento)
                        
                elif movimento in passos["C"]:
                    if proximaPeca[0] == "C":
                        pecas.append(proximaPeca)
                        coordenadas.append(coordProxPeca)
                        lado.append(movimento)
                else:
                    if (proximaPeca[0] == "B" or proximaPeca[0] == "D"):
                        pecas.append(proximaPeca)
                        coordenadas.append(coordProxPeca)
                        lado.append(movimento)
                        
                    elif proximaPeca[0] == "P": 
                        if casa == casaAnalise:
                            corPeao = proximaPeca[1]                            
                            passosPeao = passos[proximaPeca[0]]
                            if corPeao == 1:
                                passosPeao = [(val[0]*-1,val[1]*-1) for val in passosPeao]
                            for movsP in passosPeao:
                                if movsP == movimentoCorrigido:
                                    pecas.append(proximaPeca)
                                    coordenadas.append(coordProxPeca)
                                    lado.append(movimento)

        
    return pecas,coordenadas,lado
        
def coordenadaPeca(tabuleiro,peca):
    pecas = [(i,j) for i in range(len(tabuleiro)) for j in range(len(tabuleiro[i])) if tabuleiro[i][j] == peca]
    return pecas

def jogadasTotal(jogo,cor):
    pecas = [("R",cor),("P",cor),("B",cor),("C",cor),("T",cor),("D",cor)]
    passagem = copy.deepcopy(jogo.enPassant)
    coordenadasPecas = list()
    coordenadasCasas = list()
    for peca in pecas:
        coordPeca = coordenadaPeca(jogo.tabuleiro,peca)
        tipoPeca = peca[0]
        movimentos = copy.deepcopy(passos[tipoPeca])
        if tipoPeca == 'P':
            movimentos.append((-2,0))
            if cor == 1:
                movimentos = [(val[0]*-1,val[1]*-1) for val in movimentos]
        for coordenada in coordPeca:
            for movimento in movimentos:
                x = coordenada[0] + movimento[0]
                y = coordenada[1] + movimento[1]
                casa = (x,y)
                while 0<=x<8 and 0<=y<8:
                    # print('='*50)
                    # print('ANTES')
                    # print(f'Peca = {peca}')
                    # print(f'Coordenada = {coordenada}')
                    # print(f'Movimento = {movimento}')
                    # print(f'Peça na Coordenada = {jogo.tabuleiro[coordenada[0]][coordenada[1]]}')
                    # print(f'Coordenada da Nova Casa = {(x,y)}')
                    # print(f'Nova Casa = {jogo.tabuleiro[x][y]}')
                    resultado = verificarJogada(jogo,cor,coordenada,casa)
                    # print('='*50)
                    # print('DEPOIS')
                    # print(f'Peca = {peca}')
                    # print(f'Coordenada = {coordenada}')
                    # print(f'Movimento = {movimento}')
                    # print(f'Peça na Coordenada = {jogo.tabuleiro[coordenada[0]][coordenada[1]]}')
                    # print(f'Coordenada da Nova Casa = {(x,y)}')
                    # print(f'Nova Casa = {jogo.tabuleiro[x][y]}')
                    # print('='*50)
                    if resultado[0] == 1:
                        coordenadasPecas.append(coordenada)
                        if resultado[1] == True:
                            for promocao in ["B","C","T","D"]:
                                coordenadasCasas.append((casa,promocao))
                        else:
                            coordenadasCasas.append((casa,False))
   
                    if jogo.enPassant != passagem:
                        jogo.enPassant = passagem
                    if tipoPeca == "R" or tipoPeca == "C" or tipoPeca == "P":
                        break
                    x += movimento[0]
                    y += movimento[1]
                    casa = (x,y)
    return coordenadasPecas,coordenadasCasas

def moverPeca(tabuleiro,casaPeca,casaFinal,promocao=False):
    x,y = casaPeca
    novaCasaX,novaCasaY = casaFinal
    novaCasa = tabuleiro[novaCasaX][novaCasaY]
    casaAtual = tabuleiro[x][y]
    
    casaAtualPeca,casaAtualCor = casaAtual
    novaCasaPeca,novaCasaCor = novaCasa
    
    if promocao != False:
        tabuleiro[novaCasaX][novaCasaY] = (promocao,tabuleiro[x][y][1])
    else:
        tabuleiro[novaCasaX][novaCasaY] = tabuleiro[x][y]
    
    tabuleiro[x][y] = ("S",10)
    
    if casaAtualPeca == 'R' and ((y - novaCasaY == 2) or (y - novaCasaY == -2)):
        if y - novaCasaY == -2:
            torreRoq = (x,7)
            moverPeca(tabuleiro,torreRoq,(x,5))
        else:
            torreRoq = (x,0)
            moverPeca(tabuleiro,torreRoq,(x,3))
    
    if casaAtualPeca == 'P' and (y - novaCasaY != 0) and novaCasaPeca == 'S':
        if casaAtualCor == 0:
            tabuleiro[novaCasaX+1][novaCasaY] = ("S",10)
        else:
            tabuleiro[novaCasaX-1][novaCasaY] = ("S",10)
    
    movimentacao = notacaoXadrez(tabuleiro,casaPeca,casaFinal,novaCasaPeca)
    
    return movimentacao

def verificarJogada(jogo,cor,casaOrigem,novaCasa):
    tabuleiro = jogo.tabuleiro
    peaoEnPassant = copy.deepcopy(jogo.enPassant)
    pecas = list()
    pecasProxima = list()

    casaX,casaY = casaOrigem
    novaCasaX,novaCasaY = novaCasa
    
    peca = tabuleiro[casaX][casaY]
    
    tipo,corPeca = peca
        
    #0 - ver se a casa tem de fato alguma peça pra movimentar (ou se tá movendo peça dos outros)
    if tipo == "S" or corPeca != cor:
        return 0,False
    
    offsets = passos[tipo]

    if tipo == "P" and corPeca == 1:
        offsets = [(val[0]*-1,val[1]*-1) for val in offsets]
    
    #1 - ver se a posição existe no tabuleiro (ou se o jogador não fez movimento)
    if ((novaCasaX<0 or novaCasaX>=8) or (novaCasaY<0 or novaCasaY>=8)) or (novaCasaX == casaOrigem[0] and novaCasaY == casaOrigem[1]):
        return 0,False
    
    peca2 = tabuleiro[novaCasaX][novaCasaY]
    
    #2 - se existe, verificar se é possível andar com a peça até o local
    deltaX = novaCasaX - casaX
    deltaY = novaCasaY - casaY
    
    if tipo != "C" and tipo != "P" and tipo != 'R':
        if abs(deltaX) >= abs(deltaY) and deltaX != 0:
            movimento = (deltaX/abs(deltaX),deltaY/abs(deltaX))
        else:
            movimento = (deltaX/abs(deltaY),deltaY/abs(deltaY))
    else:
        movimento = (deltaX,deltaY)
    if movimento in offsets:
        if tipo == 'R' and (movimento == (0,2) or movimento == (0,-2)):
            movimento = (deltaX,deltaY/abs(deltaY))
        pass
    elif (tipo == 'P') and ((movimento == (-2,0) and cor == 0 and casaX == 6) or (movimento == (2,0)  and cor == 1 and casaX == 1)):
        movimento = (deltaX/abs(deltaX),deltaY)
    else:
        return 0,False
    #refazendo pq qnd for fazer operações tem que ser em int se não dá problema
    movimento = (int(movimento[0]),int(movimento[1]))
    

    #3 - ver se a casa que será ocupada tem uma peça aliada (ou se for um peão indo pra frente se tem alguma peça na casa)
    
    if peca2[1] == cor or ((movimento[1] == 0 and tipo == "P") and peca2[0] != "S"):
            return 0,False

    #4 - ver se tem peça no meio do trajeto
    x = int(casaX + movimento[0])
    y = int(casaY + movimento[1])
    while (x,y) != novaCasa:
        p = tabuleiro[x][y]
        if p[0] != "S":
            pecas.append(p)
        x += movimento[0]
        y += movimento[1]
    if len(pecas) > 0:
        return 0,False
    
    #4.1 se for um peão indo na diagonal, verificar se tem alguma peça na diagonal(o que nesse caso seria uma jogada legal, já que peões só podem andar na diagonal caso houverem peças da cor oposta) OU em passagem
    if (tipo == "P" and movimento[1] != 0):
        #não precisa verificar a cor pois eu já verifiquei anteriormente
        if peaoEnPassant == None:
            if peca2[0] == "S":
                return 0,False
        else:
            if corPeca == 0:
                passagem = (peaoEnPassant[0]-1,peaoEnPassant[1])
            else:
                passagem = (peaoEnPassant[0]+1,peaoEnPassant[1])
            if peca2[0] == 'S':
                if novaCasa != passagem:
                    return 0,False

    #5 - ver se o rei está em xeque
    
    
    if tipo != "R":
        
        rei = ("R",cor)
        coordenadaRei = coordenadaPeca(jogo.tabuleiro,rei)
        pecasXeque,coordenadasXeque,deltaXeque = pecasAtacando(jogo.tabuleiro,coordenadaRei[0])
        
        passosRei = passos["R"][:-2]
        
        if len(pecasXeque) > 0:
            for i in range (len(pecasXeque)):
                coordenadaProximaPeca = coordenadasXeque[i]
                movimentoProximaPeca = deltaXeque[i]
                casas = list()
                x,y = coordenadaProximaPeca
                #if proximaPeca[0] == "T" or proximaPeca[0] == "D" or proximaPeca[0] == "B":
                    #5.1 se estiver em xeque: ver se a jogada cobre o xeque
                while (x,y) != coordenadaRei[0]:
                    casas.append((x,y))
                    x -= movimentoProximaPeca[0]
                    y -= movimentoProximaPeca[1]
                if novaCasa not in casas:
                    return 0,False
                    #código que eu tinha escrito antes (deixei comentado vai que não funciona a gambiarra de cima)
                    #5.1.1 se for peão ver se está realmente atacando o rei
                    # elif proximaPeca[0] == "P" or proximaPeca[0] == "C" :
                    #     #primeiro ver se ela tem a chance de estar atacando o rei (no caso se ela estiver grudada nele)
                    #     if (x - reiX) == coordenadaRei[0][0] and (y - reiY) == coordenadaRei[0][1]:
                    #         if proximaPeca[0] == "C":
                    #             if novaCasa != coordenadaProximaPeca:
                    #                 return 0,False
                    #         else:
                    #             corPeao = proximaPeca[1]
                    #             passosPeao = passos[proximaPeca]
                    #             if corPeao == 1 and proximaPeca == 'P':
                    #                 passosPeao = [(val[0]*-1,val[1]*-1) for val in passosPeao]
                    #             for movsP in passosPeao:
                    #                 if movsP == movimento:
                    #                     if novaCasa != coordenadaProximaPeca:
                    #                         return 0,False   
        #6 - ver se a peça que está sendo movimentada está cravada (nesse caso ver se o rei é protegido pela peça)
    
        for movimentos in passosRei:
            pecasProxima.append(primeiraPecaEncontrada(jogo.tabuleiro,casaOrigem,movimentos,True,False))
        
        if rei in pecasProxima:
            indexRei = pecasProxima.index(rei)
            direcaoRei = passosRei[indexRei]
            direcaoInverso = (direcaoRei[0]*-1,direcaoRei[1]*-1)
            indexInverso = passosRei.index(direcaoInverso)
            pecaOposta = pecasProxima[indexInverso]
            if pecaOposta != "--":
                if movimento != direcaoRei and movimento != direcaoInverso:
                    if direcaoRei[0] == 0 or direcaoRei[1] == 0:
                        if (pecaOposta[0] == "T" or pecaOposta[0] == "D") and pecaOposta[1] != corPeca:
                            return 0,False
                    else:
                        if (pecaOposta[0] == "B" or pecaOposta[0] == "D") and pecaOposta[1] != corPeca:
                            return 0,False
    else:
        #5.2.1 ver se a casa onde o rei se deslocará é atacada por alguma peça
        
        #aqui era pra ter a verificação do roque mas eu não quis fazer por ser muito complexo e por ter pouco tempo ops
        #VOU FAZER SIMMM
        #verificar se a o rei se movimentou (não pode ser feito o roque se o rei tiver se movimentado antes)
        if deltaY == 2 or deltaY == -2:
            lancesCor = [jogo.logComposto[i] for i in range(len(jogo.logComposto)) if i%2 == cor]
            #não pode fazer o roque se o rei estiver em xeque
            xeque = pecasAtacando(tabuleiro,casaOrigem)
            
            if len(xeque[0]) > 0:
                return 0,False
            
            #não pode fazer o roque se o rei ja andou no jogo
            temRei = coordenadaPeca(lancesCor,casaOrigem)
            if len(temRei) > 0:
                return 0,False
            
            if deltaY == 2:
                casaTorre = tabuleiro[casaOrigem[0]][7]
            else:
                casaTorre = tabuleiro[casaOrigem[0]][0]
            
            #não pode fazer o roque se a torre do roque ja andou no jogo
            temTorre = coordenadaPeca(lancesCor,casaTorre)
            if len(temTorre) > 0:
                return 0,False
            
            if deltaY == 2:
                coordenadaTorreRoq = (casaOrigem[0],5)
                coordenadaPecaReiRoq = (casaOrigem[0],casaOrigem[1] + 1)
            else:
                coordenadaTorreRoq = (casaOrigem[0],3)
                coordenadaPecaReiRoq = (casaOrigem[0],casaOrigem[1] - 1)
            
            if tabuleiro[coordenadaTorreRoq[0]][coordenadaTorreRoq[1]] != ('T',cor):
                return 0,False
            
            totalPecasAtacando = pecasAtacando(tabuleiro,coordenadaPecaReiRoq)
            if len(totalPecasAtacando[0]) > 0:
                return 0,False
            #não pode fazer o roque também se a casa onde o rei passar estiver sendo atacada
            
            
        tabuleiroTemp = copy.deepcopy(jogo.tabuleiro)
        moverPeca(tabuleiroTemp,casaOrigem,novaCasa)
        totalPecasAtacando = pecasAtacando(tabuleiroTemp,novaCasa)
        if len(totalPecasAtacando[0]) > 0:
            return 0,False
    #7 - se for um peão na última coluna retornar que há promoção
    if tipo == "P" and ((corPeca == 0 and novaCasaX == 0) or (corPeca == 1 and novaCasaX == 7)):
        return 1,True #nesse caso indica que há promoção

    

    #8 - se vc passou por todas essas regras parabéns sua jogada é de acordo com as regras do xadrez!
    return 1,False

def primeiraPecaEncontrada(tabuleiro,casa,orientacao,returnPeca=True,unicaInstancia=False):
    x,y = casa
    peca = '--'
    constX,constY = orientacao
    x += constX
    y += constY
    while 0<=x<8 and 0<=y<8:
        peca = tabuleiro[x][y]
        if peca[0] != "S":
            if not returnPeca:
                return (x,y)
            return peca
        peca = '--'
        if unicaInstancia:
            return peca
        x += constX
        y += constY
    return peca

def engine(jogo,cor):
    while True:
        tabuleiro = jogo.tabuleiro
        if cor == 0:
            jogadorPecas = jogo.pecasBrancas
        else:
            jogadorPecas = jogo.pecasPretas
        pecaTupla = random.choice(jogadorPecas)
        peca,cor = pecaTupla

        pecas = coordenadaPeca(tabuleiro,pecaTupla)
        casa = random.choice(pecas)
        
        
        if peca == "P":
            offsets = passos[peca]
            if cor == 1:
                offsets = [(val[0]*-1,val[1]*-1) for val in offsets]
            offsetX,offsetY = random.choice(offsets)
            if offsetY == 0:
                if (casa[0] == 6 and cor == 0) or (casa[0] == 1 and cor == 1):
                    doisPassos = random.randint(1,2)
                    offsetX *= doisPassos
            passosX = casa[0] + offsetX
            passosY = casa[1] + offsetY
        else:
            offsets = passos[peca]
            offsetX,offsetY = random.choice(offsets)
            if peca == "C" or peca == "R":
                passosX =  casa[0] + offsetX
                passosY =  casa[1] + offsetY
            else:
                rand = random.randint(0,7)
                passosX = casa[0] + rand * offsetX
                passosY = casa[1] + rand * offsetY
        novaCasa = (passosX,passosY)
        resp,promocao = verificarJogada(jogo,cor,casa,novaCasa)
        if resp == 1:
            if promocao == True:
                pecasPromocao = ["B","C","T","D"]
                promocao = random.choice(pecasPromocao)
                
            jogada = moverPeca(tabuleiro,casa,novaCasa,promocao)
            jogo.enPassant = enPassant(jogo.tabuleiro,casa,novaCasa)
            jogo.log.append(jogada)
            jogo.logComposto.append([casa,novaCasa])
            break
        else:
            passosX = 0
            passosY = 0
            continue

def acabarOJogo(jogo,cor):
    tabuleiro = copy.deepcopy(jogo.tabuleiro)
    ultimaJogada = jogo.log[-1]

    rei = ("R", cor)
    passosRei = passos["R"][:-2]
    
    pecas = [("P",cor),("B",cor),("C",cor),("T",cor),("D",cor)]
    coordRei = coordenadaPeca(tabuleiro,rei)

    #1 verificar se o rei consegue andar pra alguma casa
    jogadaValida = 0

    for movimentos in passosRei:
        outraCasa = (coordRei[0][0] + movimentos[0],coordRei[0][1] + movimentos[1])
        resultado = verificarJogada(jogo,cor,coordRei[0],outraCasa)
        jogadaValida += resultado[0]

    #2 ver se a jogada não cai no polêmico lance dos 50 lances sem comer peça (ou sem movimentar peão)
    if 'x' not in ultimaJogada and any(char.isupper() for char in ultimaJogada):
        jogo.incrementarLance()
    else:
        jogo.cinquentaLances = 0
    lancesContados = jogo.cinquentaLances
        
    if jogadaValida == 0:        
        #3 se tá aqui quer dizer que o rei não tem casa pra andar
        # nesse caso analisar se há xeques
        pecasXeque,coordenadasXeque,deltaXeque = pecasAtacando(tabuleiro,coordRei[0])
            
        if len(pecasXeque) == 0:
            #se não tem xeque, ver se dá pra movimentar pelo menos uma peça, se não é empate
            for peca in pecas:
                coordPeca = coordenadaPeca(tabuleiro,peca)
                tipoPeca = peca[0]
                movimentos = passos[tipoPeca]
                if cor == 1 and tipoPeca == "P":
                    movimentos = [(val[0]*-1,val[1]*-1) for val in movimentos]
                for coordenada in coordPeca:
                    for movimento in movimentos:
                        casa = (coordenada[0] + movimento[0], coordenada[1] + movimento[1])
                        resultado = verificarJogada(jogo,cor,coordenada,casa)
                        if resultado[0] == 1:
                            if lancesContados >= 50:
                                return None
                            else:
                                return False
            return None

        elif len(pecasXeque) == 1:
            #se tem uma peça em xeque, como não é possível movimentar o rei, ver se dá pra por alguma peça na frente OU comer a peça
            casas = list()
            x,y = coordenadasXeque[0]
            while x != coordRei[0][0] or y != coordRei[0][1]:
                casas.append((x,y))
                x -= deltaXeque[0][0]
                y -= deltaXeque[0][1]            
            for peca in pecas:
                coordPeca = coordenadaPeca(tabuleiro,peca)
                for coordenada in coordPeca:
                    for casa in casas:
                        resultado = verificarJogada(jogo,cor,coordenada,casa)
                        if resultado[0] == 1:
                            if lancesContados >= 50:
                                return None
                            else:
                                return False #segue la pelota 
            return True
            
        else:
            # xeque duplo e não dá pra movimentar o rei? é xeque-mate
            return True
    else:
        if lancesContados >= 50:
            return None
        else:
            return False

def printarTabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            print(tabuleiro[i][j],end=" ")
        print()

def traduzirCoordenadas(coordenadas):
    coord = [*coordenadas]
    x = fileirasPraColunas[coord[0]]
    y = fileirasPraLinhas[coord[1]]
    return (y,x)

jogo = Estado()
opcao = 0

print("="*50)
print("Xadrez Muito Mal Feito")
print("="*50)
print()
while True:
    print("="*50)
    print("Selecione o modo: ")
    print("1 - Humano X Humano")
    print("2 - Humano X Máquina")
    print("3 - Máquina X Máquina")
    print("="*50)
    escolha = int(input("Escolha: "))

    if 1<=escolha<=3:
        break
    else:
        print("Opção inválida, escolha novamente")
        

if escolha == 1 or escolha == 2:
    while True:
        print("="*50)
        print("Escolha sua cor:")
        print("0 - Branco")
        print("1 - Preto")
        print("2 - Aleatório")
        print("="*50)
        jogador1cor = int(input("Escolha: "))
        jogador1tipo = "humano"
        if 0<=jogador1cor<=2:
            if jogador1cor == 2:
                jogador1cor = random.randint(0,1)
            jogador2cor = (jogador1cor+1)%2
            break
        else:
            print("Opção inválida, escolha novamente")

    if escolha == 2:
        while True:
            print("="*50)
            print("Escolha a dificuldade:")
            print("1 - Fácil")
            print("2 - Médio")
            print("3 - Difícil")
            print("="*50)
            dificuldade = int(input("Escolha: "))
            if 1<=dificuldade<=3:
                if dificuldade  == 1:
                    jogador2tipo = "minmaxreverso"
                elif dificuldade == 2:
                    jogador2tipo = "jogadasaleatorias"
                elif dificuldade == 3:
                    jogador2tipo = "minmax"
                break
            else:
                print("Opção inválida, escolha novamente")
    else:
        jogador2tipo = "humano"
            
elif escolha == 3:
    while True:
        print("="*50)
        print("Opções:")
        print("1 - Uma Partida")
        print("2 - Batida de testes (200 partidas)")
        print("="*50)
        opcao = int(input("Escolha: "))
        jogador1cor = random.randint(0,1)
        jogador2cor = (jogador1cor+1)%2
        if 1<=opcao<=2:
            break
        else:
            print("Opção inválida, escolha novamente")
        
    for i in range (2):
        while True:
            print("="*50)
            print(f"Escolha a engine {i+1}")
            print("1 - Pior Jogada")
            print("2 - Jogadas aleatórias")
            print("3 - Melhor jogada (profundidade 2)")
            print("="*50)
            opcaoEngine = int(input("Escolha: "))
            if opcaoEngine == 1:
                tipoEngine = "minmaxreverso"
            elif opcaoEngine == 2:
                tipoEngine = "jogadasaleatorias"
            elif opcaoEngine == 3:
                tipoEngine = "minmax"
            else:
                print("Opção inválida, escolha novamente")
                continue
            if i == 0:
                    jogador1tipo = tipoEngine
                    break
            else:
                jogador2tipo = tipoEngine
                break


jogador1 = Jogador(jogador1cor,jogador1tipo)
jogador2 = Jogador(jogador2cor,jogador2tipo)

jogadores = (jogador1,jogador2)
if opcao == 0:
    while jogo.fim_de_jogo == False:
        for jogador in jogadores:
            if jogo.fim_de_jogo or jogo.fim_de_jogo == None:
                break
            print("="*50)
            printarTabuleiro(jogo.tabuleiro)
            print("="*50)
            if jogo.turno % 2 == jogador.cor:
                if jogador.engine == "humano":
                    while True:
                        pontoInicial = traduzirCoordenadas(input("Digite a posição da casa que quer mover: "))
                        pontoFinal = traduzirCoordenadas(input("Digite a posição da casa onde a peça será colocada: "))
                        resultado,promocao = verificarJogada(jogo,jogador.cor,pontoInicial,pontoFinal)
                        if resultado == 0:
                            print("Essa jogada não pode ser efetuada, tente novmanete.")
                        else:
                            if promocao:
                                while True:
                                    print("O peão a ser movido será promovido! Escolha para qual peça será promovido(a)\nOpções\nC- Cavalo\nB- Bispo\nT- Torre\n D- Dama")
                                    promocao = input()
                                    if promocao == "C" or promocao == "B" or promocao == "T" or promocao == "D":
                                        break
                                    else:
                                        print("Opção inválida, escolha novamente")
                            jogada = moverPeca(jogo.tabuleiro,pontoInicial,pontoFinal,promocao)
                            jogo.enPassant = enPassant(jogo.tabuleiro,pontoInicial,pontoFinal)
                            jogo.log.append(jogada)
                            jogo.logComposto.append([pontoInicial,pontoFinal])
                            break
                        
                elif jogador.engine == "jogadasaleatorias":
                    engine(jogo,jogador.cor)
                    
                elif jogador.engine == "minmax":
                    vlr,jogada=minmax(jogo,jogador.cor,2)
                    peca = moverPeca(jogo.tabuleiro,jogada[0],jogada[1][0],jogada[1][1])
                    jogo.enPassant = enPassant(jogo.tabuleiro,jogada[0],jogada[1][0])
                    jogo.log.append(peca)
                    jogo.logComposto.append([jogada[0],jogada[1][0]])
                
                elif jogador.engine == "minmaxreverso":
                    vlr,jogada = minmaxReverso(jogo,jogador.cor,jogador.cor,2)
                    peca = moverPeca(jogo.tabuleiro,jogada[0],jogada[1][0],jogada[1][1])
                    jogo.enPassant = enPassant(jogo.tabuleiro,jogada[0],jogada[1][0])
                    jogo.log.append(peca)
                    jogo.logComposto.append([jogada[0],jogada[1][0]])
                    
                
                jogo.turno += 1

                jogo.pecasBrancas = [jogo.tabuleiro[i][j] for i in range(len(jogo.tabuleiro)) for j in range(len(jogo.tabuleiro[i])) if jogo.tabuleiro[i][j][1] == 0]
                jogo.pecasPretas = [jogo.tabuleiro[i][j] for i in range(len(jogo.tabuleiro)) for j in range(len(jogo.tabuleiro[i])) if jogo.tabuleiro[i][j][1] == 1]
                
                if jogo.fim_de_jogo:
                        mate = jogo.log.pop()
                        novaJogada = mate.replace('+','#')
                        jogo.log.append(novaJogada)
                        log = jogo.log.copy()
                
                if jogador.cor == 0:
                    jogo.fim_de_jogo = acabarOJogo(jogo,1)
                    if jogo.fim_de_jogo:
                        jogo.log[-1].replace('+','#')
                    print(f"Brancas: {jogo.log[-1]}")
                else:
                    jogo.fim_de_jogo = acabarOJogo(jogo,0)
                    if jogo.fim_de_jogo:
                        jogo.log[-1].replace('+','#')
                    print(f"Pretas: {jogo.log[-1]}")
                    
                if jogo.fim_de_jogo or jogo.fim_de_jogo == None:
                    jogo.log[-1].replace('+','#')
                    break
                

    print("="*50)
    printarTabuleiro(jogo.tabuleiro)
    print("="*50)

    if jogo.fim_de_jogo == None:
        print("Empate")
    elif jogo.turno % 2 == 0:
        print("Vitória das Pretas")
    elif jogo.turno % 2 == 1:
        print("Vitória das Brancas")

else:
    if opcao == 1:
        qtdJogos = 1
    elif opcao == 2:
        qtdJogos = 100
        
    vitoriasJogador1Brancas = 0
    vitoriasJogador1Pretas = 0
    vitoriasJogador2Brancas = 0
    vitoriasJogador2Pretas = 0
    empates = 0
    
    print(f"{jogador1tipo},{jogador1cor}")
    print(f"{jogador2tipo},{jogador2cor}")
    
    txt = open('log batida de testes.txt','a')
    for i in range(qtdJogos):
        log = None
        novoJogo = copy.deepcopy(jogo)
        if i == 50:
            jogador1.cor, jogador2.cor = jogador2.cor, jogador1.cor
        while novoJogo.fim_de_jogo == False:
            for jogador in jogadores:
                if novoJogo.fim_de_jogo or novoJogo.fim_de_jogo == None:
                    log = novoJogo.log.copy()
                    break
                elif novoJogo.turno % 2 == jogador.cor:
                    if jogador.engine == "jogadasaleatorias":
                        engine(novoJogo,jogador.cor)
                        
                    elif jogador.engine == "minmax":
                        vlr,jogada=minmax(novoJogo,jogador.cor,2)
                        peca = moverPeca(novoJogo.tabuleiro,jogada[0],jogada[1][0],jogada[1][1])
                        novoJogo.enPassant = enPassant(novoJogo.tabuleiro,jogada[0],jogada[1][0])
                        novoJogo.log.append(peca)
                        novoJogo.logComposto.append([jogada[0],jogada[1][0]])
                    
                    elif jogador.engine == "minmaxreverso":
                        vlr,jogada = minmaxReverso(novoJogo,jogador.cor,jogador.cor,2)
                        peca = moverPeca(novoJogo.tabuleiro,jogada[0],jogada[1][0],jogada[1][1])
                        novoJogo.enPassant = enPassant(novoJogo.tabuleiro,jogada[0],jogada[1][0])
                        novoJogo.log.append(peca)
                        novoJogo.logComposto.append([jogada[0],jogada[1][0]])
                    
                    novoJogo.turno += 1

                    novoJogo.pecasBrancas = [novoJogo.tabuleiro[i][j] for i in range(len(novoJogo.tabuleiro)) for j in range(len(novoJogo.tabuleiro[i])) if novoJogo.tabuleiro[i][j][1] == 0]
                    novoJogo.pecasPretas = [novoJogo.tabuleiro[i][j] for i in range(len(novoJogo.tabuleiro)) for j in range(len(novoJogo.tabuleiro[i])) if novoJogo.tabuleiro[i][j][1] == 1]
                    
                    if jogador.cor == 0:
                        novoJogo.fim_de_jogo = acabarOJogo(novoJogo,1)
                    else:
                        novoJogo.fim_de_jogo = acabarOJogo(novoJogo,0)
                        
                    if novoJogo.fim_de_jogo:
                        mate = novoJogo.log.pop()
                        novaJogada = mate.replace('+','#')
                        novoJogo.log.append(novaJogada)
                    if jogador.cor == 0:
                        print(f"Brancas: {novoJogo.log[-1]}")
                    else:
                        print(f"Pretas: {novoJogo.log[-1]}")
                        
        if novoJogo.fim_de_jogo == None:
            print(f"Jogo {i+1}: Empate")
            txt.write(f"Jogo {i+1}: Empate")
            empates += 1
        elif novoJogo.turno % 2 == 0:
            if jogador1.cor == 1:
                vitoriasJogador1Pretas += 1
            else:
                vitoriasJogador2Pretas += 1
            print(f"Jogo {i+1}: Vitória das Pretas")
            txt.write(f"Jogo {i+1}: Vitória das Pretas\n")
            
        elif novoJogo.turno % 2 == 1:
            if jogador1.cor == 0:
                vitoriasJogador1Brancas += 1
            else:
                vitoriasJogador2Brancas += 1
            print(f"Jogo {i+1}: Vitória das Brancas")
            txt.write(f"Jogo {i+1}: Vitória das Brancas\n")
        
        print(f"Notações da partida: {log}")
        txt.write(f"Notações da partida: {log}\n")
        print("="*50)
        printarTabuleiro(novoJogo.tabuleiro)
        print("="*50)
    
    print("="*50)
    print(f"Engine: {jogador1tipo}")
    print(f"Vitórias de brancas: {vitoriasJogador1Brancas}")
    print(f"Vitórias de pretas: {vitoriasJogador1Pretas}")
    print()
    print(f"Engine: {jogador2tipo}")
    print(f"Vitórias de brancas: {vitoriasJogador2Brancas}")
    print(f"Vitórias de pretas: {vitoriasJogador2Pretas}")
    print()
    print(f"Empates: {empates}")
    txt.close()
    
