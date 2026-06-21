#!/usr/bin/env python
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

def main():
    print("=" * 60)
    print("🚀 SUPABASE DEPLOYMENT & MIGRATION HELPER FOR CINEGLOW")
    print("=" * 60)
    
    # Cargar el .env
    base_dir = Path(__file__).resolve().parent
    env_path = base_dir / '.env'
    if env_path.exists():
        load_dotenv(env_path)
        print("✅ Archivo .env cargado con éxito.")
    else:
        print("❌ No se encontró el archivo .env.")
        print("Por favor crea un archivo .env en la raíz del proyecto.")
        sys.exit(1)
        
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        print("\n⚠️  DATABASE_URL no está configurado en tu archivo .env.")
        print("Para conectar con tu base de datos de Supabase, agrega la siguiente línea a tu .env:")
        print("DATABASE_URL=postgresql://postgres:[TU_CONTRASEÑA]@[TU_HOST_SUPABASE]:5432/postgres")
        print("\nEjemplo de variables a colocar:")
        print("DATABASE_URL=postgresql://postgres.abcdefghijklmnop:mi_password@aws-0-us-west-1.pooler.supabase.com:6543/postgres")
        sys.exit(1)
        
    print(f"📡 Conexión detectada a: {db_url.split('@')[-1] if '@' in db_url else 'DATABASE_URL'}")
    
    # Importar y configurar django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalogo.settings')
    try:
        import django
        django.setup()
    except Exception as e:
        print(f"❌ Error al configurar Django: {e}")
        sys.exit(1)
        
    print("\n🔄 Probando conexión a Supabase...")
    from django.db import connections
    from django.db.utils import OperationalError
    
    db_conn = connections['default']
    try:
        db_conn.cursor()
        print("✅ ¡Conexión exitosa a la base de datos de Supabase!")
    except OperationalError as e:
        print(f"❌ Error de conexión: {e}")
        print("\nPor favor, verifica:")
        print("1. Que tu contraseña y host en DATABASE_URL sean correctos.")
        print("2. Que no tengas bloqueos de red o firewall.")
        print("3. Que la base de datos en Supabase esté activa.")
        sys.exit(1)
        
    print("\n⏳ Ejecutando migraciones de Django en Supabase...")
    from django.core.management import call_command
    try:
        call_command('migrate')
        print("✅ ¡Migraciones aplicadas con éxito en Supabase!")
    except Exception as e:
        print(f"❌ Error al aplicar migraciones: {e}")
        sys.exit(1)
        
    # Cargar datos seed
    print("\n¿Deseas cargar los datos de películas iniciales (seed) en Supabase? (s/n): ", end="")
    try:
        choice = input().strip().lower()
    except KeyboardInterrupt:
        print("\nProceso cancelado.")
        sys.exit(0)
        
    if choice == 's':
        print("⏳ Cargando películas iniciales...")
        try:
            call_command('seed')
            print("✅ ¡Datos iniciales cargados con éxito!")
        except Exception as e:
            print(f"❌ Error al cargar datos: {e}")
    else:
        print("⏭️ Omitiendo carga de datos iniciales.")
        
    print("\n🎉 ¡Todo listo! Tu aplicación CineGlow ahora está conectada y configurada en Supabase.")
    print("=" * 60)

if __name__ == '__main__':
    main()
