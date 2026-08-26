from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class LibroBancoBase(BaseModel):
    id_cuenta_mensual: int
    fecha_movimiento: date
    numero_comprobante: Optional[str] = Field(default=None, max_length=100)
    tipo_movimiento: str = Field(
        max_length=20,
        examples=["DEBITO", "CREDITO"],
    )
    concepto_texto_libre: str
    monto: Decimal = Field(max_digits=15, decimal_places=2)
    saldo_resultante: Decimal = Field(max_digits=15, decimal_places=2)
    cuit_contraparte: Optional[str] = Field(
        default=None,
        min_length=11,
        max_length=11,
        examples=["30700000001"],
    )


class LibroBancoCreate(LibroBancoBase):
    pass


class LibroBancoResponse(LibroBancoBase):
    id_banco: int
    conciliado: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
