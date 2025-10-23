from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.data == b"Hola Mundo"
    assert response.status_code == 200
