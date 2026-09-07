from datetime import datetime
from typing import TYPE_CHECKING, Optional, List
from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.cuenta_anual import CuentaAnual

class Organizacion(Base):
    __tablename__ = "organizaciones"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(255), nullable=False)
    unidad: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    rubro: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    jurisdiccion: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    activo: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    cuentas_anual: Mapped[List["CuentaAnual"]] = relationship(back_populates="organizacion", lazy="selectin")
