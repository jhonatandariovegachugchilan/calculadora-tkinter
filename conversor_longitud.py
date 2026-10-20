import tkinter as tk
from tkinter import ttk, messagebox

# --- Constantes y Factores de Conversión (Metro 'm' como unidad base) ---
FACTORES_A_METROS = {
    "Milímetros (mm)": 0.001,
    "Centímetros (cm)": 0.01,
    "Metros (m)": 1.0,
}

SIMBOLOS = {
    "Milímetros (mm)": "mm",
    "Centímetros (cm)": "cm",
    "Metros (m)": "m",
}

OPCIONES_UNIDADES = list(FACTORES_A_METROS.keys())

def convertir():
    """Valida la entrada, realiza la conversión de longitud y actualiza el resultado."""
    texto_entrada = entry_valor.get().strip().replace(',', '.')
    
    # Validación: campo no vacío
    if not texto_entrada:
        messagebox.showerror(
            "Error de entrada", 
            "El campo de entrada está vacío. Por favor, introduce un valor numérico."
        )
        return

    # Validación: número válido (entero o decimal)
    try:
        valor = float(texto_entrada)
    except ValueError:
        messagebox.showerror(
            "Error de entrada", 
            "Entrada no válida. Asegúrate de introducir solo números (enteros o decimales)."
        )
        return

    unidad_origen = combo_origen.get()
    unidad_destino = combo_destino.get()

    # Conversión matemática usando el metro como unidad central
    # 1. Convertir origen -> metros
    valor_en_metros = valor * FACTORES_A_METROS[unidad_origen]
    # 2. Convertir metros -> unidad destino
    resultado = valor_en_metros / FACTORES_A_METROS[unidad_destino]

    # Formateo limpio del resultado
    if resultado.is_integer():
        resultado_str = str(int(resultado))
    else:
        resultado_str = f"{resultado:.6g}"

    simbolo_destino = SIMBOLOS[unidad_destino]
    label_resultado.config(text=f"Resultado: {resultado_str} {simbolo_destino}")

def limpiar():
    """Restaura todos los campos y selectores a su estado inicial."""
    entry_valor.delete(0, tk.END)
    combo_origen.set(OPCIONES_UNIDADES[0])   # Milímetros (mm)
    combo_destino.set(OPCIONES_UNIDADES[2])  # Metros (m)
    label_resultado.config(text="Resultado: ---")
    entry_valor.focus_set()

# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Conversor de Longitud")
ventana.geometry("420x350")
ventana.resizable(False, False)

# Configuración de estilos ttk
estilo = ttk.Style(ventana)
estilo.theme_use("clam")

# Fuentes y estilos
estilo.configure("TLabel", font=("Segoe UI", 10))
estilo.configure("TButton", font=("Segoe UI", 10), padding=6)
estilo.configure("TCombobox", font=("Segoe UI", 10))

# Estilo destacado para el botón Convertir
estilo.configure(
    "Primary.TButton",
    font=("Segoe UI", 10, "bold"),
    foreground="#ffffff",
    background="#0066cc",
    padding=6
)
estilo.map("Primary.TButton", background=[("active", "#0052a3")])

# Contenedor principal con márgenes interiores
contenedor = ttk.Frame(ventana, padding=20)
contenedor.pack(fill=tk.BOTH, expand=True)

# 1. Campo de Entrada (Input)
lbl_valor = ttk.Label(contenedor, text="Cantidad numérica:")
lbl_valor.pack(anchor=tk.W, pady=(0, 2))
entry_valor = ttk.Entry(contenedor, font=("Segoe UI", 11))
entry_valor.pack(fill=tk.X, pady=(0, 15))
entry_valor.focus_set()

# 2. Selector de Origen (Dropdown)
lbl_origen = ttk.Label(contenedor, text="De (Origen):")
lbl_origen.pack(anchor=tk.W, pady=(0, 2))
combo_origen = ttk.Combobox(
    contenedor,
    values=OPCIONES_UNIDADES,
    state="readonly",
    font=("Segoe UI", 10)
)
combo_origen.set(OPCIONES_UNIDADES[0])  # Valor por defecto: Milímetros (mm)
combo_origen.pack(fill=tk.X, pady=(0, 15))

# 3. Selector de Destino (Dropdown)
lbl_destino = ttk.Label(contenedor, text="A (Destino):")
lbl_destino.pack(anchor=tk.W, pady=(0, 2))
combo_destino = ttk.Combobox(
    contenedor,
    values=OPCIONES_UNIDADES,
    state="readonly",
    font=("Segoe UI", 10)
)
combo_destino.set(OPCIONES_UNIDADES[2])  # Valor por defecto: Metros (m)
combo_destino.pack(fill=tk.X, pady=(0, 20))

# 4. Fila de Botones ("Convertir" y "Limpiar")
frame_botones = ttk.Frame(contenedor)
frame_botones.pack(fill=tk.X, pady=(0, 20))

btn_convertir = ttk.Button(
    frame_botones,
    text="Convertir",
    style="Primary.TButton",
    command=convertir
)
btn_convertir.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

btn_limpiar = ttk.Button(
    frame_botones,
    text="Limpiar",
    command=limpiar
)
btn_limpiar.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))

# 5. Etiqueta de Resultado
label_resultado = ttk.Label(
    contenedor,
    text="Resultado: ---",
    font=("Segoe UI", 13, "bold"),
    anchor=tk.CENTER
)
label_resultado.pack(fill=tk.X)

# --- Bucle de Eventos ---
if __name__ == "__main__":
    ventana.mainloop()
