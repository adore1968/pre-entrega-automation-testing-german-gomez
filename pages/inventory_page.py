from selenium.webdriver.common.by import By

class InventoryPage:
  def __init__(self, driver):
    self.driver = driver
    
    self.titulo = (By.CSS_SELECTOR, "div.header_secondary_container .title")
    self.logo = (By.CLASS_NAME, "app_logo")

    self.productos = (By.CLASS_NAME, "inventory_item")
    self.filtros = (By.CLASS_NAME, "select_container")
    self.menu = (By.CLASS_NAME, "bm-burger-button")

    self.nombre_producto = (By.CLASS_NAME, "inventory_item_name")
    self.precio_producto = (By.CLASS_NAME, "inventory_item_price")

    self.boton_producto = (By.TAG_NAME, "button")

    self.badge = (By.CLASS_NAME, "shopping_cart_badge")
    self.link_carrito = (By.CLASS_NAME, "shopping_cart_link")


  def obtener_titulo(self):
    return self.driver.find_element(*self.titulo).text

  def obtener_logo(self):
    return self.driver.find_element(*self.logo).text
  
  def obtener_productos(self):
    return self.driver.find_elements(*self.productos)

  def obtener_filtros(self):
    return self.driver.find_element(*self.filtros)

  def obtener_menu(self):
    return self.driver.find_element(*self.menu)
  
  def obtener_nombre_producto(self, producto):
    return producto.find_element(*self.nombre_producto).text

    
  def obtener_precio_producto(self, producto):
    return producto.find_element(*self.precio_producto).text

  def agregar_al_carrito(self, producto):
    producto.find_element(*self.boton_producto).click()

  def obtener_badge(self): 
    return self.driver.find_element(*self.badge).text

  def ir_al_carrito(self):
    self.driver.find_element(*self.link_carrito).click()