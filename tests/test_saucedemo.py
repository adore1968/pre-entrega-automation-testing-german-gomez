from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized") # El navegador se abrira en ventana grande


driver = webdriver.Chrome(options=options)

driver.implicitly_wait(5) # Espera implicita de 5 segundos

try:
  driver.get("https://www.saucedemo.com/")

  # 1) Login
  driver.find_element(By.ID, "user-name").send_keys("standard_user")
  driver.find_element(By.ID, "password").send_keys("secret_sauce")

  driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

  # 2) Validar login exitoso
  assert "/inventory.html" in driver.current_url

  titulo = driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text

  assert titulo == "Products"

  # 3) Comprobar existencia de productos y elementos importantes de la interfaz
  productos = driver.find_elements(By.CLASS_NAME,"inventory_item")

  assert len(productos) > 0

  # filtros = driver.find_element(By.CLASS_NAME, "select_container")

  producto = productos[0]

  nombreProducto = producto.find_element(By.CLASS_NAME, "inventory_item_name").text
  precioProducto = producto.find_element(By.CLASS_NAME, "inventory_item_price").text

  print(f"Nombre del producto: {nombreProducto}. Precio: ${precioProducto}")

  # 4) Interaccion con productos
  producto.find_element(By.TAG_NAME, "button").click()

  badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

  assert badge == "1"

  driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

  assert "/cart.html" in driver.current_url

  productosCarrito = driver.find_elements(By.CLASS_NAME,"cart_item")

  productoCarrito = productosCarrito[0]

  nombreProductoCarrito = productoCarrito.find_element(By.CLASS_NAME, "inventory_item_name").text

  assert nombreProducto == nombreProductoCarrito
finally:
  driver.quit()