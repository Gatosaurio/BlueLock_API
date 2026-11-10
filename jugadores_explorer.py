import requests
import tkinter as tk
from tkinter import messagebox

API_URL = "https://bluelock-api-gmy1.onrender.com"

# ==========================================
# BUSCAR VISION POR NOMBRE
# ==========================================
def buscar_por_nombre():

    nombre_busqueda = entrada_nombre.get().strip()

    if nombre_busqueda == "":

        messagebox.showwarning(
            "Aviso",
            "Escribe un nombre o te devoro"
        )
        return 

    try:
        respuesta = requests.get(
        f"{API_URL}/jugadores/search/{nombre_busqueda}",
        timeout=30
    )

        print("Código:", respuesta.status_code)
        print("Respuesta:", respuesta.text)
    respuesta.raise_for_status()
    resultados = respuesta.json()

    if len(resultados) > 0:

        mostrar_jugador(resultados[0])

    else:

        messagebox.showerror(
            "67",
            "No se encontró ningun jugador, mediocre."
        )
    except requests.exceptions.RequestException as error:
        messagebox.showerror(
            "Error de conexión",
            f"No se pudo conectar con la API:\n{error}"
        )

    except requests.exceptions.JSONDecodeError:
        messagebox.showerror(
            "Error",
            "La API no devolvió un JSON válido."
        )
# ==========================================
# VISION ALEATORIA
# ==========================================

def jugador_aleatorio():
    try:
        respuesta = requests.get(
            f"{API_URL}/jugadores/random",
            timeout=30
        )
        respuesta.raise_for_status()
        jugador = respuesta.json()
        mostrar_jugador(jugador)
    except requests.exceptions.RequestException as error:
        messagebox.showerror(
            "Error",
            f"No se pudo obtener el jugador:\n{error}"
        )

    except requests.exceptions.JSONDecodeError:
        messagebox.showerror(
            "6767",
            "No se pudo obtener en jugador alatorie"
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