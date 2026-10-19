import pytest
from utils.driver import create_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.waits import wait_for_url

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