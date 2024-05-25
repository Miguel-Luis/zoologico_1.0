class Animal:
    def __init__(self, nombre, edad, habitat):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat

    def mostrar_información(self, atributos):
        for clave, valor in atributos.items():
            print(f"{clave}: {valor}")
