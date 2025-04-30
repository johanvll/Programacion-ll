import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod

class Boleto(ABC):
    def __init__(self, numero):
        self.numero = numero

    @abstractmethod
    def calcular_precio(self):
        pass

    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.calcular_precio()}"

class Palco(Boleto):
    def calcular_precio(self):
        return 100.0

class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias_anticipacion = dias_anticipacion

    def calcular_precio(self):
        return 50.0 if self.dias_anticipacion >= 10 else 60.0

class Galeria(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias_anticipacion = dias_anticipacion

    def calcular_precio(self):
        return 25.0 if self.dias_anticipacion >= 10 else 30.0

def vender_boleto():
    numero = int(numero_entry.get())
    tipo = tipo_combo.get()
    dias = int(dias_entry.get()) if dias_entry.get() else 0

    if tipo == "Palco":
        boleto = Palco(numero)
    elif tipo == "Platea":
        boleto = Platea(numero, dias)
    else:
        boleto = Galeria(numero, dias)

    info_label.config(text=str(boleto))

root = tk.Tk()
root.title("Teatro Municipal")

tk.Label(root, text="Número de Boleto:").grid(row=0, column=0)
numero_entry = tk.Entry(root)
numero_entry.grid(row=0, column=1)

tk.Label(root, text="Tipo de Boleto:").grid(row=1, column=0)
tipo_combo = ttk.Combobox(root, values=["Palco", "Platea", "Galería"])
tipo_combo.grid(row=1, column=1)
tipo_combo.current(0)

tk.Label(root, text="Días para el Evento:").grid(row=2, column=0)
dias_entry = tk.Entry(root)
dias_entry.grid(row=2, column=1)

vende_button = tk.Button(root, text="Vende", command=vender_boleto)
vende_button.grid(row=3, column=0)

salir_button = tk.Button(root, text="Salir", command=root.quit)
salir_button.grid(row=3, column=1)

info_label = tk.Label(root, text="Información:")
info_label.grid(row=4, columnspan=2)

root.mainloop()
