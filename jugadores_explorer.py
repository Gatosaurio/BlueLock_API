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