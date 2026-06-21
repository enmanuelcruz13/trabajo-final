# 🔧 Documentación Técnica - Estructura Consolidada

## Índice

1. [Arquitectura](#arquitectura)
2. [Módulo de Configuración](#módulo-de-configuración)
3. [Aplicaciones](#aplicaciones)
4. [Importaciones](#importaciones)
5. [Rutas y URLs](#rutas-y-urls)
6. [Variables de Entorno](#variables-de-entorno)
7. [Deployment](#deployment)
8. [Testing](#testing)

---

## Arquitectura

### Árbol de Directorios

```
trabajofinal/                              # Raíz del proyecto
├── .venv/                                 # Entorno virtual
├── app/                                   # 🎯 ESTRUCTURA CONSOLIDADA
│   ├── __init__.py
│   ├── catalogo/                          # Config principal
│   │   ├── __init__.py
│   │   ├── settings.py                    # ⚙️ Configuración
│   │   ├── urls.py                        # 🔗 URLs
│   │   ├── views.py                       # 📄 Vistas generales
│   │   ├── wsgi.py                        # 🌐 WSGI
│   │   ├── asgi.py                        # ⚡ ASGI
│   │   └── apps/                          # Aplicaciones
│   │       ├── __init__.py
│   │       ├── peliculas/
│   │       │   ├── __init__.py
│   │       │   ├── apps.py
│   │       │   ├── models.py
│   │       │   ├── views.py
│   │       │   ├── urls.py
│   │       │   ├── forms.py
│   │       │   ├── admin.py
│   │       │   ├── migrations/
│   │       │   │   ├── __init__.py
│   │       │   │   └── 0001_initial.py
│   │       │   └── tests.py
│   │       └── accounts/
│   │           ├── __init__.py
│   │           ├── apps.py
│   │           ├── views.py
│   │           ├── urls.py
│   │           └── tests.py
│   └── __init__.py
├── templates/                             # 🎨 Templates
│   ├── base.html
│   ├── peliculas/
│   └── registration/
├── static/                                # 📦 Archivos estáticos
│   ├── css/
│   ├── js/
│   └── img/
├── scripts/                               # 🔨 Scripts útiles
│   └── create_db.py
├── db.sqlite3                             # 💾 BD SQLite
├── manage_new.py                          # ✨ Punto de entrada
├── run.py                                 # ✨ Wrapper alternativo
├── manage.py                              # 🚫 ANTIGUO (no usar)
├── Makefile                               # 📋 Comandos
├── docker-compose.yml                     # 🐳 Docker
├── Dockerfile                             # 🐳 Docker
├── requirements.txt                       # 📦 Dependencias
├── .env                                   # 🔐 Variables de entorno
└── README.md                              # 📖 Documentación
```

### Cambio de Módulos

| Aspecto | Estructura Antigua | Estructura Nueva |
|---------|-------------------|------------------|
| **Settings** | `catalogo.settings` | `app.catalogo.settings` |
| **URLs** | `catalogo.urls` | `app.catalogo.urls` |
| **WSGI** | `catalogo.wsgi` | `app.catalogo.wsgi` |
| **ASGI** | `asgi.py` (root) | `app.catalogo.asgi` |
| **App Peliculas** | `peliculas` | `app.catalogo.apps.peliculas` |
| **App Accounts** | `accounts` | `app.catalogo.apps.accounts` |

---

## Módulo de Configuración

### `app/catalogo/settings.py`

```python
# INSTALLED_APPS - Todas las apps registradas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.catalogo.apps.peliculas',      # ✨ Ruta completa
    'app.catalogo.apps.accounts',       # ✨ Ruta completa
]

# ROOT_URLCONF - Punto de entrada de URLs
ROOT_URLCONF = 'app.catalogo.urls'

# WSGI_APPLICATION - Para production
WSGI_APPLICATION = 'app.catalogo.wsgi.application'
```

### BASE_DIR

```python
# Apunta a la raíz del proyecto (trabajofinal/)
# Desde: app/catalogo/settings.py
#        └─ parent.parent.parent.parent = trabajofinal/
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Permite acceder a:
# - templates/
# - static/
# - db.sqlite3
```

---

## Aplicaciones

### Estructura de Apps

Cada app sigue la estructura estándar de Django:

```
app/catalogo/apps/peliculas/
├── __init__.py
├── apps.py              # Configuración de la app
├── models.py            # Modelos de BD
├── views.py             # Vistas
├── urls.py              # URLs de la app
├── forms.py             # Formularios
├── admin.py             # Admin de Django
├── tests.py             # Tests
└── migrations/
    ├── __init__.py
    └── 0001_initial.py
```

### Configuración de Apps (`apps.py`)

```python
# app/catalogo/apps/peliculas/apps.py
from django.apps import AppConfig

class PeliculasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.catalogo.apps.peliculas'  # ✨ Ruta completa
```

### Registrar en INSTALLED_APPS

```python
# app/catalogo/settings.py
INSTALLED_APPS = [
    'app.catalogo.apps.peliculas',       # ✨ Ruta completa
    'app.catalogo.apps.accounts',        # ✨ Ruta completa
]
```

---

## Importaciones

### Importar Modelos

```python
# Desde app.catalogo.apps.peliculas.models
from app.catalogo.apps.peliculas.models import Pelicula, Genero

# Desde app.catalogo.apps.accounts (si existieran modelos)
from app.catalogo.apps.accounts.models import CustomUser
```

### Importar Vistas

```python
# Desde urls.py
from app.catalogo.apps.peliculas import views

# Desde otro módulo
from app.catalogo.apps.peliculas.views import index, detalle
```

### Importar Formularios

```python
from app.catalogo.apps.peliculas.forms import PeliculaForm
```

### Importar Configuración

```python
from django.conf import settings

# Acceder a variables de entorno
DEBUG = settings.DEBUG
SECRET_KEY = settings.SECRET_KEY
```

---

## Rutas y URLs

### Configuración de URLs

#### URL Principal (`app/catalogo/urls.py`)

```python
from django.contrib import admin
from django.urls import path, include
from .views import healthz

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include apps
    path('', include('app.catalogo.apps.peliculas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('app.catalogo.apps.accounts.urls')),
    # Health check
    path('healthz', healthz),
]
```

#### URLs de Peliculas (`app/catalogo/apps/peliculas/urls.py`)

```python
from django.urls import path
from . import views

app_name = 'peliculas'

urlpatterns = [
    path('', views.index, name='index'),
    path('pelicula/<int:pk>/', views.detalle, name='detalle'),
    path('pelicula/<int:pk>/favorito/', views.toggle_favorito, name='toggle_favorito'),
    path('pelicula/<int:pk>/calificar/', views.calificar_pelicula, name='calificar_pelicula'),
    path('favoritos/', views.mis_favoritos, name='mis_favoritos'),
    path('agregar/', views.agregar_pelicula, name='agregar_pelicula'),
]
```

### Acceder a URLs desde Templates

```html
<!-- Usar namespace de app -->
<a href="{% url 'peliculas:index' %}">Catálogo</a>
<a href="{% url 'peliculas:detalle' pk=pelicula.id %}">Ver película</a>

<!-- Accounts -->
<a href="{% url 'login' %}">Login</a>
<a href="{% url 'accounts:register' %}">Registro</a>
```

---

## Variables de Entorno

### Archivo `.env`

```env
# Django
DJANGO_SECRET_KEY=tu-clave-secreta-aqui
DJANGO_DEBUG=1
DJANGO_USE_SQLITE=1
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# MySQL (si DJANGO_USE_SQLITE=0)
MYSQL_DATABASE=catalogo_db
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
```

### Acceder desde Python

```python
import os
from dotenv import load_dotenv

load_dotenv()

debug = os.getenv('DJANGO_DEBUG', '1') == '1'
secret = os.getenv('DJANGO_SECRET_KEY', 'default')
```

---

## Deployment

### WSGI (Para Gunicorn/uWSGI)

```python
# app/catalogo/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.catalogo.settings')
application = get_wsgi_application()

# Ejecutar con:
# gunicorn app.catalogo.wsgi:application
```

### ASGI (Para Daphne/Hypercorn)

```python
# app/catalogo/asgi.py
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.catalogo.settings')
application = get_asgi_application()

# Ejecutar con:
# daphne -b 0.0.0.0 -p 8000 app.catalogo.asgi:application
```

### Docker

```dockerfile
# Dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage_new.py", "runserver", "0.0.0.0:8000"]
```

---

## Testing

### Crear Tests

```python
# app/catalogo/apps/peliculas/tests.py
from django.test import TestCase
from .models import Pelicula, Genero

class PeliculaTestCase(TestCase):
    def setUp(self):
        self.genero = Genero.objects.create(nombre='Acción')
        self.pelicula = Pelicula.objects.create(
            titulo='Test',
            genero=self.genero
        )
    
    def test_pelicula_creation(self):
        self.assertEqual(self.pelicula.titulo, 'Test')
```

### Ejecutar Tests

```bash
# Todos los tests
python manage_new.py test

# Tests específicos de una app
python manage_new.py test app.catalogo.apps.peliculas

# Tests específicos de un módulo
python manage_new.py test app.catalogo.apps.peliculas.tests.PeliculaTestCase
```

---

## Troubleshooting Técnico

### Problema: "ModuleNotFoundError: No module named 'app'"

**Causa**: No estás en la raíz del proyecto  
**Solución**:
```bash
cd C:\Users\Estudiante\Desktop\trabajofinal
python manage_new.py check
```

### Problema: "Import error: cannot import name"

**Causa**: Rutas de importación incorrectas  
**Solución**: Usa las rutas completas:
```python
# ❌ Incorrecto
from peliculas.models import Pelicula

# ✅ Correcto
from app.catalogo.apps.peliculas.models import Pelicula
```

### Problema: "App 'peliculas' doesn't have a 'migrations' module"

**Causa**: Carpeta de migraciones no existe  
**Solución**:
```bash
python manage_new.py makemigrations
python manage_new.py migrate
```

### Problema: Migraciones no se aplican

**Causa**: Usas `manage.py` antiguo  
**Solución**: Usa `manage_new.py`
```bash
# ❌ Incorrecto
python manage.py migrate

# ✅ Correcto
python manage_new.py migrate
```

---

## Referencias

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Apps](https://docs.djangoproject.com/en/5.0/ref/applications/)
- [Django URLs](https://docs.djangoproject.com/en/5.0/topics/http/urls/)
- [Django WSGI](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/)

---

**Última actualización**: Junio 2026  
**Versión**: 1.0 - Estructura Consolidada
