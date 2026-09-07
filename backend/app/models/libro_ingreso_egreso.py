from datetime import date, datetime
from decimal import Decimal
from typing import TYPE_CHECKING, Optional
from sqlalchemy import String, Date, DateTime, Numeric, Text, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.cuenta_mensual import CuentaMensual

class LibroIngresoEgreso(Base):
    __tablename__ = "libro_ingresos_egresos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_cuenta_mensual: Mapped[int] = mapped_column(ForeignKey("cuentas_mensual.id", ondelete="CASCADE"))

    fecha: Mapped[date] = mapped_column(Date, nullable=False)
    concepto: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    numero_cheque: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    numero_comprobante: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    caja_debe: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    caja_haber: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    caja_saldo: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)

    banco_debe: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    banco_haber: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    banco_saldo: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)

    egreso_inc1: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    egreso_inc2: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    egreso_inc3: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    egreso_inc4: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    egreso_inc5: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)

    ingreso_municipal: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    ingreso_otras: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)

    cuentas_varias_concepto: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    cuentas_varias_debe: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    cuentas_varias_haber: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    cuenta_mensual: Mapped["CuentaMensual"] = relationship(back_populates="libros_ingresos_egresos")

    __table_args__ = (
        Index('idx_ingresos_egresos_cuenta_mensual', 'id_cuenta_mensual'),
        Index('idx_ingresos_egresos_fecha', 'fecha'),
        Index('idx_ingresos_egresos_cheque', 'numero_cheque'),
    )
