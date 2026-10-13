import tkinter as tk
from tkinter import ttk, messagebox

# --- Configuración de Colores basada en la imagen (Tema Oscuro / Dark Mode) ---
COLOR_BG = "#0d1b2a"           # Fondo oscuro azulado profundo
COLOR_CARD = "#0d1b2a"         # Fondo del contenedor
COLOR_INPUT_BG = "#132338"     # Fondo de los inputs/campos
COLOR_INPUT_BORDER = "#253b59" # Borde sutil de los campos
COLOR_TEXT_PRIMARY = "#ffffff" # Blanco para valores de entrada
COLOR_TEXT_LABEL = "#cdd9e5"   # Azul grisáceo claro para títulos/etiquetas
COLOR_BTN_CALC = "#4eedb0"     # Botón Calcular: Verde azulado brillante / Turquesa menta
COLOR_BTN_CALC_HOVER = "#38d99b"
COLOR_BTN_CALC_TEXT = "#0a241a"
COLOR_BTN_CLEAR = "#20334d"    # Botón Limpiar: Azul oscuro suave
COLOR_BTN_CLEAR_HOVER = "#2a4263"
COLOR_BTN_CLEAR_TEXT = "#ffffff"
COLOR_RESULT_TEXT = "#4eedb0"  # Texto del resultado brillante

def calcular():
    """Realiza el cálculo aritmético seleccionado."""
    try:
        num1 = float(entry_num1.get().strip().replace(',', '.'))
        num2 = float(entry_num2.get().strip().replace(',', '.'))
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce números válidos en ambos campos.")
        label_resultado.config(text="Resultado: Error")
        return

    operacion = combo_operacion.get()

    if operacion == "Sumar":
        res = num1 + num2
    elif operacion == "Restar":
        res = num1 - num2
    elif operacion == "Multiplicar":
        res = num1 * num2
    elif operacion == "Dividir":
        if num2 == 0:
            messagebox.showerror("Error", "No se puede dividir entre cero.")
            label_resultado.config(text="Resultado: Indefinido")
            return
        res = num1 / num2
    else:
        return

    # Si el número no tiene decimales significativos, mostrar como entero
    if res.is_integer():
        res_formateado = str(int(res))
    else:
        res_formateado = f"{res:.6g}"

    label_resultado.config(text=f"Resultado: {res_formateado}")

def limpiar():
    """Borra el contenido de los campos y reinicia el estado."""
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    combo_operacion.current(0)
    label_resultado.config(text="Resultado: —")
    entry_num1.focus_set()

# 1. Ventana Principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("640x260")
ventana.configure(bg=COLOR_BG)
ventana.resizable(False, False)

# 2. Configuración de estilos ttk
style = ttk.Style(ventana)
style.theme_use("clam")

# Estilo para Combobox (fondo y desplegable)
style.configure(
    "Dark.TCombobox",
    fieldbackground=COLOR_INPUT_BG,
    background=COLOR_INPUT_BG,
    foreground=COLOR_TEXT_PRIMARY,
    arrowcolor=COLOR_TEXT_PRIMARY,
    bordercolor=COLOR_INPUT_BORDER,
    lightcolor=COLOR_INPUT_BORDER,
    darkcolor=COLOR_INPUT_BORDER,
    padding=6
)
style.map(
    "Dark.TCombobox",
    fieldbackground=[("readonly", COLOR_INPUT_BG)],
    selectbackground=[("readonly", COLOR_INPUT_BG)],
    selectforeground=[("readonly", COLOR_TEXT_PRIMARY)]
)
ventana.option_add("*TCombobox*Listbox.background", COLOR_INPUT_BG)
ventana.option_add("*TCombobox*Listbox.foreground", COLOR_TEXT_PRIMARY)
ventana.option_add("*TCombobox*Listbox.selectBackground", "#1f3b5c")
ventana.option_add("*TCombobox*Listbox.selectForeground", "#ffffff")
ventana.option_add("*TCombobox*Listbox.font", ("Segoe UI", 11))

# 3. Contenedor principal con margen
contenedor = tk.Frame(ventana, bg=COLOR_BG, padx=25, pady=25)
contenedor.pack(fill=tk.BOTH, expand=True)

# 4. Fila superior: Tres columnas en horizontal (Grid)
# Grid cols: Col 0 (Primer número) | Col 1 (Operación) | Col 2 (Segundo número)
contenedor.columnconfigure(0, weight=1)
contenedor.columnconfigure(1, weight=1)
contenedor.columnconfigure(2, weight=1)

