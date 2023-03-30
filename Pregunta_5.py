# PREGUNTA 5

# La alianza rebelde necesita comunicarse de manera segura pero el imperio galáctico interviene todas la comunicaciones, por lo que la princesa Leia nos encarga el desarrollo de un algoritmo de encriptación para las comunicaciones rebeldes, que contemple los siguientes requerimientos:

#  cada carácter deberá ser encriptado a ocho caracteres;
#  se deberá generar dos tablas hash para encriptar y desencriptar, para los caracteres desde el “ ” hasta el “}” –es decir desde el 32 al 125 de la tabla ASCII.

from builtins import chr

class NodoHash:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

class TablaHash:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.tabla = [None] * capacidad

    def hash(self, clave):
        return sum(ord(c) for c in clave) % self.capacidad

    def agregar(self, clave, valor):
        indice = self.hash(clave)
        nodo = self.tabla[indice]
        if nodo is None:
            self.tabla[indice] = NodoHash(clave, valor)
        else:
            while nodo.siguiente is not None:
                if nodo.clave == clave:
                    nodo.valor = valor
                    return
                nodo = nodo.siguiente
            if nodo.clave == clave:
                nodo.valor = valor
            else:
                nodo.siguiente = NodoHash(clave, valor)

    def buscar(self, clave):
        indice = self.hash(clave)
        nodo = self.tabla[indice]
        while nodo is not None:
            if nodo.clave == clave:
                return nodo.valor
            nodo = nodo.siguiente
        return None

class Encriptador:
    def __init__(self, capacidad):
        self.encriptar_tabla = TablaHash(capacidad)
        self.desencriptar_tabla = TablaHash(capacidad)
        self.generar_tablas()

    def generar_tablas(self):
        caracteres = [chr(i) for i in range(32, 126)]
        desplazamiento = 8
        
        for i, c in enumerate(caracteres):
            encriptado = ''.join(chr(((ord(c) - 32 + j) % 94) + 32) for j in range(1, desplazamiento + 1))
            self.encriptar_tabla.agregar(c, encriptado)
            self.desencriptar_tabla.agregar(encriptado, c)

    def encriptar(self, mensaje):
        encriptado = []
        for c in mensaje:
            if 32 <= ord(c) <= 125:
                encriptado.append(self.encriptar_tabla.buscar(c))
            else:
                encriptado.append(c)
        return ''.join(encriptado)


    def desencriptar(self, mensaje_encriptado):
        desencriptado = []
        i = 0
        while i < len(mensaje_encriptado):
            chunk = mensaje_encriptado[i:i + 8]
            if all(32 <= ord(c) <= 125 for c in chunk):
                resultado = self.desencriptar_tabla.buscar(chunk)
                if resultado is not None:
                    desencriptado.append(resultado)
                else:
                    desencriptado.append(chunk)
                i += 8
            else:
                desencriptado.append(mensaje_encriptado[i])
                i += 1
        return ''.join(desencriptado)

def main(capacidad, mensaje):
    encriptador = Encriptador(capacidad)

    mensaje_encriptado = encriptador.encriptar(mensaje)
    print("Mensaje encriptado:", mensaje_encriptado)

    mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
    print("Mensaje desencriptado:", mensaje_desencriptado)

if __name__ == "__main__":
    main(93, "Que la fuerza te acompañe!")
