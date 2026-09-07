from datetime import datetime
from typing import TYPE_CHECKING, List
from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.organizacion import Organizacion
    from app.models.cuenta_mensual import CuentaMensual

class CuentaAnual(Base):
    __tablename__ = "cuentas_anual"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_organizacion: Mapped[int] = mapped_column(ForeignKey("organizaciones.id", ondelete="CASCADE"))
    anio: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    organizacion: Mapped["Organizacion"] = relationship(back_populates="cuentas_anual")
    cuentas_mensual: Mapped[List["CuentaMensual"]] = relationship(back_populates="cuenta_anual", lazy="selectin", cascade="all, delete-orphan")
