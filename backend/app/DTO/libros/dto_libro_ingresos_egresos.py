from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class LibroIngresosEgresosBase(BaseModel):
    id_cuenta_mensual: int
    fecha: date
    tipo: str = Field(
        max_length=10,
        examples=["INGRESO", "EGRESO"],
    )
    fuente_financiamiento: Optional[str] = Field(default=None, max_length=100)
    clasificacion_economica: Optional[str] = Field(default=None, max_length=100)
    monto: Decimal = Field(gt=0.0, max_digits=15, decimal_places=2)
    descripcion: str


class LibroIngresosEgresosCreate(LibroIngresosEgresosBase):
    pass


class LibroIngresosEgresosResponse(LibroIngresosEgresosBase):
    id_movimiento: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
