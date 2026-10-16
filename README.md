# Proyecto de Automatización QA - SauceDemo

Proyecto de automatización de pruebas funcionales sobre la plataforma **SauceDemo**, desarrollado utilizando **Python, Selenium WebDriver y Pytest**.

## Propósito

El objetivo del proyecto es automatizar casos de prueba funcionales para verificar el inicio de sesión, la navegación por el catálogo de productos y la interacción con el carrito de compras.

El proyecto utiliza el patrón de diseño **Page Object Model (POM)** para organizar las interacciones con la aplicación y facilitar el mantenimiento y la reutilización del código.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Google Chrome

## Estructura del proyecto

```text
.
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_catalog.py
│   └── test_cart.py
├── utils/
│   ├── driver.py
│   └── waits.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Pruebas automatizadas

### Inicio de sesión

- Apertura de la página de inicio de sesión.
- Ingreso de credenciales válidas.
- Espera de la redirección a `/inventory.html`.
- Verificación del título **Products**.
- Verificación del logo **Swag Labs**.

### Catálogo de productos

- Verificación de la presencia de productos.
- Verificación de la visibilidad de los filtros y el menú.
- Obtención del nombre y precio del primer producto.

### Carrito de compras

- Selección y agregado de un producto al carrito.
- Verificación del contador del carrito.
- Navegación a la página del carrito.
- Verificación de la presencia del producto agregado.
- Comparación del producto seleccionado con el producto del carrito.

## Instalación

Se recomienda utilizar un entorno virtual de Python.

Crear el entorno virtual:

```bash
python -m venv .venv
```

Activarlo en Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Se requiere tener Google Chrome instalado. Selenium WebDriver administra el controlador del navegador según la configuración del entorno.

## Ejecución de las pruebas

Para ejecutar todos los tests y mostrar su resultado detallado:

```bash
python -m pytest -v
```

Para ejecutar un archivo de pruebas específico:

```bash
python -m pytest tests/test_login.py -v
```

Para ejecutar las pruebas y generar un reporte HTML:

```bash
python -m pytest -v --html=reporte.html
```

El reporte se genera en el archivo `reporte.html`, en el directorio desde el que se ejecuta el comando.

## Evidencias de ejecución

Según la configuración y las funcionalidades implementadas, pueden generarse archivos como:

- `reporte.html`: reporte HTML de pytest.
- `ejecucion.log`: registro de eventos de ejecución.
- `captura_fallo.png`: captura de pantalla ante un fallo, si está implementada esa lógica.

Estos archivos son artefactos locales de ejecución y no forman parte de los tests en sí.

## Sitio bajo prueba

[SauceDemo](https://www.saucedemo.com/)

## Credenciales de prueba

Usuario:

```text
standard_user
```

Contraseña:

```text
secret_sauce
```
