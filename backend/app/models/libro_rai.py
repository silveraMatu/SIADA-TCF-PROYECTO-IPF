from datetime import date, datetime
from decimal import Decimal
from typing import TYPE_CHECKING, ClassVar, Optional
from sqlalchemy import ForeignKey, Index, Numeric, Column
from sqlalchemy.sql import func
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.cuenta_mensual import CuentaMensual
    from app.models.partida_presupuestaria import PartidaPresupuestaria


class LibroRAI(SQLModel, table=True):
    __tablename__: ClassVar[str] = "libro_rai"

    id: Optional[int] = Field(default=None, primary_key=True)

    # ForeignKey con ondelete configurado correctamente
    id_cuenta_mensual: int = Field(foreign_key="cuentas_mensual.id")
    
    id_partida: int = Field(foreign_key="partida_presupuestaria.id")

    numero_asiento: Optional[int] = Field(default=None)
    fecha_ingreso: date
    numero_planilla: Optional[str] = Field(default=None, max_length=50)
    concepto: Optional[str] = Field(default=None)

    ingreso_diario: Decimal = Field(sa_column=Column(Numeric(14, 2), nullable=False, default=0))
    
    ingreso_mensual: Decimal = Field(sa_column=Column(Numeric(14, 2), nullable=False, default=0))
    
    ingreso_acumulado: Decimal = Field(sa_column=Column(Numeric(14, 2), nullable=False, default=0))
    
    saldo: Decimal = Field(sa_column=Column(Numeric(14, 2), nullable=False, default=0))

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

    # Relaciones
    cuenta_mensual: Optional["CuentaMensual"] = Relationship(back_populates="libros_rai" )
    partida: Optional["PartidaPresupuestaria"] = Relationship(back_populates="libros_rai")

    __table_args__: ClassVar[tuple] = (
        Index("idx_rai_cuenta_mensual", "id_cuenta_mensual"),
        Index("idx_rai_partida", "id_partida"),
        Index("idx_rai_fecha", "fecha_ingreso"),
        Index("idx_rai_planilla", "numero_planilla"),
    )