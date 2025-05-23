# Proyecto calculadora de notas escolares
# Autor: Edwin Hernan Gil Rodriguez
# Fecha: 2025-05-23 
'''Este programa permite calcular la nota final de un estudiante en una evaluacion, donde el usuario establecera
el numero de preguntas de la evaluacion y luego ingresara el numero de aciertos para calcular su nota en una escala de 0'''

import tkinter as tk
from tkinter import messagebox

class CalculadoraNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Notas Escolares - Edwin Gil")
        self.num_preguntas = None
        self.setup_num_preguntas()

    def setup_num_preguntas(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        label = tk.Label(self.root, text="Ingrese el número de preguntas del examen:")
        label.pack(pady=10)
        self.entry_preguntas = tk.Entry(self.root)
        self.entry_preguntas.pack(pady=5)
        btn = tk.Button(self.root, text="Continuar", command=self.guardar_num_preguntas)
        btn.pack(pady=10)

    def guardar_num_preguntas(self):
        try:
            num = int(self.entry_preguntas.get())
            if num <= 0:
                raise ValueError
            self.num_preguntas = num
            self.setup_num_aciertos()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido de preguntas.")

    def setup_num_aciertos(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        label = tk.Label(self.root, text=f"Ingrese el número de respuestas correctas (0 a {self.num_preguntas}):")
        label.pack(pady=10)
        self.entry_aciertos = tk.Entry(self.root)
        self.entry_aciertos.pack(pady=5)
        btn = tk.Button(self.root, text="Calcular Nota", command=self.calcular_nota)
        btn.pack(pady=10)

    def calcular_nota(self):
        try:
            aciertos = int(self.entry_aciertos.get())
            if not (0 <= aciertos <= self.num_preguntas):
                raise ValueError
            nota = (aciertos / self.num_preguntas) * 5.0
            messagebox.showinfo("Resultado", f"La calificación es: {nota:.2f}")
            self.setup_num_preguntas()
        except ValueError:
            messagebox.showerror("Error", f"Ingrese un número de aciertos válido (0 a {self.num_preguntas}).")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraNotas(root)
    root.mainloop()

