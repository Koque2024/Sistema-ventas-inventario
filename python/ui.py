import tkinter as tk
from tkinter import ttk

# paleta de colores para interfaz / MUY BLANCA CAMBIARLA CUANDO PUEDAS
BG_COLOR = "#F3F4F6"
PANEL_COLOR = "#FFFFFF"
PRIMARY = "#4F46E5"
OPERATOR = "#6366F1"
TEXT = "#111827"

FONT_TITLE = ("Segoe UI", 14, "bold")
FONT_NORMAL = ("Segoe UI", 10)
FONT_CALC = ("Segoe UI", 16)

# pantalla main
root = tk.Tk()
root.title("Sistema de Ventas - Bazar")
root.geometry("1100x700")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# contenedor superior
top_container = tk.Frame(root, bg=BG_COLOR)
top_container.pack(padx=20, pady=20, fill="x")

# panel izquierdo: productos
left_panel = tk.Frame(top_container, bg=PANEL_COLOR, width=500, height=380)
left_panel.pack(side="left", padx=10)
left_panel.pack_propagate(False)

tk.Label(
    left_panel,
    text="Productos",
    font=FONT_TITLE,
    bg=PANEL_COLOR,
    fg=TEXT
).pack(anchor="w", padx=20, pady=10)

products_list = tk.Listbox(
    left_panel,
    font=FONT_NORMAL,
    bd=0,
    highlightthickness=0,
    height=14
)
products_list.pack(fill="both", expand=True, padx=20, pady=10)

# lista testeo
for p in ["Arroz", "Azúcar", "Aceite", "Pan", "Leche", "Café", "Té"]:
    products_list.insert(tk.END, p)

# panel der
right_panel = tk.Frame(top_container, bg=PANEL_COLOR, width=500, height=380)
right_panel.pack(side="right", padx=10)
right_panel.pack_propagate(False)

tk.Label(
    right_panel,
    text="Calculadora",
    font=FONT_TITLE,
    bg=PANEL_COLOR,
    fg=TEXT
).pack(anchor="w", padx=20, pady=10)

calc_var = tk.StringVar()

calc_display = tk.Entry(
    right_panel,
    textvariable=calc_var,
    font=FONT_CALC,
    justify="right",
    bd=0,
    bg="#EEF2FF"
)
calc_display.pack(fill="x", padx=20, pady=10)

# calculadora funciones
def add_to_calc(value):
    calc_var.set(calc_var.get() + value)

def clear_calc():
    calc_var.set("")

def calculate():
    try:
        result = eval(calc_var.get())
        calc_var.set(str(result))
    except:
        calc_var.set("Error")

# botones calculadora
buttons_frame = tk.Frame(right_panel, bg=PANEL_COLOR)
buttons_frame.pack(padx=20, pady=10)

buttons = [
    ("7", PRIMARY), ("8", PRIMARY), ("9", PRIMARY), ("/", OPERATOR),
    ("4", PRIMARY), ("5", PRIMARY), ("6", PRIMARY), ("*", OPERATOR),
    ("1", PRIMARY), ("2", PRIMARY), ("3", PRIMARY), ("-", OPERATOR),
    ("0", PRIMARY), ("C", "#EF4444"), ("=", "#22C55E"), ("+", OPERATOR),
]

row = col = 0
for text, color in buttons:

    if text == "=":
        cmd = calculate
    elif text == "C":
        cmd = clear_calc
    else:
        cmd = lambda v=text: add_to_calc(v)

    btn = tk.Button(
        buttons_frame,
        text=text,
        width=6,
        height=2,
        bg=color,
        fg="white",
        bd=0,
        font=("Segoe UI", 12, "bold"),
        command=cmd
    )
    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col == 4:
        col = 0
        row += 1


# resumen de compra
bottom_panel = tk.Frame(root, bg=PANEL_COLOR, height=220)
bottom_panel.pack(padx=20, pady=(0, 20), fill="x")
bottom_panel.pack_propagate(False)

tk.Label(
    bottom_panel,
    text="Boleta",
    font=FONT_TITLE,
    bg=PANEL_COLOR,
    fg=TEXT
).pack(anchor="w", padx=20, pady=10)

boleta = tk.Text(
    bottom_panel,
    height=7,
    font=FONT_NORMAL,
    bd=0,
    bg="#F9FAFB"
)
boleta.pack(fill="both", expand=True, padx=20, pady=10)

boleta.insert(tk.END, "Producto    Cant   Precio   Subtotal\n")
boleta.insert(tk.END, "------------------------------------------\n")

root.mainloop()
