from datetime import date, datetime
from typing import TYPE_CHECKING, Optional
from sqlalchemy import Date, DateTime, Text, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.db.base import Base
from app.models.enums import DecisionIntervencion

if TYPE_CHECKING:
    from app.models.deteccion_ml import DeteccionML
    from app.models.usuario_rbac import UsuarioRBAC

class IntervencionAuditor(Base):
    __tablename__ = "intervenciones_auditor"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_deteccion: Mapped[int] = mapped_column(ForeignKey("detecciones_ml.id", ondelete="CASCADE"))
    id_auditor: Mapped[int] = mapped_column(ForeignKey("usuarios_rbac.id"))
    id_juez: Mapped[int] = mapped_column(ForeignKey("usuarios_rbac.id"))

    decision: Mapped[DecisionIntervencion] = mapped_column(nullable=False)
    observaciones: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    fecha_resolucion: Mapped[Optional[date]] = mapped_column(Date, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    deteccion: Mapped["DeteccionML"] = relationship(back_populates="intervenciones")
    auditor: Mapped["UsuarioRBAC"] = relationship(foreign_keys=[id_auditor], back_populates="intervenciones_auditor")
    juez: Mapped["UsuarioRBAC"] = relationship(foreign_keys=[id_juez], back_populates="intervenciones_juez")

    __table_args__ = (
        Index('idx_intervencion_deteccion', 'id_deteccion'),
        Index('idx_intervencion_auditor', 'id_auditor'),
        Index('idx_intervencion_juez', 'id_juez'),
    )
