import requests

URL_API = "https://bluelock-api-gmy1.onrender.com"

respuesta = requests.get(
    f"{URL_API}/jugadores",
    timeout=20
)

print("Código HTTP:", respuesta.status_code)

if respuesta.ok:
    print("Respuesta JSON:")
    print(respuesta.json())
else:
    print("La API respondió con un error.")
    print(respuesta.text)