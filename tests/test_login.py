from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest
from utils.datos import leer_csv_login

CASOS_LOGIN = leer_csv_login("datos/login.csv")

@pytest.mark.parametrize("usuario, clave, debe_funcionar, descripcion", CASOS_LOGIN)
def test_login_desde_csv(driver, usuario, clave, debe_funcionar, descripcion):
    """
    Test parametrizado que verifica el login con datos del CSV
    """

    print(f"\n🧪 Probando: {descripcion}")
    print(f"  Usuario: {usuario}")
    print(f"  Debe funcionar: {'✅' if debe_funcionar else '❌'}")

    # Paso 1: Abrir página de login
    login_page = LoginPage(driver)
    login_page.abrir()

    # Paso 2: Completar credenciales
    login_page.completar_usuario(usuario)
    login_page.completar_clave(clave)
    login_page.hacer_clic_login()

    if debe_funcionar:
        # Login exitoso: debe llegar al inventario
        assert "inventory.html" in driver.current_url, f"Login falló para {usuario}"

        inventory_page = InventoryPage(driver)
        titulo = inventory_page.obtener_titulo()
        assert titulo == "Products", f"Título incorrecto: {titulo}"
        print(f"  ✅ Login exitoso - llegó al inventario")
    else:
        # Login fallido: debe mostrar error
        assert login_page.esta_error_visible(), f"No se mostró error para {usuario}"
        
        mensaje_error = login_page.obtener_mensaje_error()
        assert len(mensaje_error) > 0, "El mensaje de error está vacio"
        print(f"  ❌ Login falló correctamente - Error: {mensaje_error}")