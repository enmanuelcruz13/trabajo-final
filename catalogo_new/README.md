Catalogo nuevo (catalogo_new)

Proyecto Django mínimo creado dentro del repositorio en `catalogo_new/`.

Comandos rápidos (desde la raíz del repo):

- Crear venv e instalar deps:
  - python -m venv .venv
  - \.venv\Scripts\activate  (Windows) o source .venv/bin/activate (Unix)
  - pip install -r catalogo_new/requirements.txt

- Migrar y ejecutar (usar MySQL o SQLite según variables de entorno):
  - python catalogo_new/manage.py migrate
  - python catalogo_new/manage.py runserver
