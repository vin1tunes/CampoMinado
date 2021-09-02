import random


class CampoMinado:
    """Representa um campo minado.

    atributos: matriz, linhas, colunas, minas.
    """


    def __init__(self, linhas=int, colunas=int, valor=0):
        # Inicializa a matriz de forma aleatória com 0's e 1's.

        self.linhas = linhas
        self.colunas = colunas
        self.valor = 0
        self.matriz = []
    
        for i in range(self.linhas):
            self.matriz.append([valor] * self.colunas)
        
        for i in range(self.linhas):
            for j in range(self.colunas):
                self.matriz[i][j] = random.randint(-1, 0)
        

    def quantidade_minas(self, i=int, j=int):
        # Método responsável por calcular a quantidade de minas em volta de uma posição (i, j).

        minas = 0
        if i-1 >= 0:
            if self.matriz[i-1][j] == -1:
                minas += 1
            if j-1 >= 0:
                if self.matriz[i-1][j-1] == -1:
                    minas += 1
            if j+1 < self.colunas:
                if self.matriz[i-1][j+1] == -1:
                    minas += 1
        if i+1 < self.linhas:
            if self.matriz[i+1][j] == -1:
                minas += 1
            if j-1 >= 0:
                if self.matriz[i+1][j-1] == -1:
                    minas += 1
            if j+1 < self.colunas:
                if self.matriz[i+1][j+1] == -1:
                    minas += 1
        if j-1 >= 0:
            if self.matriz[i][j-1] == -1:
                minas += 1
        if j+1 < self.colunas:
            if self.matriz[i][j+1] == -1:
                minas += 1
        
        return minas
    

    def matriz_quantidade_minas(self):
        # Método responsável por calcular a matriz cujo os elementos são a quantidade de minas em cada posição (i, j) da matriz.

        M = []       

        for i in range(self.linhas):
            M.append([0] * self.colunas)
        
        for i in range(self.linhas):
            for j in range(self.colunas):
                M[i][j] = self.quantidade_minas(i, j)
        
        return M
    

    def matriz_invisivel(self):
        # Método responsável por criar uma matriz "invisível".
        S = []

        for i in range(self.linhas):
            S.append(["-"] * self.colunas)      

        return S    


    def __str__(self):
        return str(self.matriz)
    

def main():
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    total_posicoes = a * b
    nova_matriz = []

    for i in range(a):
        nova_matriz.append(["-"] * b)
    
    for i in range(a):
        for j in range(b):
            print(nova_matriz[i][j], end=" ")
        print()
    
    j = len(nova_matriz[0]) 
    
    
    matrizB = CampoMinado(a, b)

    while True:
        posicao_i = int(input("Digite a posicao i que deseja revelar: "))
        posicao_j = int(input("Digite a posição j que deseja revelar: "))

        if matrizB.matriz[posicao_i][posicao_j] == -1:
            nova_matriz[posicao_j][posicao_j] = matrizB.matriz[posicao_j][posicao_j]
            for i in range(a):
                for j in range(b):
                    print(nova_matriz[i][j], end=" ")
                print()
            print("Você perdeu!")
            return False
        else:
            nova_matriz[posicao_i][posicao_j] = matrizB.quantidade_minas(posicao_i, posicao_j)

            for i in range(a):
                for j in range(b):
                    print(nova_matriz[i][j], end=" ")
                print()
            
        
main()
