from datetime import datetime
from typing import TYPE_CHECKING, Optional, Any
from sqlalchemy import String, DateTime, ForeignKey, Index
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.usuario_rbac import UsuarioRBAC

class LogAuditoria(Base):
    __tablename__ = "logs_auditoria"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_usuario: Mapped[Optional[int]] = mapped_column(ForeignKey("usuarios_rbac.id", ondelete="SET NULL"))

    accion: Mapped[str] = mapped_column(String(100), nullable=False)
    ip_origen: Mapped[Optional[str]] = mapped_column(String(45), nullable=True)
    detalles_payload: Mapped[Optional[dict[str, Any]]] = mapped_column(JSONB, default=dict)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    usuario: Mapped[Optional["UsuarioRBAC"]] = relationship(back_populates="logs_auditoria")

    __table_args__ = (
        Index('idx_log_usuario', 'id_usuario'),
        Index('idx_log_created_at', 'created_at'),
        Index('idx_log_accion', 'accion'),
    )
