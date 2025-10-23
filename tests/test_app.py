from app import app
import pytest

# Test para la ruta raíz
def test_home():
    client = app.test_client()
    response = client.get('/')
    
    # ✅ CORRECCIÓN: Se espera correctamente "Hola Mundo"
    assert response.data == b"Hola Mundo"
    
    assert response.status_code == 200

# Añade un segundo test simple (requisito del examen)
def test_status_code():
    client = app.test_client()
    response = client.get('/')
    # Comprueba si el código de estado es 200, un tipo de prueba diferente
    assert response.status_code == 200
