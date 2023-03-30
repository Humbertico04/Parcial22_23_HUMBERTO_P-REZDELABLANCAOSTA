# PREGUNTA 6

# Realiza el código para calcular el determinante de una matriz cuadrada de [5 x 5], regla de Sarrus de forma recursiva y de forma iterativa

class Matriz():
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

    def obtener_elemento(self, fila, columna):
        return self.matriz[fila][columna]

    def asignar_elemento(self, fila, columna, valor):
        self.matriz[fila][columna] = valor

    def __str__(self):
        return str(self.matriz)

    def submatriz(self, fila, columna):
        sub = Matriz(self.filas - 1, self.columnas - 1)
        for i in range(self.filas):
            for j in range(self.columnas):
                if i != fila and j != columna:
                    sub_fila = i if i < fila else i - 1
                    sub_columna = j if j < columna else j - 1
                    sub.asignar_elemento(sub_fila, sub_columna, self.obtener_elemento(i, j))
        return sub
    
def determinante_recursivo(matriz):
    if matriz.filas == 1 and matriz.columnas == 1:
        return matriz.obtener_elemento(0, 0)
    elif matriz.filas == 2 and matriz.columnas == 2:
        return matriz.obtener_elemento(0, 0) * matriz.obtener_elemento(1, 1) - matriz.obtener_elemento(0, 1) * matriz.obtener_elemento(1, 0)
    else:
        det = 0
        for j in range(matriz.columnas):
            det += ((-1) ** j) * matriz.obtener_elemento(0, j) * determinante_recursivo(matriz.submatriz(0, j))
        return det