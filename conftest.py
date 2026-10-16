import pytest
from utils.driver import create_driver
from pages.login_page import LoginPage
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
  login_page.iniciar_sesion("standard_user", "secret_sauce")

  wait_for_url(driver, "/inventory.html")

  return driver