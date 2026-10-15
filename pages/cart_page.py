from selenium.webdriver.common.by import By

class CartPage:
  def __init__(self, driver):
    self.driver = driver
    self.productos_carrito = (By.CLASS_NAME,"cart_item")
    self.nombre_producto_carrito = (By.CLASS_NAME, "inventory_item_name")

  def obtener_productos_carrito(self):
    return self.driver.find_elements(*self.productos_carrito)

  def obtener_nombre_producto_carrito(self, producto):
    return producto.find_element(*self.nombre_producto_carrito).text

