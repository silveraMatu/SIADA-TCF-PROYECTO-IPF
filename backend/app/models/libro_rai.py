from datetime import date, datetime
from decimal import Decimal
from typing import TYPE_CHECKING, Optional
from sqlalchemy import String, Date, DateTime, Numeric, Text, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.cuenta_mensual import CuentaMensual
    from app.models.partida_presupuestaria import PartidaPresupuestaria

class LibroRAI(Base):
    __tablename__ = "libro_rai"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_cuenta_mensual: Mapped[int] = mapped_column(ForeignKey("cuentas_mensual.id", ondelete="CASCADE"))
    id_partida: Mapped[int] = mapped_column(ForeignKey("partida_presupuestaria.id"))

    numero_asiento: Mapped[Optional[int]] = mapped_column(nullable=True)
    fecha_ingreso: Mapped[date] = mapped_column(Date, nullable=False)
    numero_planilla: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    concepto: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    ingreso_diario: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    ingreso_mensual: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    ingreso_acumulado: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    saldo: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    cuenta_mensual: Mapped["CuentaMensual"] = relationship(back_populates="libros_rai")
    partida: Mapped["PartidaPresupuestaria"] = relationship(back_populates="libros_rai")

    __table_args__ = (
        Index('idx_rai_cuenta_mensual', 'id_cuenta_mensual'),
        Index('idx_rai_partida', 'id_partida'),
        Index('idx_rai_fecha', 'fecha_ingreso'),
        Index('idx_rai_planilla', 'numero_planilla'),
    )
