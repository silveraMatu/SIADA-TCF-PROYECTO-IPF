from datetime import datetime
from typing import TYPE_CHECKING, List, ClassVar, Optional
from sqlalchemy.sql import func
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from backend.app.models.organismo import Organismo
    from app.models.cuenta_mensual import CuentaMensual

class CuentaAnual(SQLModel, table=True):
    __tablename__: ClassVar[str] = "cuentas_anual"

    id: Optional[int] = Field(primary_key=True, default=None)
    id_organismo: int = Field(foreign_key="organismos.id")
    anio: int = Field(nullable=False)
    
    created_at: datetime = Field(
        default_factory=datetime.utcnow, 
        sa_column_kwargs={"server_default":func.now()})

    organismo: "Organismo" = Relationship(back_populates="cuentas_anual")
    cuentas_mensual: List["CuentaMensual"] = Relationship(back_populates="cuenta_anual", cascade_delete=True)
