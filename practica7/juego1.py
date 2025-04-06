import random

class Juego:
    def __init__(self, vidas):
        self.vidas_inicial = vidas
        self.numeroDeVidas = vidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidas_inicial

    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
        print("Record actualizado:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas > 0:
            print(f"Te quedan {self.numeroDeVidas} vidas.")
            return True
        else:
            print("No te quedan vidas")
            return False

class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAdivinar = None

    def juega(self):
        self.reiniciaPartida()
        self.numeroAdivinar = random.randint(0, 10)
        print("\n*** Juego Adivina Número ***")
        print("Adivina un número entre 0 y 10.")
        
        while True:
            try:
                numero_usuario = int(input("Introduce un número: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            if numero_usuario == self.numeroAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if not self.quitaVida():
                    print("El número a adivinar era:", self.numeroAdivinar)
                    break
                if numero_usuario < self.numeroAdivinar:
                    print("El número a adivinar es mayor.")
                else:
                    print("El número a adivinar es menor.")
                print("Inténtalo de nuevo.")

def main():
    juego = JuegoAdivinaNumero(3)
    juego.juega()

if __name__ == "__main__":
    main()
