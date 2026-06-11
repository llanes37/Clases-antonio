"""Tests de permisos por rol."""

def test_admin_panel_forbidden_for_student(client):
    # * Un alumno no debe poder entrar en el panel admin
    client.post(
        "/login",
        data={"email": "alumno@test.local", "password": "alumno123"},
        follow_redirects=True,
    )
    response = client.get("/admin")
    assert response.status_code == 403


def test_admin_panel_ok_for_admin(client):
    # * Un admin si debe tener acceso
    client.post(
        "/login",
        data={"email": "admin@test.local", "password": "admin123"},
        follow_redirects=True,
    )
    response = client.get("/admin")
    assert response.status_code == 200
    assert b"Panel de administracion" in response.data
