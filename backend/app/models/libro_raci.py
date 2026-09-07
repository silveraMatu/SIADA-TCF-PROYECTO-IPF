from datetime import date, datetime
from decimal import Decimal
from typing import TYPE_CHECKING, Optional
from sqlalchemy import String, Date, DateTime, Numeric, Text, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.cuenta_mensual import CuentaMensual
    from app.models.partida_presupuestaria import PartidaPresupuestaria

class LibroRACI(Base):
    __tablename__ = "libro_raci"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_cuenta_mensual: Mapped[int] = mapped_column(ForeignKey("cuentas_mensual.id", ondelete="CASCADE"))
    id_partida: Mapped[int] = mapped_column(ForeignKey("partida_presupuestaria.id"))

    numero_asiento: Mapped[Optional[int]] = mapped_column(nullable=True)
    fecha_compromiso: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    fecha_devengado: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    fecha_pago: Mapped[Optional[date]] = mapped_column(Date, nullable=True)

    numero_cheque: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    numero_orden_pago: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    numero_expediente: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    concepto: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    beneficiario: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    monto_comprometido: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    monto_devengado: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    monto_pagado: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)

    observaciones: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    cuenta_mensual: Mapped["CuentaMensual"] = relationship(back_populates="libros_raci")
    partida: Mapped["PartidaPresupuestaria"] = relationship(back_populates="libros_raci")

    __table_args__ = (
        Index('idx_raci_cuenta_mensual', 'id_cuenta_mensual'),
        Index('idx_raci_partida', 'id_partida'),
        Index('idx_raci_fecha_compromiso', 'fecha_compromiso'),
        Index('idx_raci_cheque', 'numero_cheque'),
        Index('idx_raci_orden_pago', 'numero_orden_pago'),
    )
