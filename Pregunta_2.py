# PREGUNTA 2

# Recorre el listado del ejemplo y realiza las siguientes operaciones:

# [18, 50, 210, 80, 145, 333, 70, 30]

# Imprimir el número en caso de que sea múltiplo de 10 y menor que 200
# Parar el programa si llega a un número mayor que 300
# Organizar la lista mediante el método de ordenamiento merge sort
# Dada la lista anterior y un valor 145 devolver el índice de 145 en la lista si 145 está en la lista, y −1 si 145 no está en la lista

lista = [18, 50, 210, 80, 145, 333, 70, 30]

def excepciones(lista):
    for i in lista:
        if i > 300:
            print("Existe un número mayor que 300")
            break
        elif i % 10 == 0 and i < 200:
            print(i)

def mergesort(lista):
    """Método de ordenamiento mergesort"""
    if (len(lista) <= 1):
        return lista
    else:
        medio = len(lista)//2
        izquierda = []
        for i in range(0, medio):
            izquierda.append(lista[i])
        derecha = []
        for i in range(medio, len(lista)):
            derecha.append(lista[i])
        izquierda = mergesort(izquierda)
        derecha = mergesort(derecha)
        if (izquierda[-1] <= derecha[0]):
            izquierda += derecha
            return izquierda
        resultado = merge(izquierda, derecha)
        return resultado
    
def merge(izquierda, derecha):
    """Función para mezclar listas"""
    lista_mezclada = []
    while (len(izquierda) > 0) and (len(derecha) > 0):
        if (izquierda[0] < derecha[0]):
            lista_mezclada.append(izquierda.pop(0))
        else:
            lista_mezclada.append(derecha.pop(0))
    if (len(izquierda) > 0):
        lista_mezclada += izquierda
    if (len(derecha) > 0):
        lista_mezclada += derecha
    return lista_mezclada

lista = mergesort(lista)

def binaria(lista, buscado):
    """Método de búsqueda binaria"""
    posicion = -1
    primero = 0
    ultimo = len(lista)-1
    while (primero <= ultimo) and (posicion == -1):
        medio = (primero + ultimo) // 2
        if (lista[medio] == buscado):
            posicion = medio
        else:
            if (buscado < lista[medio]):
                ultimo = medio - 1
            else:
                primero = medio + 1
    return posicion

print(f"El número buscado se encuentra en la posición {binaria(lista, 145)} según python, para un humano está en la posición {binaria(lista, 145)+1}")

# PRUEBAS
import unittest

class Test(unittest.TestCase):
    def test_mergesort(self):
        self.assertEqual(mergesort([18, 50, 210, 80, 145, 333, 70, 30]), [18, 30, 50, 70, 80, 145, 210, 333])
    def test_binaria(self):
        self.assertEqual(binaria([18, 30, 50, 70, 80, 145, 210, 333], 145), 5)

if __name__ == "__main__":
    unittest.main()
