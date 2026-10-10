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