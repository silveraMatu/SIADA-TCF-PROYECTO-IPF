from datetime import date, datetime
from typing import TYPE_CHECKING, Optional, List
from sqlalchemy import Date, DateTime, Enum as SQLEnum, Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.db.base import Base
from app.models.enums import EstadoCuentaMensual

if TYPE_CHECKING:
    from app.models.cuenta_anual import CuentaAnual
    from app.models.libro_ingreso_egreso import LibroIngresoEgreso
    from app.models.libro_banco import LibroBanco
    from app.models.libro_raci import LibroRACI
    from app.models.libro_rai import LibroRAI
    from app.models.validacion import Validacion
    from app.models.deteccion_ml import DeteccionML

class CuentaMensual(Base):
    __tablename__ = "cuentas_mensual"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_cuenta_anual: Mapped[int] = mapped_column(ForeignKey("cuentas_anual.id", ondelete="CASCADE"))
    mes: Mapped[int] = mapped_column(Integer, nullable=False)
    estado: Mapped[EstadoCuentaMensual] = mapped_column(SQLEnum(EstadoCuentaMensual), default=EstadoCuentaMensual.PENDIENTE)
    fecha_presentacion: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    fecha_limite_auditoria: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    fecha_cierre: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    observaciones_generales: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    cuenta_anual: Mapped["CuentaAnual"] = relationship(back_populates="cuentas_mensual")
    libros_ingresos_egresos: Mapped[List["LibroIngresoEgreso"]] = relationship(back_populates="cuenta_mensual", lazy="selectin", cascade="all, delete-orphan")
    libros_banco: Mapped[List["LibroBanco"]] = relationship(back_populates="cuenta_mensual", lazy="selectin", cascade="all, delete-orphan")
    libros_raci: Mapped[List["LibroRACI"]] = relationship(back_populates="cuenta_mensual", lazy="selectin", cascade="all, delete-orphan")
    libros_rai: Mapped[List["LibroRAI"]] = relationship(back_populates="cuenta_mensual", lazy="selectin", cascade="all, delete-orphan")
    validaciones: Mapped[List["Validacion"]] = relationship(back_populates="cuenta_mensual", lazy="selectin", cascade="all, delete-orphan")
    detecciones_ml: Mapped[List["DeteccionML"]] = relationship(back_populates="cuenta_mensual", lazy="selectin", cascade="all, delete-orphan")
