class Zoologico:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)
        print(f"{animal.nombre} agregado al zoológico.")

    def eliminar_animal(self, nombre):
        self.animales = [animal for animal in self.animales if animal.nombre != nombre]
        print(f"{nombre} eliminado del zoológico.")

    def listar_animales(self):
        print('-------------------')
        
        for animal in self.animales:
            animal.mostrar_informacion()
            print('-------------------')

