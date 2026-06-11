"""Tests de la API de cursos (CRUD completo).

Secuencia:
- Crear -> Listar -> Detalle -> Actualizar -> Borrar
"""


def test_crud_cursos(client):
    # Crear
    r = client.post('/api/cursos', json={"titulo": "Nuevo", "descripcion": "Prueba", "publicado": True})
    assert r.status_code == 201
    data = r.get_json()
    cid = data["id"]

    # Listar
    r = client.get('/api/cursos')
    assert r.status_code == 200
    lista = r.get_json()
    assert any(c['id'] == cid for c in lista)

    # Detalle
    r = client.get(f'/api/cursos/{cid}')
    assert r.status_code == 200
    assert r.get_json()['titulo'] == 'Nuevo'

    # Actualizar
    r = client.put(f'/api/cursos/{cid}', json={"titulo": "Actualizado"})
    assert r.status_code == 200
    assert r.get_json()['titulo'] == 'Actualizado'

    # Borrar
    r = client.delete(f'/api/cursos/{cid}')
    assert r.status_code == 200
    assert r.get_json()['deleted'] is True
