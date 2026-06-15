Resumen rápido

- Este repositorio es una pequeña app Django llamada "catalogo" (manage.py, catalogo/, app peliculas/) con soporte Docker (Dockerfile, docker-compose.yml). Tiene seed data y un script de creación de BD en scripts/create_db.py.

Acciones importantes que un agente debe saber

- Leer README.md primero: contiene los comandos exactos para venv, instalación, migraciones, y atajos de Make/Docker.
- No borrar db.sqlite3 ni la carpeta .venv sin confirmación explícita.

Cómo ejecutar (rápido)

- Entorno virtual (Windows): `python -m venv .venv` then `\.venv\Scripts\activate` (Unix: `source .venv/bin/activate`).
- Instalar dependencias: `pip install -r requirements.txt`.
- Migrar y arrancar servidor (local rápido usando SQLite o MySQL según env): `python manage.py migrate` then `python manage.py runserver`.
- Crear superusuario: `python manage.py createsuperuser`.
- Poblar datos de ejemplo: `python manage.py seed`.

Docker (recomendado para usar mysqlclient)

- Construir y levantar: `make build` && `make up` o `docker-compose up --build`.
- docker-compose arranca MySQL (servicio db) y la app web. La compose file ha sido ajustada para permitir contraseña MySQL vacía en desarrollo (MYSQL_ALLOW_EMPTY_PASSWORD).

Detalles técnicos / configuración de BD

- Django usa MySQL vía mysqlclient y lee credenciales desde variables de entorno (MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT). Si no se pasan, PASSWORD por defecto queda vacío — esto permite conexiones con root sin contraseña en desarrollo.
- El archivo scripts/create_db.py crea la DB si falta y ya funciona con contraseña vacía.

Advertencias de seguridad

- Permitir contraseña vacía (MYSQL_ALLOW_EMPTY_PASSWORD) es inseguro. Úsalo solo en desarrollo local o entornos controlados. Para producción, establecer MYSQL_ROOT_PASSWORD y variables seguras.

Qué no hacer sin permiso

- No cambiar Dockerfile a otra versión de Python ni eliminar .venv sin confirmación.
- No eliminar artefactos como db.sqlite3 ni archivos de migraciones sin verificar con el usuario.

Dónde mirar primero

- README.md, docker-compose.yml, Dockerfile, catalogo/settings.py, peliculas/management/commands/seed.py, scripts/create_db.py.

Confirmación antes de commits

- He aplicado cambios menores en docker-compose.yml para permitir contraseña vacía. También crearé `.env.example` y commitearé los cambios si confirmas.

Commit sugerido

- "Configure MySQL for development (allow empty root password) and add .env.example"

Siguiente paso

- Si quieres que haga push a un remoto, dime a qué remoto/branch; no hago push sin permiso.
