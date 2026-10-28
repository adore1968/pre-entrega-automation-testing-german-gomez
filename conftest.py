import pytest
from utils.driver import create_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.waits import wait_for_url
import requests

@pytest.fixture
def driver():
  driver = create_driver()

  yield driver

  driver.quit()

@pytest.fixture
def usuario_logueado(driver):
  login_page = LoginPage(driver)
  login_page.abrir()
  login_page.login_completo("standard_user", "secret_sauce")

  assert "inventory.html" in driver.current_url

  return InventoryPage(driver)

BASE_URL = 'https://jsonplaceholder.typicode.com'

@pytest.fixture(scope="module")
def posts_url():
  return f"{BASE_URL}/posts"

@pytest.fixture(scope="module")
def post_by_id_url():
  def _get_url(post_id):
    return f"{BASE_URL}/posts/{post_id}"
  return _get_url

@pytest.fixture(scope="module")
def created_post():
  """Crea un post y devuelve sus datos para otros tests"""
  payload = {"title": "Post para testing", "body": "Contenido de prueba", "userId": 1}

  response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)

  assert response.status_code == 201
  return response.json()

