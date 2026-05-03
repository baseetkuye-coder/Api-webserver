# https://my-json-server.typicode.com/
# https://canvas.kdg.be/courses/55832/pages/oefening-json-api?module_item_id=1344505

from flask import Flask, render_template
import requests

app = Flask(__name__)

URL = "https://my-json-server.typicode.com/baseetkuye-coder/Api-webserver"


# API get and printing in the console
print("Data ophalen van de API...")
response = requests.get(URL + "/motorcycles")
data_check = response.json()
for m in data_check:
    print(m["id"], "-", m["brand"], m["name"])
print("Data succesvol opgehaald!\n")


# home page
@app.route("/")
def home():
    response = requests.get(URL + "/motorcycles")
    motorcycles = response.json()

    response = requests.get(URL + "/brands")
    brands = response.json()

    return render_template("index.html", motorcycles=motorcycles, brands=brands)


# detail page
@app.route("/motorcycles/<int:motorcycle_id>")
def motorcycle_detail(motorcycle_id):
    response = requests.get(URL + "/motorcycles/" + str(motorcycle_id))
    motorcycle = response.json()
    return render_template("motorcycle.html", motorcycle=motorcycle)


if __name__ == "__main__":
    app.run()
