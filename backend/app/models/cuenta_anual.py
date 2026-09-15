from datetime import datetime, timezone
from typing import TYPE_CHECKING, List, ClassVar, Optional
from sqlalchemy.sql import func
from sqlmodel import Field, Relationship, UniqueConstraint
from backend.app.schemas.cuentaAnualDTO import CuentaAnualBase

if TYPE_CHECKING:
    from app.models.organismo import Organismo
    from app.models.cuenta_mensual import CuentaMensual

class CuentaAnual(CuentaAnualBase, table=True):
    __tablename__: ClassVar[str] = "cuentas_anuales"

    id: Optional[int] = Field(primary_key=True, default=None)
    id_organismo: int = Field(foreign_key="organismos.id", index=True)
    
    created_at: datetime = Field(
        default_factory= lambda: datetime.now(timezone.utc), 
        sa_column_kwargs={"server_default":func.now()})
    
    updated_at: datetime = Field(
        default_factory= lambda: datetime.now(timezone.utc), 
        sa_column_kwargs={
            "server_default":func.now(),
            "on_update" : func.now()
            })
    
    __table_args__: ClassVar[tuple] = (
        UniqueConstraint("id_organismo", "ejercicio", name="uq_organismo_ejercicio"),
    )

    organismo: Optional["Organismo"] = Relationship(back_populates="cuentas_anuales")
    cuentas_mensuales: List["CuentaMensual"] = Relationship(back_populates="cuenta_anual", cascade_delete=True)