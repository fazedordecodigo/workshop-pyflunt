import pytest
from flask import Flask
from src.presentation.routes.version import version_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(version_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_version_route(client):
    response = client.get('/version')
    assert response.status_code == 200
    data = response.get_json()
    assert 'version' in data
    assert isinstance(data['version'], str)
