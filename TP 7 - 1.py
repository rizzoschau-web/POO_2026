import sqlite3
#codigo ya arreglado por la IA
class Factura:
    """Responsabilidad única: representar los datos y la lógica de cálculo de una factura."""

    DESCUENTOS = {
        "VIP": 0.20,
        "REGULAR": 0.10,
    }

    def __init__(self, nombre_cliente: str, monto_base: float, tipo_cliente: str):
        self.nombre_cliente = nombre_cliente
        self.monto_base = monto_base
        self.tipo_cliente = tipo_cliente

    def calcular_total(self) -> float:
        porcentaje_descuento = self.DESCUENTOS.get(self.tipo_cliente, 0.0)
        descuento = self.monto_base * porcentaje_descuento
        return self.monto_base - descuento


class RepositorioFacturas:
    """Responsabilidad única: persistir facturas en la base de datos."""

    def __init__(self, ruta_db: str = "mi_empresa.db"):
        self.ruta_db = ruta_db

    def guardar(self, factura: Factura, total: float) -> None:
        try:
            with sqlite3.connect(self.ruta_db) as conexion:
                cursor = conexion.cursor()
                query = "INSERT INTO facturas (cliente, total) VALUES (?, ?)"
                cursor.execute(query, (factura.nombre_cliente, total))
                conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al guardar en la base de datos: {e}")


class ImpresoraFacturas:
    """Responsabilidad única: presentar la factura al usuario."""

    def imprimir(self, factura: Factura, total: float) -> None:
        print(f"FACTURA: {factura.nombre_cliente} | Total: ${total:.2f}")


class ServicioFacturacion:
    """Orquesta el proceso completo, delegando cada tarea a la clase responsable."""

    def __init__(self, repositorio: RepositorioFacturas, impresora: ImpresoraFacturas):
        self.repositorio = repositorio
        self.impresora = impresora

    def procesar(self, factura: Factura) -> None:
        total = factura.calcular_total()
        self.repositorio.guardar(factura, total)
        self.impresora.imprimir(factura, total)


# Uso
if __name__ == "__main__":
    factura = Factura("Juan Pérez", 1000.0, "VIP")
    servicio = ServicioFacturacion(RepositorioFacturas(), ImpresoraFacturas())
    servicio.procesar(factura)