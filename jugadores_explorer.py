import requests
import tkinter as tk
from tkinter import messagebox

API_URL = "http://127.0.0.1:5000"

# ==========================================
# BUSCAR VISION POR NOMBRE
# ==========================================
def buscar_por_nombre():

    nombre_busqueda = entrada_nombre.get()

    if nombre_busqueda == "":

        messagebox.showwarning(
            "Aviso",
            "Escribe un nombre o te devoro"
        )
        return 

    respuesta = requests.get(
        f"{API_URL}/jugadores/search/{nombre_busqueda}"
    )
    resultados = respuesta.json()

    if len(resultados) > 0:

        mostrar_jugador(resultados[0])

    else:

        messagebox.showerror(
            "67",
            "No se encontró ningun jugador, mediocre."
        )
# ==========================================
# VISION ALEATORIA
# ==========================================

def jugador_aleatorio():

    respuesta = requests.get(
        f"{API_URL}/jugadores/random"
    )

    if respuesta.status_code == 200:

        jugador = respuesta.json()

        mostrar_jugador(jugador)

    else:

        messagebox.showerror(
            "676",
            "No se pudo obtener un jugador aleatorie."
        )
# ==========================================
# MOSTRAR INFORMACIÓN DE LA VISION
# ==========================================

def mostrar_jugador(jugador):

    nombre.config(
        text=jugador["nombre"]
    )

    equipos.config(
        text=f"Equipo: {jugador["equipo"]}"
    )

    posicion.config(
        text=f"Posición: {jugador["posicion"]}"
    )

    habilidades.config(
        text=f"Habilidades: {', '.join(jugador["habilidades"])}"
    )
# ==========================================
# CREAR VENTANA
# ==========================================

ventana = tk.Tk()

ventana.title(
    "Diamantes bien brutos - Vision Explorer"
)

ventana.geometry("500x520")

# ==========================================
# TÍTULO
# ==========================================

titulo = tk.Label(
    ventana,
    text="JUGADORES EXPLORER",
    font=("Arial", 22, "bold")
)

titulo.pack(pady=20)
# ==========================================
# BÚSQUEDA POR NOMBRE
# ==========================================

tk.Label(
    ventana,
    text="Buscar por nombre:"
).pack()


entrada_nombre = tk.Entry(
    ventana,
    font=("Arial", 14)
)

entrada_nombre.pack(pady=5)


boton_nombre = tk.Button(
    ventana,
    text="Buscar nombre",
    command=buscar_por_nombre
)

boton_nombre.pack(pady=10)
# ==========================================
# VISION ALEATORIA
# ==========================================

boton_random = tk.Button(
    ventana,
    text="🎲 Jugador aleatorio",
    command=jugador_aleatorio,
    font=("Arial", 12, "bold")
)

boton_random.pack(pady=15)
# ==========================================
# INFORMACIÓN DEL JUGADOR
# ==========================================

nombre = tk.Label(
    ventana,
    text="Nombre",
    font=("Arial", 18, "bold")
)

nombre.pack(pady=15)


equipos = tk.Label(
    ventana,
    text="Origen:"
)

equipos.pack()

posicion = tk.Label(
    ventana,
    text="Posición:"
)

posicion.pack()


habilidades = tk.Label(
    ventana,
    text="Elementos:"
)

habilidades.pack()

# ==========================================
# EJECUTAR APLICACIÓN
# ==========================================

ventana.mainloop()