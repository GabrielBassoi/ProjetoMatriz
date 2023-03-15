from matriz import Matriz


class ABC(Matriz):
    def __init__(self, matrizA, matrizB, matrizC, operacoes, multiplicacoes, ordemOperacao):
        self.matrizA = matrizA
        self.matrizB = matrizB
        self.matrizC = matrizC
        self.matrizABC = []

        self.operacoes = operacoes
        self.multiplicacoes = multiplicacoes
        self.ordemOperacao = ordemOperacao

    def operacao1(self):
        A = super().trocarsinalMatriz(self.operacoes[0], super().multiplicarMatriz(self.multiplicacoes[0], self.matrizA))
        B = super().trocarsinalMatriz(self.operacoes[1], super().multiplicarMatriz(self.multiplicacoes[1], self.matrizB))
        C = super().trocarsinalMatriz(self.operacoes[2], super().multiplicarMatriz(self.multiplicacoes[2], self.matrizC))

        self.matrizABC = A + B + C

        return self.matrizABC

    def operacao2(self):
        ABC = super().determinanteMatriz(self.matrizABC)
        if type(ABC) != str:
            return ABC.round(0)
        return ABC

    def operacao3(self):
        d = {"A": self.matrizA, "B": self.matrizB, "C": self.matrizC}

        multiplicaAB = d[self.ordemOperacao[0]] @ d[self.ordemOperacao[1]]
        quadradoC = d[self.ordemOperacao[2]] @ d[self.ordemOperacao[2]]

        return multiplicaAB, quadradoC