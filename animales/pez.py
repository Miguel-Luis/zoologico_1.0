from animal import Animal

class Pez(Animal):
    def __init__(self, nombre, edad, habitat, tamaño, dieta):
        super().__init__(nombre, edad, habitat)
        self.tamaño = tamaño
        self.dieta = dieta

    def get_name(self):
        return self.__nombre

    def swim (self):
        print(f"{self.__init__}")

    def mostrar_informacion(self):

        atributo_pez = {
            'Nombre': self.nombre,
            'Edad': self.edad,
            'Habitad': self.habitat,
            'Tamaño': self.tamaño,
            'Dieta': self.dieta
        }
        super().mostrar_informacion(atributo_pez)

piraña= Pez ("piraña", "5", "rio", "mediano", "carnívoro")
piraña.mostrar_informacion()





# name, tamaño, habitad, coloración, comestible, escamas, aletas, dientes