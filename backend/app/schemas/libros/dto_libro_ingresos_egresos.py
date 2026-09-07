from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class LibroIngresoEgresoBase(BaseModel):
    id_cuenta_mensual: int
    fecha: date
    concepto: Optional[str] = None
    numero_cheque: Optional[str] = Field(default=None, max_length=50)
    numero_comprobante: Optional[str] = Field(default=None, max_length=50)

    caja_debe: Decimal = Field(max_digits=15, decimal_places=2)
    caja_haber: Decimal = Field(max_digits=15, decimal_places=2)
    caja_saldo: Optional[Decimal] = Field(default=None, max_digits=15, decimal_places=2)

    banco_debe: Decimal = Field(max_digits=15, decimal_places=2)
    banco_haber: Decimal = Field(max_digits=15, decimal_places=2)
    banco_saldo: Optional[Decimal] = Field(default=None, max_digits=15, decimal_places=2)

    egreso_inc1: Decimal = Field(max_digits=15, decimal_places=2)
    egreso_inc2: Decimal = Field(max_digits=15, decimal_places=2)
    egreso_inc3: Decimal = Field(max_digits=15, decimal_places=2)
    egreso_inc4: Decimal = Field(max_digits=15, decimal_places=2)
    egreso_inc5: Decimal = Field(max_digits=15, decimal_places=2)

    ingreso_municipal: Decimal = Field(max_digits=15, decimal_places=2)
    ingreso_otras: Decimal = Field(max_digits=15, decimal_places=2)

    cuentas_varias_concepto: Optional[str] = None
    cuentas_varias_debe: Decimal = Field(max_digits=15, decimal_places=2)
    cuentas_varias_haber: Decimal = Field(max_digits=15, decimal_places=2)


class LibroIngresoEgresoCreate(LibroIngresoEgresoBase):
    pass


class LibroIngresoEgresoResponse(LibroIngresoEgresoBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
