# 🚀 Guía de Migración: Estructura Consolidada

## ¿Qué cambió?

Tu proyecto Django ahora está **completamente consolidado en una única carpeta `app/`** en lugar de tener archivos dispersos en el raíz.

### Antes (Viejo)
```
catalogo/
  settings.py
  urls.py
  wsgi.py
  asgi.py
peliculas/
  models.py
  views.py
accounts/
  views.py
manage.py
```

### Ahora (Nuevo)
```
app/
├── catalogo/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── apps/
│       ├── peliculas/
│       └── accounts/
manage_new.py
run.py
```

## ¿Por qué?

✅ **Mejor organización**: Todo el código está en una carpeta  
✅ **Más escalable**: Fácil de expandir con nuevas apps  
✅ **Más profesional**: Sigue patrones de proyectos grandes  
✅ **Menos conflictos**: Evita nombres de carpetas ambiguos  

## Pasos para usar la nueva estructura

### 1️⃣ Activar entorno virtual

**Windows:**
```bash
.\.venv\Scripts\activate
```

**Unix/Linux/macOS:**
```bash
source .venv/bin/activate
```

### 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3️⃣ Verificar configuración

```bash
python manage_new.py check
```

Deberías ver solo una advertencia sobre archivos estáticos (no es problema).

### 4️⃣ Aplicar migraciones

```bash
python manage_new.py migrate
```

### 5️⃣ Crear usuario admin

```bash
python manage_new.py createsuperuser
```

### 6️⃣ Cargar datos de ejemplo (opcional)

```bash
python manage_new.py seed
```

### 7️⃣ Iniciar servidor

```bash
python manage_new.py runserver
```

Accede a:
- **Catálogo**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

## Comandos Alternativos

Puedes usar cualquiera de estos indistintamente:

```bash
# Opción 1: Usar manage_new.py directamente
python manage_new.py runserver

# Opción 2: Usar el script wrapper (recomendado)
python run.py runserver

# Opción 3: Usar Make (si tienes make instalado)
make runserver
```

## Archivos Importantes

| Archivo | Ubicación | Descripción |
|---------|-----------|-------------|
| `manage_new.py` | Raíz | Punto de entrada para comandos Django |
| `run.py` | Raíz | Script wrapper alternativo |
| `settings.py` | `app/catalogo/` | Configuración de Django |
| `urls.py` | `app/catalogo/` | URLs principales |
| `wsgi.py` | `app/catalogo/` | Para producción (WSGI) |
| `asgi.py` | `app/catalogo/` | Para async (ASGI) |
| `models.py` | `app/catalogo/apps/peliculas/` | Modelos de BD |
| `views.py` | `app/catalogo/apps/peliculas/` | Vistas de películas |
| `.env` | Raíz | Variables de entorno |

## Variables de Entorno (.env)

```env
# Django
DJANGO_SECRET_KEY=changeme-en-produccion
DJANGO_DEBUG=1
DJANGO_USE_SQLITE=1
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# MySQL (opcional, si usas MySQL en lugar de SQLite)
MYSQL_DATABASE=catalogo_db
MYSQL_USER=root
MYSQL_PASSWORD=tu_contraseña
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
```

## Docker (Recomendado)

### Construir contenedores

```bash
docker-compose build
```

### Levantar servicios

```bash
docker-compose up -d
```

### Ver logs

```bash
docker-compose logs -f web
```

### Ejecutar comando dentro del contenedor

```bash
docker-compose exec web python manage_new.py createsuperuser
```

### Detener servicios

```bash
docker-compose down
```

## Troubleshooting

### ❌ Error: "No installed app with label 'peliculas'"

**Causa**: Estás usando `manage.py` viejo  
**Solución**: Usa `manage_new.py` o `run.py`

```bash
# ✅ Correcto
python manage_new.py migrate

# ❌ Incorrecto
python manage.py migrate
```

### ❌ Error: "ModuleNotFoundError: No module named 'app'"

**Causa**: No estás ejecutando desde la raíz del proyecto  
**Solución**: Asegúrate de estar en la raíz de `trabajofinal/`

```bash
# Correcto
cd C:\Users\Estudiante\Desktop\trabajofinal
python manage_new.py runserver
```

### ❌ Error: "DJANGO_SETTINGS_MODULE not set"

**Solución**: Usa `manage_new.py` que ya configura esto automáticamente

### ❌ Advertencia: "The directory ... in STATICFILES_DIRS does not exist"

**Esto es normal** - solo es una advertencia. Los archivos estáticos se encuentran donde deben.

## Integración Continua

Si estás usando CI/CD, actualiza los comandos a:

```bash
# En lugar de
python manage.py migrate

# Usa
python manage_new.py migrate
```

## Próximos Pasos

Una vez todo esté funcionando:

1. **Eliminar archivos antiguos** (cuando confirmes que todo funciona):
   - `catalogo/` (viejo)
   - `peliculas/` (viejo)
   - `accounts/` (viejo)
   - `manage.py` (viejo)
   - `asgi.py` (viejo)

2. **Renombrar archivos** (opcional):
   - `manage_new.py` → `manage.py`
   - `run.py` → Mantener como alias

3. **Actualizar documentación** en README principal

## Comandos Rápidos de Referencia

```bash
# Desarrollo
python manage_new.py runserver           # Iniciar servidor
python manage_new.py makemigrations      # Crear migraciones
python manage_new.py migrate             # Aplicar migraciones
python manage_new.py shell               # Shell interactivo
python manage_new.py test                # Ejecutar tests

# Crear datos
python manage_new.py createsuperuser     # Usuario admin
python manage_new.py seed                # Datos de ejemplo

# Admin
python manage_new.py changepassword      # Cambiar contraseña

# Utilidades
python manage_new.py check               # Verificar configuración
python manage_new.py collectstatic       # Recolectar archivos estáticos
```

## 📞 Soporte

Si tienes problemas:

1. Revisa este documento
2. Consulta `ESTRUCTURA_NUEVA.md` para más detalles
3. Verifica que estés en la carpeta correcta
4. Asegúrate de que el entorno virtual esté activado

¡Bienvenido a la estructura mejorada! 🎉
