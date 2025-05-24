# Proyecto calculadora de notas escolares
# Autor: Edwin Hernan Gil Rodriguez
# Fecha: 2025-05-23 
'''
Este programa permite calcular la nota final de un estudiante en una evaluación, donde el usuario establece:
- Materia
- Curso
- Número de preguntas de la evaluación
Luego, el usuario ingresa el número de aciertos para calcular su nota en una escala de 0.0 a 5.0.
La nota se redondea a una cifra decimal: si el segundo decimal está entre 0-4 se redondea hacia abajo, si está entre 5-9 se redondea hacia arriba.
'''

import tkinter as tk
from tkinter import messagebox

class CalculadoraNotas:
    def __init__(self, root):
        # Configuración inicial de la ventana principal
        self.root = root
        self.root.title("Calculadora de Notas Escolares - Edwin Gil")
        self.root.geometry("440x400")
        self.root.configure(bg="#f7faff")  # Fondo claro y suave
        self.num_preguntas = None
        self.resultado_label = None
        self.setup_main_ui()

    def setup_main_ui(self):
        # Construye la interfaz principal: botones y etiquetas
        for widget in self.root.winfo_children():
            widget.destroy()
        # Botón para configurar materia, curso y número de preguntas
        self.btn_config = tk.Button(
            self.root,
            text="Configurar materia, curso y número de preguntas",
            command=self.setup_configuracion,
            font=("Segoe UI", 13, "bold"),
            bg="#4f8cff",
            fg="white",
            activebackground="#357ae8",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            bd=0
        )
        self.btn_config.pack(pady=18)
        # Etiquetas para mostrar la materia, curso y número de preguntas configurados
        label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#f7faff", "fg": "#2d3436"}
        self.label_materia = tk.Label(self.root, text="Materia: No configurada", **label_style)
        self.label_materia.pack(pady=2)
        self.label_curso = tk.Label(self.root, text="Curso: No configurado", **label_style)
        self.label_curso.pack(pady=2)
        self.label_preguntas = tk.Label(self.root, text="Número de preguntas: No configurado", **label_style)
        self.label_preguntas.pack(pady=6)
        # Entrada para el número de aciertos
        self.label_aciertos = tk.Label(
            self.root,
            text="Ingrese el número de respuestas correctas:",
            font=("Segoe UI", 14, "bold"),
            bg="#f7faff",
            fg="#0984e3"
        )
        self.label_aciertos.pack(pady=14)
        self.entry_aciertos = tk.Entry(
            self.root,
            font=("Segoe UI", 20, "bold"),
            width=8,
            justify="center",
            bg="#eaf0fb",
            fg="#2d3436",
            relief="flat",
            bd=2,
            highlightbackground="#4f8cff",
            highlightcolor="#4f8cff",
            highlightthickness=1
        )
        self.entry_aciertos.pack(pady=6)
        # Botón para calcular la nota
        self.btn_calcular = tk.Button(
            self.root,
            text="Calcular Nota",
            command=self.calcular_nota,
            font=("Segoe UI", 15, "bold"),
            bg="#00b894",
            fg="white",
            activebackground="#00a383",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            bd=0
        )
        self.btn_calcular.pack(pady=16)
        # Etiqueta para mostrar el resultado de la nota en grande
        self.resultado_label = tk.Label(
            self.root,
            text="",
            font=("Segoe UI", 44, "bold"),
            bg="#f7faff",
            fg="#d35400"
        )
        self.resultado_label.pack(pady=10)
        # Variables para materia y curso
        self.materia = None
        self.curso = None
        self.update_estado_configuracion()

    def setup_configuracion(self):
        # Ventana emergente para configurar materia, curso y número de preguntas
        top = tk.Toplevel(self.root)
        top.title("Configuración")
        top.geometry("370x260")
        top.configure(bg="#f7faff")
        label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#f7faff", "fg": "#2d3436"}
        tk.Label(top, text="Materia:", **label_style).pack(pady=6)
        entry_materia = tk.Entry(top, font=("Segoe UI", 13), width=20, bg="#eaf0fb", fg="#2d3436", relief="flat")
        entry_materia.pack(pady=2)
        tk.Label(top, text="Curso:", **label_style).pack(pady=6)
        entry_curso = tk.Entry(top, font=("Segoe UI", 13), width=20, bg="#eaf0fb", fg="#2d3436", relief="flat")
        entry_curso.pack(pady=2)
        tk.Label(top, text="Número de preguntas:", **label_style).pack(pady=6)
        entry_preguntas = tk.Entry(top, font=("Segoe UI", 13), width=8, justify="center", bg="#eaf0fb", fg="#2d3436", relief="flat")
        entry_preguntas.pack(pady=2)
        def guardar():
            # Guarda los valores ingresados y actualiza la interfaz principal
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
                  font=("Segoe UI", 13, "bold"), bg="#4f8cff", fg="white", activebackground="#357ae8", relief="flat", cursor="hand2", bd=0).pack(pady=14)

    def update_estado_configuracion(self):
        # Actualiza las etiquetas de materia, curso y número de preguntas en la interfaz principal
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
        # Calcula la nota según los aciertos y muestra el resultado redondeado
        if not self.num_preguntas:
            messagebox.showerror("Error", "Primero configure la materia, curso y número de preguntas.")
            return
        try:
            aciertos = int(self.entry_aciertos.get())
            if not (0 <= aciertos <= self.num_preguntas):
                raise ValueError
            nota = (aciertos / self.num_preguntas) * 5.0
            # Redondeo personalizado: segundo decimal 0-4 baja, 5-9 sube
            decimales = int((nota * 100) % 10)
            if decimales <= 4:
                nota_redondeada = float(f"{nota:.1f}")
            else:
                nota_redondeada = round(nota + 0.05, 1)
            self.resultado_label.config(text=f"{nota_redondeada}")
        except ValueError:
            self.resultado_label.config(text="")
            messagebox.showerror("Error", f"Ingrese un número de aciertos válido (0 a {self.num_preguntas}).")

if __name__ == "__main__":
    # Punto de entrada de la aplicación
    root = tk.Tk()
    app = CalculadoraNotas(root)
    root.mainloop()

