from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal
from typing import TYPE_CHECKING, List, Any
from sqlalchemy import String, Text, Numeric, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.organizacion import CuentaMensual
    from app.models.auditoria import UsuarioRBAC


class DeteccionPLNLoRA(Base):
    __tablename__ = "detecciones_pln_lora"

    id_deteccion: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_cuenta_mensual: Mapped[int] = mapped_column(
        ForeignKey("cuenta_mensual.id_cuenta_mensual", ondelete="CASCADE"), 
        nullable=False, 
        index=True
    )
    origen_tabla: Mapped[str] = mapped_column(String(50), nullable=False)
    id_registro_origen: Mapped[int] = mapped_column(Integer, nullable=False)
    lora_adapter_utilizado: Mapped[str] = mapped_column(String(100), nullable=False)
    entidades_ner_json: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False)
    score_anomalia: Mapped[Decimal] = mapped_column(Numeric(5, 4), nullable=False, index=True)
    tipo_alerta: Mapped[str] = mapped_column(String(50), nullable=False)
    explicacion_xai: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    cuenta_mensual: Mapped[CuentaMensual] = relationship(back_populates="detecciones_ia")
    intervenciones: Mapped[List[IntervencionAuditor]] = relationship(back_populates="deteccion")


class IntervencionAuditor(Base):
    __tablename__ = "intervenciones_auditor"

    id_intervencion: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_deteccion: Mapped[int] = mapped_column(
        ForeignKey("detecciones_pln_lora.id_deteccion", ondelete="RESTRICT"), 
        nullable=False
    )
    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("usuarios_rbac.id_usuario", ondelete="RESTRICT"), 
        nullable=False
    )
    decision: Mapped[str] = mapped_column(String(50), nullable=False)
    observaciones_dictamen: Mapped[str] = mapped_column(Text, nullable=False)
    fecha_resolucion: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    deteccion: Mapped[DeteccionPLNLoRA] = relationship(back_populates="intervenciones")
    usuario: Mapped[UsuarioRBAC] = relationship(back_populates="intervenciones")