from __future__ import annotations

from datetime import date, datetime, timezone
from typing import TYPE_CHECKING, List
from sqlalchemy import String, Integer, Date, DateTime, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.libros import LibroBanco, LibroRAI, LibroRACI, LibroIngresosEgresos
    from app.models.ml_ia import DeteccionPLNLoRA


class Organismo(Base):
    __tablename__ = "organismos"

    id_organismo: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(255), nullable=False)
    cuit: Mapped[str] = mapped_column(String(11), unique=True, nullable=False, index=True)
    rubro: Mapped[str] = mapped_column(String(100), nullable=False)
    jurisdiccion: Mapped[str] = mapped_column(String(100), default="Provincial")
    activo: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    cuentas_anuales: Mapped[List[CuentaAnual]] = relationship(
        back_populates="organismo", 
        cascade="all, delete-orphan"
    )


class CuentaAnual(Base):
    __tablename__ = "cuenta_anual"
    __table_args__ = (
        UniqueConstraint("id_organismo", "ejercicio_fiscal", name="uq_organismo_ejercicio"),
    )

    id_cuenta_anual: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_organismo: Mapped[int] = mapped_column(
        ForeignKey("organismos.id_organismo", ondelete="RESTRICT"), 
        nullable=False
    )
    ejercicio_fiscal: Mapped[int] = mapped_column(Integer, nullable=False)
    estado_general: Mapped[str] = mapped_column(String(50), default="EN_REVISION")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    organismo: Mapped[Organismo] = relationship(back_populates="cuentas_anuales")
    cuentas_mensuales: Mapped[List[CuentaMensual]] = relationship(
        back_populates="cuenta_anual", 
        cascade="all, delete-orphan"
    )


class CuentaMensual(Base):
    __tablename__ = "cuenta_mensual"
    __table_args__ = (
        UniqueConstraint("id_cuenta_anual", "mes", name="uq_cuenta_mensual"),
    )

    id_cuenta_mensual: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_cuenta_anual: Mapped[int] = mapped_column(
        ForeignKey("cuenta_anual.id_cuenta_anual", ondelete="CASCADE"), 
        nullable=False
    )
    mes: Mapped[int] = mapped_column(Integer, nullable=False)
    fecha_presentacion: Mapped[date] = mapped_column(Date, nullable=False)
    estado: Mapped[str] = mapped_column(String(50), default="INGRESADA")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    cuenta_anual: Mapped[CuentaAnual] = relationship(back_populates="cuentas_mensuales")

    libro_banco: Mapped[List[LibroBanco]] = relationship(
        back_populates="cuenta_mensual", 
        cascade="all, delete-orphan"
    )
    libro_rai: Mapped[List[LibroRAI]] = relationship(
        back_populates="cuenta_mensual", 
        cascade="all, delete-orphan"
    )
    libro_raci: Mapped[List[LibroRACI]] = relationship(
        back_populates="cuenta_mensual", 
        cascade="all, delete-orphan"
    )
    libro_ingresos_egresos: Mapped[List[LibroIngresosEgresos]] = relationship(
        back_populates="cuenta_mensual", 
        cascade="all, delete-orphan"
    )
    detecciones_ia: Mapped[List[DeteccionPLNLoRA]] = relationship(
        back_populates="cuenta_mensual", 
        cascade="all, delete-orphan"
    )