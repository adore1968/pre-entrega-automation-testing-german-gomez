from pages.inventory_page import InventoryPage
import logging
from utils.waits import wait_for_url
from pages.cart_page import CartPage

def test_cart(usuario_logueado):
  inventory_page = InventoryPage(usuario_logueado)

  productos = inventory_page.obtener_productos()

  assert len(productos) > 0

  producto = productos[0]

  nombre_producto = inventory_page.obtener_nombre_producto(producto)

  inventory_page.agregar_al_carrito(producto)
  
  badge = inventory_page.obtener_badge()
  
  assert badge == "1"
  
  inventory_page.ir_al_carrito()

  wait_for_url(usuario_logueado, "/cart.html")

  cart_page = CartPage(usuario_logueado)

  productos_carrito = cart_page.obtener_productos_carrito()

  assert len(productos_carrito) > 0

  producto_carrito = productos_carrito[0]

  nombre_producto_carrito = cart_page.obtener_nombre_producto_carrito(producto_carrito)

  assert nombre_producto == nombre_producto_carrito

  logging.info("Prueba finalizada correctamente")