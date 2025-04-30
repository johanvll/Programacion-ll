import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

abstract class Boleto {
    protected int numero;

    public Boleto(int numero) {
        this.numero = numero;
    }

    public abstract double calcularPrecio();

    @Override
    public String toString() {
        return "<html><strong>Número:</strong> " + numero + ", <strong>Precio:</strong> " + calcularPrecio() + "</html>";
    }
}

class Palco extends Boleto {
    public Palco(int numero) {
        super(numero);
    }

    @Override
    public double calcularPrecio() {
        return 100.0;
    }
}

class Platea extends Boleto {
    private int diasAnticipacion;

    public Platea(int numero, int diasAnticipacion) {
        super(numero);
        this.diasAnticipacion = diasAnticipacion;
    }

    @Override
    public double calcularPrecio() {
        return diasAnticipacion >= 10 ? 50.0 : 60.0;
    }
}

class Galeria extends Boleto {
    private int diasAnticipacion;

    public Galeria(int numero, int diasAnticipacion) {
        super(numero);
        this.diasAnticipacion = diasAnticipacion;
    }

    @Override
    public double calcularPrecio() {
        return diasAnticipacion >= 10 ? 25.0 : 30.0;
    }
}

public class TeatroMunicipalGUI extends JFrame {
    private JTextField numeroField, diasField;
    private JComboBox<String> tipoBox;
    private JLabel infoLabel;

    public TeatroMunicipalGUI() {
        setTitle("Teatro Municipal");
        setSize(420, 300);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        setLocationRelativeTo(null);

        try {
            UIManager.setLookAndFeel("com.formdev.flatlaf.FlatDarkLaf"); // Tema moderno
        } catch (Exception e) {
            e.printStackTrace();
        }

        JPanel panel = new JPanel(new GridLayout(5, 2, 10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

        panel.add(new JLabel("Número de Boleto:"));
        numeroField = new JTextField();
        panel.add(numeroField);

        panel.add(new JLabel("Tipo de Boleto:"));
        String[] tipos = {"Palco", "Platea", "Galería"};
        tipoBox = new JComboBox<>(tipos);
        panel.add(tipoBox);

        panel.add(new JLabel("Días para el Evento:"));
        diasField = new JTextField();
        panel.add(diasField);

        JButton vendeButton = new JButton("Vender");
        vendeButton.addActionListener(e -> venderBoleto());
        panel.add(vendeButton);

        JButton salirButton = new JButton("Salir");
        salirButton.addActionListener(e -> System.exit(0));
        panel.add(salirButton);

        infoLabel = new JLabel("Información:");
        infoLabel.setHorizontalAlignment(SwingConstants.CENTER);

        add(panel, BorderLayout.CENTER);
        add(infoLabel, BorderLayout.SOUTH);

        setVisible(true);
    }

    private void venderBoleto() {
        int numero = Integer.parseInt(numeroField.getText());
        String tipo = (String) tipoBox.getSelectedItem();
        int dias = diasField.getText().isEmpty() ? 0 : Integer.parseInt(diasField.getText());

        Boleto boleto;
        if ("Palco".equals(tipo)) {
            boleto = new Palco(numero);
        } else if ("Platea".equals(tipo)) {
            boleto = new Platea(numero, dias);
        } else {
            boleto = new Galeria(numero, dias);
        }

        infoLabel.setText(boleto.toString());
    }

    public static void main(String[] args) {
        new TeatroMunicipalGUI();
    }
}
