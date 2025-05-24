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
        self.root.geometry("420x370")
        self.root.configure(bg="#222f3e")  # Fondo oscuro para mejor contraste
        self.num_preguntas = None
        self.resultado_label = None
        self.setup_main_ui()

    def setup_main_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.btn_config = tk.Button(self.root, text="Configurar materia, curso y número de preguntas", command=self.setup_configuracion,
                                    font=("Segoe UI", 13, "bold"), bg="#54a0ff", fg="white", activebackground="#2e86de", relief="flat", cursor="hand2")
        self.btn_config.pack(pady=18)
        self.label_materia = tk.Label(self.root, text="Materia: No configurada", font=("Segoe UI", 12, "bold"), bg="#222f3e", fg="#feca57")
        self.label_materia.pack(pady=2)
        self.label_curso = tk.Label(self.root, text="Curso: No configurado", font=("Segoe UI", 12, "bold"), bg="#222f3e", fg="#feca57")
        self.label_curso.pack(pady=2)
        self.label_preguntas = tk.Label(self.root, text="Número de preguntas: No configurado",
                                        font=("Segoe UI", 13, "bold"), bg="#222f3e", fg="#feca57")
        self.label_preguntas.pack(pady=6)
        self.label_aciertos = tk.Label(self.root, text="Ingrese el número de respuestas correctas:",
                                      font=("Segoe UI", 14, "bold"), bg="#222f3e", fg="#feca57")
        self.label_aciertos.pack(pady=14)
        self.entry_aciertos = tk.Entry(self.root, font=("Segoe UI", 18, "bold"), width=8, justify="center", bg="#f1f2f6", fg="#222f3e", relief="flat")
        self.entry_aciertos.pack(pady=6)
        self.btn_calcular = tk.Button(self.root, text="Calcular Nota", command=self.calcular_nota,
                                      font=("Segoe UI", 15, "bold"), bg="#1dd1a1", fg="white", activebackground="#10ac84", relief="flat", cursor="hand2")
        self.btn_calcular.pack(pady=16)
        self.resultado_label = tk.Label(self.root, text="", font=("Segoe UI", 38, "bold"), bg="#222f3e", fg="#ff6b6b")
        self.resultado_label.pack(pady=10)
        self.materia = None
        self.curso = None
        self.update_estado_configuracion()

    def setup_configuracion(self):
        top = tk.Toplevel(self.root)
        top.title("Configuración")
        top.geometry("370x260")
        top.configure(bg="#222f3e")
        tk.Label(top, text="Materia:", font=("Segoe UI", 12, "bold"), bg="#222f3e", fg="#feca57").pack(pady=6)
        entry_materia = tk.Entry(top, font=("Segoe UI", 13), width=20, bg="#f1f2f6", fg="#222f3e", relief="flat")
        entry_materia.pack(pady=2)
        tk.Label(top, text="Curso:", font=("Segoe UI", 12, "bold"), bg="#222f3e", fg="#feca57").pack(pady=6)
        entry_curso = tk.Entry(top, font=("Segoe UI", 13), width=20, bg="#f1f2f6", fg="#222f3e", relief="flat")
        entry_curso.pack(pady=2)
        tk.Label(top, text="Número de preguntas:", font=("Segoe UI", 12, "bold"), bg="#222f3e", fg="#feca57").pack(pady=6)
        entry_preguntas = tk.Entry(top, font=("Segoe UI", 13), width=8, justify="center", bg="#f1f2f6", fg="#222f3e", relief="flat")
        entry_preguntas.pack(pady=2)
        def guardar():
            try:
                materia = entry_materia.get().strip()
                curso = entry_curso.get().strip()
                num = int(entry_preguntas.get())
                if not materia or not curso or num <= 0:
                    raise ValueError
                self.materia = materia
                self.curso = curso
                self.num_preguntas = num
                self.update_estado_configuracion()
                top.destroy()
            except ValueError:
                messagebox.showerror("Error", "Por favor, complete todos los campos correctamente.")
        tk.Button(top, text="Guardar", command=guardar,
                  font=("Segoe UI", 13, "bold"), bg="#54a0ff", fg="white", activebackground="#2e86de", relief="flat", cursor="hand2").pack(pady=14)

    def update_estado_configuracion(self):
        if self.materia:
            self.label_materia.config(text=f"Materia: {self.materia}")
        else:
            self.label_materia.config(text="Materia: No configurada")
        if self.curso:
            self.label_curso.config(text=f"Curso: {self.curso}")
        else:
            self.label_curso.config(text="Curso: No configurado")
        if self.num_preguntas:
            self.label_preguntas.config(text=f"Número de preguntas: {self.num_preguntas}")
        else:
            self.label_preguntas.config(text="Número de preguntas: No configurado")

    def calcular_nota(self):
        if not self.num_preguntas:
            messagebox.showerror("Error", "Primero configure la materia, curso y número de preguntas.")
            return
        try:
            aciertos = int(self.entry_aciertos.get())
            if not (0 <= aciertos <= self.num_preguntas):
                raise ValueError
            nota = (aciertos / self.num_preguntas) * 5.0
            nota_redondeada = round(nota + 0.05, 1)  # Redondeo hacia arriba a la décima más cercana
            self.resultado_label.config(text=f"{nota_redondeada}")
        except ValueError:
            self.resultado_label.config(text="")
            messagebox.showerror("Error", f"Ingrese un número de aciertos válido (0 a {self.num_preguntas}).")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraNotas(root)
    root.mainloop()

