import requests
import pytest
LOGIN_URL = "https://reqres.in/api/login"

@pytest.mark.api
@pytest.mark.parametrize("email, password, esperado", [("eve.holt@reqres.in", "cityslicka", 200), ("german.holt@reqres.in", None, 400)])
def test_login_api(email, password, esperado):
  creds = {"email": email, "password": password}

  resp = requests.post(LOGIN_URL, json=creds)

  assert resp.status_code == esperado

  if (esperado == 200):
    assert "token" in resp.json()
  


