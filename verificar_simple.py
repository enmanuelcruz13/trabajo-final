#!/usr/bin/env python
"""
Verificador de Estructura Consolidada
Usa este script para verificar que todo esta configurado correctamente.

Uso: python verificar_simple.py
"""

import os
import sys
from pathlib import Path

def print_header(text):
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")

def check_file_exists(path, description):
    full_path = Path(__file__).parent / path
    if full_path.exists():
        print(f"[OK] {description}")
        return True
    else:
        print(f"[FAIL] {description}")
        print(f"       Esperado en: {full_path}")
        return False

def check_directory_exists(path, description):
    full_path = Path(__file__).parent / path
    if full_path.is_dir():
        print(f"[OK] {description}")
        return True
    else:
        print(f"[FAIL] {description}")
        print(f"       Esperado en: {full_path}")
        return False

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.catalogo.settings')
    
    print_header("VERIFICACION DE ESTRUCTURA CONSOLIDADA")
    
    checks = []
    
    # Verificar directorios principales
    print("[DIRECTORIOS] Directorios principales:")
    checks.append(check_directory_exists('app', 'Carpeta app/'))
    checks.append(check_directory_exists('app/catalogo', 'Carpeta app/catalogo/'))
    checks.append(check_directory_exists('app/catalogo/apps', 'Carpeta app/catalogo/apps/'))
    checks.append(check_directory_exists('app/catalogo/apps/peliculas', 'Carpeta de peliculas'))
    checks.append(check_directory_exists('app/catalogo/apps/accounts', 'Carpeta de accounts'))
    
    # Verificar archivos de configuración
    print("\n[CONFIG] Archivos de configuración:")
    checks.append(check_file_exists('app/catalogo/settings.py', 'settings.py'))
    checks.append(check_file_exists('app/catalogo/urls.py', 'urls.py'))
    checks.append(check_file_exists('app/catalogo/wsgi.py', 'wsgi.py'))
    checks.append(check_file_exists('app/catalogo/asgi.py', 'asgi.py'))
    
    # Verificar archivos de apps
    print("\n[APPS] Archivos de apps:")
    checks.append(check_file_exists('app/catalogo/apps/peliculas/models.py', 'models.py (peliculas)'))
    checks.append(check_file_exists('app/catalogo/apps/peliculas/views.py', 'views.py (peliculas)'))
    checks.append(check_file_exists('app/catalogo/apps/peliculas/urls.py', 'urls.py (peliculas)'))
    checks.append(check_file_exists('app/catalogo/apps/peliculas/forms.py', 'forms.py (peliculas)'))
    checks.append(check_file_exists('app/catalogo/apps/peliculas/admin.py', 'admin.py (peliculas)'))
    checks.append(check_file_exists('app/catalogo/apps/accounts/views.py', 'views.py (accounts)'))
    checks.append(check_file_exists('app/catalogo/apps/accounts/urls.py', 'urls.py (accounts)'))
    
    # Verificar archivos de utilidad
    print("\n[UTILS] Archivos de utilidad:")
    checks.append(check_file_exists('manage_new.py', 'manage_new.py'))
    checks.append(check_file_exists('run.py', 'run.py'))
    checks.append(check_file_exists('Makefile', 'Makefile'))
    checks.append(check_file_exists('requirements.txt', 'requirements.txt'))
    
    # Verificar documentacion
    print("\n[DOCS] Documentacion:")
    checks.append(check_file_exists('ESTRUCTURA_NUEVA.md', 'ESTRUCTURA_NUEVA.md'))
    checks.append(check_file_exists('GUIA_MIGRACION.md', 'GUIA_MIGRACION.md'))
    checks.append(check_file_exists('CAMBIOS_RESUMEN.md', 'CAMBIOS_RESUMEN.md'))
    checks.append(check_file_exists('TECNICO.md', 'TECNICO.md'))
    
    # Resumen
    print_header("RESUMEN")
    total = len(checks)
    passed = sum(checks)
    failed = total - passed
    
    print(f"Total de verificaciones: {total}")
    print(f"[OK] Pasadas: {passed}")
    print(f"[FAIL] Fallidas: {failed}")
    
    if failed == 0:
        print(f"\n{'='*60}")
        print("ESTRUCTURA COMPLETAMENTE VERIFICADA!")
        print(f"{'='*60}")
        return 0
    else:
        print(f"\nHay {failed} verificacion(es) fallida(s)")
        print("Por favor, revisa los errores arriba")
        return 1

if __name__ == '__main__':
    sys.exit(main())
