from collections.abc import Generator
from sqlmodel import Session, create_engine

from app.core.config import settings

# Si usás SQLite local podés agregar connect_args={"check_same_thread": False}
# Para PostgreSQL/MySQL la configuración estándar es directa:
engine = create_engine(
    str(settings.DATABASE_URI),  # o settings.SQLALCHEMY_DATABASE_URI según cómo lo llames en config.py
    echo=False,
    pool_pre_ping=True,
)


def get_session() -> Generator[Session, None, None]:
    """Dependencia para inyectar la sesión en endpoints de FastAPI."""
    with Session(engine) as session:
        yield session