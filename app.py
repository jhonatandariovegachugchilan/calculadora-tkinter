import tkinter as tk
from tkinter import ttk

def mostrar_mensaje():
    """Función que se ejecuta cuando el usuario hace clic en el botón."""
    # Actualiza el texto de la etiqueta dentro de la ventana
    etiqueta_resultado.config(text="Hello World")
    # Imprime también en la consola
    print("Hello World")

# 1. Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera app")
ventana.geometry("300x200")
ventana.resizable(False, False)

# 2. Etiqueta para mostrar el texto al hacer clic
etiqueta_resultado = ttk.Label(
    ventana,
    text="",
    font=("Segoe UI", 14, "bold"),
    foreground="#2b2b2b"
)
etiqueta_resultado.pack(pady=20)

# 3. Botón 'Apriétame'
boton = ttk.Button(
    ventana,
    text="Apriétame",
    command=mostrar_mensaje
)
boton.pack(pady=10)

# 4. Iniciar el bucle principal de la aplicación
if __name__ == "__main__":
    ventana.mainloop()

