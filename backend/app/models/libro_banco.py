from datetime import date, datetime
from decimal import Decimal
from typing import TYPE_CHECKING, ClassVar, Optional
from sqlalchemy import Column, ForeignKey, Index, Numeric
from sqlalchemy.sql import func
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.cuenta_mensual import CuentaMensual


class LibroBanco(SQLModel, table=True):
    __tablename__: ClassVar[str] = "libro_banco"

    id: Optional[int] = Field(default=None, primary_key=True)
    id_cuenta_mensual: int = Field(
        sa_column_args=[ForeignKey("cuentas_mensual.id", ondelete="CASCADE")]
    )

    fecha_movimiento: date
    numero_cheque: Optional[str] = Field(default=None, max_length=50)

    orden_salto_anterior: Optional[Decimal] = Field(
        default=None,
        sa_column=Column(Numeric(14, 2), nullable=True),
    )
    depositos: Decimal = Field(
        sa_column=Column(Numeric(15, 2), nullable=False, default=0)
    )
    retiros: Decimal = Field(
        sa_column=Column(Numeric(15, 2), nullable=False, default=0)
    )
    saldo_resultante: Optional[Decimal] = Field(
        default=None,
        sa_column=Column(Numeric(15, 2), nullable=True),
    )

    conciliado: bool = Field(default=False) #Columna que sera true cuando se concilie con el libro ingresos egresos

    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={"server_default": func.now()},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={
            "server_default": func.now(),
            "onupdate": func.now(),
        },
    )

    cuenta_mensual: Optional["CuentaMensual"] = Relationship(
        back_populates="libros_banco"
    )

    __table_args__: ClassVar[tuple] = (
        Index("idx_banco_cuenta_mensual", "id_cuenta_mensual"),
        Index("idx_banco_fecha", "fecha_movimiento"),
        Index("idx_banco_cheque", "numero_cheque"),
        Index("idx_banco_conciliado", "conciliado"),
    )