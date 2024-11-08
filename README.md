# Nombre de la Aplicación

Descripción breve de la aplicación y su propósito.

## Requisitos

Asegúrate de tener instalados los siguientes programas:

- Python 3.x
- Node.js
- Docker

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu_usuario/nombre_del_repositorio.git
   cd nombre_del_repositorio
   ```

2. Crea y activa un entorno virtual:

   ```bash
   .venv\Scripts\activate  # En Windows
   # o
   source .venv/bin/activate  # En macOS/Linux
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Genera el cliente de Prisma:

   ```bash
   npx prisma@5.17.0 generate
   ```

5. Realiza la migración inicial de la base de datos:

   ```bash
   npx prisma migrate dev --name init
   ```

6. Genera nuevamente el cliente de Prisma:

   ```bash
   npx prisma generate
   ```

7. Sincroniza el esquema de la base de datos:

   ```bash
   npx prisma db push
   ```

## Ejecución

Para iniciar la aplicación, utiliza el siguiente comando:

```bash
uvicorn app.main:app --reload
```

## Despliegue con Docker

Para ejecutar la aplicación en un contenedor Docker, utiliza:

```bash
docker compose up -d
```

## Cuerpo de Datos de la API

La API utiliza el siguiente cuerpo de datos para las tareas:

```json
{
  "title": "Mi nueva tarea",
  "description": "Esta es una tarea de prueba",
  "completed": true
}
```

## Contribuciones

Si deseas contribuir, por favor abre un issue o envía un pull request.
