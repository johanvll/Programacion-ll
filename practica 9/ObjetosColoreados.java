import java.util.Random;

interface Coloreado {
    String comoColorear();
}

abstract class Figura {
    protected String color;

    public Figura(String color) {
        this.color = color;
    }

    public abstract double area();
    public abstract double perimetro();
    public String getColor() {
        return color;
    }
    public void setColor(String color) {
        this.color = color;
    }
}

class Cuadrado extends Figura implements Coloreado {
    private double lado;

    public Cuadrado(double lado, String color) {
        super(color);
        this.lado = lado;
    }

    @Override
    public double area() {
        return lado * lado;
    }

    @Override
    public double perimetro() {
        return 4 * lado;
    }

    @Override
    public String comoColorear() {
        return "Colorear los cuatro lados";
    }

    @Override
    public String toString() {
        return "Cuadrado de lado " + lado + " y color " + color;
    }
}

class Circulo extends Figura {
    private double radio;

    public Circulo(double radio, String color) {
        super(color);
        this.radio = radio;
    }

    @Override
    public double area() {
        return Math.PI * radio * radio;
    }

    @Override
    public double perimetro() {
        return 2 * Math.PI * radio;
    }

    @Override
    public String toString() {
        return "Círculo de radio " + radio + " y color " + color;
    }
}

public class ObjetosColoreados {
    public static void main(String[] args) {
        String[] colores = {"rojo", "azul", "verde", "amarillo", "negro"};
        Figura[] figuras = new Figura[5];
        Random r = new Random();

        for (int i = 0; i < figuras.length; i++) {
            String color = colores[r.nextInt(colores.length)];
            if (r.nextBoolean()) {
                double lado = 1 + r.nextDouble() * 9;
                figuras[i] = new Cuadrado(lado, color);
            } else {
                double radio = 1 + r.nextDouble() * 9;
                figuras[i] = new Circulo(radio, color);
            }
        }

        for (int i = 0; i < figuras.length; i++) {
            System.out.println("Figura " + (i + 1) + ": " + figuras[i]);
            System.out.printf("Área: %.2f", figuras[i].area());
            System.out.printf("Perímetro: %.2f", figuras[i].perimetro());

            if (figuras[i] instanceof Coloreado) {
                System.out.println("Cómo colorear: " + ((Coloreado) figuras[i]).comoColorear());
            }
        }
    }
}
