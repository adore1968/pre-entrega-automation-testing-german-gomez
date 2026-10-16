from selenium.webdriver.common.by import By
from tests.test_catalog import test_catalog
from tests.test_login import test_login
from utils.waits import wait_for_url
import logging
from pages.cart_page import CartPage


logging.basicConfig(
    filename="ejecucion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

def test_saucedemo(driver):
  try:
    test_login(driver)

    test_catalog()

    # 4) Interaccion con productos
    inventory_page.agregar_al_carrito(producto)
  
    badge = inventory_page.obtener_badge()
  
    assert badge == "1"
  
    inventory_page.ir_al_carrito()

    wait_for_url(driver, "/cart.html")

    cart_page = CartPage(driver)

    productos_carrito = cart_page.obtener_productos_carrito()

    assert len(productos_carrito) > 0

    producto_carrito = productos_carrito[0]

    nombre_producto_carrito = cart_page.obtener_nombre_producto_carrito(producto_carrito)

    assert nombre_producto == nombre_producto_carrito

    logging.info("Prueba finalizada correctamente")
  except Exception:
    logging.exception("La prueba falló")
    driver.save_screenshot("captura_fallo.png")
    raise