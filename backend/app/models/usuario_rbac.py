from datetime import datetime
from typing import TYPE_CHECKING, Optional, List
from sqlalchemy import String, DateTime, Boolean, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.db.base import Base
from app.models.enums import RolUsuario

if TYPE_CHECKING:
    from app.models.log_auditoria import LogAuditoria
    from app.models.intervencion_auditor import IntervencionAuditor

class UsuarioRBAC(Base):
    __tablename__ = "usuarios_rbac"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    apellido: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    rol: Mapped[RolUsuario] = mapped_column(SQLEnum(RolUsuario), nullable=False)
    activo: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    logs_auditoria: Mapped[List["LogAuditoria"]] = relationship(back_populates="usuario", lazy="selectin", cascade="all, delete-orphan")
    intervenciones_auditor: Mapped[List["IntervencionAuditor"]] = relationship(foreign_keys="IntervencionAuditor.id_auditor", back_populates="auditor", lazy="selectin")
    intervenciones_juez: Mapped[List["IntervencionAuditor"]] = relationship(foreign_keys="IntervencionAuditor.id_juez", back_populates="juez", lazy="selectin")
