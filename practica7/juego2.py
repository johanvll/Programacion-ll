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
        print("Record:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas > 0:
            print(f"Te quedan {self.numeroDeVidas} vidas.")
            return True
        else:
            print("¡No te quedan vidas!")
            return False

class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAdivinar = None

    def validaNumero(self, numero):
        return 0 <= numero <= 10

    def juega(self):
        self.reiniciaPartida()
        self.numeroAdivinar = random.randint(0, 10)
        print("\n*** Juego Adivina Número ***")
        print("Adivina un número entre 0 y 10.")
        
        while True:
            try:
                numero_usuario = int(input("Introduce un número: "))
            except ValueError:
                print("Ingresa un número válido.")
                continue

            if not self.validaNumero(numero_usuario):
                print("Error: el número debe estar entre 0 y 10.")
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

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if not (0 <= numero <= 10):
            return False
        if numero % 2 != 0:
            print("Error: el número debe ser par.")
            return False
        return True

    def juega(self):
        self.reiniciaPartida()
        self.numeroAdivinar = random.choice([n for n in range(0, 11) if n % 2 == 0])
        print("\n*** Juego Adivina Número Par ***")
        print("Adivina un número par entre 0 y 10.")
        
        while True:
            try:
                numero_usuario = int(input("Introduce un número: "))
            except ValueError:
                print("Ingresa un número válido.")
                continue

            if not self.validaNumero(numero_usuario):
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

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if not (0 <= numero <= 10):
            return False
        if numero % 2 == 0:
            print("Error: el número debe ser impar.")
            return False
        return True

    def juega(self):
        self.reiniciaPartida()
        self.numeroAdivinar = random.choice([n for n in range(0, 11) if n % 2 != 0])
        print("\n*** Juego Adivina Número Impar ***")
        print("Adivina un número impar entre 0 y 10.")
        
        while True:
            try:
                numero_usuario = int(input("Introduce un número: "))
            except ValueError:
                print("Ingresa un número válido.")
                continue

            if not self.validaNumero(numero_usuario):
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
    print("Juego de adivinanza básico:")
    juegoNormal = JuegoAdivinaNumero(3)
    juegoNormal.juega()

    print("\nJuego de adivinanza (números pares):")
    juegoPar = JuegoAdivinaPar(3)
    juegoPar.juega()

    print("\nJuego de adivinanza (números impares):")
    juegoImpar = JuegoAdivinaImpar(3)
    juegoImpar.juega()

if __name__ == "__main__":
    main()
