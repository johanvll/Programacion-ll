import java.awt.*;

public class Circulo {
    Punto centro;
    int radio;

    public Circulo(Punto centro, int radio) {
        this.centro = centro;
        this.radio = radio;
    }

    public void dibujaCirculo(Graphics g) {
        g.drawOval(centro.x - radio, centro.y - radio, 2 * radio, 2 * radio);
    }
}
