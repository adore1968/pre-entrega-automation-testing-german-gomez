import requests
import pytest

URL = "https://jsonplaceholder.typicode.com/posts/1"

@pytest.mark.api
def test_delete_post():
  r = requests.delete(URL)

  assert r.status_code == 200

  body = r.json()

  assert body == {} or "id" not in body or body["id"] is None

  print("DELETE completado - Recurso eliminado")