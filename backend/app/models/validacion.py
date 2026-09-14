from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING, ClassVar, Optional
from sqlalchemy import Column, Enum as SQLEnum, ForeignKey, Index, Numeric
from sqlalchemy.sql import func
from sqlmodel import Field, Relationship, SQLModel

from app.models.enums import TipoValidacion

if TYPE_CHECKING:
    from app.models.cuenta_mensual import CuentaMensual


class Validacion(SQLModel, table=True):
    __tablename__: ClassVar[str] = "validaciones"

    id: Optional[int] = Field(default=None, primary_key=True)
    id_cuenta_mensual: int = Field(
        sa_column_args=[ForeignKey("cuentas_mensual.id", ondelete="CASCADE")]
    )

    id_registro_origen: Optional[int] = Field(default=None)
    tabla_origen: str = Field(max_length=50)

    tipo_validacion: TipoValidacion = Field(
        sa_column=Column(SQLEnum(TipoValidacion), nullable=False)
    )
    resultado: bool

    mensaje: Optional[str] = Field(default=None)

    monto_esperado: Optional[Decimal] = Field(
        default=None,
        sa_column=Column(Numeric(15, 2), nullable=True),
    )
    monto_real: Optional[Decimal] = Field(
        default=None,
        sa_column=Column(Numeric(15, 2), nullable=True),
    )

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

    cuenta_mensual: Optional["CuentaMensual"] = Relationship(
        back_populates="validaciones"
    )

    __table_args__: ClassVar[tuple] = (
        Index("idx_validacion_cuenta_mensual", "id_cuenta_mensual"),
        Index("idx_validacion_tabla", "tabla_origen"),
        Index("idx_validacion_tipo", "tipo_validacion"),
        Index("idx_validacion_resultado", "resultado"),
    )