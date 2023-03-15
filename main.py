import matplotlib.pyplot as plt
import customtkinter as tk
import numpy

from ABC import ABC
from DE import DE
from poligono import Poligono

matrizABC = 0
matrizABCdeterminante = 0
matrizABCmultiplica = 0
matrizABCquadrado = 0

matrizDE = 0
matrizDEdeterminante = 0

areaPoligono = 0

x = []
y = []


def mainWindow(root):
    page = tk.CTkScrollableFrame(root)
    page.pack(pady=20, padx=60, fill='both', expand=True)

    tituloMatrizABC = tk.CTkLabel(page, text='Matriz ABC')
    tituloMatrizABC.configure("bold", font=("Roboto", 20))
    tituloMatrizABC.grid(row=0)
    tituloMatrizABC.pack(pady=12, padx=10)

    tituloEx1 = tk.CTkLabel(page, text='Ex: [1, 2], [3, 4]')
    tituloEx1.pack(pady=12, padx=10)

    entryMatrizA = tk.CTkEntry(page, placeholder_text='Matriz A')
    entryMatrizA.pack(pady=12, padx=10)

    entryMatrizB = tk.CTkEntry(page, placeholder_text='Matriz B')
    entryMatrizB.pack(pady=12, padx=10)

    entryMatrizC = tk.CTkEntry(page, placeholder_text='Matriz C')
    entryMatrizC.pack(pady=12, padx=10)

    entryOperacoes = tk.CTkEntry(page, placeholder_text='Operações')
    entryOperacoes.pack(pady=12, padx=10)

    entryMultiplicacoes = tk.CTkEntry(page, placeholder_text='Multiplicações')
    entryMultiplicacoes.pack(pady=12, padx=10)

    tituloEx2 = tk.CTkLabel(page, text='Ex: A*B , C^2')
    tituloEx2.pack(pady=12, padx=10)

    entryOrdemOperacao = tk.CTkEntry(page, placeholder_text='Ordem de Operação')
    entryOrdemOperacao.pack(pady=12, padx=10)

    tituloMatrizDE = tk.CTkLabel(page, text='Matriz DE')
    tituloMatrizDE.configure("bold", font=("Roboto", 20))
    tituloMatrizDE.pack(pady=12, padx=10)

    entryMatrizD = tk.CTkEntry(page, placeholder_text='Matriz D')
    entryMatrizD.pack(pady=12, padx=10)

    entryMatrizE = tk.CTkEntry(page, placeholder_text='Matriz E')
    entryMatrizE.pack(pady=12, padx=10)

    entryOrderOperacaoDE = tk.CTkEntry(page, placeholder_text='Ordem de Operação')
    entryOrderOperacaoDE.pack(pady=12, padx=10)

    tituloPoligono = tk.CTkLabel(page, text='Area do Polígono')
    tituloPoligono.configure("bold", font=("Roboto", 20))
    tituloPoligono.pack(pady=12, padx=10)

    entryX = tk.CTkEntry(page, placeholder_text='X')
    entryX.pack(pady=12, padx=10)

    entryY = tk.CTkEntry(page, placeholder_text='Y')
    entryY.pack(pady=12, padx=10)

    def getData():
        calcularABC(entryMatrizA.get(), entryMatrizB.get(), entryMatrizC.get(), entryOperacoes.get(), entryMultiplicacoes.get(), entryOrdemOperacao.get())
        calcularDE(entryMatrizD.get(), entryMatrizE.get(), entryOrderOperacaoDE.get())
        calcularPoligono(entryX.get(), entryY.get())
        graph()
        changepage()

    button = tk.CTkButton(page, text='Calcular', command=getData)
    button.pack(pady=12, padx=10)

def resultsWindow(root):
    page = tk.CTkScrollableFrame(root)
    page.pack(pady=20, padx=60, fill='both', expand=True)

    titulo1 = tk.CTkLabel(page, text='Matriz ABC')
    titulo1.configure("bold", font=("Roboto", 20))
    titulo1.pack(pady=12, padx=10)

    tk.CTkLabel(page, text=f'Matriz resultante: {matrizABC}').pack(pady=12, padx=10)

    tk.CTkLabel(page, text=f'Determinante: {matrizABCdeterminante}').pack(pady=12, padx=10)

    tk.CTkLabel(page, text=f'Multiplicação: {matrizABCmultiplica}').pack(pady=12, padx=10)

    tk.CTkLabel(page, text=f'Quadrado: {matrizABCquadrado}').pack(pady=12, padx=10)

    titulo2 = tk.CTkLabel(page, text='Matriz DE')
    titulo2.configure("bold", font=("Roboto", 20))
    titulo2.pack(pady=12, padx=10)

    tk.CTkLabel(page, text=f'Matriz resultante: {matrizDE}').pack(pady=12, padx=10)

    tk.CTkLabel(page, text=f'Determinante: {matrizDEdeterminante}').pack(pady=12, padx=10)

    titulo3 = tk.CTkLabel(page, text='Polígono')
    titulo3.configure("bold", font=("Roboto", 20))
    titulo3.pack(pady=12, padx=10)

    tk.CTkLabel(page, text=f'Área: {areaPoligono}').pack(pady=12, padx=10)

    button = tk.CTkButton(page, text='Voltar', command=changepage)
    button.pack(pady=12, padx=10)


def textToList(text):
    text = text.replace(' ', '')
    elements = [list(map(int, s.strip('[]').split(','))) for s in text.split('],[')]
    arr = numpy.array(elements)
    return numpy.array(elements)


def graph():
    global x, y

    x = list(map(int, x))
    y = list(map(int, y))

    plt.fill(x, y, 'b')
    plt.show()


def calcularABC(matrizA, matrizB, matrizC, operacoes, multiplicacoes, ordemOperacao):
    global matrizABC, matrizABCdeterminante, matrizABCmultiplica, matrizABCquadrado

    abc = ABC(
        textToList(matrizA),
        textToList(matrizB),
        textToList(matrizC),
        operacoes.replace(' ', '').split(','),
        multiplicacoes.replace(' ', '').split(','),
        ordemOperacao.replace(' ', '').split(','))

    matrizABC = abc.operacao1()
    matrizABCdeterminante = abc.operacao2()
    matrizABCmultiplica, matrizABCquadrado = abc.operacao3()


def calcularDE(matrizD, matrizE, ordemOperacaoDE):
    global matrizDE, matrizDEdeterminante

    de = DE(
        textToList(matrizD),
        textToList(matrizE),
        ordemOperacaoDE.replace(' ', '').split(','))

    matrizDE = de.operacao1()
    matrizDEdeterminante = de.operacao2()


def calcularPoligono(xs, ys):
    global areaPoligono, x, y

    x = xs.replace(' ', '').split(',')
    y = ys.replace(' ', '').split(',')
    poligono = Poligono(x, y)

    areaPoligono = poligono.calcularAreaPoligono()


def changepage():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
    if pagenum == 1:
        resultsWindow(root)
        pagenum = 2
    else:
        mainWindow(root)
        pagenum = 1


tk.set_appearance_mode('dark')
tk.set_default_color_theme('dark-blue')
pagenum = 1
root = tk.CTk()

def main():
    global root
    root.geometry('500x600')
    root.title('Projeto Matriz')
    mainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()