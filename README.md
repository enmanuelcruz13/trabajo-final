Proyecto Final Integrador: Catalogo de Peliculas y Series

## 1. Proposito

Desarrollar una plataforma web que permita a los usuarios consultar informacion de peliculas y series, organizarlas en favoritos y calificarlas para mejorar su experiencia de entretenimiento.

## 2. Alcance

Incluye: registro de usuarios, autenticacion, catalogo, busqueda por titulo o genero, favoritos y calificaciones.

No incluye: reproduccion de contenido, descargas ni integracion con servicios de streaming.

## 3. Happy Path

1. El usuario inicia sesion.
2. Busca una pelicula.
3. Accede a los detalles.
4. La agrega a favoritos.
5. La califica.
6. El sistema guarda la informacion exitosamente.

## 4. Unhappy Path

1. El usuario intenta calificar una pelicula sin iniciar sesion.
2. El sistema muestra un mensaje de error.
3. Solicita autenticacion antes de continuar.

## 5. Alternative Path

1. El usuario navega por generos.
2. Encuentra una pelicula sin utilizar el buscador.
3. La agrega a favoritos.

## 6. Diagrama de Flujo (Descripcion)

Inicio -> Usuario autenticado? -> Si -> Ver catalogo -> Seleccionar pelicula -> Agregar a favoritos o calificar -> Guardar -> Fin.
Si no esta autenticado -> Login -> Ver catalogo.

## 7. Wireframes y Prototipos

Pantallas principales:
- Inicio
- Registro
- Login
- Catalogo
- Detalle de pelicula
- Favoritos
- Perfil de usuario

## 8. Diagrama Entidad Relacion (DER)

USUARIO(id, nombre, email, contrasena)

GENERO(id, nombre)

PELICULA(id, titulo, descripcion, anio, imagen, genero_id)

FAVORITO(id, usuario_id, pelicula_id)

CALIFICACION(id, usuario_id, pelicula_id, puntuacion)

## 9. Restricciones y Justificacion

email: UNIQUE NOT NULL para evitar cuentas duplicadas.



Llaves foraneas para mantener integridad referencial.

## 10. Stack Tecnologico

Python 3.13
Django 5.x
SQLite3
HTML5
CSS3
Bootstrap 5
JavaScript

## 11. Modelos Django

```python
class Genero(models.Model):
    nombre = models.CharField(max_length=100)

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    anio = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
```

## 12. Despliegue

El proyecto sera desplegado en Render y utilizara SQLite o una base de datos en la nube segun disponibilidad.

## 13. Presentacion Final

Explicar la problematica, mostrar el analisis, el DER, las tecnologias utilizadas y realizar una demostracion en vivo desde el enlace publico.
