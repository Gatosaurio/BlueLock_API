from flask import Flask, jsonify
import random

from jugadores_data import jugadores

app = Flask(__name__)

@app.route("/jugadores")
def obtener_jugadores():
    return jsonify(jugadores)

app = Flask(__name__)

@app.route("/jugadores")
def obtener_jugadores():
    return jsonify(jugadores)

@app.route("/jugadores/habilidades/<habilidades>")
def buscar_por_habilidad(habilidades):
    resultados = []

    for jugador in jugadores:
        if habilidades.lower() in [
            elemento_vision.lower()
            for elemento_vision in ["elementos"]
        ]:

            resultados.append(jugador)

    return jsonify(resultados)

@app.route("/jugadores/posicion/<posicion>")
def buscar_por_rol(posicion):

    resultados = []

    for jugador in jugadores:

        if posicion.lower() in jugador["posicion"].lower():

            resultados.append(jugador)

    return jsonify(resultados)

@app.route("/jugadores/equipos/<equipo>")
def buscar_por_equipo(equipo):

    resultados = []

    for jugador in jugadores:

        if equipo.lower() in jugador["equipo"].lower():

            resultados.append(jugador)

    return jsonify(resultados)

@app.route("/jugadores/search/<nombre>")
def buscar_por_nombre(nombre):

    resultados = []

    for jugador in jugadores:

        if nombre.lower() in jugador["nombre"].lower():

            resultados.append(jugador)

    return jsonify(resultados)