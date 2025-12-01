import tkinter as tk
from tkinter import messagebox, simpledialog
import hashlib
import smtplib
from email.mime.text import MIMEText
import json
import os
import urllib.request
import urllib.error

CONFIG_FILE = "config.json"

# ---------------------- UTILIDADES ----------------------
def cargar_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"urls": [], "email": "", "app_password": ""}

def guardar_config(cfg):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=4)

def hash_contenido(url):
    """Obtiene el hash del contenido de una URL usando urllib (incluido en Python)"""
    try:
        # Crear request con headers para evitar bloqueos
        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            contenido = response.read()
            return hashlib.md5(contenido).hexdigest()
    except urllib.error.HTTPError as e:
        return None, f"HTTP Error {e.code}: {e.reason}"
    except urllib.error.URLError as e:
        return None, f"URL Error: {e.reason}"
    except Exception as e:
        return None, f"Error: {str(e)}"

def enviar_mail(destinatario, app_password, mensaje):
    """Envía email usando las credenciales del usuario"""
    msg = MIMEText(mensaje, 'plain', 'utf-8')
    msg["Subject"] = "Actualización detectada en una página web"
    msg["From"] = destinatario
    msg["To"] = destinatario

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(destinatario, app_password)
            server.send_message(msg)
        return True, ""
    except smtplib.SMTPAuthenticationError:
        return False, "Error de autenticación. Verifica tu email y App Password."
    except smtplib.SMTPException as e:
        return False, f"Error SMTP: {str(e)}"
    except Exception as e:
        return False, f"Error: {str(e)}"

