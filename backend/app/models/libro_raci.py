from datetime import date, datetime
from decimal import Decimal
from typing import TYPE_CHECKING, ClassVar, Optional
from sqlalchemy import Column, Index, Numeric
from sqlalchemy.sql import func
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.cuenta_mensual import CuentaMensual
    from app.models.partida_presupuestaria import PartidaPresupuestaria


class LibroRACI(SQLModel, table=True):
    __tablename__: ClassVar[str] = "libro_raci"

    id: Optional[int] = Field(default=None, primary_key=True)
    id_cuenta_mensual: Optional[int] = Field(
        default=None,
        foreign_key="cuentas_mensual.id",
    )
    id_partida: int = Field(foreign_key="partida_presupuestaria.id")

    numero_asiento: Optional[int] = Field(default=None)
    fecha: Optional[date] = Field(default=None)
    numero_expediente: int

    concepto: Optional[str] = Field(default=None)

    compromiso_acumulado: Decimal = Field(
        sa_column=Column(Numeric(14, 2), nullable=False, default=0)
    )

    devengado_acumulado: Decimal = Field(
        sa_column=Column(Numeric(14, 2), nullable=False, default=0)
    )
    devengado_saldo: Decimal = Field(
        sa_column=Column(Numeric(14, 2), nullable=False, default=0)
    )

    pago_numero_cheque: Optional[str] = Field(default=None, max_length=50)
    pago_acumulado: Decimal = Field(
        sa_column=Column(Numeric(14, 2), nullable=False, default=0)
    )
    pago_saldo_a_pagar: Decimal = Field(
        sa_column=Column(Numeric(14, 2), nullable=False, default=0)
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

    cuenta_mensual: Optional["CuentaMensual"] = Relationship(back_populates="libros_raci")
    partida: Optional["PartidaPresupuestaria"] = Relationship(back_populates="libros_raci")

    __table_args__: ClassVar[tuple] = (
        Index("idx_raci_cuenta_mensual", "id_cuenta_mensual"),
        Index("idx_raci_partida", "id_partida"),
        Index("idx_raci_fecha", "fecha"),
        Index("idx_raci_expediente", "numero_expediente"),
        Index("idx_raci_cheque", "pago_numero_cheque"),
    )