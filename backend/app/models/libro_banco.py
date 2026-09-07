from datetime import date, datetime
from decimal import Decimal
from typing import TYPE_CHECKING, Optional
from sqlalchemy import String, Date, DateTime, Numeric, Boolean, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.cuenta_mensual import CuentaMensual

class LibroBanco(Base):
    __tablename__ = "libro_banco"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_cuenta_mensual: Mapped[int] = mapped_column(ForeignKey("cuentas_mensual.id", ondelete="CASCADE"))

    fecha_movimiento: Mapped[date] = mapped_column(Date, nullable=False)
    numero_cheque: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    beneficiario: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    depositos: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    retiros: Mapped[Decimal] = mapped_column(Numeric(15, 2), default=0)
    saldo_resultante: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)

    conciliado: Mapped[bool] = mapped_column(Boolean, default=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    cuenta_mensual: Mapped["CuentaMensual"] = relationship(back_populates="libros_banco")

    __table_args__ = (
        Index('idx_banco_cuenta_mensual', 'id_cuenta_mensual'),
        Index('idx_banco_fecha', 'fecha_movimiento'),
        Index('idx_banco_cheque', 'numero_cheque'),
        Index('idx_banco_conciliado', 'conciliado'),
    )
