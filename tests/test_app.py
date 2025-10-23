from app import app
import pytest

# Test para la ruta raíz
def test_home():
    client = app.test_client()
    response = client.get('/')
    
    # ✅ CORRECCIÓN: Ahora espera correctamente "Hola Mundo"
    assert response.data == b"Hola Mundo"
    
    assert response.status_code == 200

# Segundo test
def test_status_code():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
