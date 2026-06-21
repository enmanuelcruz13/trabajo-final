# Catálogo de Películas - Django Consolidado

Este proyecto ha sido reorganizado en una **única carpeta** (`app/`) con toda la configuración de Django centralizada.

## Nueva Estructura

```
app/
├── catalogo/                          # Configuración principal de Django
│   ├── __init__.py
│   ├── settings.py                    # Configuración centralizada
│   ├── urls.py                        # URLs principales
│   ├── views.py                       # Vistas generales
│   ├── wsgi.py                        # WSGI para producción
│   ├── asgi.py                        # ASGI para async
│   └── apps/                          # Aplicaciones Django
│       ├── peliculas/                 # App de películas
│       │   ├── apps.py
│       │   ├── models.py
│       │   ├── views.py
│       │   ├── urls.py
│       │   ├── forms.py
│       │   ├── admin.py
│       │   └── migrations/
│       └── accounts/                  # App de cuentas de usuario
│           ├── apps.py
│           ├── views.py
│           ├── urls.py
│           └── migrations/
├── __init__.py
templates/                             # Plantillas compartidas
static/                                # Archivos estáticos
db.sqlite3                            # Base de datos (SQLite por defecto)
manage_new.py                         # Nuevo manage.py configurado
.env                                  # Variables de entorno
requirements.txt                      # Dependencias Python
```

## Cambios Principales

- **Ruta de Django Settings**: `app.catalogo.settings` (antes: `catalogo.settings`)
- **URLs**: `app.catalogo.urls` (antes: `catalogo.urls`)
- **WSGI**: `app.catalogo.wsgi` (antes: `catalogo.wsgi`)
- **Apps**: `app.catalogo.apps.peliculas` y `app.catalogo.apps.accounts`

## Instalación y Ejecución

### 1. Crear y activar entorno virtual

```bash
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# Unix/Linux/macOS
source .venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Preparar variables de entorno

Crear o actualizar archivo `.env`:

```env
DJANGO_SECRET_KEY=changeme-in-production
DJANGO_DEBUG=1
DJANGO_USE_SQLITE=1
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
```

### 4. Ejecutar migraciones

```bash
python manage_new.py migrate
```

### 5. Crear superusuario (admin)

```bash
python manage_new.py createsuperuser
```

### 6. Cargar datos de ejemplo (opcional)

```bash
python manage_new.py seed
```

### 7. Iniciar servidor de desarrollo

```bash
python manage_new.py runserver
```

Accede a:
- **Catálogo**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

## Uso con Docker

### Construir y levantar servicios

```bash
make build
make up
```

### Comandos útiles

```bash
make shell    # Shell interactivo en el contenedor
make logs     # Ver logs en tiempo real
make stop     # Detener los servicios
```

## Base de Datos

### SQLite (Default en desarrollo)

Por defecto, el proyecto usa SQLite. La base de datos se crea automáticamente en `db.sqlite3`.

### MySQL (Producción)

Para usar MySQL, establece `DJANGO_USE_SQLITE=0` en `.env` y configura:

```env
DJANGO_USE_SQLITE=0
MYSQL_DATABASE=catalogo_db
MYSQL_USER=root
MYSQL_PASSWORD=tu_contraseña
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
```

## Estructura de Apps

### Peliculas (`app.catalogo.apps.peliculas`)

Gestiona el catálogo de películas, géneros, favoritos y calificaciones.

**Modelos:**
- `Genero`: Categorías de películas
- `Pelicula`: Información de películas
- `Favorito`: Películas marcadas como favoritas
- `Calificacion`: Puntuaciones de usuarios

**Rutas:**
- `/` - Catálogo principal
- `/pelicula/<id>/` - Detalle de película
- `/pelicula/<id>/favorito/` - Alternar favorito
- `/pelicula/<id>/calificar/` - Calificar película
- `/favoritos/` - Mis películas favoritas
- `/agregar/` - Agregar nueva película

### Accounts (`app.catalogo.apps.accounts`)

Maneja autenticación y registro de usuarios.

**Rutas:**
- `/accounts/register/` - Registro de usuario
- `/accounts/login/` - Iniciar sesión (Django built-in)
- `/accounts/logout/` - Cerrar sesión (Django built-in)

## Stack Tecnológico

- Python 3.13
- Django 5.x
- SQLite3 / MySQL
- Bootstrap 5
- HTML5 / CSS3 / JavaScript
- Docker & Docker Compose

## Características

✅ Catálogo de películas con búsqueda  
✅ Filtrado por género  
✅ Sistema de favoritos  
✅ Sistema de calificaciones (1-5 estrellas)  
✅ Autenticación de usuarios  
✅ Panel de administración  
✅ Dockerizado para fácil despliegue  
✅ Soporte para videos de YouTube  

## Variables de Entorno Disponibles

| Variable | Descripción | Default |
|----------|-------------|---------|
| `DJANGO_SECRET_KEY` | Clave secreta de Django | `dev-secret-change-in-production` |
| `DJANGO_DEBUG` | Modo debug | `1` (activado) |
| `DJANGO_USE_SQLITE` | Usar SQLite en lugar de MySQL | `1` (activado) |
| `DJANGO_ALLOWED_HOSTS` | Hosts permitidos | `localhost,127.0.0.1,0.0.0.0` |
| `MYSQL_DATABASE` | Nombre de BD MySQL | `catalogo_db` |
| `MYSQL_USER` | Usuario MySQL | `root` |
| `MYSQL_PASSWORD` | Contraseña MySQL | `` (vacía) |
| `MYSQL_HOST` | Host de MySQL | `127.0.0.1` |
| `MYSQL_PORT` | Puerto de MySQL | `3306` |

## Despliegue en Render

1. Conectar repositorio a Render
2. Establecer variables de entorno
3. Configurar comando de inicio: `python manage_new.py runserver 0.0.0.0:8000`
4. Ejecutar migraciones en Render post-deploy

## Próximos Pasos

- [ ] Reemplazar el antiguo `manage.py` por `manage_new.py` (cuando esté confirmado)
- [ ] Crear sistema de notificaciones
- [ ] Agregar más filtros avanzados
- [ ] Implementar API REST con DRF
- [ ] Agregar tests automatizados

## Notas Importantes

⚠️ **Seguridad**: En producción:
- Cambiar `DJANGO_SECRET_KEY`
- Establecer `DJANGO_DEBUG=0`
- Usar contraseñas fuertes en MySQL
- Configurar `ALLOWED_HOSTS` correctamente
- Usar variables de entorno seguras

📝 **Migración desde la estructura anterior**:
Si necesitas migrar datos del antiguo proyecto, ejecuta:
```bash
python manage_new.py dumpdata --all > backup.json
```

## Support

Para reportar problemas o sugerencias:
https://github.com/anomalyco/opencode
