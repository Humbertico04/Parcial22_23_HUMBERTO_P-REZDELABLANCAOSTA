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
    
    def copiar(self):
        matriz_copia = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                valor = self.obtener_elemento(i, j)
                matriz_copia.asignar_elemento(i, j, valor)
        return matriz_copia
    
    def intercambiar_filas(self, fila1, fila2):
        self.matriz[fila1], self.matriz[fila2] = self.matriz[fila2], self.matriz[fila1]

    def eliminacion_gauss(self):
        n = self.filas
        det = 1
        for i in range(n):
            if self.obtener_elemento(i, i) == 0:
                for j in range(i + 1, n):
                    if self.obtener_elemento(j, i) != 0:
                        self.intercambiar_filas(i, j)
                        det *= -1
                        break
                else:
                    return 0

            det *= self.obtener_elemento(i, i)
            for j in range(i + 1, n):
                factor = self.obtener_elemento(j, i) / self.obtener_elemento(i, i)
                for k in range(i, n):
                    valor = self.obtener_elemento(j, k) - factor * self.obtener_elemento(i, k)
                    self.asignar_elemento(j, k, valor)
        return det
    
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
    
def determinante_iterativo(matriz):
    assert matriz.filas == matriz.columnas, "La matriz debe ser cuadrada"
    matriz_copia = matriz.copiar()
    return matriz_copia.eliminacion_gauss()

# PRUEBAS
import unittest

class TestMatriz(unittest.TestCase):
    def setUp(self):
        self.matriz = Matriz(5, 5)
        self.matriz.asignar_elemento(0, 0, 1)
        self.matriz.asignar_elemento(0, 1, 6)
        self.matriz.asignar_elemento(0, 2, 2)
        self.matriz.asignar_elemento(0, 3, 3)
        self.matriz.asignar_elemento(0, 4, 4)
        self.matriz.asignar_elemento(1, 0, 9)
        self.matriz.asignar_elemento(1, 1, 5)
        self.matriz.asignar_elemento(1, 2, 7)
        self.matriz.asignar_elemento(1, 3, 8)
        self.matriz.asignar_elemento(1, 4, 9)
        self.matriz.asignar_elemento(2, 0, 4)
        self.matriz.asignar_elemento(2, 1, 3)
        self.matriz.asignar_elemento(2, 2, 2)
        self.matriz.asignar_elemento(2, 3, 1)
        self.matriz.asignar_elemento(2, 4, 0)
        self.matriz.asignar_elemento(3, 0, 1)
        self.matriz.asignar_elemento(3, 1, 2)
        self.matriz.asignar_elemento(3, 2, 3)
        self.matriz.asignar_elemento(3, 3, 4)
        self.matriz.asignar_elemento(3, 4, 5)
        self.matriz.asignar_elemento(4, 0, 6)
        self.matriz.asignar_elemento(4, 1, 7)
        self.matriz.asignar_elemento(4, 2, 8)
        self.matriz.asignar_elemento(4, 3, 9)
        self.matriz.asignar_elemento(4, 4, 0)

    def test_determinante_recursivo(self):
        self.assertEqual(determinante_recursivo(self.matriz), 1050)

    def test_determinante_iterativo(self):
        self.assertAlmostEqual(determinante_iterativo(self.matriz), 1050)

if __name__ == "__main__":
    unittest.main()
