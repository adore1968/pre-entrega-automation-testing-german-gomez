from pages.inventory_page import InventoryPage
import logging


def test_catalog(usuario_logueado):
  inventory_page = InventoryPage(usuario_logueado)

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