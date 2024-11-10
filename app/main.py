from fastapi import FastAPI, HTTPException
from prisma import Prisma
from app.routes import router
from contextlib import asynccontextmanager
from dotenv import load_dotenv

load_dotenv()
# Inicializar Prisma como variable global
prisma = Prisma()

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await prisma.connect() 
        yield
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        raise e
    finally:
        await prisma.disconnect() 

app = FastAPI(lifespan=lifespan)
app.include_router(router)

# Verificar la conexión al inicio (opcional)
@app.on_event("startup")
async def startup():
    try:
        await prisma.connect()  
        print("Conexión exitosa a la base de datos")
    except Exception as e:
        print(f"Error al conectar con la base de datos en startup: {e}")
        raise HTTPException(status_code=500, detail="Error al conectar con la base de datos.")
