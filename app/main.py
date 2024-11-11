from fastapi import FastAPI, HTTPException
from prisma import Prisma
from app.routes import router
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

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

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

app.include_router(router)