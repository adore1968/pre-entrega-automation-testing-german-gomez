import requests
import pytest
CREATE_URL = "https://reqres.in/api/users"
from datetime import datetime, timezone

@pytest.mark.api
@pytest.mark.parametrize("name, job", [("Matias QA", "tester"), ("Jose", "front end developer"), ("Lucia", "back end developer"), ("Julian", "ux/ui designer")])
def test_create_user(name, job):
  payload = {"name": name, "job": job}

  r = requests.post(CREATE_URL, json=payload)

  assert r.status_code == 201 

  current_year = datetime.now(timezone.utc).year

  new_user = r.json()

  assert "id" in new_user and "createdAt" in new_user

  assert str(current_year) in new_user["createdAt"]