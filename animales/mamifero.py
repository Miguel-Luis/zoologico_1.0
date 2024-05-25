from animal import Animal

class Mamifero (Animal):
    def __init__(self, nombre, edad, habitat, alimentación, peso, pelaje, color, manchas):
        super().__init__(nombre, edad, habitat)
        self.alimentación = alimentación
        self.peso = peso
        self.pelaje = pelaje
        self.color = color
        self.manchas = manchas

    def mostrar_información (self):
        atributos_mamifero= {
            "Nombre": self.nombre,
            "Edad": self.edad,
            "Hábitat": self.habitat,
            "Alimentación": self.alimentación,
            "Peso": self.peso,
            "Pelaje": self.pelaje,
            "Color": self.color,
            "Manchas": self.manchas,

        }

        super().mostrar_información(atributos_mamifero)


if __name__ == "__main__":
    leopardo = Mamifero( "Leopardo", 5, "Sabana", "Carnívoro", "25 y 90 kg", "Denso", "beige, crema, grisáceo", "Negras marron oscuro grisáceas")
    leopardo.mostrar_información()

