class CampoMinado:
    """Representa um campo minado.

    atributos: matriz, linhas, colunas, minas.
    """


    def __init__(self, linhas=int, colunas=int, valor=0):
        # Inicializa a matriz com 0's e 1's.

        self.linhas = linhas
        self.colunas = colunas
        self.valor = 0
        self.matriz = []
    
        for i in range(self.linhas):
            self.matriz.append([valor] * self.colunas)
        
        for i in range(self.linhas):
            print("Digite os valores para a linha", i)
            for j in range(self.colunas):
                self.matriz[i][j] = int(input("Digite os valores da matriz: "))
        

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
        # Método responsável por retornar a matriz em forma de uma string.

        return str(self.matriz)
    

def main():
    a = int(input("Linhas da matriz: "))
    b = int(input("Colunas da matriz: "))
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
    minas = int(input("Quantidade de minas: "))
    contador = 0

    while True:
        posicao_i = int(input("Digite a posicao i que deseja revelar: "))
        posicao_j = int(input("Digite a posição j que deseja revelar: "))

        if matrizB.matriz[posicao_i][posicao_j] == -1:
            # Verifica se a posição digita é igual a -1, se for, o jogo termina.
            nova_matriz[posicao_j][posicao_j] = matrizB.matriz[posicao_j][posicao_j]
            for i in range(a):
                for j in range(b):
                    print(nova_matriz[i][j], end=" ")
                print()
            print("Você perdeu!")
            return False
        else:
            nova_matriz[posicao_i][posicao_j] = matrizB.quantidade_minas(posicao_i, posicao_j)
            # Se a posição (i, j) não for igual a -1, o jogo continua, abrindo a posição indicando a quantidade
            # de mina ao redor da mesma.
            contador += 1

            for i in range(a):
                for j in range(b):
                    print(nova_matriz[i][j], end=" ")
                print()
            
            if total_posicoes - contador == minas:
                # O jogo terminrá quando as posições que não foram abertas for igual ao número de minas.
                print("Você ganhou!")

               
main()
