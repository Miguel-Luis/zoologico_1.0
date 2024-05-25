from animal import Animal

class  Anfibio(Animal):
    def __init__(self, name, edad, habitat, especie, alimentacion):
        super().__init__(name, edad, habitat)
        self.especie = especie
        self.alimentacion = alimentacion

    def mostrar_informacion(self):
        dict_anfibios = {
        'nombre': self.nombre,
        'edad':self.edad,
        'especie':self.especie ,
        'habitat': self.habitat,
        'alimentacion':self.alimentacion
}

        super().mostrar_informacion(dict_anfibios)

Rana = Anfibio('Martica', 5, 'lago', 'anfibio', 'moscas')
Rana.mostrar_informacion()