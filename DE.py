from matriz import Matriz


class DE(Matriz):
    def __init__(self, matrizD, matrizE, ordemOperacao):
        self.matrizD = matrizD
        self.matrizE = matrizE
        self.ordemOperacao = ordemOperacao

        self.multiplicaDE = None

    def operacao1(self):
        if self.ordemOperacao[0] == "D":
            self.multiplicaDE = self.matrizD @ self.matrizE
        else:
            self.multiplicaDE = self.matrizE @ self.matrizD
        return self.multiplicaDE

    def operacao2(self):
        determinante = super().determinanteMatriz(self.multiplicaDE)
        if type(determinante) != str:
            return determinante.round(0)
        return determinante
