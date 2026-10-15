from utils.driver import create_driver
from selenium.webdriver.common.by import By
from utils.waits import wait_for_url
import logging
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

logging.basicConfig(
    filename="ejecucion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

driver = create_driver()

def test_saucedemo():
  try:
    logging.info("Iniciando prueba de SauceDemo")
    # Login

    login_page = LoginPage(driver)

    login_page.abrir()

    login_page.iniciar_sesion("standard_user", "secret_sauce")

    # 2) Validar login exitoso
    wait_for_url(driver, "/inventory.html")

    inventory_page = InventoryPage(driver)

    titulo = inventory_page.obtener_titulo()

    assert titulo == "Products"

    app_logo = inventory_page.obtener_logo()

    assert app_logo == "Swag Labs"

    logging.info("Login realizado correctamente")

    # 3) Comprobar existencia de productos y elementos importantes de la interfaz
    productos = inventory_page.obtener_productos()

    assert len(productos) > 0

    filtros = inventory_page.obtener_filtros()
    assert filtros.is_displayed()

    menu = inventory_page.obtener_menu()
    assert menu.is_displayed()

    logging.info("Productos encontrados correctamente")

    producto = productos[0]

    nombre_producto = inventory_page.obtener_nombre_producto(producto)
    precio_producto = inventory_page.obtener_precio_producto(producto)

    print(f"Nombre del producto: {nombre_producto}. Precio: ${precio_producto}")

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
  finally:
    driver.quit()