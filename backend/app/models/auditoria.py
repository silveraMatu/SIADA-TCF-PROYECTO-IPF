from __future__ import annotations

from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional, List, Any
from sqlalchemy import String, Boolean, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.ml_ia import IntervencionAuditor


class UsuarioRBAC(Base):
    __tablename__ = "usuarios_rbac"

    id_usuario: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    apellido: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    rol: Mapped[str] = mapped_column(String(50), nullable=False)
    activo: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    intervenciones: Mapped[List[IntervencionAuditor]] = relationship(back_populates="usuario")
    logs: Mapped[List[LogAuditoria]] = relationship(back_populates="usuario")


class LogAuditoria(Base):
    __tablename__ = "logs_auditoria"

    id_log: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_usuario: Mapped[Optional[int]] = mapped_column(
        ForeignKey("usuarios_rbac.id_usuario", ondelete="SET NULL"), 
        nullable=True
    )
    accion: Mapped[str] = mapped_column(String(100), nullable=False)
    ip_origen: Mapped[str] = mapped_column(String(45), nullable=False)
    detalles_payload: Mapped[Optional[dict[str, Any]]] = mapped_column(JSONB, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    usuario: Mapped[Optional[UsuarioRBAC]] = relationship(back_populates="logs")