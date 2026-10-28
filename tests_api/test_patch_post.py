import requests
import pytest

URL = "https://jsonplaceholder.typicode.com/posts/1"

PATCH_PAYLOAD = {
  "title": "Titulo actualizado por PATCH"
}

@pytest.mark.api
def test_patch_post(post_by_id_url):
  url = post_by_id_url(1)

  r = requests.patch(URL, json=PATCH_PAYLOAD)

  assert r.status_code == 200

  body = r.json()

  assert body["title"] == "Titulo actualizado por PATCH"

  assert "body" in body

  assert "userId" in body

  print(f"PATCH completado - Solo titulo actualizado")