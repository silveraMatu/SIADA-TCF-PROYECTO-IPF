from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class LibroRAIBase(BaseModel):
    id_cuenta_mensual: int
    id_partida: Optional[int] = None
    fecha_imputacion: date
    numero_orden_pago: str = Field(
        max_length=100,
        examples=["OP-2026-0012"],
    )
    beneficiario: str = Field(
        max_length=255,
        examples=["Proveedor SA"],
    )
    cuit_beneficiario: str = Field(
        min_length=11,
        max_length=11,
        examples=["30700000001"],
    )
    concepto_gasto: str
    monto_imputado: Decimal = Field(max_digits=15, decimal_places=2)


class LibroRAICreate(LibroRAIBase):
    pass


class LibroRAIResponse(LibroRAIBase):
    id_rai: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
