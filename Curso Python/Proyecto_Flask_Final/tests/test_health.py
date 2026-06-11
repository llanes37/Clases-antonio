"""Tests del endpoint de healthcheck."""

def test_health(client):
    r = client.get('/api/health')
    assert r.status_code == 200
    data = r.get_json()
    assert data.get('status') == 'ok'
    assert 'cursos' in data and 'usuarios' in data
