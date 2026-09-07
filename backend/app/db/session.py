from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import AsyncGenerator

DATABASE_URL = "postgresql+asyncpg://admin:adminpassword@localhost:5432/siada_db" #Esto después vamos a guardarlo en core/config.py

engine = create_async_engine(
    DATABASE_URL, 
    echo= True, #log en terminal
    pool_size=10, #mantiene 10 conexiones abiertas
    max_overflow=20 #20 conexiones extras temporales
    )

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False #evitar enviar cambios sin commit()
    )

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()