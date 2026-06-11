"""Tests de subida y descarga de ficheros."""
import io

def test_upload_and_download_file(client):
    # Crear un archivo en memoria
    data = {
        'file': (io.BytesIO(b'contenido de prueba'), 'demo.txt')
    }
    r = client.post('/files/upload', data=data, content_type='multipart/form-data')
    assert r.status_code == 200
    filename = r.get_json()['filename']

    # Descargar
    r = client.get(f'/files/download/{filename}')
    assert r.status_code == 200
    assert r.data.startswith(b'contenido')
