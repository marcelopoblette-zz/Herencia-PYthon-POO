# superclase
class Persona:
    def __init__(self,clv, nom, ed):
        self.clave = clv
        self.nombre = nom
        self.edad = ed
    def mostrarDatos(self):
        print("Mostrando los datos desde la Super Clase")
        print("Clave: ", self.clave)
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)