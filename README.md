# Proyecto de Automatización QA - SauceDemo

Proyecto de automatización de pruebas funcionales sobre la plataforma **SauceDemo**, desarrollado utilizando **Python, Selenium WebDriver y Pytest**.

## Propósito

El objetivo del proyecto es automatizar diferentes casos de prueba sobre la plataforma SauceDemo, verificando el funcionamiento del inicio de sesión, la navegación por el catálogo de productos y la interacción con el carrito de compras.

Además, el proyecto incorpora mecanismos de registro de ejecución, generación de reportes HTML y captura automática de evidencia ante fallos.

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
* Verificación del título **"Products"**.
* Verificación de **"Swag Labs"**.

### Catálogo de productos

* Verificación del título de la página de inventario.
* Verificación de la presencia de productos.
* Verificación de elementos importantes de la interfaz.
* Obtención del nombre y precio del primer producto.

### Carrito de compras

* Agregado de un producto al carrito.
* Verificación del contador del carrito.
* Navegación hacia la página del carrito.
* Verificación de la presencia del producto agregado.
* Verificación de que el producto del carrito coincida con el producto seleccionado.

## Evidencias y registro de ejecución

El proyecto incluye mecanismos para facilitar el análisis de las ejecuciones:

* **Reporte HTML:** generado mediante `pytest-html`.
* **Logs de ejecución:** registrados automáticamente en `ejecucion.log`.
* **Capturas de pantalla:** generadas automáticamente cuando una prueba falla.

## Instalación

Instalar las dependencias necesarias mediante:

```bash
pip install selenium pytest pytest-html
```

## Ejecución de las pruebas

Para ejecutar las pruebas:

```bash
python -m pytest -v
```

Para ejecutar las pruebas y generar un reporte HTML:

```bash
python -m pytest -v --html=reporte.html
```

El reporte se generará en el archivo:

```text
reporte.html
```

## Archivos de evidencia

Luego de ejecutar las pruebas, pueden generarse los siguientes archivos en el directorio del proyecto:

```text
ejecucion.log
reporte.html
captura_fallo.png
```

`captura_fallo.png` se genera únicamente cuando ocurre un fallo durante la ejecución de una prueba.

## Sitio utilizado

**SauceDemo:** https://www.saucedemo.com/

## Credenciales de prueba

**Usuario:**

```text
standard_user
```

**Contraseña:**

```text
secret_sauce
```
