# Instanciando superclase
from Persona import Persona

# se crea la herencia
class Trabajador(Persona):
    def __init__(self, clv, nom, ed, suel):
        self.clave = clv
        self.nombre = nom
        self.edad = ed
        self.sueldo = suel

    def mostrarDatos(self):
        print("Mostrando los datos desde la Sub Clase")
        print("Clave: ", self.clave)
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("sueldo: ", self.sueldo)
