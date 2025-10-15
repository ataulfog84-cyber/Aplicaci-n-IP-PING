# Herramienta de Red

Una simple aplicación de escritorio para visualizar información de red y realizar diagnósticos básicos.

## Características

*   **Visualiza tu IP Local:** Muestra la dirección IP local de tu máquina en la red.
*   **Herramienta de Ping:** Permite enviar solicitudes de ping a cualquier dirección IP o nombre de dominio para verificar su conectividad.

## Requisitos

*   Python 3.x
*   La librería `tkinter` (generalmente incluida en la instalación estándar de Python).

## ¿Cómo usar la aplicación?

1.  **Ejecutar la aplicación:**
    Abre una terminal o línea de comandos y ejecuta el siguiente comando en el directorio del proyecto:
    ```bash
    python app.py
    ```

2.  **Ver tu IP Local:**
    La aplicación mostrará automáticamente tu dirección IP local en la parte superior de la ventana.

3.  **Hacer Ping:**
    *   Introduce la dirección IP o el nombre de dominio que deseas verificar en el campo de texto "IP para hacer ping".
    *   Haz clic en el botón "Ping".
    *   Los resultados del ping aparecerán en el cuadro de texto inferior.

## Nota sobre "Cambiar Configuración de IP"

La sección "Cambiar Configuración de IP" es puramente informativa. Explica que la modificación de la configuración de red es una operación sensible que requiere privilegios de administrador y conocimientos técnicos para evitar problemas de conexión. La aplicación **no** realiza cambios en la configuración de red.
