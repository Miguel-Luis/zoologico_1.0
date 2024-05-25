from animal import Animal

class Ave(Animal):
    def __init__(self,nombre,edad,habitat,altura,color):
        super().__init__(nombre, edad, habitat)
        self.altura = altura
        self.color = color
        
    def mostrar_informacion(self):
        atributos_ave= {
            "nombre":self.nombre,
            "edad":self.edad,
            "habitat":self.habitat,
            "altura":self.altura,
            "color":self.color
        }
            
        super().mostrar_informacion(atributos_ave)
        
avestruz= Ave('aveztruz',6,'Africa','1m','negro')
avestruz.mostrar_informacion()