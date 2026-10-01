# Proyecto de Automatización QA - SauceDemo

Proyecto de automatización de pruebas funcionales sobre la plataforma SauceDemo, desarrollado utilizando Python, Selenium WebDriver y Pytest.

## Propósito

El objetivo del proyecto es automatizar diferentes casos de prueba sobre la plataforma SauceDemo, verificando el funcionamiento del inicio de sesión, la navegación por el catálogo de productos y la interacción con el carrito de compras.

## Tecnologías utilizadas

* Python
* Selenium WebDriver
* Pytest
* pytest-html
* Google Chrome

## Pruebas automatizadas

### Inicio de sesión

* Navegación a la página de inicio de sesión.
* Ingreso de credenciales válidas.
* Verificación de redirección a `/inventory.html`.
* Verificación del título "Products".
* Verificación de "Swag Labs".

### Catálogo de productos

* Verificación del título de la página de inventario.
* Verificación de la presencia de productos.
* Verificación de elementos importantes de la interfaz.
* Obtención del nombre y precio del primer producto.

### Carrito de compras

* Agregado de un producto al carrito.
* Verificación del contador del carrito.
* Navegación hacia la página del carrito.
* Verificación de que el producto agregado coincida con el seleccionado.

## Instalación

Instalar las dependencias necesarias mediante:

```bash
pip install selenium pytest pytest-html
```

## Ejecución de las pruebas

Para ejecutar las pruebas:

```bash
pytest -v
```

Para ejecutar las pruebas y generar un reporte HTML:

```bash
pytest -v --html=reporte.html
```

El reporte se generará en el archivo `reporte.html`.

## Reporte de ejecución

El proyecto utiliza `pytest-html` para generar un reporte HTML con los resultados de la ejecución de las pruebas.

## Sitio utilizado

SauceDemo:

https://www.saucedemo.com/

## Credenciales de prueba

Usuario:

```text
standard_user
```

Contraseña:

```text
secret_sauce
```
