from animal import Animal

class Reptil(Animal):
    def __init__(self, nombre, edad, habitat, piel, alimentacion, color):
        super().__init__(nombre, edad, habitat)
        self.piel = piel
        self.alimentacion = alimentacion
        self.color = color

    def mostrar_informacion(self):
        atributos_reptil = {
                "Nombre" : self.nombre,
                "Edad" : self.edad,
                "Habitat" : self.habitat,
                "Piel" : self.piel,
                "Alimentacion" : self.alimentacion,
                "Color" : self.color
            }        

        super().mostrar_informacion(atributos_reptil)

tortuga = Reptil("Josefina", 100, "Lagos", "Impermeable", "Insectos", "Cafe")
tortuga.mostrar_informacion()