from abc import ABC, abstractmethod
#codigo corregido por la ia
class Correo(ABC):
    """Clase abstracta que define el contrato que todo correo debe cumplir."""

    @abstractmethod
    def calcular_costo(self, peso: float) -> float:
        pass


class OCA(Correo):
    def calcular_costo(self, peso: float) -> float:
        return peso * 15.0


class FedEx(Correo):
    def calcular_costo(self, peso: float) -> float:
        return (peso * 50.0) + 100.0  # Costo + aduana


class Andreani(Correo):
    def calcular_costo(self, peso: float) -> float:
        return peso * 20.0


# --- Extensión futura: agregar un nuevo correo NO requiere tocar nada existente ---
class DHL(Correo):
    def calcular_costo(self, peso: float) -> float:
        return (peso * 45.0) + 80.0  # Ejemplo de nueva regla propia de DHL


class CalculadoraEnvios:
    """Ya no conoce ningún tipo de correo en particular: solo sabe delegar."""

    def obtener_costo(self, correo: Correo, peso: float) -> float:
        return correo.calcular_costo(peso)


# Uso
if __name__ == "__main__":
    calculadora = CalculadoraEnvios()

    print(calculadora.obtener_costo(OCA(), 10))       # 150.0
    print(calculadora.obtener_costo(FedEx(), 10))     # 600.0
    print(calculadora.obtener_costo(Andreani(), 10))  # 200.0
    print(calculadora.obtener_costo(DHL(), 10))       # 530.0