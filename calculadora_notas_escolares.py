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
        self.root.geometry("400x350")
        self.root.configure(bg="#f5f6fa")
        self.num_preguntas = None
        self.setup_main_ui()

    def setup_main_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.label_info = tk.Label(self.root, text="Configure el número de preguntas antes de calcular la nota.",
                                   font=("Segoe UI", 14, "bold"), bg="#f5f6fa", fg="#273c75")
        self.label_info.pack(pady=18)
        self.btn_config = tk.Button(self.root, text="Configurar número de preguntas", command=self.setup_num_preguntas,
                                    font=("Segoe UI", 12), bg="#00a8ff", fg="white", activebackground="#0097e6", relief="flat", cursor="hand2")
        self.btn_config.pack(pady=8)
        self.label_preguntas = tk.Label(self.root, text="Número de preguntas: No configurado",
                                        font=("Segoe UI", 12), bg="#f5f6fa", fg="#353b48")
        self.label_preguntas.pack(pady=6)
        self.label_aciertos = tk.Label(self.root, text="Ingrese el número de respuestas correctas:",
                                      font=("Segoe UI", 13), bg="#f5f6fa", fg="#353b48")
        self.label_aciertos.pack(pady=14)
        self.entry_aciertos = tk.Entry(self.root, font=("Segoe UI", 16), width=8, justify="center", bg="#dff9fb", relief="flat")
        self.entry_aciertos.pack(pady=6)
        self.btn_calcular = tk.Button(self.root, text="Calcular Nota", command=self.calcular_nota,
                                      font=("Segoe UI", 13, "bold"), bg="#44bd32", fg="white", activebackground="#4cd137", relief="flat", cursor="hand2")
        self.btn_calcular.pack(pady=16)
        self.update_estado_preguntas()

    def setup_num_preguntas(self):
        top = tk.Toplevel(self.root)
        top.title("Configurar número de preguntas")
        top.geometry("320x150")
        top.configure(bg="#f5f6fa")
        tk.Label(top, text="Ingrese el número de preguntas del examen:",
                 font=("Segoe UI", 12, "bold"), bg="#f5f6fa", fg="#273c75").pack(pady=12)
        entry = tk.Entry(top, font=("Segoe UI", 15), width=8, justify="center", bg="#dff9fb", relief="flat")
        entry.pack(pady=5)
        def guardar():
            try:
                num = int(entry.get())
                if num <= 0:
                    raise ValueError
                self.num_preguntas = num
                self.update_estado_preguntas()
                top.destroy()
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número válido de preguntas.")
        tk.Button(top, text="Guardar", command=guardar,
                  font=("Segoe UI", 12, "bold"), bg="#00a8ff", fg="white", activebackground="#0097e6", relief="flat", cursor="hand2").pack(pady=10)

    def update_estado_preguntas(self):
        if self.num_preguntas:
            self.label_preguntas.config(text=f"Número de preguntas: {self.num_preguntas}")
        else:
            self.label_preguntas.config(text="Número de preguntas: No configurado")

    def calcular_nota(self):
        if not self.num_preguntas:
            messagebox.showerror("Error", "Primero configure el número de preguntas.")
            return
        try:
            aciertos = int(self.entry_aciertos.get())
            if not (0 <= aciertos <= self.num_preguntas):
                raise ValueError
            nota = (aciertos / self.num_preguntas) * 5.0
            messagebox.showinfo("Resultado", f"La calificación es: {nota:.2f}")
        except ValueError:
            messagebox.showerror("Error", f"Ingrese un número de aciertos válido (0 a {self.num_preguntas}).")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraNotas(root)
    root.mainloop()

