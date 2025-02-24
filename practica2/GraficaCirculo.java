import javax.swing.*;
import java.awt.*;

public class GraficaCirculo extends JPanel {
    Circulo circulo;

    public GraficaCirculo() {

        Punto centro = new Punto(300, 150);
        circulo = new Circulo(centro, 50);
    }


    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        g.drawLine(getWidth() / 2, 0, getWidth() / 2, getHeight());
        g.drawLine(0, getHeight() / 2, getWidth(), getHeight() / 2);


        g.setColor(Color.RED);
        circulo.dibujaCirculo(g);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Dibujar Círculo");
        GraficaCirculo panel = new GraficaCirculo();

        frame.add(panel);
        frame.setSize(600, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
