# PREGUNTA 4

# Creación (0,5 puntos)
# Copia el ejercicio anterior y realicemos una modificación:

# Junto al método init y calificación, vamos a crear otro método especial de Python, el método str. Al igual que init, debe ir encerrado entre dobles guiones bajos, y debe tener el siguiente formato:

 

# def __str__(self): return "Lo que quiero mostrar"

 

# Este método nos sirve para imprimir por pantalla la información de un objeto, si tenemos un objeto alumno1 creado y realizamos print(alumno1), Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que desea en un string).

 

# Experimentación (0,5 puntos)
# Implementa el método str y haz que muestre el nombre y la nota del alumno
# Crea algun objeto de la clase Alumno
# Realiza print de esos objetos para visualizar por pantalla la información del str

class Alumno(object):
    """Clase alumno"""
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("Alumno creado con éxito")
    
    def calificacion(self):
        """Imprime por pantalla si el alumno ha aprobado o suspendido en base a su nota"""
        if (self.nota >= 5):
            print("El alumno ha aprobado")
            return True
        else:
            print("El alumno ha suspendido")
            return False
    
    def __str__(self):
        return "Nombre: " + self.nombre + ", nota: " + str(self.nota)