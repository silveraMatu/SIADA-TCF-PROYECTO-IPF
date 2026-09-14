from datetime import date, datetime
from decimal import Decimal
from typing import TYPE_CHECKING, ClassVar, Optional
from sqlalchemy import Column, ForeignKey, Index, Numeric
from sqlalchemy.sql import func
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.cuenta_mensual import CuentaMensual


class LibroIngresoEgreso(SQLModel, table=True):
    __tablename__: ClassVar[str] = "libro_ingresos_egresos"

    id: Optional[int] = Field(default=None, primary_key=True)
    id_cuenta_mensual: int = Field(
        sa_column_args=[ForeignKey("cuentas_mensual.id", ondelete="CASCADE")]
    )

    fecha: date
    concepto: Optional[str] = Field(default=None)
    numero_cheque: Optional[str] = Field(default=None, max_length=50)
    numero_comprobante: Optional[str] = Field(default=None, max_length=50)

    # Caja
    caja_debe: Decimal = Field(
        sa_column=Column(Numeric(15, 2), nullable=False, default=0)
    )
    caja_haber: Decimal = Field(
        sa_column=Column(Numeric(15, 2), nullable=False, default=0)
    )
    caja_saldo: Optional[Decimal] = Field(
        default=None,
        sa_column=Column(Numeric(15, 2), nullable=True)
    )

    # Banco
    banco_debe: Decimal = Field(
        sa_column=Column(Numeric(15, 2), nullable=False, default=0)
    )
    banco_haber: Decimal = Field(
        sa_column=Column(Numeric(15, 2), nullable=False, default=0)
    )
    banco_saldo: Optional[Decimal] = Field(
        default=None,
        sa_column=Column(Numeric(15, 2), nullable=True)
    )

    # Egresos por inciso
    egreso_inc1: Decimal = Field(
        sa_column=Column(Numeric(15, 2), nullable=False, default=0)
    )
    egreso_inc2: Decimal = Field(
        sa_column=Column(Numeric(15, 2), nullable=False, default=0)
    )
    egreso_inc3: Decimal = Field(
        sa_column=Column(Numeric(15, 2), nullable=False, default=0)
    )
    egreso_inc4: Decimal = Field(
        sa_column=Column(Numeric(15, 2), nullable=False, default=0)
    )
    egreso_inc5: Decimal = Field(
        sa_column=Column(Numeric(15, 2), nullable=False, default=0)
    )

    # Ingresos
    ingreso_municipal: Decimal = Field(
        sa_column=Column(Numeric(15, 2), nullable=False, default=0)
    )
    ingreso_otras: Decimal = Field(
        sa_column=Column(Numeric(15, 2), nullable=False, default=0)
    )

    # Cuentas varias
    cuentas_varias_concepto: Optional[str] = Field(default=None)
    cuentas_varias_debe: Decimal = Field(
        sa_column=Column(Numeric(15, 2), nullable=False, default=0)
    )
    cuentas_varias_haber: Decimal = Field(
        sa_column=Column(Numeric(15, 2), nullable=False, default=0)
    )

    # Timestamps
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
    cuenta_mensual: Optional["CuentaMensual"] = Relationship(
        back_populates="libros_ingresos_egresos"
    )

    # Índices
    __table_args__: ClassVar[tuple] = (
        Index("idx_ingresos_egresos_cuenta_mensual", "id_cuenta_mensual"),
        Index("idx_ingresos_egresos_fecha", "fecha"),
        Index("idx_ingresos_egresos_cheque", "numero_cheque"),
    )