import requests
import pytest

URL = "https://reqres.in/api/users?page=1"

@pytest.mark.api
def test_get_users():
  r = requests.get(URL)

  assert r.status_code == 200

  data = r.json()

  assert data["page"] == 1

  assert len(data["data"]) > 0 

  data = r.json()

  assert {"id", "email", "first_name", "last_name"} <= set(data.keys())