# --- Columna 0: Primer número ---
frame_col1 = tk.Frame(contenedor, bg=COLOR_BG)
frame_col1.grid(row=0, column=0, padx=(0, 10), sticky="ew")

lbl_num1 = tk.Label(
    frame_col1, text="Primer número", bg=COLOR_BG,
    fg=COLOR_TEXT_LABEL, font=("Segoe UI", 11)
)
lbl_num1.pack(anchor="w", pady=(0, 8))

entry_num1_border = tk.Frame(frame_col1, bg=COLOR_INPUT_BORDER, padx=1, pady=1)
entry_num1_border.pack(fill="x")

entry_num1 = tk.Entry(
    entry_num1_border,
    bg=COLOR_INPUT_BG,
    fg=COLOR_TEXT_PRIMARY,
    insertbackground=COLOR_TEXT_PRIMARY,
    font=("Segoe UI", 12),
    bd=0,
    relief="flat"
)
entry_num1.pack(fill="x", ipady=8, padx=10)

# --- Columna 1: Operación ---
frame_col2 = tk.Frame(contenedor, bg=COLOR_BG)
frame_col2.grid(row=0, column=1, padx=10, sticky="ew")

lbl_op = tk.Label(
    frame_col2, text="Operación", bg=COLOR_BG,
    fg=COLOR_TEXT_LABEL, font=("Segoe UI", 11)
)
lbl_op.pack(anchor="w", pady=(0, 8))

combo_operacion = ttk.Combobox(
    frame_col2,
    values=["Sumar", "Restar", "Multiplicar", "Dividir"],
    state="readonly",
    style="Dark.TCombobox",
    font=("Segoe UI", 12)
)
combo_operacion.current(0)
combo_operacion.pack(fill="x", ipady=3)

# --- Columna 2: Segundo número ---
frame_col3 = tk.Frame(contenedor, bg=COLOR_BG)
frame_col3.grid(row=0, column=2, padx=(10, 0), sticky="ew")

lbl_num2 = tk.Label(
    frame_col3, text="Segundo número", bg=COLOR_BG,
    fg=COLOR_TEXT_LABEL, font=("Segoe UI", 11)
)
lbl_num2.pack(anchor="w", pady=(0, 8))

entry_num2_border = tk.Frame(frame_col3, bg=COLOR_INPUT_BORDER, padx=1, pady=1)
entry_num2_border.pack(fill="x")

entry_num2 = tk.Entry(
    entry_num2_border,
    bg=COLOR_INPUT_BG,
    fg=COLOR_TEXT_PRIMARY,
    insertbackground=COLOR_TEXT_PRIMARY,
    font=("Segoe UI", 12),
    bd=0,
    relief="flat"
)
entry_num2.pack(fill="x", ipady=8, padx=10)

# 5. Fila de botones (Calcular y Limpiar)
frame_botones = tk.Frame(contenedor, bg=COLOR_BG)
frame_botones.grid(row=1, column=0, columnspan=3, sticky="w", pady=(20, 16))

btn_calcular = tk.Button(
    frame_botones,
    text="Calcular",
    command=calcular,
    bg=COLOR_BTN_CALC,
    fg=COLOR_BTN_CALC_TEXT,
    activebackground=COLOR_BTN_CALC_HOVER,
    activeforeground=COLOR_BTN_CALC_TEXT,
    font=("Segoe UI", 10, "bold"),
    bd=0,
    relief="flat",
    padx=16,
    pady=6,
    cursor="hand2"
)
btn_calcular.pack(side="left", padx=(0, 10))

btn_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    command=limpiar,
    bg=COLOR_BTN_CLEAR,
    fg=COLOR_BTN_CLEAR_TEXT,
    activebackground=COLOR_BTN_CLEAR_HOVER,
    activeforeground=COLOR_BTN_CLEAR_TEXT,
    font=("Segoe UI", 10, "bold"),
    bd=0,
    relief="flat",
    padx=16,
    pady=6,
    cursor="hand2"
)
btn_limpiar.pack(side="left")

# 6. Fila de Resultado
label_resultado = tk.Label(
    contenedor,
    text="Resultado: —",
    bg=COLOR_BG,
    fg=COLOR_RESULT_TEXT,
    font=("Segoe UI", 16, "bold"),
    anchor="w"
)
label_resultado.grid(row=2, column=0, columnspan=3, sticky="w")

# Bucle principal
if __name__ == "__main__":
    ventana.mainloop()
