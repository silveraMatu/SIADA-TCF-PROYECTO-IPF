from datetime import datetime
from typing import TYPE_CHECKING, List, ClassVar, Optional
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy.sql import func

if TYPE_CHECKING:
    from app.models.cuenta_anual import CuentaAnual

class Organizacion(SQLModel, table=True):
    __tablename__: ClassVar[str] = "organizaciones"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=255, nullable=False)
    rubro: str = Field(max_length=100, nullable=True)
    jurisdiccion: str = Field(max_length=100, nullable=True)
    activo: bool = Field(default=True)
    
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={
            "server_default": func.now(),
            "onupdate": func.now(),
        },
    )

    cuentas_anual: List["CuentaAnual"] = Relationship(back_populates="organizacion", cascade_delete=True)
