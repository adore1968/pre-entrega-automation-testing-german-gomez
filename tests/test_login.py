from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest
from utils.datos import leer_csv_login
from utils.logger import logger 

CASOS_LOGIN = leer_csv_login("datos/login.csv")

@pytest.mark.ui
@pytest.mark.parametrize("usuario, clave, debe_funcionar, descripcion", CASOS_LOGIN)
def test_login_desde_csv(driver, usuario, clave, debe_funcionar, descripcion):
    """
    Test parametrizado que verifica el login con datos del CSV
    """

    logger.info("Iniciando login con usuario: %s", usuario)    

    # Paso 1: Abrir página de login
    login_page = LoginPage(driver)
    login_page.abrir()

    # Paso 2: Completar credenciales
    logger.info("Completando credenciales...")

    login_page.completar_usuario(usuario)
    login_page.completar_clave(clave)
    login_page.hacer_clic_login()

    if debe_funcionar:
        # Login exitoso: debe llegar al inventario
        logger.info("Verificando redireccion exitosa")

        assert "inventory.html" in driver.current_url, f"Login falló para {usuario}"

        inventory_page = InventoryPage(driver)
        titulo = inventory_page.obtener_titulo()
        assert titulo == "Products", f"Título incorrecto: {titulo}"

        logger.info("Test de login completado exitosamente")
    else:
        # Login fallido: debe mostrar error
        assert login_page.esta_error_visible(), f"No se mostró error para {usuario}"
        
        mensaje_error = login_page.obtener_mensaje_error()
        assert len(mensaje_error) > 0, "El mensaje de error está vacio"
        
        logger.info("Login fallo correctamente")