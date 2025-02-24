import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        String opcion = JOptionPane.showInputDialog("Escriba 'linea' o 'circulo' para dibujar:");

        if (opcion.equalsIgnoreCase("linea")) {
            SwingUtilities.invokeLater(() -> {
                JFrame frame = new JFrame("Dibujar Línea");
                frame.add(new GraficaLinea());
                frame.setSize(600, 400);
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                frame.setVisible(true);
            });
        } else if (opcion.equalsIgnoreCase("circulo")) {
            SwingUtilities.invokeLater(() -> {
                JFrame frame = new JFrame("Dibujar Círculo");
                frame.add(new GraficaCirculo());
                frame.setSize(600, 400);
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                frame.setVisible(true);
            });
        } else {
            JOptionPane.showMessageDialog(null, "Opción no válida. Escriba 'linea' o 'circulo'.");
        }
    }
}
