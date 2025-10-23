from flask import Flask
from urllib.parse import quote as url_quote  # reemplaza la función obsoleta de werkzeug

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola Mundo"

if __name__ == '__main__':
    app.run(debug=True)
