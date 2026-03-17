import os
os.system('clear')
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input('Digite um número: '))
        linha.append(numero)
    matriz.append(linha)
os.system('clear')
def tabuleiro():
    for linha in matriz:
        print(*linha, sep=' | ')
def ganhou(jogador):
    for i in range(3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] == jogador:
            return True
    for c in range(3):
        if matriz[0][c] == matriz[1][c] == matriz[2][c] == jogador:
            return True
    if matriz[0][0] == matriz[1][1] == matriz[2][2] == jogador:
        return True
    if matriz[0][2] == matriz[1][1] == matriz[2][0] == jogador:
        return True
    return False
def velha():
    for linha in matriz: 
        for n in linha:
            if type(n) == int:
                return False
    return True
while True:
    tabuleiro()
    x = int(input('Em qual número quer jogar o X? '))
    achou = False
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == x:
                matriz[i][j] = 'X'
                achou = True
    if achou == False:
        print('JOGADA INVÁLIDA')
        continue
    if ganhou('X'):
        tabuleiro()
        print('X ganhou!')
        break
    if velha():
        tabuleiro()
        print('Deu velha!')
        break
    os.system('clear')
    tabuleiro()
    o = int(input('Em qual número quer jogar a O? '))
    achou = False
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == o:
                matriz[i][j] = 'O'
                achou = True
    if achou == False:
        print('JOGADA INVÁLIDA')
        continue
    if ganhou('O'):
        tabuleiro()
        print('O ganhou!')
        break
    if velha():
        tabuleiro()
        print('Deu velha!')
        break
    os.system('clear')