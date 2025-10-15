
import tkinter as tk
from tkinter import scrolledtext
import socket
import subprocess
import platform

def get_local_ip():
    """
    Encuentra la dirección IP local.
    """
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # No es necesario que se pueda conectar, solo para obtener la interfaz
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception as e:
        ip = f"No se pudo obtener la IP: {e}"
    finally:
        if s:
            s.close()
    return ip

def ping_ip():
    """
    Hace ping a la dirección IP especificada en el cuadro de entrada.
    """
    ip_to_ping = ping_entry.get()
    if not ip_to_ping:
        ping_results.delete(1.0, tk.END)
        ping_results.insert(tk.END, "Por favor, introduce una dirección IP.")
        return

    ping_results.delete(1.0, tk.END)
    ping_results.insert(tk.END, f"Haciendo ping a {ip_to_ping}...")
    
    # Actualiza la GUI para mostrar el mensaje "Haciendo ping..."
    app.update_idletasks()

    try:
        # Parámetro de ping dependiente del sistema operativo
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        
        # Oculta la ventana de la consola en Windows
        startupinfo = None
        if platform.system().lower() == 'windows':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        command = ['ping', param, '4', ip_to_ping]
        
        result = subprocess.run(command, capture_output=True, text=True, startupinfo=startupinfo, timeout=10)
        
        ping_results.delete(1.0, tk.END)
        if result.returncode == 0:
            ping_results.insert(tk.END, result.stdout)
        else:
            ping_results.insert(tk.END, result.stderr)
            
    except subprocess.TimeoutExpired:
        ping_results.delete(1.0, tk.END)
        ping_results.insert(tk.END, "El ping ha caducado. El host puede no ser alcanzable.")
    except Exception as e:
        ping_results.delete(1.0, tk.END)
        ping_results.insert(tk.END, f"Ha ocurrido un error: {e}")


# --- Configuración de la GUI ---
app = tk.Tk()
app.title("Herramienta de Red")
app.geometry("500x500")

# --- Frame para la IP Local ---
ip_frame = tk.Frame(app, pady=5)
ip_frame.pack(fill='x', padx=10)

local_ip_label = tk.Label(ip_frame, text="Tu dirección IP local:")
local_ip_label.pack(side='left')

local_ip_value = tk.Label(ip_frame, text=get_local_ip(), font=('Helvetica', 10, 'bold'))
local_ip_value.pack(side='left', padx=5)

# --- Frame para Ping ---
ping_frame = tk.Frame(app, pady=5)
ping_frame.pack(fill='x', padx=10)

ping_label = tk.Label(ping_frame, text="IP para hacer ping:")
ping_label.pack(side='left')

ping_entry = tk.Entry(ping_frame)
ping_entry.pack(side='left', fill='x', expand=True, padx=5)

ping_button = tk.Button(ping_frame, text="Ping", command=ping_ip)
ping_button.pack(side='left')

# --- Resultados de Ping ---
ping_results = scrolledtext.ScrolledText(app, height=15)
ping_results.pack(fill='both', expand=True, padx=10, pady=5)

# --- Frame para Cambiar IP ---
change_ip_frame = tk.LabelFrame(app, text="Cambiar Configuración de IP", pady=5)
change_ip_frame.pack(fill='x', padx=10, pady=10)

change_ip_info = tk.Label(
    change_ip_frame, 
    text="Cambiar la IP de forma programática es una operación delicada\nque requiere permisos de administrador y conocer detalles de la red\n(nombre de la interfaz, máscara de subred, puerta de enlace).\nUna configuración incorrecta puede causar la pérdida de conexión a la red.",
    justify='left',
    fg='grey'
)
change_ip_info.pack(pady=5, padx=5)


# --- Iniciar la aplicación ---
app.mainloop()
