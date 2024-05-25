from animal import Animal

class Insecto(Animal):
    def __init__(self, nombre, edad, habitat, ciclo_de_vida, alimentacion):
        super().__init__(nombre, edad, habitat)
        self.ciclo_de_vida = ciclo_de_vida
        self.alimentacion = alimentacion

    def mostrar_informacion(self):
        atributos_insecto = {
            "Nombre": self.nombre,
            "Edad": self.edad,
            "habitat": self.habitat,
            "ciclo_de_vida": self.ciclo_de_vida,
            "alimentacion": self.alimentacion
        }

        super().mostrar_informacion(atributos_insecto)

cucaracha = Insecto('Matilda', 1, 'Cocina', 5, 'sobrados')
cucaracha.mostrar_informacion()