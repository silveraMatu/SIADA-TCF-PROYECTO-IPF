from datetime import datetime
from typing import TYPE_CHECKING, Optional, List
from sqlalchemy import String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.libro_raci import LibroRACI
    from app.models.libro_rai import LibroRAI

class PartidaPresupuestaria(Base):
    __tablename__ = "partida_presupuestaria"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    codigo_completo: Mapped[str] = mapped_column(String(20), nullable=False)
    nivel: Mapped[int] = mapped_column(Integer, nullable=False)  # 1=Principal, 2=Parcial, 3=Subparcial
    codigo_principal: Mapped[str] = mapped_column(String(10), nullable=False)
    codigo_parcial: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    codigo_subparcial: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    denominacion: Mapped[str] = mapped_column(String(255), nullable=False)
    descripcion_objeto: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    id_partida_padre: Mapped[Optional[int]] = mapped_column(ForeignKey("partida_presupuestaria.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    partida_padre: Mapped[Optional["PartidaPresupuestaria"]] = relationship(remote_side=[id], back_populates="subpartidas")
    subpartidas: Mapped[List["PartidaPresupuestaria"]] = relationship(back_populates="partida_padre", lazy="selectin")
    libros_raci: Mapped[List["LibroRACI"]] = relationship(back_populates="partida", lazy="selectin")
    libros_rai: Mapped[List["LibroRAI"]] = relationship(back_populates="partida", lazy="selectin")
