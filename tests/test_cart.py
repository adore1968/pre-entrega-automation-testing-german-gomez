import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.datos import leer_json_productos

PRODUCTOS = leer_json_productos("datos/productos.json")

@pytest.mark.ui
@pytest.mark.parametrize("producto", PRODUCTOS)
def test_agregar_producto_desde_json(usuario_logueado, producto):
  """
  Test que agrega cada producto del JSON al carrito
  """
  inventory_page = usuario_logueado
  nombre_producto = producto["nombre"]

  print(f"\n🛒 Agregando producto: {nombre_producto}")

  # Obtener contador inicial del carrito
  contador_inicial = inventory_page.obtener_contador_carrito()
  print(f"  Contador inicial {contador_inicial}")

  # Agregar producto específico
  inventory_page.agregar_producto_por_nombre(nombre_producto)

  # Verificar que el contador se incrementó
  contador_final = inventory_page.obtener_contador_carrito()
  print(f"  Contador final: {contador_final}")

  assert contador_final == contador_inicial + 1, f"El contador no se incrementó correctamente para {nombre_producto}"

  print (f" ✅ Producto agregado correctamente")

@pytest.mark.ui
def test_agregar_todos_los_productos(usuario_logueado):
  """
  Test que agrega todos los productos de una vez
  """
  inventory_page = usuario_logueado
  productos = leer_json_productos("datos/productos.json")

  print(f"\n🛒 Agregando {len(productos)} productos al carrito")

  contador_inicial = inventory_page.obtener_contador_carrito()

  for i, producto in enumerate(productos, 1):
    nombre_producto = producto["nombre"]
    print(f"  {i}. Agregando: {nombre_producto}")

    inventory_page.agregar_producto_por_nombre(nombre_producto)
    contador_actual = inventory_page.obtener_contador_carrito()

    assert contador_actual == contador_inicial + i, f"Contador incorrecto después de agregar {nombre_producto}"

  print(f"✅ Todos los productos agregados. Total en carrito: {contador_actual}")