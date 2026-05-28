Entero.java
public class Entero {

    private int numero;

    public Entero(int numero) {
        this.numero = numero;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public long cuadrado() {
        return (long) numero * numero;
    }

    public boolean esPar() {
        return numero % 2 == 0;
    }

    public boolean esImpar() {
        return numero % 2 != 0;
    }

    public long factorial() {
        if (numero < 0) {
            return -1;
        }
        long resultado = 1;
        for (int i = 2; i <= numero; i++) {
            resultado *= i;
        }
        return resultado;
    }

    public boolean esPrimo() {
        if (numero < 2) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(numero); i++) {
            if (numero % i == 0) {
                return false;
            }
        }
        return true;
    }
}
Main.java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("========================================");
        System.out.println("       PRUEBA DE LA CLASE Entero        ");
        System.out.println("========================================");

        // ── Número ingresado por el usuario ──────────────────────
        System.out.print("Ingrese un número entero: ");
        int valor = scanner.nextInt();
        Entero e = new Entero(valor);

        mostrarResultados(e);

        // ── Prueba de setNumero() con un segundo valor ────────────
        System.out.println("\n========================================");
        System.out.print("Ingrese otro número para probar setNumero(): ");
        int otroValor = scanner.nextInt();
        e.setNumero(otroValor);
        System.out.println("\n--- Resultados con el nuevo número: " + e.getNumero() + " ---");
        mostrarResultados(e);

        // ── Casos borde hardcodeados ──────────────────────────────
        int[] casosBorde = { -5, 0, 1 };
        for (int cb : casosBorde) {
            System.out.println("\n========================================");
            System.out.println("--- Prueba con número: " + cb + " ---");
            Entero aux = new Entero(cb);
            mostrarResultados(aux);
        }

        System.out.println("\n========================================");
        System.out.println("           FIN DE LAS PRUEBAS          ");
        System.out.println("========================================");

        scanner.close();
    }

    // Método auxiliar: centraliza la impresión para no repetir código
    private static void mostrarResultados(Entero e) {
        System.out.println("Número:    " + e.getNumero());
        System.out.println("Cuadrado:  " + e.cuadrado());
        System.out.println("¿Es par?   " + (e.esPar()   ? "Sí" : "No"));
        System.out.println("¿Es impar? " + (e.esImpar() ? "Sí" : "No"));

        long fact = e.factorial();
        if (fact == -1) {
            System.out.println("Factorial: No definido para números negativos.");
        } else {
            System.out.println("Factorial: " + fact);
        }

        System.out.println("¿Es primo? " + (e.esPrimo() ? "Sí" : "No"));
    }
}


---
========================================
       PRUEBA DE LA CLASE Entero
========================================
Ingrese un número entero: 7
Número:    7
Cuadrado:  49
¿Es par?   No
¿Es impar? Sí
Factorial: 5040
¿Es primo? Sí

========================================
Ingrese otro número para probar setNumero(): 12
--- Resultados con el nuevo número: 12 ---
Número:    12
Cuadrado:  144
¿Es par?   Sí
¿Es impar? No
Factorial: 479001600
¿Es primo? No

========================================
--- Prueba con número: -5 ---
Número:    -5
Cuadrado:  25
¿Es par?   No
¿Es impar? Sí
Factorial: No definido para números negativos.
¿Es primo? No

========================================
--- Prueba con número: 0 ---
Número:    0
Cuadrado:  0
¿Es par?   Sí
¿Es impar? No
Factorial: 1
¿Es primo? No

========================================
--- Prueba con número: 1 ---
Número:    1
Cuadrado:  1
¿Es par?   No
¿Es impar? Sí
Factorial: 1
¿Es primo? No

========================================
           FIN DE LAS PRUEBAS
========================================




