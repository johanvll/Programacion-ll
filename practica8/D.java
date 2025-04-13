interface A {
    void muestraX();
}

interface B {
    void muestraY();
}

class D implements A, B {
    private int x, y, z;

    D(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public void muestraX() {
        System.out.println("Valor de x: " + x);
    }

    public void muestraY() {
        System.out.println("Valor de y: " + y);
    }

    public void muestraTodos() {
        muestraX();
        muestraY();
        System.out.println("Valor de z: " + z);
    }

    public static void main(String[] args) {
        D objetoD = new D(10, 20, 30);
        System.out.println("valores:");
        objetoD.muestraTodos();
    }
}
