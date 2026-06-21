.PHONY: help build up down logs shell migrate createsuperuser seed clean test runserver

help:
	@echo "Catálogo de Películas - Comandos disponibles"
	@echo ""
	@echo "Desarrollo local:"
	@echo "  make venv           - Crear entorno virtual"
	@echo "  make install        - Instalar dependencias"
	@echo "  make migrate        - Aplicar migraciones"
	@echo "  make createsuperuser- Crear usuario admin"
	@echo "  make seed           - Cargar datos de ejemplo"
	@echo "  make runserver      - Iniciar servidor"
	@echo "  make test           - Ejecutar tests"
	@echo ""
	@echo "Docker:"
	@echo "  make build          - Construir contenedores"
	@echo "  make up             - Levantar servicios"
	@echo "  make down           - Detener servicios"
	@echo "  make logs           - Ver logs"
	@echo "  make shell          - Shell en el contenedor web"
	@echo ""
	@echo "Limpieza:"
	@echo "  make clean          - Limpiar archivos generados"
	@echo "  make clean-db       - Eliminar base de datos"

venv:
	python -m venv .venv
	@echo "Entorno virtual creado. Actívalo con: .\.venv\Scripts\activate (Windows) o source .venv/bin/activate (Unix)"

install:
	pip install -r requirements.txt

migrate:
	python manage_new.py migrate

createsuperuser:
	python manage_new.py createsuperuser

seed:
	python manage_new.py seed

runserver:
	python manage_new.py runserver

shell:
	python manage_new.py shell

test:
	python manage_new.py test

makemigrations:
	python manage_new.py makemigrations

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f web

docker-shell:
	docker-compose exec web bash

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true

clean-db:
	@echo "⚠️  Esto eliminará la base de datos SQLite"
	@read -p "¿Está seguro? (s/n) " -n 1 -r; \
	echo; \
	if [[ $$REPLY =~ ^[Ss]$$ ]]; then \
		rm -f db.sqlite3; \
		echo "✓ Base de datos eliminada"; \
	fi

fresh: clean migrate createsuperuser seed
	@echo "✓ Proyecto reiniciado completamente"
