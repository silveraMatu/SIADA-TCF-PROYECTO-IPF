from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING, Optional, List, Any
from sqlalchemy import String, DateTime, Numeric, Text, ForeignKey, Index
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.db.base import Base
from app.models.enums import TipoDeteccionML, NivelRiesgo, EstadoDeteccionML

if TYPE_CHECKING:
    from app.models.cuenta_mensual import CuentaMensual
    from app.models.intervencion_auditor import IntervencionAuditor

class DeteccionML(Base):
    __tablename__ = "detecciones_ml"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_cuenta_mensual: Mapped[int] = mapped_column(ForeignKey("cuentas_mensual.id", ondelete="CASCADE"))

    id_registro_origen: Mapped[Optional[int]] = mapped_column(nullable=True)
    tabla_origen: Mapped[str] = mapped_column(String(50), nullable=False)
    tipo_deteccion: Mapped[TipoDeteccionML] = mapped_column(nullable=False)
    modelo_utilizado: Mapped[str] = mapped_column(String(100), nullable=False)

    entidades_json: Mapped[Optional[dict[str, Any]]] = mapped_column(JSONB, default=dict)
    score_anomalia: Mapped[Optional[Decimal]] = mapped_column(Numeric(10, 4), nullable=True)
    nivel_riesgo: Mapped[NivelRiesgo] = mapped_column(default=NivelRiesgo.BAJO)
    explicacion_xai: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    estado: Mapped[EstadoDeteccionML] = mapped_column(default=EstadoDeteccionML.PENDIENTE)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    cuenta_mensual: Mapped["CuentaMensual"] = relationship(back_populates="detecciones_ml")
    intervenciones: Mapped[List["IntervencionAuditor"]] = relationship(back_populates="deteccion", lazy="selectin", cascade="all, delete-orphan")

    __table_args__ = (
        Index('idx_deteccion_cuenta_mensual', 'id_cuenta_mensual'),
        Index('idx_deteccion_tabla', 'tabla_origen'),
        Index('idx_deteccion_tipo', 'tipo_deteccion'),
        Index('idx_deteccion_estado', 'estado'),
        Index('idx_deteccion_riesgo', 'nivel_riesgo'),
    )
