# Proyecto DRF con Docker Compose y PostgreSQL
📦 Proyecto DRF con Docker Compose y PostgreSQL

Este proyecto es una API RESTful construida con Django Rest Framework (DRF) y PostgreSQL como base de datos. Utiliza Docker Compose para la gestión de contenedores, lo que facilita su despliegue y administración

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu pc:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Configuración del proyecto

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/diegoslh/ApiRestDjango_Quick
   cd ApiRestDjango_Quick


2. **Inicializa el proyecto:**

   ```bash
   docker-compose up --build
   docker-compose exec backend python manage.py migrate


3. **Termina la ejecución del proyecto:**

   ```bash
   docker-compose down
