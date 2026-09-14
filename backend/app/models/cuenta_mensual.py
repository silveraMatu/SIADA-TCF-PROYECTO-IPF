from datetime import date, datetime
from typing import TYPE_CHECKING, ClassVar, List, Optional
from sqlalchemy import Column, Enum as SQLEnum
from sqlalchemy.sql import func
from sqlmodel import Field, Relationship, SQLModel

from app.models.enums import EstadoCuentaMensual

if TYPE_CHECKING:
    from app.models.cuenta_anual import CuentaAnual
    from app.models.libro_banco import LibroBanco
    from app.models.libro_ingreso_egreso import LibroIngresoEgreso
    from app.models.libro_raci import LibroRACI
    from app.models.libro_rai import LibroRAI
    from app.models.validacion import Validacion


class CuentaMensual(SQLModel, table=True):
    __tablename__: ClassVar[str] = "cuentas_mensual"

    id: Optional[int] = Field(default=None, primary_key=True)
    id_cuenta_anual: int = Field(foreign_key="cuentas_anual.id")
    mes: int

    estado: EstadoCuentaMensual = Field(
        default=EstadoCuentaMensual.PENDIENTE,
        sa_column=Column(
            SQLEnum(EstadoCuentaMensual),
            nullable=False,
            default=EstadoCuentaMensual.PENDIENTE,
        ),
    )

    fecha_presentacion: Optional[date] = Field(default=None)
    fecha_limite_auditoria: Optional[date] = Field(default=None)
    fecha_cierre: Optional[date] = Field(default=None)
    observaciones_generales: Optional[str] = Field(default=None)

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
    libros_ingresos_egresos: List["LibroIngresoEgreso"] = Relationship(
        back_populates="cuenta_mensual", cascade_delete=True
    )
    libros_banco: List["LibroBanco"] = Relationship(
        back_populates="cuenta_mensual", cascade_delete=True
    )
    libros_raci: List["LibroRACI"] = Relationship(
        back_populates="cuenta_mensual", cascade_delete=True
    )
    libros_rai: List["LibroRAI"] = Relationship(
        back_populates="cuenta_mensual", cascade_delete=True
    )
    validaciones: List["Validacion"] = Relationship(
        back_populates="cuenta_mensual", cascade_delete=True
    )
    # detecciones_ml: List["DeteccionML"] = Relationship(
    #     back_populates="cuenta_mensual", cascade_delete=True
    # )