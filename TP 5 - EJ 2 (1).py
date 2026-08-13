import math
from abc import ABC, abstractmethod

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class ElementoGrafico(ABC):
    def __init__(self, colorHex, posicionCentro, nombreCapa):
        self.colorHex = colorHex
        self.posicionCentro = posicionCentro
        self.nombreCapa = nombreCapa

    def moverA(self, nuevoDestino):
        self.posicionCentro = nuevoDestino

    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass

    def __str__(self):
        return (f"ElementoGrafico[color={self.colorHex}, "
                f"centro={self.posicionCentro}, capa={self.nombreCapa}]")

class Rectangulo(ElementoGrafico):
    def __init__(self, colorHex, posicionCentro, nombreCapa, ladoMenor, ladoMayor):
        super().__init__(colorHex, posicionCentro, nombreCapa)
        self.ladoMenor = ladoMenor
        self.ladoMayor = ladoMayor

    def calcularArea(self):
        return self.ladoMenor * self.ladoMayor

    def calcularPerimetro(self):
        return 2 * (self.ladoMenor + self.ladoMayor)

    def escalar(self, factor):
        if factor <= 0:
            print("Factor invalido: debe ser mayor a 0. No se escala.")
            return
        self.ladoMenor *= factor
        self.ladoMayor *= factor

    def __str__(self):
        return (super().__str__() +
                f" -> Rectangulo[ladoMenor={self.ladoMenor}, "
                f"ladoMayor={self.ladoMayor}, area={self.calcularArea()}, "
                f"perimetro={self.calcularPerimetro()}]")

class Elipse(ElementoGrafico):
    def __init__(self, colorHex, posicionCentro, nombreCapa, radioMayor, radioMenor):
        super().__init__(colorHex, posicionCentro, nombreCapa)
        self.radioMayor = radioMayor  # R
        self.radioMenor = radioMenor  # r

    def calcularArea(self):
        return math.pi * self.radioMayor * self.radioMenor

    def calcularPerimetro(self):
        a = self.radioMayor
        b = self.radioMenor
        h = ((a - b) ** 2) / ((a + b) ** 2)
        return math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

    def escalar(self, factor):
        if factor <= 0:
            print("Factor invalido: debe ser mayor a 0. No se escala.")
            return
        self.radioMayor *= factor
        self.radioMenor *= factor

    def __str__(self):
        return (super().__str__() +
                f" -> Elipse[radioMayor={self.radioMayor}, "
                f"radioMenor={self.radioMenor}, area={self.calcularArea():.2f}, "
                f"perimetro={self.calcularPerimetro():.2f}]")
    
class Cuadrado(Rectangulo):
    def __init__(self, colorHex, posicionCentro, nombreCapa, lado):
        super().__init__(colorHex, posicionCentro, nombreCapa, lado, lado)

    def setLadoMenor(self, valor):
        self.ladoMenor = valor
        self.ladoMayor = valor

    def setLadoMayor(self, valor):
        self.ladoMenor = valor
        self.ladoMayor = valor

    def setLado(self, valor):
        self.ladoMenor = valor
        self.ladoMayor = valor

    def __str__(self):
        return super().__str__().replace("Rectangulo", "Cuadrado")  
    
class Circulo(Elipse):

    def __init__(self, colorHex, posicionCentro, nombreCapa, radio):

        super().__init__(
            colorHex,
            posicionCentro,
            nombreCapa,
            radio,
            radio
        )

    def setRadioMayor(self, radio):
        self.radioMayor = radio
        self.radioMenor = radio

    def setRadioMenor(self, radio):
        self.radioMenor = radio
        self.radioMayor = radio

    def __str__(self):
        return super().__str__()

class Triangulo(ElementoGrafico):

    def __init__(self, colorHex, posicionCentro, nombreCapa, base, altura, lado1, lado2):

        super().__init__(
            colorHex,
            posicionCentro,
            nombreCapa
        )

        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcularArea(self):
        return (self.base * self.altura) / 2

    def calcularPerimetro(self):
        return self.base + self.lado1 + self.lado2    

    def __str__(self):
        return (
        super().__str__() +
        f" -> Triangulo[base={self.base}, altura={self.altura}, "
        f"area={self.calcularArea():.2f}, "
        f"perimetro={self.calcularPerimetro():.2f}]"
        )
class Lienzo:

    def __init__(self):
        self.elementos = []

    def agregarElemento(self, elemento):
        self.elementos.append(elemento)

    def mostrarElementos(self):
        for elemento in self.elementos:
            print(elemento)
            
def main():

    lienzo = Lienzo()

    rectangulo = Rectangulo(
        "#FF0000",
        Punto(10, 20),
        "Capa 1",
        5,
        10
    )

    elipse = Elipse(
        "#00FF00",
        Punto(30, 40),
        "Capa 2",
        8,
        4
    )

    cuadrado = Cuadrado(
        "#0000FF",
        Punto(50, 60),
        "Capa 3",
        10
    )

    circulo = Circulo(
        "#FFFF00",
        Punto(70, 80),
        "Capa 4",
        5
    )

    lienzo.agregarElemento(rectangulo)
    lienzo.agregarElemento(elipse)
    lienzo.agregarElemento(cuadrado)
    lienzo.agregarElemento(circulo)

    print("ELEMENTOS ANTES DE MODIFICAR:")
    lienzo.mostrarElementos()

    print()

    for elemento in lienzo.elementos:

        elemento.colorHex = "#808080"
        elemento.moverA(Punto(0, 0))

    print("ELEMENTOS DESPUÉS DE MODIFICAR:")
    lienzo.mostrarElementos()

    print()

    areaTotal = 0

    for elemento in lienzo.elementos:

        areaTotal += elemento.calcularArea()

    print("Área total:", areaTotal)

#despues de aplicar abstraccion y polimorfismo probamos con el ejemplo del traingulo 
    
    triangulo = Triangulo(
        "#FF00FF",
        Punto(90, 100),
        "Capa 5",
        10,
        8,
        6,
        7
    )

    lienzo.agregarElemento(triangulo)

    print("ELEMENTOS DESPUÉS DE AGREGAR EL TRIANGULO:")
    lienzo.mostrarElementos()

    areaTotal = 0
    
    for elemento in lienzo.elementos:
    
        areaTotal += elemento.calcularArea()
    
    print("Área total:", areaTotal)

main()