# ---------------------- GUI ----------------------
class WebMonitorApp:
    def __init__(self, root):
        self.root = root
        root.title("Website Update Monitor - Configuración")
        root.geometry("550x650")
        root.configure(bg="#f0f4ff")
        
        # Evitar que se pueda redimensionar demasiado pequeño
        root.minsize(550, 650)

        self.cfg = cargar_config()

        # Título principal
        titulo = tk.Label(root, text="Website Update Monitor", 
                font=("Segoe UI", 16, "bold"), 
                bg="#f0f4ff", 
                fg="#2c3e50")
        titulo.pack(pady=10)

        subtitulo = tk.Label(root, text="Monitor de actualizaciones de sitios web", 
                font=("Segoe UI", 9, "italic"), 
                bg="#f0f4ff", 
                fg="#7f8c8d")
        subtitulo.pack()

        # ========== SECCIÓN URLs ==========
        tk.Label(root, text="📋 URLs a Monitorear:", 
                font=("Segoe UI", 11, "bold"), 
                bg="#f0f4ff",
                fg="#34495e").pack(pady=(10,5))

        # Lista de URLs
        self.urls_list = tk.Listbox(root, width=60, height=8, 
                                    font=("Consolas", 9),
                                    selectmode=tk.SINGLE)
        self.urls_list.pack(pady=5)
        for url in self.cfg.get("urls", []):
            self.urls_list.insert(tk.END, url)

        # Botones de URL
        frm_urls = tk.Frame(root, bg="#f0f4ff")
        frm_urls.pack(pady=5)

        tk.Button(frm_urls, text="➕ Agregar URL", 
                 command=self.agregar_url, 
                 bg="#3498db", fg="white",
                 font=("Segoe UI", 9, "bold"),
                 cursor="hand2",
                 padx=10, pady=5).grid(row=0, column=0, padx=5)
        
        tk.Button(frm_urls, text="🗑️ Eliminar URL", 
                 command=self.eliminar_url, 
                 bg="#e74c3c", fg="white",
                 font=("Segoe UI", 9, "bold"),
                 cursor="hand2",
                 padx=10, pady=5).grid(row=0, column=1, padx=5)

        # Línea separadora
        tk.Frame(root, height=2, bg="#bdc3c7").pack(fill="x", padx=20, pady=15)

        # ========== SECCIÓN EMAIL ==========
        tk.Label(root, text="📧 Configuración de Gmail:", 
                font=("Segoe UI", 11, "bold"), 
                bg="#f0f4ff",
                fg="#34495e").pack(pady=(5,10))

        # Email
        frm_email = tk.Frame(root, bg="#f0f4ff")
        frm_email.pack(pady=5)
        
        tk.Label(frm_email, text="Correo Gmail:", 
                bg="#f0f4ff", 
                font=("Segoe UI", 9)).grid(row=0, column=0, sticky="e", padx=5)
        
        self.email_entry = tk.Entry(frm_email, width=35, font=("Segoe UI", 9))
        self.email_entry.grid(row=0, column=1, padx=5)
        self.email_entry.insert(0, self.cfg.get("email", ""))

        # App Password
        frm_pass = tk.Frame(root, bg="#f0f4ff")
        frm_pass.pack(pady=5)
        
        tk.Label(frm_pass, text="App Password:", 
                bg="#f0f4ff", 
                font=("Segoe UI", 9)).grid(row=0, column=0, sticky="e", padx=5)
        
        self.password_entry = tk.Entry(frm_pass, width=35, 
                                       show="•", 
                                       font=("Segoe UI", 9))
        self.password_entry.grid(row=0, column=1, padx=5)
        self.password_entry.insert(0, self.cfg.get("app_password", ""))

        # Botón mostrar/ocultar contraseña
        self.mostrar_pass = tk.BooleanVar(value=False)
        tk.Checkbutton(frm_pass, text="Mostrar", 
                      variable=self.mostrar_pass,
                      command=self.toggle_password,
                      bg="#f0f4ff",
                      font=("Segoe UI", 8)).grid(row=0, column=2, padx=5)

        # Información de ayuda
        info_text = "ℹ️ ¿Cómo obtener tu App Password de Gmail?"
        tk.Label(root, text=info_text, 
                bg="#fff3cd", 
                fg="#856404",
                font=("Segoe UI", 8),
                cursor="hand2",
                padx=10, pady=5).pack(pady=10, fill="x", padx=20)
        
        help_btn = tk.Button(root, text="📖 Ver instrucciones", 
                            command=self.mostrar_ayuda,
                            bg="#ffc107", 
                            font=("Segoe UI", 8, "bold"),
                            cursor="hand2",
                            padx=10, pady=3)
        help_btn.pack()

        # Línea separadora
        tk.Frame(root, height=2, bg="#bdc3c7").pack(fill="x", padx=20, pady=15)

        # ========== BOTONES DE ACCIÓN ==========
        frm_botones = tk.Frame(root, bg="#f0f4ff")
        frm_botones.pack(pady=10)

        tk.Button(frm_botones, text="💾 Guardar Configuración", 
                 command=self.guardar, 
                 bg="#27ae60", fg="white",
                 font=("Segoe UI", 10, "bold"),
                 cursor="hand2",
                 padx=15, pady=8).grid(row=0, column=0, padx=5)

        tk.Button(frm_botones, text="🧪 Probar Configuración", 
                 command=self.probar, 
                 bg="#f39c12", fg="white",
                 font=("Segoe UI", 10, "bold"),
                 cursor="hand2",
                 padx=15, pady=8).grid(row=0, column=1, padx=5)

        # Estado
        self.status_label = tk.Label(root, text="Website Update Monitor v1.0", 
                                     bg="#f0f4ff", 
                                     font=("Segoe UI", 8, "italic"),
                                     fg="#7f8c8d")
        self.status_label.pack(pady=5)

        # ========== CRÉDITOS ==========
        tk.Frame(root, height=1, bg="#bdc3c7").pack(fill="x", padx=20, pady=10)
        
        creditos_frame = tk.Frame(root, bg="#f0f4ff")
        creditos_frame.pack(pady=5)
        
        tk.Label(creditos_frame, text="By Lalita635", 
                bg="#f0f4ff", 
                font=("Segoe UI", 8, "bold"),
                fg="#34495e").pack()
        
        links_frame = tk.Frame(creditos_frame, bg="#f0f4ff")
        links_frame.pack()
                
        colabora_label = tk.Label(links_frame, text="Colabora: http://bit.ly/4fS0yUa", 
                                bg="#f0f4ff", 
                                font=("Segoe UI", 7),
                                fg="#e67e22",
                                cursor="hand2")
        colabora_label.pack(side="left", padx=5)
        colabora_label.bind("<Button-1>", lambda e: self.abrir_link("http://bit.ly/4fS0yUa"))

    def toggle_password(self):
        """Muestra u oculta la contraseña"""
        if self.mostrar_pass.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="•")

    def mostrar_ayuda(self):
        """Muestra instrucciones para obtener App Password"""
        ayuda = """
📧 CÓMO OBTENER TU APP PASSWORD DE GMAIL:

1️⃣ Ve a tu cuenta de Google:
   https://myaccount.google.com/

2️⃣ En el menú izquierdo, selecciona "Seguridad"

3️⃣ Busca la sección "Cómo inicias sesión en Google"

4️⃣ Activa la "Verificación en dos pasos" (si no está activa)

5️⃣ Busca "Contraseñas de aplicaciones" 
   (aparece después de activar verificación en 2 pasos)

6️⃣ Selecciona "Correo" y "Otro (nombre personalizado)"

7️⃣ Escribe "Website Update Monitor" como nombre

8️⃣ Google te dará una contraseña de 16 caracteres

9️⃣ Copia esa contraseña y pégala aquí

⚠️ IMPORTANTE: 
   - Esta contraseña es DIFERENTE a tu contraseña de Gmail
   - Es específica para esta aplicación
   - La puedes revocar en cualquier momento
   - No incluyas espacios al pegarla
        """
        messagebox.showinfo("Website Update Monitor - Ayuda", ayuda)

    def agregar_url(self):
        url = simpledialog.askstring("Nueva URL", 
                                     "Ingresa la URL a monitorear:\n(ejemplo: https://ejemplo.com)")
        if url:
            url = url.strip()
            if url.startswith("http://") or url.startswith("https://"):
                self.urls_list.insert(tk.END, url)
                self.status_label.config(text="✅ URL agregada. No olvides guardar la configuración.", 
                                       fg="#27ae60")
            else:
                messagebox.showwarning("URL inválida", 
                                      "La URL debe comenzar con http:// o https://")

    def eliminar_url(self):
        sel = self.urls_list.curselection()
        if sel:
            self.urls_list.delete(sel)
            self.status_label.config(text="🗑️ URL eliminada. No olvides guardar la configuración.", 
                                   fg="#e67e22")
        else:
            messagebox.showwarning("Selección", "Por favor selecciona una URL para eliminar")

    def guardar(self):
        urls = list(self.urls_list.get(0, tk.END))
        email = self.email_entry.get().strip()
        app_password = self.password_entry.get().strip()

        # Validaciones
        if not urls:
            messagebox.showwarning("URLs vacías", "Agrega al menos una URL para monitorear")
            return

        if not email:
            messagebox.showwarning("Email vacío", "Ingresa tu correo Gmail")
            return

        if not app_password:
            messagebox.showwarning("Password vacía", 
                                  "Ingresa tu App Password de Gmail\n\n" +
                                  "Presiona '📖 Ver instrucciones' para saber cómo obtenerla")
            return

        if "@gmail.com" not in email.lower():
            respuesta = messagebox.askyesno("Confirmar email", 
                                           f"El email '{email}' no parece ser de Gmail.\n\n" +
                                           "¿Estás seguro que es correcto?")
            if not respuesta:
                return

        self.cfg["urls"] = urls
        self.cfg["email"] = email
        self.cfg["app_password"] = app_password
        
        guardar_config(self.cfg)
        self.status_label.config(text="✅ Configuración guardada correctamente", 
                               fg="#27ae60")
        messagebox.showinfo("Website Update Monitor - Guardado", 
                          f"✅ Configuración guardada:\n\n" +
                          f"• URLs: {len(urls)}\n" +
                          f"• Email: {email}\n" +
                          f"• Password: {'*' * len(app_password)}")

    def probar(self):
        urls = list(self.urls_list.get(0, tk.END))
        email = self.email_entry.get().strip()
        app_password = self.password_entry.get().strip()

        if not urls or not email or not app_password:
            messagebox.showerror("Error", 
                               "⚠️ Configura URLs, email y password antes de probar.\n\n" +
                               "Luego presiona 'Guardar Configuración'")
            return

        self.status_label.config(text="🔄 Probando configuración...", fg="#3498db")
        self.root.update()

        # Probar URLs
        problemas = []
        for url in urls:
            resultado = hash_contenido(url)
            if resultado is None or (isinstance(resultado, tuple) and resultado[0] is None):
                if isinstance(resultado, tuple):
                    problemas.append(f"{url}\n   → {resultado[1]}")
                else:
                    problemas.append(f"{url}\n   → Error desconocido")

        # Probar email
        email_ok = False
        email_error = ""
        resultado_email = enviar_mail(email, app_password, 
                               "✅ Prueba exitosa del Website Update Monitor.\n\n" +
                               "Tu configuración de email funciona correctamente.")
        email_ok, email_error = resultado_email

        # Mostrar resultados
        mensaje = ""
        
        if problemas:
            mensaje += "❌ PROBLEMAS CON URLs:\n\n"
            for problema in problemas:
                mensaje += f"{problema}\n\n"
        else:
            mensaje += "✅ Todas las URLs son accesibles\n\n"

        if email_ok:
            mensaje += "✅ Email de prueba enviado correctamente\n"
            mensaje += f"   Revisa tu bandeja: {email}"
            self.status_label.config(text="✅ Prueba completada exitosamente", 
                                   fg="#27ae60")
        else:
            mensaje += "❌ ERROR al enviar email:\n"
            mensaje += f"   {email_error}\n\n"
            mensaje += "Verifica:\n"
            mensaje += "  • Que el email sea correcto\n"
            mensaje += "  • Que el App Password sea correcto (sin espacios)\n"
            mensaje += "  • Que tengas verificación en 2 pasos activa\n"
            mensaje += "  • Que tengas conexión a internet"
            self.status_label.config(text="❌ Error en la configuración de email", 
                                   fg="#e74c3c")

        if problemas or not email_ok:
            messagebox.showerror("Website Update Monitor - Resultados", mensaje)
        else:
            messagebox.showinfo("¡Éxito!", mensaje)


if __name__ == "__main__":
    root = tk.Tk()
    app = WebMonitorApp(root)
    root.mainloop()
