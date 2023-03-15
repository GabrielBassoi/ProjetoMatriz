import numpy

class Matriz:
    def multiplicarMatriz(self, multiplicacao, matriz):
        return numpy.multiply(int(multiplicacao), matriz)

    def trocarsinalMatriz(self, sinal, matriz):
        if sinal == "-":
            return numpy.multiply(-1, matriz)
        return matriz

    def is_square_matrix(self, matrix):
        num_rows = len(matrix)
        num_cols = len(matrix[0]) if num_rows > 0 else 0
        return num_rows == num_cols

    def determinanteMatriz(self, matriz):
        if self.is_square_matrix(matriz):
            return numpy.linalg.det(matriz)
        return "Invalido: A matriz nao e quadrada"
