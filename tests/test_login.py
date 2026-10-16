from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import logging

from utils.waits import wait_for_url


def test_login(driver):
  logging.info("Iniciando prueba de SauceDemo")
  login_page = LoginPage(driver)
  
  login_page.abrir()
  
  login_page.iniciar_sesion("standard_user", "secret_sauce")
  
  wait_for_url(driver, "/inventory.html")
  
  inventory_page = InventoryPage(driver)
  
  titulo = inventory_page.obtener_titulo()
  
  assert titulo == "Products"
  
  app_logo = inventory_page.obtener_logo()
  
  assert app_logo == "Swag Labs"
  
  logging.info("Login realizado correctamente")