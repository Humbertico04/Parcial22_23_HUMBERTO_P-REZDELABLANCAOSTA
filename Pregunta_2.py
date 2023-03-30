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

excepciones(lista)