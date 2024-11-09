# Nombre de la Aplicación

Descripción breve de la aplicación y su propósito.

## Requisitos

Asegúrate de tener instalados los siguientes programas:

- Python 3.x
- Node.js
- Docker

## Instalación

# Crea y activa un entorno virtual:

```bash
#1 priemra opcion
.venv\Scripts\activate  # En Windows
#2 segunda opcion
 python -m venv env
# o
source .venv/bin/activate  # En macOS/Linux

```

## Despliegue con Docker

Para ejecutar la aplicación en un contenedor Docker, utiliza:

```bash
docker compose up -d
```

# Crear un archivo .env y agregar la siguiente línea

```plaintext
DATABASE_URL="postgresql://postgres:password@localhost:5439/mydb?schema=public"
```

# Instala las dependencias:

```bash
pip install -r requirements.txt
```

# Genera el cliente de Prisma:

```bash
npx prisma@5.11.0 generate
```

# Realiza la migración inicial de la base de datos:

```bash
npx prisma@5.11.0 migrate dev --name init
```

# Sincroniza el esquema de la base de datos:

```bash
npx prisma@5.11.0 db push
```

## Ejecución

Para iniciar la aplicación, utiliza el siguiente comando:

```bash
uvicorn app.main:app --reload
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
