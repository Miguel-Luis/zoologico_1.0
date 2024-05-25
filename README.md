
# Proyecto Zoológico

El objetivo de este proyecto es diseñar y desarrollar un sistema de gestión de un zoológico utilizando los principios de la programación orientada a objetos **(POO)** en Python. Este ejercicio los ayudara a comprender cómo crear clases, herencia y la interacción entre múltiples objetos. Además les permitira practicar un flujo de trabajo en GitHub con un equipo de desarrollo.

## Descripción de Archivos
![Clonar](https://github.com/Miguel-Luis/zoologico_1.0/assets/34074599/797d3d4c-e01c-427b-bd43-29c4db9f7b47)

### `zoologico_1.0/`

- **`main.py`**: Actúa como el punto de inicio del programa. Cuando se ejecuta el programa, este archivo es el que inicia todo el proceso.
- **`zoologico.py`**: El objetivo de este archivo es definir una clase Zoologico que maneja una colección de animales, permitiendo agregar, eliminar y listar animales.


### `zoologico_1.0/animales/`

- **`__init__.py`**: Archivo de inicialización del paquete `materiales`.
- **`animal.py`**: El objetivo de esta clase es proporcionar una estructura básica para representar un animal con algunos atributos esenciales como nombre, edad, y habitat, y permitir que esta información se pueda mostrar fácilmente.
- **`mamifero.py`**: Clase que representa un mamifero.
- **`ave.py`**: Clase que representa una ave.
- **`reptil.py`**: Clase que representa un reptil.
- **`anfibio.py`**: Clase que representa un anfibio.
- **`pez.py`**: Clase que representa un pez.
- **`insecto.py`**: Clase que representa un insecto.


## Instrucciones para el Desarrollo de la Lógica de Animales en el Zoológico
Se seleccionarán parejas de trabajo encargadas de desarrollar la lógica que representará a cada tipo de animal dentro del proyecto. A continuación, se detallan los requisitos y pasos a seguir para asegurar una implementación coherente y funcional.

### Requisitos Generales
#### 1. Herencia de la Clase Animal:
- Cada tipo de animal deberá ser representado por una clase específica que herede de la clase base Animal. Esto asegura que todos los animales compartan atributos y métodos comunes, facilitando la gestión dentro del zoológico.

#### 2. Atributos Específicos de Cada Especie:
- Además de los atributos heredados de la clase Animal, cada clase específica de animal deberá incluir atributos propios que representen características particulares de la especie. Los equipos tienen libertad para agregar tantos atributos como consideren necesarios para describir adecuadamente a cada tipo de animal.

#### 3. Método mostrar_informacion:
- Cada clase específica de animal debe definir un método llamado mostrar_informacion. Dentro de este método, se deberá crear un diccionario que contenga todos los atributos de la clase, utilizando pares clave-valor.
- Al finalizar la definición del diccionario de atributos, el método debe llamar al método mostrar_informacion de la superclase (Animal) para asegurar que la información base también sea mostrada correctamente.

#### Ejemplo de Uso en main.py:
```python
from animales.mamifero import Mamifero

if __name__ == "__main__":
    leon = Mamifero("León", 5, "Sabana", "Espeso")
    leon.mostrar_informacion()
```
#### Puntos Clave:
- **Herencia y Superclase:**
    - Asegúrese de que cada nueva clase específica de animal herede correctamente de Animal.
    - Use super().__init__(...) para inicializar los atributos de la superclase.

- **Método mostrar_informacion:**
    - Cree un diccionario en el método mostrar_informacion de cada clase específica que contenga todos los atributos con sus correspondientes pares clave-valor.
    - Llame al método mostrar_informacion de la superclase al final para incluir la información base.

- **Instanciación y Funcionamiento Correcto:**
    - Al instanciar objetos de estas clases en main.py y llamar a su método mostrar_informacion, se debe asegurar que toda la información relevante de cada animal se muestre correctamente.

> [!NOTE]
> Siguiendo estas instrucciones, se logrará una implementación estructurada y coherente de las diferentes especies de animales dentro del proyecto del zoológico, permitiendo una fácil expansión y mantenimiento del código.
