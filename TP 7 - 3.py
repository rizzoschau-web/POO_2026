from abc import ABC, abstractmethod


class ICalculable(ABC):

    @abstractmethod
    def calcular_costo(self, peso):
        pass


class IRastreable(ABC):

    @abstractmethod
    def rastrear_paquete_satelital(self):
        pass


class IExportable(ABC):

    @abstractmethod
    def generar_reporte_aduana(self):
        pass


class CorreoLocalOCA(ICalculable):

    def calcular_costo(self, peso):
        return peso * 15.0


class FedEx(ICalculable, IRastreable, IExportable):

    def calcular_costo(self, peso):
        return (peso * 50.0) + 100.0

    def rastrear_paquete_satelital(self):
        return "Paquete rastreado por satélite"

    def generar_reporte_aduana(self):
        print("Reporte de aduana generado")


class Andreani(ICalculable):

    def calcular_costo(self, peso):
        return peso * 20.0

class CalculadoraEnvios:

    def obtener_costo(self, correo, peso):
        return correo.calcular_costo(peso)


calculadora = CalculadoraEnvios()

oca = CorreoLocalOCA()
fedex = FedEx()
andreani = Andreani()

print("Cálculo de costos de envío")

print("OCA:", calculadora.obtener_costo(oca, 10))
print("FedEx:", calculadora.obtener_costo(fedex, 10))
print("Andreani:", calculadora.obtener_costo(andreani, 10))

print()

print("Operaciones de FedEx:")
print(fedex.rastrear_paquete_satelital())
fedex.generar_reporte_aduana()