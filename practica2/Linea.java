import java.awt.*;

public class Linea {
    Punto p1, p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public void dibujaLinea(Graphics g) {
        g.drawLine(p1.x, p1.y, p2.x, p2.y);
    }
}
