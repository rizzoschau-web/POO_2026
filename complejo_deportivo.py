# ============================================================
#  COMPLEJO DEPORTIVO - Sistema de Reservas
#  Ejercicio 4: Caso de Estudio Integrador
# ============================================================

# ----------------------------------------------------------------
# CLASE: Turno
# Responsabilidad: Almacenar datos de una reserva (hora + nombre).
# ----------------------------------------------------------------
class Turno:
    def __init__(self, hora, nombre_persona):
        self.__hora = hora
        self.__nombre_persona = nombre_persona

    def get_hora(self):
        return self.__hora

    def get_nombre_persona(self):
        return self.__nombre_persona


# ----------------------------------------------------------------
# CLASE: Cancha
# Responsabilidad: Gestionar la lista de turnos de una cancha.
#   - NO imprime ni lee por consola.
#   - reservarTurno retorna True/False.
# ----------------------------------------------------------------
class Cancha:
    HORA_APERTURA  = 14
    HORA_CIERRE    = 23   # 23:00 es el último turno válido

    def __init__(self, numero):
        self.__numero  = numero
        self.__turnos  = []          # lista de objetos Turno

    def get_numero(self):
        return self.__numero

    def get_turnos(self):
        return list(self.__turnos)   # copia defensiva

    # Valida que la hora sea entera, en punto y dentro del rango.
    def hora_valida(self, hora):
        return (
            isinstance(hora, int)
            and self.HORA_APERTURA <= hora <= self.HORA_CIERRE
        )

    # Devuelve True si se reservó, False si la hora ya está ocupada.
    def reservar_turno(self, turno):
        for t in self.__turnos:
            if t.get_hora() == turno.get_hora():
                return False
        self.__turnos.append(turno)
        return True

    # Devuelve True si se canceló, False si no existía reserva a esa hora.
    def cancelar_turno(self, hora):
        for i, t in enumerate(self.__turnos):
            if t.get_hora() == hora:
                self.__turnos.pop(i)
                return True
        return False

    # Devuelve lista de horas libres dentro del horario del complejo.
    def horas_libres(self):
        ocupadas = {t.get_hora() for t in self.__turnos}
        return [h for h in range(self.HORA_APERTURA, self.HORA_CIERRE + 1)
                if h not in ocupadas]


# ----------------------------------------------------------------
# CLASE: Main
# Responsabilidad: TODA la interacción con el usuario.
# ----------------------------------------------------------------
class Main:
    def __init__(self):
        self.__canchas = [Cancha(i) for i in range(1, 4)]   # 3 canchas

    # ---------- helpers de presentación ----------

    def __mostrar_estado(self):
        print("\n" + "=" * 50)
        print("       ESTADO ACTUAL DEL COMPLEJO")
        print("=" * 50)
        for cancha in self.__canchas:
            print(f"\n  Cancha {cancha.get_numero()}")
            print("  " + "-" * 30)

            # Ocupadas
            turnos = cancha.get_turnos()
            if turnos:
                print("  Ocupadas:")
                for t in sorted(turnos, key=lambda x: x.get_hora()):
                    print(f"    {t.get_hora():02d}:00  →  {t.get_nombre_persona()}")
            else:
                print("  Ocupadas: (ninguna)")

            # Libres
            libres = cancha.horas_libres()
            if libres:
                horas_str = "  ".join(f"{h:02d}:00" for h in libres)
                print(f"  Libres:   {horas_str}")
            else:
                print("  Libres:   (completa)")
        print("=" * 50)

    def __seleccionar_cancha(self):
        print("  Número de cancha (1 / 2 / 3): ", end="")
        try:
            n = int(input())
        except ValueError:
            return None
        if n in (1, 2, 3):
            return self.__canchas[n - 1]
        return None

    def __pedir_hora(self):
        print(f"  Hora (14 a 23, en punto): ", end="")
        try:
            return int(input())
        except ValueError:
            return -1

    # ---------- opciones del menú ----------

    def __registrar_reserva(self):
        print("\n--- NUEVA RESERVA ---")
        cancha = self.__seleccionar_cancha()
        if cancha is None:
            print("  Error: número de cancha inválido.")
            return

        hora = self.__pedir_hora()
        if not cancha.hora_valida(hora):
            print("  Error: hora fuera del horario permitido (14-23).")
            return

        print("  Nombre del responsable: ", end="")
        nombre = input().strip()
        if not nombre:
            print("  Error: el nombre no puede estar vacío.")
            return

        turno = Turno(hora, nombre)
        if cancha.reservar_turno(turno):
            print(f"  ✔ Reserva exitosa — Cancha {cancha.get_numero()} a las {hora:02d}:00.")
        else:
            print("  ✘ Error: Turno ocupado.")

    def __cancelar_reserva(self):
        print("\n--- CANCELAR RESERVA ---")
        cancha = self.__seleccionar_cancha()
        if cancha is None:
            print("  Error: número de cancha inválido.")
            return

        hora = self.__pedir_hora()
        if cancha.cancelar_turno(hora):
            print(f"  ✔ Reserva de las {hora:02d}:00 en Cancha {cancha.get_numero()} cancelada.")
        else:
            print(f"  ✘ No existe reserva a las {hora:02d}:00 en Cancha {cancha.get_numero()}.")

    # ---------- bucle principal ----------

    def ejecutar(self):
        print("\n╔══════════════════════════════════════════╗")
        print("║    COMPLEJO DEPORTIVO — Gestión Reservas ║")
        print("╚══════════════════════════════════════════╝")

        while True:
            print("\n  [1] Ver estado de las canchas")
            print("  [2] Registrar reserva")
            print("  [3] Cancelar reserva")
            print("  [0] Salir")
            print("  Opción: ", end="")

            opcion = input().strip()

            if opcion == "1":
                self.__mostrar_estado()
            elif opcion == "2":
                self.__registrar_reserva()
            elif opcion == "3":
                self.__cancelar_reserva()
            elif opcion == "0":
                print("\n  ¡Hasta luego!\n")
                break
            else:
                print("  Opción inválida. Intente nuevamente.")


# ----------------------------------------------------------------
# Punto de entrada
# ----------------------------------------------------------------
if __name__ == "__main__":
    app = Main()
    app.ejecutar()
