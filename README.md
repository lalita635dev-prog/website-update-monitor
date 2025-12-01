# 🌐 Website Update Monitor v1.0

![Website Update Monitor](icono.png)

**¡Bienvenido al Website Update Monitor!**

Este software te permite monitorear sitios web y recibir notificaciones por email cuando detecta cambios en su contenido.

🔗 **[Descargar última versión](https://github.com/lalita635dev-prog/website-update-monitor/releases/latest)**

---

## ✨ Características

✅ Monitorea múltiples URLs simultáneamente  
✅ Notificaciones por email vía Gmail  
✅ Interfaz gráfica intuitiva y fácil de usar  
✅ Configuración personalizada para cada usuario  
✅ Detección automática de cambios en páginas web  
✅ No requiere conocimientos técnicos

---

## 💻 Requisitos del Sistema

- **Sistema Operativo:** Windows 7, 8, 10 u 11
- **Conexión a Internet** activa
- **Cuenta de Gmail** con verificación en 2 pasos
- **App Password de Gmail** (se explica cómo obtenerla en la app)

---

## 🚀 Guía de Uso Rápido

### 1️⃣ Configurar URLs a Monitorear

- Haz clic en "➕ Agregar URL"
- Ingresa la dirección web completa (http:// o https://)
- Repite para agregar más URLs
- Usa "🗑️ Eliminar URL" para quitar alguna

### 2️⃣ Configurar Gmail

- Ingresa tu correo de Gmail
- Ingresa tu App Password (contraseña de aplicación)
- Haz clic en "📖 Ver instrucciones" si necesitas ayuda

### 3️⃣ Probar la Configuración

- Haz clic en "🧪 Probar Configuración"
- El sistema verificará las URLs
- Enviará un email de prueba a tu correo
- Confirma que todo funciona correctamente

### 4️⃣ Guardar la Configuración

- Haz clic en "💾 Guardar Configuración"
- Tu configuración se guardará en `config.json`
- La próxima vez que abras la app, se cargará automáticamente

---

## 🔐 ¿Cómo obtener App Password?

Un **App Password** es una contraseña especial de 16 dígitos que Google genera para aplicaciones de terceros. Es **DIFERENTE** a tu contraseña de Gmail.

### Pasos para obtenerla:

1. Ve a [https://myaccount.google.com/](https://myaccount.google.com/)
2. Haz clic en **"Seguridad"** (menú izquierdo)
3. En **"Cómo inicias sesión en Google"**:
   - Activa la **"Verificación en dos pasos"** (si no está activa)
4. Busca **"Contraseñas de aplicaciones"**
5. Selecciona:
   - **Aplicación:** Correo
   - **Dispositivo:** Otro (escribe "Website Update Monitor")
6. Haz clic en **"Generar"**
7. Google te mostrará una contraseña de 16 caracteres
8. Cópiala y pégala en la app (sin espacios)

⚠️ **IMPORTANTE:** Guarda esta contraseña en un lugar seguro. No podrás verla nuevamente, pero puedes generar una nueva cuando quieras.

---

## 🛠️ Solución de Problemas

### ❌ "Error de autenticación al enviar email"

**Solución:**
- Verifica que tu email sea correcto
- Asegúrate de usar el App Password, no tu contraseña de Gmail
- Confirma que tienes verificación en 2 pasos activa
- Pega el App Password sin espacios

### ❌ "No se puede acceder a la URL"

**Solución:**
- Verifica que la URL sea correcta y esté completa
- Asegúrate de tener conexión a Internet
- Algunos sitios pueden bloquear accesos automáticos
- Intenta con otra URL para probar

### ❌ "No recibo el email de prueba"

**Solución:**
- Revisa tu carpeta de Spam/Correo no deseado
- Espera unos minutos, puede haber demora
- Verifica que tu conexión a Internet funcione
- Intenta regenerar el App Password

### ❌ "El ejecutable no abre"

**Solución:**
- Verifica que tu antivirus no lo esté bloqueando
- Ejecuta como administrador (clic derecho > Ejecutar como administrador)
- Descarga nuevamente si el archivo está corrupto

---

## 🔒 Seguridad y Privacidad

- ✅ Tus credenciales se guardan **SOLO en tu computadora**
- ⚠️ El archivo `config.json` contiene tu email y App Password - **NUNCA lo compartas**
- 🔓 Puedes eliminar el App Password desde tu cuenta de Google en cualquier momento
- 🚫 El software **NO** envía información a terceros
- 📧 Solo se comunica con Gmail para enviar notificaciones

---

## 📝 Notas Importantes

- El software requiere **conexión a Internet** para funcionar
- Gmail permite enviar aproximadamente **500 emails por día**
- Recomendamos no monitorear más de **50 URLs simultáneamente**
- Los cambios se detectan mediante **hash MD5** del contenido
- Cambios en publicidad o contenido dinámico también se detectan
- Para uso profesional, considera usar servicios dedicados

---

## 📦 Actualizaciones

**Versión actual:** 1.0

### Historial de Versiones

**v0.2 - Septiembre 2025**
- Monitoreo de web
- Notificaciones pop up


**v0.7 - Octubre 2025**
- Monitoreo de múltiples URL
- Notificaciones vía Gmail


**v1.0 - Noviembre 2025**
- Monitoreo de múltiples URLs simultáneamente
- Notificaciones por email vía Gmail
- Interfaz gráfica moderna e intuitiva
- Configuración persistente en JSON
- Sistema de prueba de configuración
- Detección de cambios mediante hash MD5


### 🔮 Próximamente
- Programación de verificaciones automáticas
- Historial de cambios detectados
- Soporte para más proveedores de email
- Notificaciones de escritorio
- Filtros personalizados de contenido

Para obtener actualizaciones y soporte:
- 🌐 Visita la [web oficial](https://lalita635dev-prog.github.io/website-update-monitor/)
- 📋 Revisa las [notas de la versión](https://github.com/lalita635dev-prog/website-update-monitor/releases)
- ⬇️ Descarga la última versión si está disponible

---

## 📄 Licencia y Uso

Este software se proporciona "tal cual" sin garantías de ningún tipo.  
El uso de este software es bajo tu propia responsabilidad.

El autor no se hace responsable de:
- Pérdida de datos
- Problemas con cuentas de Gmail
- Fallos en la detección de cambios
- Cualquier daño directo o indirecto

Se permite el uso personal y comercial de este software.

---

## 📞 Contacto y Soporte

**Creado por:** Lalita635

Si este software te ha sido útil, considera hacer una colaboración.  
Tu apoyo ayuda a mantener y mejorar el proyecto.

Para reportar bugs, sugerencias o consultas:
- 🐛 [Reportar un problema](https://github.com/lalita635dev-prog/website-update-monitor/issues)
- 💡 [Solicitar una función](https://github.com/lalita635dev-prog/website-update-monitor/issues)
- 📂 [Ver el código fuente](https://github.com/lalita635dev-prog/website-update-monitor)

---

<div align="center">

**¡Gracias por usar Website Update Monitor!**

⭐ Si te gusta este proyecto, dale una estrella en GitHub

</div>
