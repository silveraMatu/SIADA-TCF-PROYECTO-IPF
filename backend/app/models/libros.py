from __future__ import annotations

from datetime import datetime, date, timezone
from decimal import Decimal
from typing import TYPE_CHECKING, Optional, List
from sqlalchemy import String, Text, Numeric, Date, DateTime, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.organizacion import CuentaMensual


class PartidaPresupuestaria(Base):
    __tablename__ = "partidas_presupuestarias"

    id_partida: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    codigo_partida: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    denominacion: Mapped[str] = mapped_column(String(255), nullable=False)
    descripcion_objeto: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    registros_rai: Mapped[List[LibroRAI]] = relationship(back_populates="partida")
    registros_raci: Mapped[List[LibroRACI]] = relationship(back_populates="partida")


class LibroBanco(Base):
    __tablename__ = "libro_banco"

    id_banco: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_cuenta_mensual: Mapped[int] = mapped_column(
        ForeignKey("cuenta_mensual.id_cuenta_mensual", ondelete="CASCADE"), 
        nullable=False, 
        index=True
    )
    fecha_movimiento: Mapped[date] = mapped_column(Date, nullable=False)
    numero_comprobante: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    tipo_movimiento: Mapped[str] = mapped_column(String(20), nullable=False)
    concepto_texto_libre: Mapped[str] = mapped_column(Text, nullable=False)
    monto: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)
    saldo_resultante: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)
    cuit_contraparte: Mapped[Optional[str]] = mapped_column(String(11), nullable=True, index=True)
    conciliado: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    cuenta_mensual: Mapped[CuentaMensual] = relationship(back_populates="libro_banco")


class LibroRAI(Base):
    __tablename__ = "libro_rai"

    id_rai: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_cuenta_mensual: Mapped[int] = mapped_column(
        ForeignKey("cuenta_mensual.id_cuenta_mensual", ondelete="CASCADE"), 
        nullable=False, 
        index=True
    )
    id_partida: Mapped[Optional[int]] = mapped_column(
        ForeignKey("partidas_presupuestarias.id_partida", ondelete="SET NULL"), 
        nullable=True
    )
    fecha_imputacion: Mapped[date] = mapped_column(Date, nullable=False)
    numero_orden_pago: Mapped[str] = mapped_column(String(100), nullable=False)
    beneficiario: Mapped[str] = mapped_column(String(255), nullable=False)
    cuit_beneficiario: Mapped[str] = mapped_column(String(11), nullable=False, index=True)
    concepto_gasto: Mapped[str] = mapped_column(Text, nullable=False)
    monto_imputado: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    cuenta_mensual: Mapped[CuentaMensual] = relationship(back_populates="libro_rai")
    partida: Mapped[Optional[PartidaPresupuestaria]] = relationship(back_populates="registros_rai")


class LibroRACI(Base):
    __tablename__ = "libro_raci"

    id_raci: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_cuenta_mensual: Mapped[int] = mapped_column(
        ForeignKey("cuenta_mensual.id_cuenta_mensual", ondelete="CASCADE"), 
        nullable=False, 
        index=True
    )
    id_partida: Mapped[Optional[int]] = mapped_column(
        ForeignKey("partidas_presupuestarias.id_partida", ondelete="SET NULL"), 
        nullable=True
    )
    fecha_rendicion: Mapped[date] = mapped_column(Date, nullable=False)
    numero_expediente: Mapped[str] = mapped_column(String(100), nullable=False)
    responsable_anticipo: Mapped[str] = mapped_column(String(255), nullable=False)
    monto_rendido: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)
    observaciones_raci: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    cuenta_mensual: Mapped[CuentaMensual] = relationship(back_populates="libro_raci")
    partida: Mapped[Optional[PartidaPresupuestaria]] = relationship(back_populates="registros_raci")


class LibroIngresosEgresos(Base):
    __tablename__ = "libro_ingresos_egresos"

    id_movimiento: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_cuenta_mensual: Mapped[int] = mapped_column(
        ForeignKey("cuenta_mensual.id_cuenta_mensual", ondelete="CASCADE"), 
        nullable=False, 
        index=True
    )
    fecha: Mapped[date] = mapped_column(Date, nullable=False)
    tipo: Mapped[str] = mapped_column(String(10), nullable=False)
    fuente_financiamiento: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    clasificacion_economica: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    monto: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)
    descripcion: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    cuenta_mensual: Mapped[CuentaMensual] = relationship(back_populates="libro_ingresos_egresos")