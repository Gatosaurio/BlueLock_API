from flask import Flask, jsonify
import random

from jugadores_data import jugadores

app = Flask(__name__)

@app.route("/jugadores")
def obtener_jugadores():
    return jsonify(jugadores)

