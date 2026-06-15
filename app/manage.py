#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalogo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise
    # Ensure the app path is on sys.path when running from repo root
    current = Path(__file__).resolve().parent
    if str(current) not in sys.path:
        sys.path.insert(0, str(current))
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
