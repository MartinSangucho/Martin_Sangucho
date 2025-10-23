from flask import Flask

# Inicializa la aplicación Flask
app = Flask(__name__)

@app.route('/')
def home():
    # El contenido que espera el test_app.py
    return "Hola Mundo"

if __name__ == "__main__":
    # Importante: Docker requiere escuchar en 0.0.0.0
    # y el puerto 8080 (o el que se configure en el Dockerfile)
    app.run(host='0.0.0.0', port=8080)
