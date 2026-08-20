from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Todos los modelos en app/models/ heredarán de esta clase."""
    pass