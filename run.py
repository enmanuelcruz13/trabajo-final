#!/usr/bin/env python
"""
Script wrapper para ejecutar comandos de Django con la nueva estructura consolidada.
Uso: python run.py [comando]

Ejemplo:
  python run.py runserver
  python run.py migrate
  python run.py createsuperuser
"""

import os
import sys
from pathlib import Path

def setup_django():
    """Configura el entorno de Django"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalogo.settings')
    
    # Asegura que la ruta está disponible
    current = Path(__file__).resolve().parent
    if str(current) not in sys.path:
        sys.path.insert(0, str(current))

def main():
    setup_django()
    
    from django.core.management import execute_from_command_line
    
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nComandos comunes:")
        print("  python run.py runserver           - Iniciar servidor de desarrollo")
        print("  python run.py migrate             - Aplicar migraciones")
        print("  python run.py createsuperuser     - Crear usuario admin")
        print("  python run.py seed                - Cargar datos de ejemplo")
        print("  python run.py shell               - Shell interactivo de Django")
        print("  python run.py test                - Ejecutar tests")
        sys.exit(1)
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
