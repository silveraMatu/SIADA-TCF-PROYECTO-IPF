from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class LibroBancoBase(BaseModel):
    id_cuenta_mensual: int
    fecha_movimiento: date
    numero_cheque: Optional[str] = Field(default=None, max_length=50)
    beneficiario: Optional[str] = Field(default=None, max_length=255)
    depositos: Decimal = Field(max_digits=15, decimal_places=2)
    retiros: Decimal = Field(max_digits=15, decimal_places=2)
    saldo_resultante: Optional[Decimal] = Field(default=None, max_digits=15, decimal_places=2)


class LibroBancoCreate(LibroBancoBase):
    pass


class LibroBancoResponse(LibroBancoBase):
    id: int
    conciliado: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
