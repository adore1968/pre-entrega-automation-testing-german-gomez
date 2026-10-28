import requests 
import pytest
import time

payload = {
  "id": 1,
  "title": "Automation Testing Guide",
  "body": "Guía completa de testing",
  "userId": 1
}

@pytest.mark.api
def test_put_post(post_by_id_url):
  url = post_by_id_url(1)

  start = time.time()

  r = requests.put(url, json=payload)

  assert r.status_code == 200

  body = r.json()

  assert body["title"] == "Automation Testing Guide"
  
  assert body["body"] == "Guía completa de testing"

  assert body["id"] == 1

  r.elapsed.total_seconds() < 1

  print(f"PUT completado")