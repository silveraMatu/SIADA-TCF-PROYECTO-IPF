from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from app.core.config import settings
# from app.routes.api_router import api_router
from app.db.session import engine
from app.db.base import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    #Ejecuta create all sincrono dentro del pool asincrono para la creación de tablas
   async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)

    yield
    await engine.dispose() #Cierra el pool al apagar el server


#Metada de la instancia de fastapi
app = FastAPI(
    title="SIADA API - Sistema de Auditoría",
    description="Backend en capas para auditoría y rendición de cuentas",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Configuración de CORS para permitir la conexión desde el Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #En producción definir dominios específicos (ej: http://localhost:5173)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar el router general bajo /api/v1
# app.include_router(api_router, prefix="/api/v1")


@app.get("/health", tags=["Health Check"])
def health_check():
    return {
        "status": "ok",
        "service": "SIADA Backend",
        # "environment": settings.ENVIRONMENT
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)