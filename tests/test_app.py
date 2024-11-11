from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_root_deve_retornar_ok_e_ola_mundo_do_html():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/respostaHTML')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert '<h1> Olá Mundo </h1>' in response.text
