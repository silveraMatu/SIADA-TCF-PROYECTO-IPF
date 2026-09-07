from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING, Optional
from sqlalchemy import String, DateTime, Numeric, Text, Boolean, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.db.base import Base
from app.models.enums import TipoValidacion

if TYPE_CHECKING:
    from app.models.cuenta_mensual import CuentaMensual

class Validacion(Base):
    __tablename__ = "validaciones"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_cuenta_mensual: Mapped[int] = mapped_column(ForeignKey("cuentas_mensual.id", ondelete="CASCADE"))

    id_registro_origen: Mapped[Optional[int]] = mapped_column(nullable=True)
    tabla_origen: Mapped[str] = mapped_column(String(50), nullable=False)
    tipo_validacion: Mapped[TipoValidacion] = mapped_column(nullable=False)
    resultado: Mapped[bool] = mapped_column(Boolean, nullable=False)
    mensaje: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    monto_esperado: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    monto_real: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    cuenta_mensual: Mapped["CuentaMensual"] = relationship(back_populates="validaciones")

    __table_args__ = (
        Index('idx_validacion_cuenta_mensual', 'id_cuenta_mensual'),
        Index('idx_validacion_tabla', 'tabla_origen'),
        Index('idx_validacion_tipo', 'tipo_validacion'),
        Index('idx_validacion_resultado', 'resultado'),
    )
