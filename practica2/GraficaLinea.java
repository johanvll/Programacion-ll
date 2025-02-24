import javax.swing.*;
import java.awt.*;

public class GraficaLinea extends JPanel {
    Linea linea;

    public GraficaLinea() {

        Punto p1 = new Punto(0, 0);
        Punto p2 = new Punto(5, 5);
        linea = new Linea(p1, p2);
    }


    protected void paintComponent(Graphics g) {
        super.paintComponent(g);


        g.drawLine(getWidth() / 2, 0, getWidth() / 2, getHeight());
        g.drawLine(0, getHeight() / 2, getWidth(), getHeight() / 2);


        g.setColor(Color.BLUE);
        linea.dibujaLinea(g);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Dibujar Línea");
        GraficaLinea panel = new GraficaLinea();

        frame.add(panel);
        frame.setSize(600, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
