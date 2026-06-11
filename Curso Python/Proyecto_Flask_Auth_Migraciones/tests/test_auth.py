"""Tests basicos de autenticacion."""

def test_register_and_login(client):
    response = client.post(
        "/register",
        data={"nombre": "Nuevo", "email": "nuevo@test.local", "password": "clave123"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Ya puedes iniciar sesion" in response.data

    response = client.post(
        "/login",
        data={"email": "nuevo@test.local", "password": "clave123"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Bienvenido" in response.data


def test_private_route_requires_login(client):
    # * Si no hay sesion, /perfil debe redirigir a login
    response = client.get("/perfil", follow_redirects=False)
    assert response.status_code == 302
