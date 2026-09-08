import pytest
import sys
import os

# Ajustar el path para que Pytest encuentre la app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == 'success'
