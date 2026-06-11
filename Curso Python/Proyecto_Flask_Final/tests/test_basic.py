"""Tests básicos de la página principal.
# * Ideal como primer smoke test para validar que la app arranca.
"""

def test_index_page(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b'Bienvenido' in res.data
