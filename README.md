# 🛠️ Herramienta de Red 🛠️

¡Bienvenido a la Herramienta de Red! Una aplicación de escritorio sencilla y eficaz para visualizar información de tu red y realizar diagnósticos de conectividad.

## 🖼️ Interfaz de Usuario

Así es como se ve la aplicación:

```
+-----------------------------------------------------+
| Herramienta de Red                                  |
+-----------------------------------------------------+
|                                                     |
|  Tu dirección IP local:   [ 192.168.1.100 ]          |
|                                                     |
|  IP para hacer ping: [_________________] [ Ping ]   |
|                                                     |
|  +-----------------------------------------------+  |
|  |                                               |  |
|  |                                               |  |
|  |      Resultados del ping aparecerán aquí...   |  |
|  |                                               |  |
|  |                                               |  |
|  +-----------------------------------------------+  |
|                                                     |
|  +-----------------------------------------------+  |
|  | Cambiar Configuración de IP                   |  |
|  | ---------------------------                   |  |
|  | Cambiar la IP de forma programática es una    |  |
|  | operación delicada que requiere permisos de   |  |
|  | administrador...                              |  |
|  +-----------------------------------------------+  |
|                                                     |
+-----------------------------------------------------+
```

## ✨ Características Principales

*   **🛰️ Visualiza tu IP Local:** Descubre al instante la dirección IP de tu máquina en la red local.
*   **📡 Herramienta de Ping:** Envía pings a cualquier IP o dominio para comprobar si está en línea y accesible.

## 🚀 Cómo Empezar

### Requisitos

*   **Python 3.x**
*   La librería `tkinter` (normalmente viene con Python).

### Ejecución

1.  Abre tu terminal.
2.  Navega hasta el directorio donde se encuentra `app.py`.
3.  Ejecuta el siguiente comando:

    ```bash
    python app.py
    ```

## 📖 Guía de Uso

### Ver tu IP Local

Al iniciar la aplicación, tu IP local se mostrará automáticamente en la parte superior.

```
+-----------------------------------------------------+
|  Tu dirección IP local:   [ 192.168.1.100 ]          |
+-----------------------------------------------------+
```

### Hacer Ping a una IP

1.  Introduce la IP o el dominio en el campo de texto.
2.  Haz clic en el botón **"Ping"**.
3.  Los resultados se mostrarán en el área de texto inferior.

```
+-----------------------------------------------------+
|  IP para hacer ping: [ google.com      ] [ Ping ]   |
|                                                     |
|  +-----------------------------------------------+  |
|  |                                               |  |
|  | Haciendo ping a google.com [142.250.200.78]... |  |
|  | Respuesta desde 142.250.200.78: bytes=32...   |  |
|  |                                               |  |
|  +-----------------------------------------------+  |
+-----------------------------------------------------+
```

## ⚠️ Nota Importante

La sección **"Cambiar Configuración de IP"** es solo informativa. La aplicación **no modifica** la configuración de tu red. Cambiar estos ajustes de forma incorrecta puede causar problemas de conexión.