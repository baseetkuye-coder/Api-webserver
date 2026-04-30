# https://flask.palletsprojects.com/
# https://my-json-server.typicode.com/
# https://requests.readthedocs.io/en/latest/

from flask import Flask, render_template
import requests

app = Flask(__name__)

# vervang USERNAME en REPO met jouw github gegevens
URL = "https://my-json-server.typicode.com/USERNAME/REPO"


# Stap 4: data ophalen via API en printen in de console
print("Data ophalen van de API...")
response = requests.get(URL + "/motorcycles")
data_check = response.json()
for m in data_check:
    print(m["id"], "-", m["brand"], m["name"])
print("Data succesvol opgehaald!\n")


# home page met lijst van motorcycles en brands
@app.route("/")
def home():
    response = requests.get(URL + "/motorcycles")
    motorcycles = response.json()

    response = requests.get(URL + "/brands")
    brands = response.json()

    return render_template("index.html", motorcycles=motorcycles, brands=brands)


# detail pagina van 1 motorcycle
@app.route("/motorcycles/<int:motorcycle_id>")
def motorcycle_detail(motorcycle_id):
    response = requests.get(URL + "/motorcycles/" + str(motorcycle_id))
    motorcycle = response.json()
    return render_template("motorcycle.html", motorcycle=motorcycle)


if __name__ == "__main__":
    app.run(debug=True)
