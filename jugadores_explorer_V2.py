import tkinter as tk
import requests

URL_API = "https://bluelock-api-gmy1.onrender.com/jugadores"

def cargar_personajes():
    lista.delete(0, tk.END)
    boton.config(state="disabled")
    estado.config(text="Consultando API...")

    try:
        respuesta = requests.get(URL_API, timeout=20)
        respuesta.raise_for_status()
        personajes = respuesta.json()

        for personaje in personajes:
            nombre = personaje.get("name", "Sin nombre")
            lista.insert(tk.END, nombre)

        estado.config(text="Datos cargados correctamente")

    except requests.RequestException as error:
        estado.config(text=f"No se pudo consultar la API: {error}")

    except ValueError:
        estado.config(text="La respuesta no contiene JSON válido")

    finally:
        boton.config(state="normal")


ventana = tk.Tk()
ventana.title("Blue Lock — Personajes")
ventana.geometry("400x400")

titulo = tk.Label(
    ventana,
    text="Personajes de Blue Lock",
    font=("Arial", 16)
)
titulo.pack(pady=10)

boton = tk.Button(
    ventana,
    text="Cargar personajes",
    command=cargar_personajes
)
boton.pack(pady=10)

lista = tk.Listbox(ventana, width=40, height=12)
lista.pack(pady=10)

estado = tk.Label(ventana, text="Presiona el botón para consultar la API")
estado.pack(pady=10)

ventana.mainloop()
