Aquí tienes un ejemplo de un `README.md` para inicializar un proyecto hecho con Django Rest Framework (DRF), PostgreSQL y orquestado con Docker Compose. Está enfocado principalmente en un entorno Windows, pero los pasos generales también sirven para Linux y Ubuntu.

---

# Proyecto DRF con PostgreSQL Orquestado con Docker Compose

📦 Proyecto DRF con PostgreSQL Orquestado con Docker Compose

Este proyecto es una API RESTful construida con Django Rest Framework (DRF) y PostgreSQL como base de datos. Utiliza Docker Compose para la gestión de contenedores, lo que facilita su despliegue y administración.

### Sistema Operativo:
- **Windows** 
- **Linux (Ubuntu)**: Los pasos también son aplicables para sistemas basados en Linux a excepción de Docker Desktop.

## Requisitos

### Software Requerido:
- **Docker**: Debes tener instalado Docker en tu sistema.[Docker](https://www.docker.com/products/docker-desktop).
  
- **Docker Compose**: Viene integrado con Docker Desktop, por lo que si tienes Docker instalado, también tendrás Docker Compose. [Docker Compose](https://docs.docker.com/compose/install/)

- **Git**: Para clonar el repositorio, necesitas tener instalado Git. [Git](https://git-scm.com/).

### Requisitos Previos:
1. Tener Docker y Docker Compose instalados y configurados en tu sistema.
2. Tener acceso a un terminal (PowerShell, CMD, o Windows Subsystem for Linux (WSL) en Windows).


## Instrucciones para levantar el proyecto 🆙

### Paso 1: Clonar el repositorio

Primero, clona el repositorio en tu máquina local:

```bash
git clone https://github.com/diegoslh/ApiRestDjango_Quick
   cd ApiRestDjango_Quick
```

### Paso 2: Crear la imagen de Docker

Antes de levantar los servicios, necesitas crear las imágenes de Docker. Esto se hace con el comando `docker-compose build`. Este comando construirá la imagen de la aplicación Django, configurando todo el entorno necesario.

Ejecuta lo siguiente en tu terminal:

```bash
docker-compose build
```

Este paso puede tardar unos minutos, dependiendo de tu conexión a internet y la potencia de tu máquina. Asegúrate de que no haya errores al ejecutar este comando. Si todo está correcto, la construcción de las imágenes habrá sido exitosa.

### Paso 3: Levantar los contenedores con Docker Compose

Una vez que la imagen está construida, puedes levantar el proyecto con el siguiente comando:

```bash
docker-compose up
```

Este comando levantará todos los servicios definidos en el archivo `docker-compose.yml` (el proyecto Django y la base de datos PostgreSQL). Si todo está bien configurado, deberías ver logs en la terminal indicando que el contenedor de Django está corriendo y que PostgreSQL está listo.

Nota: Puedes ejecutar un solo comando para realizar los dos pasos anteriores en uno solo con el comando:

```bash
docker-compose up
```

### Paso 4: Crear las migraciones de la base de datos

Cuando los contenedores están corriendo, puedes acceder a la terminal del contenedor de Django para realizar las migraciones de la base de datos.

Para acceder a la terminal del contenedor, usa:

```bash
docker-compose exec backend bash
```

Aquí `web` es el nombre del contenedor de la aplicación Django, según lo configurado en `docker-compose.yml`.

Una vez dentro, ejecuta las migraciones de Django:

```bash
python manage.py migrate
```

Este paso configura la base de datos de PostgreSQL con las tablas necesarias.

Nota: Puedes ejecutar cualquier el comando en una sola linea, unificando la sentencia de la siguiente manera:

```bash
docker-compose exec backend bash python manage.py migrate
```

### Paso 5: Acceder al proyecto

Una vez que todo está levantado y las migraciones se han ejecutado correctamente, puedes realizar las peticiones con la colección de Postman dirigida a la siguiente URL:

```
http://localhost:8000/api
```

Nota: Recuerda iniciar sesión para obtener el JWT para tener acceso a todos los demás endpoints
Claro, aquí tienes una descripción más detallada:

---

**Nota**: **Recuerda iniciar sesión para obtener el JWT (JSON Web Token)**, que es un token de autenticación necesario para acceder a todos los endpoints protegidos de la API.

### ¿Cómo enviar el JWT en las solicitudes?

Para poder acceder a los endpoints protegidos de la API, necesitas enviar el JWT en la cabecera de autorización como un **Bearer token**. Esto se hace de la siguiente manera:

1. Abre **Postman** (o cualquier cliente HTTP).
2. Selecciona el método HTTP correspondiente (por ejemplo, `GET`, `POST`, etc.).
3. En la sección de **Headers** de la solicitud, agrega lo siguiente:
   - **Key**: `Authorization`
   - **Value**: `Bearer Token <token_jwt>`
   
   Donde `<token_jwt>` es el token que obtuviste al iniciar sesión.

Después de agregar el token en la cabecera, podrás realizar las solicitudes a los endpoints protegidos.


### Paso 7: Detener los servicios 🔚

Cuando hayas terminado de trabajar con el proyecto, puedes detener los contenedores utilizando:

```bash
docker-compose down
```

## Archivos importantes

- **`docker-compose.yml`**: Configuración de los contenedores de Docker (aplicación Django, PostgreSQL).
- **`Dockerfile`**: Instrucciones para construir la imagen de Docker para la aplicación Django.

---
