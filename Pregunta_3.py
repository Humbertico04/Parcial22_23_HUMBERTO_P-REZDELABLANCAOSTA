# PREGUNTA 3

# Creación (0,5 puntos)
# Crea una clase llamada Alumno que tenga los atributos nombre y nota
# Crea el constructor de la clase. Añadir en el constructor un print para informar de que el alumno se ha creado con éxito
# Crear un método llamado calificación que imprima por pantalla si el alumno ha aprobado o suspendido en base a su nota
# Experimentación (0,5 Puntos)
# Crea algunos alumnos
# Prueba a ejecutar el método calificación de cada objeto que has creado

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

# Experimentacíon
import unittest
class TestAlumno(unittest.TestCase):
    def setUp(self):
        self.alumno1 = Alumno("Pepe", 6)
        self.alumno2 = Alumno("Juan", 4)
        self.alumno3 = Alumno("Ana", 10)
    
    def test_calificacion(self):
        self.assertTrue(self.alumno1.calificacion())
        self.assertFalse(self.alumno2.calificacion())
        self.assertTrue(self.alumno3.calificacion())

if __name__ == "__main__":
    unittest.main()
